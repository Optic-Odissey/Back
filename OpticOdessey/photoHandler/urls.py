from django.urls import path
from . import views
import uuid
from django.conf.urls import handler404


urlpatterns = [
    path('', views.index, name="main" )
]

handler404 = 'photoHandler.views.page_not_found_view'
