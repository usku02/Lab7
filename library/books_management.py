import csv
import time
time.strftime('%Y-%m-%d', time.localtime())
def add_book():
    input_ID = input('Wprowadz nowe ID dla ksiazki: ')
    input_author = input('Wprowadz imie i nazwisko autora: ')
    input_title = input('Wprowadz tytul ksiazki: ')
    input_pages = input('Wprowadz liczbe stron ksiazki: ')
    input_created = input('Kiedy powstala ksiazka: ')
    input_updated = str(time.strftime('%Y-%m-%d', time.localtime()))
    new_book = {
        'ID': input_ID,
        'AUTHOR': input_author,
        'TITLE': input_title,
        'PAGES': input_pages,
        'CREATED': input_created,
        'UPDATED': input_updated,
        'AVAILABILITY': '+'
    }
    with open('book.csv', mode='a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(new_book.values())
        csv_file.close()








