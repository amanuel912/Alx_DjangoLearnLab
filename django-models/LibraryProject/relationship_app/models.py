from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

class BookModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
class LibraryModel(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(BookModel)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(LibraryModel, on_delete=models.CASCADE)