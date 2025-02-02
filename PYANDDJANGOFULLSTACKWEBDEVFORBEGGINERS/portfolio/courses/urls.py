from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.detail, name='detail'),
]