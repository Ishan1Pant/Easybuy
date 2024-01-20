from django.urls import path 
from api.views import product_views as views 

urlpatterns = [
    path('',views.get_products,name='products'),
    path('<str:pk>/reviews',views.product_reviews,name='product_reviews'),
    path('top',views.top_products,name='top_products'),
    path('<str:pk>',views.product_details,name='product_details'),
]
