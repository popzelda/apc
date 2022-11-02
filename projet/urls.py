"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import A
from xml.dom.minidom import Document
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include
from accounts.views import home
from django.shortcuts import redirect, render
from django.conf.urls.static import static
from django.conf import settings
#from accounts.views import  

from projet.settings import MEDIA_URL
def about_site(request):
    return render(request,'about.html')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('maps/',include('maps.urls',namespace='maps')),
    path('about/',about_site,name='about_us'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)