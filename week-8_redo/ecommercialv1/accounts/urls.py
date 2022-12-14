from django.urls import path
from . import views 

urlpatterns = [
    
                        # needed some modifications
    # user login and logouts 
    # path('forget-password/',views.forget_password, name='user_forget_password'),
    # path('login/',views.login, name='login'),
    # path('register/',views.register, name='user_register'),
     
    path('register/',views.register,name='register'),
    path('login/',views.login, name= 'login'),
    path('logout/',views.logout, name= 'logout'),
                        # basic pages
                        
    path('',views.home, name='user_home'),
    path('contact/',views.contact, name='user_contact'),
    path('about/',views.about, name='user_about'),

                         # admin
    #  path('list-users/',views.list_users, name='user_list'),
    path('register/',views.register, name= 'register'),
    path('admin-login/',views.admin_login, name= 'admin_login'),
    path('admin-logout/',views.admin_logout, name= 'admin_logout'),
    path('admin-home/',views.admin_home, name= 'admin_home'),
    path('admin-list-users/',views.admin_list_users, name= 'admin_list_users'),
    path('admin-disable-users/<int:id>',views.admin_user_block, name = 'admin_disable_user'),
    path('admin-enable-users/<int:id>',views.admin_user_enable, name = 'admin_enable_user'),
]