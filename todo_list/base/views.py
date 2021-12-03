from django.contrib.auth.models import User
from django.db.models.base import Model
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from base.models import Task, Label, Project, Subtask
from datetime import date, datetime
from .forms import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
"""
Login, Authenticate, Logout
"""

class CustomLoginView(LoginView):
    template_name = 'base/sign-in.html'
    fields= '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'base/sign-up.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

"""
Class and function of model Project 
"""
class CreateProject(LoginRequiredMixin, CreateView):
    model = Project
    fields = ('name', 'due_date')
    success_url = reverse_lazy('index')
    template_name = 'base/add-project.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProject, self).form_valid(form)

class ProjectList(LoginRequiredMixin, ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(user=self.request.user)
        return context

def tasks(request, project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, 'base/project.html', {
        "project": project,
        "tasks": Task.objects.filter(project=project.project_id),
    })

class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Project
    context_object_name = 'project'
    template_name = 'base/project-delete.html'
    success_url = reverse_lazy('index')

class ProjectUpdate(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ('name', 'due_date')
    template_name = 'base/add-project.html'
    success_url = reverse_lazy('index')

"""
Class and function of model Label
"""
class CreateLabel(LoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    success_url = reverse_lazy('index')
    template_name = 'base/add-label.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateLabel, self).form_valid(form)

def task_label(request, label_id):
    label = Label.objects.get(pk=label_id)
    return render(request, 'base/label.html', {
        "label": label,
        "tasks": Task.objects.filter(label=label.label_id),
    })

class LabelDelete(LoginRequiredMixin, DeleteView):
    model = Label
    context_object_name = 'label'
    template_name = 'base/label-delete.html'
    success_url = reverse_lazy('index')

"""
Display page home
"""

class IndexView(LoginRequiredMixin, ListView):
    context_objects_name = 'home_list'
    template_name = 'base/home.html'
    queryset = Project.objects.all()
    today = datetime.now
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(user=self.request.user)

        context['tasks'] = Task.objects.filter(user=self.request.user)

        context['labels'] = Label.objects.filter(user=self.request.user)
        now = datetime.now()
        today = now.strftime("%A, %d %B %Y")
        context['date'] = today
        return context

""" 
Class and function of model Task
"""

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ('name', 'complete', 'description', 'due_date', 'project', 'label')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('name', 'complete', 'description', 'due_date', 'project', 'label')
    success_url = reverse_lazy('index')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')


"""
Control internal page
"""
def settings(request):
    return render(request, 'base/settings.html')

def support(request):
    return render(request, 'base/support.html')

def account(request):
    return render(request, 'base/account.html')