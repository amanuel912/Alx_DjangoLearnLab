from django.contrib import admin
from .models import Book
import bookshelf

# Register your models here.
admin.site.register(bookshelf.models.Book)
admin.ModelAdmin