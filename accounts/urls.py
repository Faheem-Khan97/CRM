from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('register/', views.registerPage, name = 'registerPage'),
    path('login/', views.loginPage, name = 'loginPage'),
    path('logout/', views.logoutUser, name = 'logoutUser'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'), name = 'reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_sent.html'), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_new.html'), name = 'password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'), name = 'password_reset_complete'),



 
    path('', views.home, name = "home"),
    path('products/', views.products, name = "products"),
    path('user/', views.userPage, name = "userPage"),
    path('settings/', views.settings, name = 'settings'),



    path('customers/<str:pk>', views.customers, name = 'customers'),
    path('createOrder/<str:pk>', views.createOrder, name = 'createOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name = 'updateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name = 'deleteOrder'),






]
