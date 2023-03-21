from django.urls import path, reverse
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('', views.index, name='home'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html', success_url='/'), name='change_password')
]

