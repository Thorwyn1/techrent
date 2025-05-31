from django.urls import path
from . import views

urlpatterns = [
    path('', views.strona_glowna, name='strona_glowna'),
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('sprzet/', views.lista_sprzetu, name='lista_sprzetu'),
    path('sprzet/dodaj/', views.dodaj_sprzet, name='dodaj_sprzet'),
    path('sprzet/edytuj/<int:pk>/', views.edytuj_sprzet, name='edytuj_sprzet'),
    path('wypozyczenia/', views.lista_wypozyczen, name='lista_wypozyczen'),
    path('wypozyczenia/dodaj/', views.dodaj_wypozyczenie, name='dodaj_wypozyczenie'),
    path('profil/', views.profil, name='profil'),
    path('uzytkownicy/', views.lista_uzytkownikow, name='lista_uzytkownikow'),
]