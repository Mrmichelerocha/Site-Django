from django.shortcuts import render

# Create your views here.
def produto(request):
  return render(request, 'products.html')