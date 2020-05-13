from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.registerPage, name = 'registerPage'),
    path('login/', views.loginPage, name = 'loginPage'),
    path('logout/', views.logoutUser, name = 'logoutUser'),


 
    path('', views.home, name = "home"),
    path('products/', views.products, name = "products"),
    path('user/', views.userPage, name = "userPage"),
    path('settings/', views.settings, name = 'settings'),



    path('customers/<str:pk>', views.customers, name = 'customers'),
    path('createOrder/<str:pk>', views.createOrder, name = 'createOrder'),
    path('updateOrder/<str:pk>/', views.updateOrder, name = 'updateOrder'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name = 'deleteOrder'),






]
