from django.urls import path
from .views import *
urlpatterns = [
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register')
]