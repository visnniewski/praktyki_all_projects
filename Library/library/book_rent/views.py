from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm

# Create your views here.
def index(request):
    return render(request, 'book_rent/index.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book_rent:test')
        else:
            messages.info(request, 'Username or password is inncorrect')

    context = {}
    return render(request, 'book_rent/login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('book_rent:login_user')
    context = {'form': form}
    return render(request, 'book_rent/register.html', context)

def test(request):
    return render(request, 'book_rent/index.html', {})