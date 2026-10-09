
# 🎯 Winly — Losowanie zwycięzców

Winly to prosta aplikacja internetowa do losowania
zwycięzców konkursów z listy uczestników.

## ✨ Funkcje

- 🎲 Losowanie jednego lub wielu zwycięzców
- 👥 Wklejanie listy uczestników
- 🔄 Automatyczne usuwanie duplikatów
- 🏆 Czytelna prezentacja wyników
- 📥 Pobieranie raportu z losowania w formacie JSON
- 🔐 Wykorzystanie generatora losowego
  `secrets.SystemRandom`

## 🚀 Jak korzystać?

1. Otwórz aplikację Winly.
2. Wklej uczestników, po jednej osobie w każdym wierszu.
3. Wybierz liczbę zwycięzców.
4. Kliknij „Losuj zwycięzców”.
5. Wyświetl wyniki lub pobierz raport JSON.

## 🛠️ Technologie

- Python
- Streamlit
- JSON
- SHA-256

## 💻 Uruchomienie lokalne

Zainstaluj zależności:

pip install -r requirements.txt

Uruchom aplikację:

streamlit run app.py
