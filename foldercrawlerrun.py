#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import os
import sys

import django
import logging

from django.conf import settings

sys.path.append(os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pandabackup.settings")
django.setup()

from core.local.foldercrawler import FolderCrawler

crawler_settings = settings.CRAWLER_SETTINGS
logger = logging.getLogger()

h = logging.StreamHandler(stream=sys.stdout)
h.setLevel(logging.DEBUG)
logger.addHandler(h)

if __name__ == "__main__":
    argv = sys.argv[1:]

    folder_crawler = FolderCrawler(crawler_settings)

    folder_crawler.start_crawling(argv)

    logger.removeHandler(h)
