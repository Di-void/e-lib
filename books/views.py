from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from library.models import Book, Category

# Create your views here.

@login_required
def index(request):
    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'books/index.html', context=context)