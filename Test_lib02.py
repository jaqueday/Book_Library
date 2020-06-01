"""
This is a test on the book ISBN library for python
JRDay
01/06/2020
"""

from isbnlib import meta
import get_from_user

SERVICE = 'openl'


def get_isbn():
    isbn = get_from_user.any_string('Type the book ISBN: ')
    book = (meta(isbn, SERVICE))
    return book


def main():
    new_book = get_isbn()



main()
