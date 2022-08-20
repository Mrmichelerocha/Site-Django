from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from .models import Customer
from .forms import CustomerForm

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

# def view(request, pk):
#   data = {}
#   data['db'] = Customer.objects.get(pk=pk)
#   return render(request, '#', data)

# def edit(request, pk):
#   data = {}
#   data['db'] = Customer.objects.get(pk=pk)
#   data['formu'] = CustomerForm(instance=data['db'])
#   return render(request, '#', data)

# def update(request, pk):
#   data = {}
#   data['db'] = Customer.objects.get(pk=pk)
#   form = CustomerForm(request.POST or None, instance=data['db'])
#   if form.is_valid():
#     form.save()
#   return redirect('/')

# def delete(request, pk):
#   db = Customer.objects.get(pk=pk)
#   db.delete()
#   return redirect('/')