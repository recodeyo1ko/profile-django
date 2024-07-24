from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
from .forms import ReplyForm
from django.views import View

# Create your views here.

class QuestionForm(View):

    form_class = QuestionForm
    template_name = 'introduce/form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            question = Question()
            question.name = form.cleaned_data['name']
            question.title = form.cleaned_data['title']
            question.content = form.cleaned_data['content']
            question.save()
            return redirect('introduce:index')
        return render(request, self.template_name, {'form': form})

    
class ReplyForm(View):

    form_class = ReplyForm
    template_name = 'introduce/show.html'

    def get(self, request, id):
        question = Question.objects.get(id=id)
        replies = question.reply_set.all()
        form = self.form_class()
        return render(request, 'introduce/show.html', {'question': question, 'replies': replies, 'form': form, 'id': id})
    
    def post(self, request, *args, **kwargs):
        question_id = self.kwargs['id']
        question = Question.objects.get(id=question_id)
        reply = question.reply_set.create()
        reply.name = request.POST['name']
        reply.content = request.POST['content']
        reply.save()
        return redirect('introduce:reply', id=question_id)


def introduce(request):
    return render(request, 'introduce/introduce.html')

def index(request):
    questions = Question.objects.all()
    return render(request, 'introduce/index.html', {'questions': questions})

