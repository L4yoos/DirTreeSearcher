# DirTreeSearcher

DirTreeSearcher to skrypt w Pythonie, który wyświetla strukturę katalogów w formie drzewa, z opcjami filtrowania plików według rozszerzeń, ograniczania głębokości rekurencji, wyszukiwania konkretnych plików oraz zapisywania wyników do pliku. Skrypt używa ANSI escape codes do kolorowania wyjścia, co ułatwia czytanie i nawigację po strukturze katalogów.

## Funkcje

- Wyświetlanie struktury katalogów w formie drzewa.
- Ograniczenie głębokości rekurencji.
- Filtrowanie plików według rozszerzeń.
- Wyszukiwanie plików zawierających podaną nazwę lub wzorzec.
- Zapisywanie wyników do pliku.
- Kolorowanie wyjścia za pomocą ANSI escape codes.

### list_files(startpath, indent='', depth=None, file_filter=None, search=None)**:

- Wyświetla strukturę katalogów w formie drzewa.
- startpath (str): Katalog początkowy.
- indent (str): Wcięcie używane do formatowania wyjścia (domyślnie '').
- depth (int, opcjonalnie): Maksymalna głębokość rekurencji (domyślnie None, czyli bez ograniczeń).
- file_filter (str, opcjonalnie): Filtrowanie plików według rozszerzeń (np. '.txt').
- search (str, opcjonalnie): Wyszukiwanie plików zawierających podaną nazwę lub wzorzec.

## Uruchamianie skryptu

- **Podstawowe uruchomienie**:
   ```bash
   python dirTreeSearcher.py /sciezka/do/katalogu
   ```
   ```bash
   python dirTreeSearcher.py /sciezka/do/katalogu -d 2
   ```
   ```bash
   python dirTreeSearcher.py /sciezka/do/katalogu -f .txt
   ```
   ```bash
   python dirTreeSearcher.py /sciezka/do/katalogu -s nazwa_pliku
   ```
   ```bash
   python dirTreeSearcher.py /sciezka/do/katalogu -o output.txt
   ```
   ```bash
   python dirTreeSearcher.py /sciezka/do/katalogu -d 2 -f .txt -s nazwa_pliku -o output.txt
   ```

## Przykładowa struktura katalogów
   ```bash
    ├── folder1/
    │ ├── file1.txt [2023-07-06 12:34:56]
    │ └── file2.py [2023-07-06 12:34:56]
    └── folder2/
    ├── file3.txt [2023-07-06 12:34:56]
    └── file4.md [2023-07-06 12:34:56]
   ```
