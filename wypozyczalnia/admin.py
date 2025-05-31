from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Uzytkownik, Sprzet, Wypozyczenie

@admin.register(Uzytkownik)
class UzytkownikAdmin(UserAdmin):
    list_display = ('username', 'imie_nazwisko', 'email', 'typ_uzytkownika', 'status_konta', 'date_joined')
    list_filter = ('typ_uzytkownika', 'status_konta', 'date_joined')
    search_fields = ('username', 'imie_nazwisko', 'email')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Dodatkowe informacje', {'fields': ('imie_nazwisko', 'typ_uzytkownika', 'status_konta')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Dodatkowe informacje', {'fields': ('imie_nazwisko', 'typ_uzytkownika', 'status_konta')}),
    )

@admin.register(Sprzet)
class SprzetAdmin(admin.ModelAdmin):
    list_display = ('model', 'koszt_dzienny', 'status_wypozyczenia', 'data_dodania')
    list_filter = ('status_wypozyczenia', 'data_dodania')
    search_fields = ('model', 'opis')
    list_editable = ('status_wypozyczenia',)

@admin.register(Wypozyczenie)
class WypozyczenieAdmin(admin.ModelAdmin):
    list_display = ('sprzet', 'klient', 'data_rozpoczecia', 'data_zakonczenia', 'data_utworzenia')
    list_filter = ('data_rozpoczecia', 'data_zakonczenia', 'data_utworzenia')
    search_fields = ('sprzet__model', 'klient__imie_nazwisko')
    date_hierarchy = 'data_rozpoczecia'