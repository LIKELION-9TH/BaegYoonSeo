"""bgyoons URL Configuration

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
from django.urls import path
import bgapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bgapp.views.home, name="home"),
    path('bgyoon/<str:id>', bgapp.views.detail, name="detail"),
    path('blog/new/', bgapp.views.new, name="new"),
    path('blog/create/', bgapp.views.create, name="create"),
    path('edit/<str:id>', bgapp.views.edit, name="edit"),
    path('update/<str:id>', bgapp.views.update, name="update"),
    path('delete/<str:id>', bgapp.views.delete, name="delete"),
]
