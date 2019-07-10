# users/urls.py
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.UserListView.as_view()),
    path('create/', views.UserCreate.as_view(), name='users-create'),
]
