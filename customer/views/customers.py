
from django.http import HttpResponse
from customer.notifications import notify_user_via_sms_and_email

from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from customer.models import Customer
from customer.forms import CustomerModelForm


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer-list.html'
    context_object_name = 'customer_list'

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        if search_query:
            return Customer.objects.filter(
                Q(full_name__icontains=search_query) | Q(address__icontains=search_query))
        else:
            return Customer.objects.all()


class AddCustomerView(CreateView):
    form_class = CustomerModelForm
    template_name = 'customer/add-customer.html'
    success_url = reverse_lazy('customers')


class DeleteCustomerView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customers')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Customer successfully deleted')
        return super().delete(request, *args, **kwargs)


class EditCustomerView(UpdateView):
    model = Customer
    form_class = CustomerModelForm
    template_name = 'customer/update-customer.html'
    success_url = reverse_lazy('customers')


def send_sms_view(request):
    phone_number = '+1234567890'
    sms_body = 'Your SMS message here'
    email_subject = 'SMS Sent Notification'
    email_message = 'The following SMS was sent:'
    recipient_email = 'recipient_email@gmail.com'

    notify_user_via_sms_and_email(phone_number, sms_body, email_subject, email_message, recipient_email)

    return HttpResponse('SMS and email notification sent.')

