from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView

from venue.sitemaps import HallSitemap, StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "halls": HallSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
        name="robots_txt",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("home/", RedirectView.as_view(url="/", permanent=True)),
    path("", include("venue.urls")),
]


# SEO-ЗАДАНИЕ (страница 404):
# ПОДСКАЗКА: Django сам покажет templates/404.html, если DEBUG = False.
# Создайте такой шаблон (в стиле сайта, с навигацией и ссылкой на главную).
# Проверить: запустите с DJANGO_DEBUG=0 и флагом --insecure (см. README).
