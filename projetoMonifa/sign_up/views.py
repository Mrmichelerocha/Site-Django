from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Customer
from .forms import CustomerForm, CustomerUpdateForm

# Create your views here.
def sign_up(request):
  form = CustomerForm()
  
  if request.method == 'POST':
    form = CustomerForm(request.POST)
    if form.is_valid():
      form.save()

  data = {'formu':form}
  return render(request, 'sign-up.html', data)

def sign_in(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
  
    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Username OR password is incorrect')

  context = {}
  context['db'] = User.objects.all()
  return render(request, 'sign-in.html', context)

def sign_out(request):
  logout(request)
  return redirect('/sign_in/')

def create(request):
  form = CustomerForm(request.POST or None)
  if form.is_valid():
    form.save()

    user = form.cleaned_data.get('username')
    messages.success(request, 'Account was created for ' + user)

    return redirect('/sign_in/')

def view(request, pk):
  data = {}
  data['db'] = User.objects.get(id=pk)
  return render(request, 'view.html', data)

def edit(request, pk):
  form = CustomerUpdateForm()
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = CustomerUpdateForm(request.POST, instance=request.user)
      if form.is_valid():
        messages.success(request, 'Profile Updated!!!')
        form.save()
    else:
      form = CustomerUpdateForm(instance=request.user)

  return render(request, 'edit.html' , {'formu':form})

def delete(request, pk):
  db = User.objects.get(pk=pk)
  db.delete()
  return redirect('/')

def db(request):
  data = {}
  search = request.GET.get('search')

  if search:
    data['db'] = User.objects.filter(username__icontains=search)
  else:
    data['db'] = User.objects.all()
  return render(request, 'db.html', data)