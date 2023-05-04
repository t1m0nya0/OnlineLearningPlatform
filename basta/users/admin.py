from django.contrib import admin

from .models import User
from courses.models import Course, Category


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(User)
