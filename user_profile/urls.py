from django.urls import path

from user_profile.views import login_user

from .views import *

urlpatterns = [
    path('blog_login/', login_user, name='login'),
    path('blog_logout/', logout_user, name='logout'),
    path('register_user/', register_user, name='register_user'),
    path('profile/', profile, name='profile'),
    path('change_profile_picture/', change_profile_picture,
         name='change_profile_picture'),
    path('view_user_information/<str:username>/',
         view_user_information, name="view_user_information"),
]

# first and 2nd row changed from 'login/', 'logout/' into 'blog_login/', 'blog_logout/'
