from django.urls import path , include
from realOwner import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home,name='home'),
    path('items/', views.item_list, name='item_list'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/', include([
        path('profile/', views.profile, name='profile'),
    ])),
    path('items/create/',views.create_item, name='create_item'),
    path('items/edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('users/<str:username>/', views.view_user_profile, name='view_user_profile'),
    path('profile/edit/', views.edit_user_profile, name='edit_user_profile'),
    


]
