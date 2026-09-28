"""
SEO-ЗАДАНИЕ: карта сайта (sitemap.xml).

Этот файл — заготовка. Сейчас он НИГДЕ не подключён.
Шаги:
  1. Добавьте "django.contrib.sitemaps" в INSTALLED_APPS (podzemka/settings.py).
  2. Раскомментируйте классы ниже и допишите их.
  3. Подключите маршрут /sitemap.xml в podzemka/urls.py (там есть подсказка).
  4. Откройте http://127.0.0.1:8000/sitemap.xml и проверьте результат.
  5. Добавьте строку «Sitemap: ...» в robots.txt.

Документация: https://docs.djangoproject.com/en/stable/ref/contrib/sitemaps/
"""

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Hall


class StaticViewSitemap(Sitemap):
    """Статичные страницы сайта"""
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
          "venue:home",
          "venue:hall_list",
          "venue:poster_list",
           "venue:menu",
           "venue:events",
           "venue:gallery",
           "venue:contacts",
         ]

    def location(self, item):
        return reverse(item)


class HallSitemap(Sitemap):
    """Страницы отдельных залов — берутся из БД."""
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Hall.objects.filter(is_active=True)
    # location() не нужен, если у модели есть get_absolute_url()
