from django.contrib import admin

from base.models import *

# Register your models here.
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Label)
admin.site.register(Subtask)

