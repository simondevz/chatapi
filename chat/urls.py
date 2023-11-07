from django.urls import path

from . import views
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', views.ListUsers.as_view(), name='list_users'),
    path('register/', RegisterView.as_view(), name='register'),
]
