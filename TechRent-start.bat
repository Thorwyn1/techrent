@echo off
echo Uruchamianie serwera Django...

:: Sprawdzenie, czy plik manage.py istnieje
if not exist manage.py (
    echo Błąd: nie znaleziono pliku manage.py w tym folderze.
    pause
    exit /b
)

:: Uruchomienie serwera Django
python manage.py runserver

pause