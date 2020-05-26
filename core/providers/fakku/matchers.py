import os
import re
from typing import Optional
from urllib.parse import urljoin, quote

import requests
from bs4 import BeautifulSoup

from core.base.matchers import Matcher
from core.base.types import DataDict
from core.base.utilities import (
    filecount_in_zip,
    get_zip_filesize,
    request_with_retries, construct_request_dict)
from . import constants
from .utilities import clean_title


class TitleMatcher(Matcher):

    name = 'title'
    provider = constants.provider_name
    type = 'title'
    time_to_wait_after_compare = 0
    default_cutoff = 0.6

    def format_to_search_title(self, file_name: str) -> str:
        if file_name.endswith('.zip'):
            return clean_title(self.get_title_from_path(file_name))
        else:
            return clean_title(file_name)

    def format_to_compare_title(self, file_name: str) -> str:
        if file_name.endswith('.zip'):
            return clean_title(self.get_title_from_path(file_name))
        else:
            return clean_title(file_name)

    def search_method(self, title_to_search: str) -> bool:
        return self.compare_by_title_json(title_to_search)

    def format_match_values(self) -> Optional[DataDict]:

        if not self.match_values:
            return None
        self.match_gid = self.match_values.gid
        values = {
            'title': self.match_title,
            'title_jpn': '',
            'zipped': self.file_path,
            'crc32': self.crc32,
            'match_type': self.found_by,
            'filesize': get_zip_filesize(os.path.join(self.settings.MEDIA_ROOT, self.file_path)),
            'filecount': filecount_in_zip(os.path.join(self.settings.MEDIA_ROOT, self.file_path)),
            'source_type': self.provider
        }

        return values

    def compare_by_title(self, title: str) -> bool:

        request_dict = construct_request_dict(self.settings, self.own_settings)

        r = request_with_retries(
            urljoin(constants.main_url, 'search/') + quote(title),
            request_dict,
            logger=self.logger
        )

        if not r:
            self.logger.info("Got no response from server")
            return False

        r.encoding = 'utf-8'
        soup_1 = BeautifulSoup(r.text, 'html.parser')

        matches_links = set()

        # content-row manga row
        for gallery in soup_1.find_all("div", class_=re.compile("content-row")):
            link_container = gallery.find("a", class_="content-title")
            if link_container:
                matches_links.add(urljoin(constants.main_url, link_container['href']))

        self.gallery_links = list(matches_links)
        if len(self.gallery_links) > 0:
            self.found_by = self.name
            return True
        else:
            return False

    def compare_by_title_json(self, title: str) -> bool:

        # https://www.fakku.net/suggest/return%20of%20me
        headers = {
            'Content-Type': 'application/json',
            'Referer': constants.main_url + '/',
            'X-Requested-With': 'XMLHttpRequest',
        }

        self.logger.info("Querying URL: {}".format(urljoin(constants.main_url, 'suggest/') + quote(title.lower())))

        request_dict = construct_request_dict(self.settings, self.own_settings)
        request_dict['headers'] = {**headers, **self.settings.requests_headers}

        response = request_with_retries(
            urljoin(constants.main_url, 'suggest/') + quote(title.lower()),
            request_dict,
            post=False, retries=3, logger=self.logger
        )

        if not response:
            self.logger.info("Got no response from server")
            return False

        response_data = response.json()

        matches_links = set()

        if 'error' in response_data:
            self.logger.info("Got error from server: {}".format(response_data['error']))
            return False

        for gallery in response_data:
            if gallery['type'] in ('doujinshi', 'manga', 'hentai'):
                matches_links.add(urljoin(constants.main_url, gallery['link']))

        self.gallery_links = list(matches_links)
        if len(self.gallery_links) > 0:
            self.found_by = self.name
            return True
        else:
            return False


API = (
    TitleMatcher,
)
