"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework.authtoken import views
from .views import home


urlpatterns = [
  path('',home,name='api.home'),
  path('worker/',include('api.worker.urls')),
  path('project/',include('api.project.urls')),
  path('info/',include('api.info.urls')),
  path('schedule/',include('api.schedule.urls')),
  path('finance/',include('api.finance.urls')),
]
