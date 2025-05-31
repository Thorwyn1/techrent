from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Uzytkownik, Sprzet, Wypozyczenie

class RejestracjaForm(UserCreationForm):
    imie_nazwisko = forms.CharField(max_length=100, label="Imię i nazwisko")
    email = forms.EmailField(required=True)
    
    class Meta:
        model = Uzytkownik
        fields = ('username', 'imie_nazwisko', 'email', 'password1', 'password2')

class SprzetForm(forms.ModelForm):
    class Meta:
        model = Sprzet
        fields = ['model', 'opis', 'koszt_dzienny', 'status_wypozyczenia']
        labels = {
            'model': 'Model',
            'opis': 'Opis',
            'koszt_dzienny': 'Koszt dzienny (PLN)',
            'status_wypozyczenia': 'Status wypożyczenia',
        }

class WypozyczenieForm(forms.ModelForm):
    class Meta:
        model = Wypozyczenie
        fields = ['sprzet', 'klient', 'data_rozpoczecia', 'data_zakonczenia', 'uwagi']
        labels = {
            'sprzet': 'Sprzęt',
            'klient': 'Klient',
            'data_rozpoczecia': 'Data rozpoczęcia',
            'data_zakonczenia': 'Data zakończenia',
            'uwagi': 'Uwagi',
        }
        widgets = {
            'data_rozpoczecia': forms.DateInput(attrs={'type': 'date'}),
            'data_zakonczenia': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Uzytkownik
        fields = ['imie_nazwisko', 'email']
        labels = {
            'imie_nazwisko': 'Imię i nazwisko',
            'email': 'Email',
        }