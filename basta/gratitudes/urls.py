from django.urls import path
from .views import gratitude_list, gratitude_detail

urlpatterns = [
    path('gratitudes/', gratitude_list),
    path('gratitudes/<int:pk>/', gratitude_detail),
]
