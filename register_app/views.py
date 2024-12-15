from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserType1RegistrationForm, UserType2RegistrationForm, CustomAuthenticationForm
from .models import User, Item


def home(request):
    return render(request, 'register_app/home.html')

def register_type1(request):
    if request.method == 'POST':
        form = UserType1RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserType1RegistrationForm()
    return render(request, 'register_app/register_type1.html', {'form': form})

def register_type2(request):
    if request.method == 'POST':
        form = UserType2RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserType2RegistrationForm()
    return render(request, 'register_app/register_type2.html', {'form': form})


from django.shortcuts import redirect


def custom_login(request):
    if request.user.is_authenticated:  # Check if the user is already logged in
        if request.user.user_type == 'type1':
            return redirect('type1_dashboard')
        elif request.user.user_type == 'type2':
            return redirect('type2_dashboard')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.user_type == user_type:
                login(request, user)
                if user_type == 'type1':
                    return redirect('type1_dashboard')
                elif user_type == 'type2':
                    return redirect('type2_dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'register_app/login.html', {'form': form})


@login_required
def type1_dashboard(request):
    utype = request.user.user_type
    if utype == 'type1':
        users_type2 = User.objects.filter(user_type='type2')
        return render(request, 'register_app/type1_dashboard.html', {'users': users_type2, 'name': request.user.username})
    else:
        return redirect('home')

@login_required
def type2_dashboard(request):
    utype = request.user.user_type
    if utype == 'type2':
        items = Item.objects.all()
        return render(request, 'register_app/type2_dashboard.html', {'items': items, 'name': request.user.username})
    else:
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('login')
