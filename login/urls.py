from django.conf.urls import url
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'verify',verify),
    url(r'generate',generatePassword),
    url(r'createPassword/(?P<faculty_id>\w+)',createPassword),
    url(r'auth',auth_view),
    url(r'login',login),
    url(r'changeUser',changeUser),
    url(r'change',change),
    url(r'logout',logout),
    url(r'',login)
]