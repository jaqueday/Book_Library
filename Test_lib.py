"""
This is a test on the book ISBN library for python
JRDay
01/06/2020
"""

from isbnlib import meta
from isbnlib.registry import bibformatters

SERVICE = 'openl'

# now you can use the service
book1 = '9781593279288'
bibtex = bibformatters['bibtex']
print(bibtex(meta(book1, SERVICE)))


