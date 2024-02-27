# import
from django.shortcuts import render

# Create views here
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cat_index(request):
  return render(request, 'cats/index.html', {'cats': cats})