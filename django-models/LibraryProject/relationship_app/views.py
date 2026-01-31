from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
def list_books(request):
    """
    Display a list of all books in the database.
    """
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    """
    Display details of a specific library, including all books.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
