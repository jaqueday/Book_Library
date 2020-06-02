"""
A Personal Book Library Manager
JRDay
01.06.20
"""

from isbnlib import meta
from isbnlib.dev import DataNotFoundAtServiceError

import get_from_user
import csv
import os
import pandas as pd

SERVICE = 'openl'

library = []
isbn_list = []
csv_columns = ['ISBN-13', 'Title', 'Authors', 'Publisher', 'Year', 'Language']
filename = 'books.csv'

pd.options.display.max_colwidth = 90  # set a value as your need


def menu():
    """ Program main menu"""
    menu = (f"\nBook Library Manager Options"
            f"\n-------------------------------"
            f"\n1. Add book"
            f"\n2. View books added in this session"
            f"\n3. Export books added to CSV"
            f"\n4. Check books in CSV file"
            f"\n9. Exit"
            f"\n>> ")
    menu_choice = get_from_user.positive_int(menu)
    return menu_choice


def read_library():
    """ Check books in
    the library list"""
    for item in library:
        book = item['Title']
        print(f"- {book}")


def add_book():
    """ Get from user
    book ISBN """
    try:
        isbn = get_from_user.any_string('Type the book ISBN: ')
        book = (meta(isbn, SERVICE))
        book_isbn = book['ISBN-13']
        if book_isbn in isbn_list:
            print('Book already in list')
        else:
            library.append(book)
            isbn_list.append(book_isbn)
            print(f"Book: {book['Title']}"
                  f"\nAdded to library, please export to save to file")
    except DataNotFoundAtServiceError:
        print('Book not found in online library')


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


def read_csv():
    """ Use Pandas to
    read CSV file"""
    df = pd.read_csv(filename)
    # dropping ALL duplicte values
    #df.drop_duplicates( keep='first', inplace=True)
    #df.to_csv(filename, index=False)
    print(df['Title'])


def main():
    while True:
        choice = menu()
        if choice == 1:
            add_book()
        elif choice == 2:
            read_library()
        elif choice == 3:
            to_csv(library)
        elif choice == 4:
            read_csv()
        elif choice == 9:
            exit()


main()
