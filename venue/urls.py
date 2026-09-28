from django.urls import path

from . import views

app_name = "venue"

urlpatterns = [
    path("", views.home, name="home"),

    path("halls/", views.hall_list, name="hall_list"),
    # Сначала ЧИСЛОВОЙ pk (для 301-редиректа со старых URL),
    # потом slug — иначе slug перехватит числа.
    path("halls/<int:pk>/", views.hall_detail_redirect, name="hall_detail_old"),
    path("halls/<slug:slug>/", views.hall_detail, name="hall_detail"),

    path("menu/", views.menu, name="menu"),
    path("events/", views.events, name="events"),

    path("afisha/", views.poster_list, name="poster_list"),
    path("afisha/<int:pk>/", views.poster_detail_redirect, name="poster_detail_old"),
    path("afisha/<slug:slug>/", views.poster_detail, name="poster_detail"),

    path("gallery/", views.gallery, name="gallery"),
    path("contacts/", views.contacts, name="contacts"),
    path("booking/", views.booking, name="booking"),
]