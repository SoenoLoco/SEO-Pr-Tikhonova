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

# Блок 4. Карта сайта sitemap.xml

1. Подключено приложение `django.contrib.sitemaps` в `INSTALLED_APPS`
2. Доделан `venue/sitemaps.py`: класс `StaticViewSitemap` (7 статических страниц) и класс `HallSitemap` (только активные залы)
3. Маршрут `/sitemap.xml` подключён в `podzemka/urls.py`
4. Обновлён `robots.txt` — теперь директива `Sitemap:` ведёт на рабочий адрес

# Блок 5. Структура и контент

1. Убран второй `<h1>` на главной
2. `<h4>` в блоке «Что празднуем?» заменён на `<h3>`
3. В галерее `<h2>` заменён на `<h1>`
4. В списке залов `h1` стал конкретнее: «Банкетные залы в стиле лофт»
5. Добавлены осмысленные `alt`, `width`/`height` во все `<img>`
6. На картинки ниже первого экрана добавлен `loading="lazy"`
7. «Смотреть» → «Смотреть зал “Депо”», «Подробнее» → «Смотреть всё банкетное меню и цены», «Подробнее» → «Подробнее о «Название события»»
8. Telegram и ВК в подвале — добавлен `rel="noopener"`
9. Добавлены хлебные крошки на: hall_list, poster_list, menu, events, gallery, contacts, booking

- Внешние ссылки — нужен ли им rel="noopener"? А nofollow?
-- rel="noopener" — да, нужен. Он предотвращает доступ открытой вкладки к window.opener. nofollow — не нужен. Это ссылки на наши соцсети

- Какой уровень заголовка здесь уместен и почему не <h1>?
-- `<h2>`, потому что на странице уже есть `<h1>`, а блок акции — отдельная секция

# Блок 6: URL и дубли

1. В модель `Hall` добавлено поле `slug`, в модель `Poster` добавлено поле `slug`
2. Миграции сделаны в 2 этапа: сначала с `null=True`, потом убрали `null`
3. Slug заполнен для всех существующих записей через `manage.py shell`
4. В админке добавлен `prepopulated_fields` для авто-генерации slug из названия
5. `/halls/<int:pk>/` → `hall_detail_redirect` → 301 на новый URL
6. `/afisha/<int:pk>/` → `poster_detail_redirect` → 301 на новый URL
7. `/home/` → `RedirectView.as_view(url="/", permanent=True)` → 301 на `/`
8.  Создан `templates/404.html` в стиле сайта (заголовок «Тупик», навигация, кнопки)
9. Проверено с `DJANGO_DEBUG=0 python manage.py runserver --insecure`

- Что делать со страницей прошедшего события?
-- Оставить в архиве с пометкой «Событие прошло». 404/410 «сжигают» внешние ссылки, а архив сохраняет трафик и вес

- Что добавить на пустую афишу?
-- Текст-описание (2–3 абзаца), CTA «Забронировать зал», ссылки на соцсети, архив прошедших событий

# Блок 7: Микроразметка Schema.org

1. В `base.html` добавлен JSON-LD `EventVenue` (название, legalName, адрес, телефон, email, часы работы, координаты, sameAs на соцсети)
2. На всех внутренних страницах — `BreadcrumbList` JSON-LD, на главной (`home.html`) — `FAQPage` JSON-LD, на странице события (`poster_detail.html`) — `Event` JSON-LD