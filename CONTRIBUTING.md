# Zasady współpracy
Dziękujemy za zainteresowanie projektem! Aby współpraca była przejrzysta, efektywna i przyjemna dla każdego, prosimy o zapoznanie się z poniższymi zasadami.

## Przygotowanie projektu
1. Sklonuj repozytorium
```bash
git clone https://github.com/USER/REPO.git
```

2. Przejdź do katalogu projektu:
```bash
cd REPO
```

3. Utwórz wirutalne środowisko
```bash
python -m venv .venv
```

4. Aktywuj śrpdpwoslp o zainstaluj zależności, jeżeli projekt zawiera plik requirements.txt
```bash
..venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Praca z gałęziami
- **NIE WPROWADZAJ** zian bezpośredniona gałęzi *main*
- do każdego zadania utwórz osobą gałąź
- stosuj czytelne nazwy gałęzi:
  - feature/add-task - nowa funkcjonalność
  - docs/update-readme - zmiany w dokumentacji
    
## Zasady pisania kodu
- stosuj czytelne nazwy zmiennych i funkcji
- przestrzegaj podstawowych zasad **PEP 8**
- dodawaj komentarze tam, gdzie wymagane są wyjaśnienia
- nie powielaj kodu (zasada DRY)
- nie pisz kodu na zapas (zasada YAGNI
- **przed wysłaniem zmian sprawdź, czy program działa poprawnie**
   
## Commity
Każdy commit powinien zawierać krótkii zrozumiały opis zmian w trybie rozkazującym. Przykłady:
```bash
git commit -m"feat: dodaj zadanie..."
git commit -m"fix: popraw element input"
git commit -m"docs: zaktualizuj readme.md"
```
  
## Zgłoszenia (Issues)
...

## Pull Requests
...

## Komunikacja w zespole
- szanuj pozostałych uczestników projektu
- informuj zespół o problemach i opóźnieniach
- omawiaj istotne zmiany przed ich wprowadzeniem
- korzystaj Issue i Pull Request do dyskusji dotyczących projektu

**Dziękujemy za współpracę i wkład w rozwój projektu**
