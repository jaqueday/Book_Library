"""
This is a test on the book ISBN library for python
JRDay
01/06/2020
"""

from isbnlib import meta

SERVICE = 'openl'

book1 = '9781593279288'
print(meta(book1, SERVICE))
