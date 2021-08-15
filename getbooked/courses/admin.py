from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'day',
        'time',
        'places',

    )

admin.site.register(Course, CourseAdmin)