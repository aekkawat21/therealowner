from django.urls import path 
from realOwner import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    

    

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('edit_password/',views.edit_password,name='edit_password'),
    path('items/create/',views.create_item, name='create_item'),
    path('items/', views.item_list, name='item_list'),
    path('Trading_history/',views.Trading_history,name='Trading_history'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('edit_Trading_history/',views.edit_Trading_history,name='edit_Trading_history'),
   
    
    path('items/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    
   
   
    


]
