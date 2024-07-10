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
        name = request.POST['name']
        title = request.POST['title']
        content = request.POST['content']
        question = Question(name=name, title=title, content=content)
        question.save()
        questions = Question.objects.all()
        return render(request, 'introduce/index.html', {'questions': questions})
    return render(request, 'introduce/form.html')