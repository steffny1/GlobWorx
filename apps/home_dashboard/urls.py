from django.urls import re_path, path

from . import views

urlpatterns = [
    path('', views.display_home, name='home')
]
