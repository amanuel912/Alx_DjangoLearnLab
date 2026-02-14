from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CustomUserAdmin
import bookshelf

# Register your models here.
#admin.site.register(bookshelf.models.Book)
admin.ModelAdmin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")

admin.site.register(CustomUser, CustomUserAdmin)