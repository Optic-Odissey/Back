from django.urls import path
from . import views
import uuid

urlpatterns = [
    path('', views.index, name="main" )
]
