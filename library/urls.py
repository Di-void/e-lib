from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('', views.index, name='home'),
    path('sign-up', RegisterView.as_view(), name='sign-up')
]
