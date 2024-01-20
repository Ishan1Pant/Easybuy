from django.urls import path 
from api.views import order_views as views 

urlpatterns = [
    path('add',views.add_order,name='add_order'),
    path('myorder',views.my_order,name='my_orders'),
    path('<str:pk>/pay',views.payment,name='payment'),
    path('<str:pk>',views.get_order,name='get_order'),
]
