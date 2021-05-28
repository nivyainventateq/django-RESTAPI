from django.urls import path

from custapp.views import user_api, user_crud

urlpatterns = [

  path('one/', view=user_api,name='user_api'),
  path('two/<int:id>/', view=user_crud,name='user_crud'),


]