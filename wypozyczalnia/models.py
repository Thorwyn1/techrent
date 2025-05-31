from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Uzytkownik(AbstractUser):
    KLIENT = 'klient'
    ADMINISTRATOR = 'administrator'
    
    TYPY_UZYTKOWNIKA = [
        (KLIENT, 'Klient'),
        (ADMINISTRATOR, 'Administrator'),
    ]
    
    imie_nazwisko = models.CharField(max_length=100)
    typ_uzytkownika = models.CharField(max_length=15, choices=TYPY_UZYTKOWNIKA, default=KLIENT)
    status_konta = models.BooleanField(default=True, verbose_name="Aktywne konto")
    
    def __str__(self):
        return f"{self.username} - {self.imie_nazwisko}"

class Sprzet(models.Model):
    DOSTEPNY = 'dostepny'
    WYPOZYCZONY = 'wypozyczony'
    NIEDOSTEPNY = 'niedostepny'
    
    STATUSY = [
        (DOSTEPNY, 'Dostępny'),
        (WYPOZYCZONY, 'Wypożyczony'),
        (NIEDOSTEPNY, 'Niedostępny'),
    ]
    
    model = models.CharField(max_length=100)
    opis = models.TextField()
    koszt_dzienny = models.DecimalField(max_digits=8, decimal_places=2)
    status_wypozyczenia = models.CharField(max_length=15, choices=STATUSY, default=DOSTEPNY)
    data_dodania = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.model} - {self.get_status_wypozyczenia_display()}"

class Wypozyczenie(models.Model):
    sprzet = models.ForeignKey(Sprzet, on_delete=models.CASCADE)
    klient = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    data_rozpoczecia = models.DateField()
    data_zakonczenia = models.DateField()
    uwagi = models.TextField(blank=True)
    data_utworzenia = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sprzet.model} - {self.klient.imie_nazwisko}"