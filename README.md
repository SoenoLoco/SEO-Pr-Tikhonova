# Подземка — банкетный зал в стиле лофт / андеграунд

# ЗАДАНИЕ

АУДИТ:
1. Нет <html lang="ru">
2. Везде одинаковый <title>
3. Отсутствует <meta name="description">; <link rel="canonical">
4. Нет robots для страницы бронирования
5. Favicon — отсутствует
6. OG-теги — отсутствуют
7. twitter:card — отсутствует
8. og:image — отсутствует
9. Файл templates/robots.txt — отсутствует
10. Маршрут /robots.txt — не подключён в podzemka/urls.py
11. django.contrib.sitemaps — не подключён в settings.py
12. venue/sitemaps.py — закомментирован полностью
13. Маршрут /sitemap.xml — не подключён
14. На главной два <h1>, В галерее нет <h1>, На главной после <h2> идут <h4>
15. У изображений нет alt, width, height, loading="lazy"
16. Внешние ссылки в подвале без rel="noopener"
17. Хлебные крошки только на hall_detail.html, нет на других страницах
18. /halls/1/ вместо /halls/depo/ — нет slug
19. /afisha/1/ вместо /afisha/kviz-60-sekund/ — нет slug
20. /home/ — дубль главной, нет 301-редиректа
21. Нет templates/404.html
22. JSON-LD EventVenue / LocalBusiness — отсутствует, BreadcrumbList — отсутствует, FAQPage — отсутствует, Event — отсутствует 

# Блок 1. Мета-теги

1. В base.html добавлены: блоки description, robots, OG-теги, twitter:card, canonical, favicon-ссылки, theme-color
2. Title и description на всех страницах
3. На странице зала title/description — динамические из данных зала
4. На странице события title/description — динамические
5. og:image на странице зала и события — картинка этого зала/события

- Почему для страницы бронирования лучше использовать noindex, чем Disallow в robots.txt?
-- Disallow — «не заходи». Робот не читает страницу, но если на неё есть ссылка — адрес всё равно попадёт в поиск (пустой). Плюс: робот не видит ссылки внутри и не передаёт по ним вес. noindex — «заходи, но не показывай». Робот читает страницу, видит тег и убирает её из выдачи. Ссылки внутри работают, вес передаётся дальше.
Для бронирования: страница служебная, в поиске не нужна, но ссылки с неё важны. Поэтому noindex, follow — правильный выбор.


# Блок 2. Open Graph и соцсети

1. В `templates/base.html` добавлены OG-теги: `og:type`, `og:site_name`, `og:locale`, `og:url`, `og:title`, `og:description`, `og:image`, `twitter:card`
2. `og:title` и `og:description` подтягиваются автоматически из блоков `title` и `description` через `{{ block.super }}` — не нужно дублировать тексты
3. `og:url` — абсолютный URL текущей страницы
4. `og:image` по умолчанию — `static/img/og-default.jpg`
5. На странице зала (`hall_detail.html`) `og:image` переопределён на картинку этого зала, на странице события (`poster_detail.html`) `og:image` — картинка события

# Блок 3. robots.txt

1. Создан файл `templates/robots.txt`
2. Подключён маршрут `/robots.txt` в `podzemka/urls.py` через `TemplateView` с `content_type="text/plain"`
3. Закрыты от индексации: `/admin/`, `/booking/`, `/home/`, `/accounts/`, URL с GET-параметрами (`/*?*`)
4. Добавлена директива `Sitemap:` с абсолютным URL