"""test_dev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from dev_test import views as my_views

urlpatterns = [
    
    # /
    url(r'^$', my_views.home, name='home'),

    # /register
    url(r'^register/$', my_views.register, name='register'),

    # /connection
    url(r'^connect/$', my_views.connect, name='connection'),

    # /deconnection
    url(r'^disconnect/$', my_views.Logout, name='disconnect'),
    
    # /userId
    url(r'^infos/$', my_views.infos, name='infos'),

    url(r'^admin/', include(admin.site.urls)),
]
