from django.urls import path
from . import views
import uuid

urlpatterns = [
    path('', views.index ),
    path('/<uuid:id>/', views.result, name='result_page'),
]
