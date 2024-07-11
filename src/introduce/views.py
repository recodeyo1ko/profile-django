from django.shortcuts import render, redirect
from .models import Question

# Create your views here.
def introduce(request):
    return render(request, 'introduce/introduce.html')

def index(request):
    questions = Question.objects.all()
    return render(request, 'introduce/index.html', {'questions': questions})

def form(request):
    return render(request, 'introduce/form.html')

def create(request):
    if request.method == 'POST':
        question = Question()
        question.name = request.POST['name']
        question.title = request.POST['title']
        question.content = request.POST['content']
        question.save()
    return redirect('introduce:index')