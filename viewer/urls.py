from django.conf.urls import url
from viewer.views import head, browser, wanted, exp, api, archive, admin
from viewer.feeds import LatestArchivesFeed
from viewer.views.elasticsearch import ESHomePageView, autocomplete_view, title_suggest_view

urlpatterns = [

    url(r"^dir-browser/$", browser.directory_parser, name='directory-parser'),
    url(r"^jsearch/*$", api.json_search, name='json-search'),
    url(r"^api/*$", api.json_search, name='api'),
    url(r"^jsonapi$", api.json_parser, name='json-parser'),
    url(r"^admin-api/$", api.json_parser, name='json-parser'),
    url(r"^archive/(\d+)/$", archive.archive_details, name='archive'),
    url(r"^archive/(\d+)/(cover|full|thumbnails|edit|single)/$",
        archive.archive_details, name='archive-details'),
    url(r"^archive/(\d+)/extract-toggle/$", archive.extract_toggle, name='archive-extract-toggle'),
    url(r"^archive/(\d+)/public-toggle/$", archive.public_toggle, name='archive-public-toggle'),
    url(r"^archive/(\d+)/recalc-info/$", archive.recalc_info, name='archive-recalc-info'),
    url(r"^archive/(\d+)/recall-api/$", archive.recall_api, name='archive-recall-api'),
    url(r"^archive/(\d+)/generate-matches/$", archive.generate_matches, name='archive-generate-matches'),
    url(r"^archive/(\d+)/rematch/$", archive.rematch_archive, name='archive-rematch'),
    url(r"^archive/(\d+)/delete/$", archive.delete_archive, name='archive-delete'),
    url(r"^archive/(\d+)/download/$", archive.archive_download, name='archive-download'),
    url(r"^archive/(\d+)/thumb/$", archive.archive_thumb, name='archive-thumb'),
    url(r"^update/(\d+)/([\w-]+)/(\d*)/$", archive.archive_update, name='archive-update-tool-id'),
    url(r"^update/(\d+)/([\w-]+)/$", archive.archive_update, name='archive-update-tool'),
    url(r"^update/(\d+)/([\w-]+)/([\w-]+)/$", archive.archive_update, name='archive-update-tool-name'),
    url(r"^update/(\d+)/$", archive.archive_update, name='archive-update'),
    url(r"^gallery/(\d+)/thumb/$", head.gallery_thumb, name='gallery-thumb'),
    url(r"^gallery/(\d+)/([\w-]+)/$", head.gallery_details, name='gallery-tool'),
    url(r"^gallery/(\d+)/$", head.gallery_details, name='gallery'),
    url(r"^wanted-gallery/(\d+)/$", wanted.wanted_gallery, name='wanted-gallery'),
    url(r"^user-archive-preferences/(\d+)/([\w-]+)/$", head.user_archive_preferences, name='user-archive-preferences'),
    url(r"^submit/$", head.url_submit, name='url-submit'),
    url(r"^lists/([\w-]+)/$", head.lists, name='lists'),
    url(r"^login/$", head.viewer_login, name='login'),
    url(r"^logout/$", head.viewer_logout, name='logout'),
    url(r"^session-settings/$", head.session_settings, name='session-settings'),
    url(r"^img/(\d+)/$", head.image_url, name='image-url'),
    url(r"^content/panda.user.js$", head.panda_userscript, name='panda-user-script'),
    url(r"^(tag)/(.+?)/$", head.search, name='archive-tag-search'),
    url(r"^(gallery-tag)/(.+?)/$", head.gallery_list, name='gallery-tag-search'),
    url(r"^galleries/$", head.gallery_list, name='gallery-list'),
    url(r"^search/$", head.search, name='archive-search'),
    url(r"^about/$", head.about, name='about'),
    url(r"^$", head.search, name="main-page"),
]

# Image viewer.
urlpatterns += [
    url(r"^archive/(\d+)/img/(\d+)/$", head.image_viewer, name='image-viewer'),
    url(r"^new-image-viewer/(\d+)/img/(\d+)/$", exp.new_image_viewer, name='new-image-viewer'),
]

# Admin URLs
urlpatterns += [
    url(r"^tools/([\w-]+)/$", admin.tools, name='tools-id'),
    url(r"^tools/$", admin.tools, name='tools'),
    url(r"^logs/$", admin.logs, name='logs'),
    url(r"^stats/collection$", admin.stats_collection, name='stats-collection'),
    url(r"^public-stats/$", head.public_stats, name='public-stats'),
    url(r"^stats/workers$", admin.stats_workers, name='stats-workers'),
    url(r"^stats/settings", admin.stats_settings, name='stats-settings'),
    url(r"^web-queue/([\w-]+)/([\w-]+)$", admin.queue_operations, name='queue-operations'),
    url(r"^web-crawler/$", admin.crawler, name='crawler'),
    url(r"^folder-crawler/$", admin.foldercrawler, name='folder-crawler'),
]

urlpatterns += [
    url(r"^feed/$", LatestArchivesFeed(), name='archive-rss'),
]

urlpatterns += [
    url(r"^tag-frequency/$", exp.tag_frequency, name='tag-frequency'),
    url(r"^gallery-frequency/$", exp.gallery_frequency, name='gallery-frequency'),
    url(r"^seed$", exp.seeder),
    url(r"^posted-seed$", exp.release_date_seeder),
    url(r"^r-api/([\w-]+)/$", exp.api, name='model-all'),
    url(r"^r-api/([\w-]+)/(\d+)/$", exp.api, name='model-obj'),
    url(r"^r-api/([\w-]+)/(\d+)/([\w-]+)/$", exp.api, name='model-obj-action'),
]

urlpatterns += [
    url(r'^autocomplete-view/$', autocomplete_view, name='es-autocomplete-view'),
    url(r'^title-suggest/$', title_suggest_view, name='es-suggest-view'),
    url(r'^es-index/$', ESHomePageView.as_view(), name='es-index-view'),
]
