from django.urls import path
from . import views
urlpatterns = [
    path('su/',views.signup,name='signup'),
    path('ul/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('cp/',views.user_cpwd,name='cpwd'),
    path('cp1/',views.user_cpwd1,name='cpwd1'),
    path('',views.home),
]
