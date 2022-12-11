from .models import CoworkingSpace
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect

class IndexView(ListView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/index.html'
    context_object_name = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for x in context['index']:
            if x.favorit.filter(id=self.request.user.id).exists():
                x.is_favorit = True
        return context

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

def add_favorit(request, id):
    try:
        coworkingSpace = CoworkingSpace.objects.get(id=id)
        coworkingSpace.favorit.add(request.user)
        return redirect('/accounts/ruang_favorit/')
    except:
        messages.error(request, 'Error')

    return redirect('/coworkingSpace/')

def delete_favorit(request, id):
    try:
        coworkingSpace = CoworkingSpace.objects.get(id=id)
        coworkingSpace.favorit.remove(request.user)
        return redirect('/accounts/ruang_favorit/')
    except:
        messages.error(request, 'Error')
    
    return redirect('/coworkingSpace/')

class SearchView(TemplateView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/search.html'

class SearchResultsView(ListView):
    model = CoworkingSpace
    template_name = 'coworkingSpace/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = CoworkingSpace.objects.filter(
            Q(nama__icontains=query)
        )

        for x in object_list:
            if x.favorit.filter(id=self.request.user.id).exists():
                x.is_favorit = True

        return object_list

