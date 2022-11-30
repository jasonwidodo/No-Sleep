from .models import CoworkingSpace
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

class IndexView(ListView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/posts.html'
    context_object_name = 'posts_list'

class AddView(CreateView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/add.html'
    fields = '__all__'
    success_url = reverse_lazy('coworkingSpace:posts')

class EditView(UpdateView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('coworkingSpace:posts')

class Delete(DeleteView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/confirm-delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('coworkingSpace:posts')
