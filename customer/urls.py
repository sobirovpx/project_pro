from django.urls import path

from customer.views import customers
from customer.views.auth import login_page, logout_page, register_page, LoginPageView, LoginPage, RegisterFormView
from customer.views.customers import add_customer, delete_customer, edit_customer

urlpatterns = [
    path('customer-list/', customers, name='customers'),
    path('add-customer/', add_customer, name='add_customer'),
    path('customer/<int:pk>/delete', delete_customer, name='delete'),
    path('customer/<int:pk>/update', edit_customer, name='edit'),
    path('login-page/', LoginPage.as_view(), name='login'),
    path('logout-page/', logout_page, name='logout'),
    path('register-page/', RegisterFormView.as_view(), name='register'),
]