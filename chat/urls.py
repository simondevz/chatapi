from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.ListAvailableUsers.as_view(), name='users')
]
