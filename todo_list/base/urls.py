from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import IndexView, RegisterPage, TaskDetail, CreateTask, TaskUpdate, TaskDelete, CustomLoginView, TaskList, ProjectList, task_label, tasks, settings, support,account, CreateProject, CreateLabel, ProjectDelete, LabelDelete, ProjectUpdate


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', IndexView.as_view(), name='index'),
    path('project/<int:project_id>/', tasks, name='tasks-project-list'),
    path('task-create/', CreateTask.as_view(), name="task-create"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete"),
    path('setting/', settings, name='setting'),
    path('support/', support, name='support'),
    path('account/', account, name='account'),
    path('project-create/', CreateProject.as_view(), name='project-create'),
    path('label-create', CreateLabel.as_view(), name='label-create'),
    path('project-delete/<int:pk>', ProjectDelete.as_view(), name='project-delete'),
    path('label/<int:label_id>/', task_label, name='tasks-label-list'),
    path('label-delete/<int:pk>', LabelDelete.as_view(), name='label-delete'),
    path('project-update/<int:pk>/', ProjectUpdate.as_view(), name="project-update"),
]