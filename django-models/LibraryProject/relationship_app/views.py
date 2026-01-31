from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Function-based view to list all books
def list_books(request):
    """
    Display a list of all books in the database.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display library details
class LibraryDetailView(DetailView):
    """
    Display details of a specific library, including all books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

