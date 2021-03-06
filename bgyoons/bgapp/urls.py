from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('detail/<str:id>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('hobby/', hobby, name="hobby"),
    path('place/', place, name="place"),
    path('music/', music, name="music"),
    path('picture/', picture, name="picture"),
]