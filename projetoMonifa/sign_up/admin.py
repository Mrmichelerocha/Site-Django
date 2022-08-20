from django.contrib import admin

from .models import Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
  list_display = ('username', 'email', 'password1')

admin.site.register(Customer, CustomerAdmin)
