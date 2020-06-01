"""
A Personal Book Library Manager
JRDay
01.06.20
"""

from isbnlib import meta
import get_from_user
import csv
import os
import pandas as pd

SERVICE = 'openl'

library = []
csv_columns = ['ISBN-13', 'Title', 'Authors', 'Publisher', 'Year', 'Language']
filename = 'books.csv'


def menu():
    """ Program main menu"""
    menu = (f"\nBook Library Manager Options"
            f"\n-------------------------------"
            f"\n1. Add book"
            f"\n2. View library"
            f"\n3. Export CSV"
            f"\n4. Exit"
            f"\n>> ")
    menu_choice = get_from_user.positive_int(menu)
    return menu_choice


def read_library():
    """ Use of pandas
    to read csv"""
    df = pd.read_csv(filename)
    return df


def add_book():
    """ Get from user
    book ISBN """
    try:
        isbn = get_from_user.any_string('Type the book ISBN: ')
        book = (meta(isbn, SERVICE))
        print(f"Book: {book['Title']}"
              f"\nAdded to library, please export to save to file")
        return book
    except:
        print('Book not found')


def to_csv(library):
    """ Export books
    to a CSV file"""
    with open('books.csv', 'a', newline='') as output:
        # Variable to check if file exists
        file_is_empty = os.stat('books.csv').st_size == 0
        writer = csv.DictWriter(output, fieldnames=csv_columns)
        # if file is empty add header
        if file_is_empty:
            writer.writeheader()
        for item in library:
            writer.writerow(item)


def main():
    while True:
        df = read_library()
        choice = menu()
        if choice == 1:
            book = add_book()
            library.append(book)
        elif choice == 2:
            print(df['Title'])
        elif choice == 3:
            to_csv(library)
        elif choice == 4:
            exit()


main()