from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Sendingemail
from django.core.mail import send_mail
from .models import Video
from .models import Project, Article
from django.contrib import messages

def home(request):
      return render(request,'home.html')

def articles(request):
      articles = Article.objects.all()
      return render(request, 'article.html', {'articles':articles})

from .models import Project
def dashboard(request):
      projects = Project.objects.all()
      return render(request, 'dashboard.html', {'projects': projects})


def Videos(request):
      ve = Video.objects.all()
      return render (request,'Videos.html',{'ve':ve})




def sendemail(request):
      email_sent = False
      if request.method == 'POST':
            form = Sendingemail(request.POST)
            if form.is_valid():
                  subject = form.cleaned_data['subject']
                  message = form.cleaned_data['message']
                  send_mail(subject, message, 'ibraheemmohammed.673@gmail.com', ['fawzionlinservices@gmail.com'])
                  messages.success(request,'Data sent successfully')
                  return redirect('myhome')

      else:
            form = Sendingemail()
      context = {'form': form, 'email_sent': email_sent}
      return render(request, 'email.html', context=context)