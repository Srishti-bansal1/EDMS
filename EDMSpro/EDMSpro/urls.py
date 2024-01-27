"""
URL configuration for EDMSpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin

from EDMSapp import views

from rest_framework.routers import DefaultRouter
from django.urls import path,include
from EDMSapp.view import EDMSViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'Edms',EDMSViewSet, basename='Edms')

urlpatterns =[
    path('admin/', admin.site.urls),
    path('add/', views.EDMScreate),
    #path('list/', views.list),
    #path('update/<int:pk>', views.update),
    #path('modify/<int:pk>', views.modify),
    #path('delete/<int:pk>', views.destroy),
    
    path('edms/',include(router.urls))
]


