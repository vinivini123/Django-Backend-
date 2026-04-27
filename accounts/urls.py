from django.urls import path
from .views import register, login, profile, logout

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('profile/', profile),
    path('logout/', logout),
]