#from django.contrib.auth import forms
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Model Project

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    project_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    create_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    
    def __str__(self):
        return self.name

# Model Label

class Label(models.Model):
    label_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

# Model Task

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    complete = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    create_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True, related_name="taskP")
    label = models.ForeignKey(Label, on_delete=models.CASCADE, null=True, blank=True, related_name='taskL')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['complete']

# Model Subtask

class Subtask(models.Model):
    sub_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)