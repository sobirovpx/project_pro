from django.urls import path

from customer.views.auth import login_page, logout_page, register_page
from customer.views.customers import CustomerListView, AddCustomerView, DeleteCustomerView, EditCustomerView

urlpatterns = [
     path('customers/', CustomerListView.as_view(), name='customers'),
     path('add_customer/', AddCustomerView.as_view(), name='add_customer'),
     path('delete_customer/<int:pk>/', DeleteCustomerView.as_view(), name='delete_customer'),
     path('edit_customer/<int:pk>/', EditCustomerView.as_view(), name='edit_customer'),
     path('login-page/', login_page, name='login'),
     path('logout-page/',logout_page,name='logout'),
     path('register-page/', register_page, name='register')

]
