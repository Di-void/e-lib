from django.urls import path
from . import views
from .views import SignUpView


urlpatterns = [
    path('', views.index, name='home'),
    path('sign-up/', SignUpView.as_view(), name='sign-up')
]

