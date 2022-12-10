from .models import Booking
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(ListView):
    model = Booking
    template_name = 'booking/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Booking
    template_name = 'booking/single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = Booking
    template_name = 'booking/posts.html'
    context_object_name = 'posts_list'

class AddView(CreateView):
    model = Booking
    template_name = 'booking/add.html'
    fields = ['user', 'coworking_space', 'ticket_amount']
    success_url = reverse_lazy('booking:posts')

class EditView(UpdateView):
    model = Booking
    template_name = 'booking/update.html'
    fields = ['user', 'coworking_space', 'ticket_amount']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('booking:posts')

class VerifyView(UpdateView):
    model = Booking
    template_name = 'booking/update_verify.html'
    fields = ['payment_status']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('booking:posts')

class CancelView(UpdateView):
    model = Booking
    template_name = 'booking/update_cancel.html'
    fields = ['booking_status']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('booking:posts')

class Delete(DeleteView):
    model = Booking
    template_name = 'booking/confirm-delete.html'
