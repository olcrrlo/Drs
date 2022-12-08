"""Experiment URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from ex01 import views
from django.conf.urls import url

# 다은 실험 페이지로 이동

urlpatterns = [
   path('', views.intro, name='intro'),
   path('p1/', views.p1, name='p1'),
   path('p2/', views.p2, name='p2'),
   path('p3/', views.p3, name='p3'),
   path('p4/', views.p4, name='p4'),
   path('p5/', views.p5, name='p5'),
   path('p6/', views.p6, name='p6'),

]
