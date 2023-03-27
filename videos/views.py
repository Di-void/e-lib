from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from library.models import Category, Video

# Create your views here.

@login_required
def index(request):
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

    if (category == 'all'):
        videos = Video.objects.all()
    else:
        videos = Video.objects.all().filter(category__name__iexact=category)

    result = Category.objects.all()
    categories = list(map(formatted_category, result))

    context = {
        'videos': videos,
        'categories': categories,
        'category': category
    }    

    return render(request, 'videos/index.html', context=context)

@login_required
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    categories = video.category.all()
    context = {
        'video': video,
        'categories': categories
    }
    return render(request, 'videos/video_detail.html', context=context)