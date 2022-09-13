from django.urls import path
from . import views 

urlpatterns = [
    path('admin-login/',views.admin_login, name= 'admin_login'),
    path('admin-logout/',views.admin_logout, name= 'admin_logout'),
    path('',views.admin_home, name= 'admin_home')
]