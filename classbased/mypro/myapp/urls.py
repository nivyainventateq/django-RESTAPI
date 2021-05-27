from django.contrib import admin
from django.urls import path
from myapp.views import simple_api,simple_crud

urlpatterns = [

  path('simple/', view=simple_api,name='simple_api'),
  path('test/<int:id>/', view=simple_crud,name='simple_crud'),
  path('test/', view=simple_crud,name='simple_crud'),

]
