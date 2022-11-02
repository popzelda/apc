from unicodedata import name
from django.urls import path
from .views import *
app_name='accounts'
urlpatterns = [
 
    
    path('',home,name='home'),
   # path('administration',admine,name='admine'),
    path('singup',creat_us,name='register'),
    path('logout',user_logout,name='logout'),
    path('singin',user_singin,name='login'),
    path('<str:id>',users_profile,name='profile'),
    path('pr/<str:id>',users_req,name='reequette'),
    path('prs/',users_reqe,name='requette'),
    path('up/<str:id>',update_us,name='update_us'),
    path('link/<str:id>',liens,name='liens'),
    path('apc/<str:id>',apc,name='apc'),
    path('admina/<str:id>',del_n,name='del_n'),
    #path('news/<str:id>',news,name='news'),
    #path('weather/<str:id>',index_w,name='index'),

    
]
