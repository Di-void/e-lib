from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from library.models import Book, Category

from .forms import SearchForm

# Create your views here.

@login_required
def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            searchKey = form.cleaned_data['title']
            books = Book.objects.filter(title__contains=searchKey)
            return render(request, 'books/index.html', {'form': form, 'books': books})
        else:
            form = SearchForm()
    form = SearchForm()
    params = request.GET
    if (params):
        category = params['category']
    else:
        category = 'all'
    
    def formatted_category(item):
        label = item
        value = (str(item)).lower()
        if ('&' in value):
            value = value.replace('&', '%26')

        return (label, value)
        
    if( category == 'all' ):
        books = Book.objects.all()
    else:
        books = Book.objects.filter(category__name__iexact=category)
        print(books)
        

    result = Category.objects.all()    
    categories = list(map(formatted_category, result))
    

    context = {
        'books': books,
        'categories': categories,
        'category': category,
        'form': form
    }

    return render(request, 'books/index.html', context=context)
    
    