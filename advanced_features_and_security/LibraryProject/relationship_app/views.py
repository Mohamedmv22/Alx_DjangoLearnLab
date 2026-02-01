from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from .models import Book, Library, Author
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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


# User registration view
def register(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
from django.contrib.auth.decorators import user_passes_test

# Helper functions to check user roles
def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


# Admin view - accessible only by Admin users
@user_passes_test(is_admin)
def admin_view(request):
    """
    View accessible only to Admin users.
    """
    return render(request, 'relationship_app/admin_view.html')


# Librarian view - accessible only by Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    """
    View accessible only to Librarian users.
    """
    return render(request, 'relationship_app/librarian_view.html')


# Member view - accessible only by Member users
@user_passes_test(is_member)
def member_view(request):
    """
    View accessible only to Member users.
    """
    return render(request, 'relationship_app/member_view.html')

# View to add a book - requires 'can_add_book' permission
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View to add a new book. Only accessible to users with 'can_add_book' permission.
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        author = get_object_or_404(Author, id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('list_books')
    
    authors = Author.objects.all()
    return render(request, 'relationship_app/add_book.html', {'authors': authors})


# View to edit a book - requires 'can_change_book' permission
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    """
    View to edit an existing book. Only accessible to users with 'can_change_book' permission.
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author = get_object_or_404(Author, id=author_id)
        book.save()
        return redirect('list_books')
    
    authors = Author.objects.all()
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'authors': authors})


# View to delete a book - requires 'can_delete_book' permission
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """
    View to delete a book. Only accessible to users with 'can_delete_book' permission.
    """
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})