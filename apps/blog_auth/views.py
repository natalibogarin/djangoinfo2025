from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroForm

# Create your views here.
def registro(request):
  if request.method=='POST':
    form = RegistroForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = RegistroForm()

  return render(request, "auth/registro.html", {'form':form})

def login(request):
  if request.method=='POST':
    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
      username= form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(username=username, password=password)

      if user:
        login(request, user)
        messages.success(request, f"Bienvenido {username}")
        return redirect('index')
  else:
    form = AuthenticationForm()

  return render(request, 'auth/login.html', {"form":form})

def logout(request):
  logout(request)
  return redirect('index')