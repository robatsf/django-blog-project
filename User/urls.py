from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('profile/profile_update',views.profile_update,name='profile_update'),
    path('logout/',views.logout_users,name='logout'),
]
