
from django.urls import path
from .views import product_list,product_detail
urlpatterns = [

    path('list/', product_list),
    path('det/<int:pk>/', product_detail)
]
