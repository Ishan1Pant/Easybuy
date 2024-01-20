from django.urls import path
from api.views import user_views as views


urlpatterns = [
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('profile/update',views.profile_update,name='profile_update'),
    path('login',views.MyTokenObtainPairView.as_view(),name='token_login'),
    path('delete_user/<str:pk>',views.delete_user,name='delete_user'),
]