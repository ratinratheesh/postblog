from django.urls import path
from .views import *

urlpatterns = [
    path('signup_func/', signup_apiview, name='signup_func'),
    path('login_func/', login_apiview, name='login_func'),
    path('logout_func/',logout,name='logout_func'),
]