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
isbn_list = []
csv_columns = ['ISBN-13', 'Title', 'Authors', 'Publisher', 'Year', 'Language']
filename = 'books.csv'


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
        isbn_list.append(item['ISBN-13'])
        print(book, isbn_list)
    return isbn_list

def add_book():
    """ Get from user
    book ISBN """
    isbn = get_from_user.any_string('Type the book ISBN: ')
    book = (meta(isbn, SERVICE))
    book_name = book['Title']
    library.append(book)
    print(f"Book: {book_name}"
          f"\nAdded to library, please export to save to file")



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
        choice = menu()
        if choice == 1:
            add_book()
        elif choice == 2:
            read_library()
        elif choice == 3:
            to_csv(library)
        elif choice == 9:
            exit()


main()