from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Uzytkownik, Sprzet, Wypozyczenie
from .forms import RejestracjaForm, SprzetForm, WypozyczenieForm, ProfilForm

def rejestracja(request):
    if request.method == 'POST':
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Konto zostało utworzone pomyślnie!')
            return redirect('strona_glowna')
    else:
        form = RejestracjaForm()
    return render(request, 'registration/rejestracja.html', {'form': form})

def strona_glowna(request):
    if request.user.typ_uzytkownika == Uzytkownik.ADMINISTRATOR:
        return render(request, 'wypozyczalnia/panel_administratora.html')
    else:
        sprzet_dostepny = Sprzet.objects.filter(status_wypozyczenia=Sprzet.DOSTEPNY)
        return render(request, 'wypozyczalnia/panel_klienta.html', {
            'sprzet_dostepny': sprzet_dostepny
        })

def lista_sprzetu(request):
    sprzet = Sprzet.objects.all()
    return render(request, 'wypozyczalnia/lista_sprzetu.html', {'sprzet': sprzet})

@login_required
def dodaj_sprzet(request):
    if request.user.typ_uzytkownika != Uzytkownik.ADMINISTRATOR:
        messages.error(request, 'Brak uprawnień!')
        return redirect('strona_glowna')
    
    if request.method == 'POST':
        form = SprzetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sprzęt został dodany!')
            return redirect('lista_sprzetu')
    else:
        form = SprzetForm()
    return render(request, 'wypozyczalnia/dodaj_sprzet.html', {'form': form})

@login_required
def edytuj_sprzet(request, pk):
    if request.user.typ_uzytkownika != Uzytkownik.ADMINISTRATOR:
        messages.error(request, 'Brak uprawnień!')
        return redirect('strona_glowna')
    
    sprzet = get_object_or_404(Sprzet, pk=pk)
    if request.method == 'POST':
        form = SprzetForm(request.POST, instance=sprzet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sprzęt został zaktualizowany!')
            return redirect('lista_sprzetu')
    else:
        form = SprzetForm(instance=sprzet)
    return render(request, 'wypozyczalnia/edytuj_sprzet.html', {'form': form, 'sprzet': sprzet})

@login_required
def lista_wypozyczen(request):
    if request.user.typ_uzytkownika != Uzytkownik.ADMINISTRATOR:
        messages.error(request, 'Brak uprawnień!')
        return redirect('strona_glowna')
    
    wypozyczenia = Wypozyczenie.objects.all().order_by('-data_utworzenia')
    return render(request, 'wypozyczalnia/lista_wypozyczen.html', {'wypozyczenia': wypozyczenia})

@login_required
def dodaj_wypozyczenie(request):
    if request.user.typ_uzytkownika != Uzytkownik.ADMINISTRATOR:
        messages.error(request, 'Brak uprawnień!')
        return redirect('strona_glowna')
    
    if request.method == 'POST':
        form = WypozyczenieForm(request.POST)
        if form.is_valid():
            wypozyczenie = form.save()
            # Zaktualizuj status sprzętu
            wypozyczenie.sprzet.status_wypozyczenia = Sprzet.WYPOZYCZONY
            wypozyczenie.sprzet.save()
            messages.success(request, 'Wypożyczenie zostało dodane!')
            return redirect('lista_wypozyczen')
    else:
        form = WypozyczenieForm()
    return render(request, 'wypozyczalnia/dodaj_wypozyczenie.html', {'form': form})

@login_required
def profil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil został zaktualizowany!')
            return redirect('profil')
    else:
        form = ProfilForm(instance=request.user)
    return render(request, 'wypozyczalnia/profil.html', {'form': form})

@login_required
def lista_uzytkownikow(request):
    if request.user.typ_uzytkownika != Uzytkownik.ADMINISTRATOR:
        messages.error(request, 'Brak uprawnień!')
        return redirect('strona_glowna')
    
    uzytkownicy = Uzytkownik.objects.all()
    return render(request, 'wypozyczalnia/lista_uzytkownikow.html', {'uzytkownicy': uzytkownicy})