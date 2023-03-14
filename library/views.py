from django.shortcuts import render

# Create your views here.

def index(request):
    """View Function for the Landing Page of the Site"""
    return render(request, 'index.html')