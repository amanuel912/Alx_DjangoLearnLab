from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required,login_required
from django.shortcuts import render
from .models import Book
from .forms import ExampleForm


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # logic here
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # logic here
    return render(request, 'edit_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # logic here
    return render(request, 'delete_book.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'view_books.html', {'books': books})

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # You could handle form data here
            name = form.cleaned_data['name']
            return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
