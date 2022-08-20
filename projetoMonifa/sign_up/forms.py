from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']