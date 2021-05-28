from django.urls import path

from taskapp.views import user_api, user_crud,loginuser

urlpatterns = [

  path('new/', view=user_api,name='user_api'),
  path('test/<int:id>/', view=user_crud,name='user_crud'),
  path('login/', view=loginuser,name='loginuser'),


]