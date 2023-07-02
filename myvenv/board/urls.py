from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.detail),
]