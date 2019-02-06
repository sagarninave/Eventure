from django.contrib import admin
from .models import events
from .models import students

# Register your models here.
admin.site.register(events)
admin.site.register(students)