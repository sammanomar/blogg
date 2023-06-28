from django.urls import path

from user_profile.views import login_user

from .views import *

urlpatterns = [
    path('blog_login/', login_user, name='login'),
    path('blog_logout/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
]

# first and 2nd row changed from 'login/', 'logout/' into 'blog_login/', 'blog_logout/'
