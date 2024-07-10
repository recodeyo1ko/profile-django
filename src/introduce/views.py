from django.shortcuts import render

# Create your views here.
def introduce(request):
    return render(request, 'introduce/introduce.html')

def index(request):
    return render(request, 'introduce/index.html')

def form(request):
    return render(request, 'introduce/form.html')
