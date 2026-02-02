import models
all_books = models.Book.objects.filter(author__name="Specific Author Name")
for book in all_books:
    print(book.title)
#List all books in a library.
library = models.Library.objects.get(name="Specific Library Name")
for book in library.books.all():
    print(book.title)
#Retrieve the librarian for a library###
librarian = models.Librarian.objects.get(library__name="Specific Library Name")
print(librarian.name) 