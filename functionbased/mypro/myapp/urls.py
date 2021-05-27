from django.contrib import admin
from django.urls import path
from myapp.views import Contact_list,Contact_details

urlpatterns = [
  path('test/', view=Contact_list,name='Contact_list'),
  path('test1/<int:pk>/', view=Contact_details,name='Contact_details'),
]
