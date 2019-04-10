"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.urls import path
from datetime import datetime
from django.utils import timezone
from django.views.generic.base import TemplateView    #add basic TemplateView to display page(s)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html', extra_context={'now': timezone.now()}), name='home'),
    path('test/', TemplateView.as_view(template_name='test.html', extra_context={'now': timezone.now()}), name='test'),
    path('admin/', admin.site.urls),
]
