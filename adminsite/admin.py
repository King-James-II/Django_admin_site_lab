# Import necessary modules from Django
from django.contrib import admin
from .models import Course, Instructor, Lesson

# Define an inline class for Lesson model
class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5

# Define custom admin classes for Course and Instructor models
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

# Register the custom admin classes for Course and Instructor models
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)