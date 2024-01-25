# Nazwa Projektu: FilmRatings

Projekt `FilmRatings` to aplikacja webowa, stworzona z wykorzystaniem frameworka Django, która umożliwia użytkownikom dodawanie recenzji filmów. Aplikacja integruje się z zewnętrznym API, aby dostarczać szczegółowe informacje o filmach, a użytkownicy mogą oceniać filmy, dodawać własne recenzje oraz przeglądać recenzje innych użytkowników.

## Rozpoczęcie pracy

Te instrukcje pomogą Ci uruchomić kopię projektu na swoim lokalnym komputerze do celów rozwoju i testowania. 

### Wymagania wstępne

Przed uruchomieniem projektu, upewnij się, że masz zainstalowane następujące narzędzia:

- Python (3.8+)
- Django (4.2.9+)

### Instalacja

Kroki, aby uruchomić środowisko deweloperskie:

1. Sklonuj repozytorium:
   ```sh
   git clone https://github.com/twoj-repozytorium/twoj-projekt.git
   cd twoj-projekt
   ```
2. Zainstaluj wymagane pakiety:
   ```sh
   pip install -r requirements.txt
   ```
3. Przygotuj bazę danych:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Uruchom serwer deweloperski:
   ```sh
   python manage.py runserver
   ```

Po wykonaniu tych kroków, aplikacja powinna być dostępna pod adresem http://127.0.0.1:8000/.

# Technologie
- Django - Framework webowy użyty w projekcie
- SQLite - Baza danych
- The Movie Database (TMDb) API - Źródło danych o filmach

# Autorzy
Siarhei Hratsli
