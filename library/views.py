from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views import View
from .forms import SignUpForm
from django.contrib.auth.models import Group

# Create your views here.

# Constants
LIBRARY_USERS = 'Library Users'

def index(request):
    """View Function for the Landing Page of the Site"""
    context = {
        'page': 'sign_up',
    }
    return render(request, 'index.html', context=context)

# def signup(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'sign_up.html')

class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'sign_up.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to='/')
        return super(SignUpView, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'page': 'sign_up'})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=LIBRARY_USERS)
            user.groups.add(group)

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})