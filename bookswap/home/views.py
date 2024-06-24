from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login  # Renaming to avoid conflict
from django.contrib import messages
from home.models import Input

def create_view(request):
    return render(request, 'create.html')

def Ramcharitramanas(request):
    return render(request, 'Ramcharitramanas.html')

def saves(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        product_description = request.POST.get('product_description')
        
        data = Input(
            name=name,
            address=address,
            contact=contact,
            product_name=product_name,
            product_price=product_price,
            product_description=product_description
        )
        data.save()
        
        template_data = {
            'name': data.name,
            'address': data.address,
            'contact': data.contact,
            'product_name': data.product_name,
            'product_price': data.product_price,
            'product_description': data.product_description
        }
        
    return render(request, 'gargi.html', template_data)


def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')  # Redirect to a different page after registration
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'login.html', {'form': form})

def sid(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('sid')  # Redirect to a different page after login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'sid.html', {'form': form})

def gargi(request):
    return render(request, 'gargi.html')

def cart(request):
    return render(request, 'cart.html')
