from django.urls import path, include
from rest_framework import routers

from .views import *


router_courses = routers.SimpleRouter()
router_courses.register(r'courses', CourseViewSet)
router_categories = routers.SimpleRouter()
router_categories.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('category/<int:cat_id>/courses/', CourseByCategoryList.as_view()),
    path('', include(router_courses.urls)),
    path('', include(router_categories.urls)),
]
