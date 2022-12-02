from django.urls import path
from . import views

app_name = 'coworkingSpace'

urlpatterns = [
    path('coworkingSpace/', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name="add"),
    path('posts/', views.PostsView.as_view(), name="posts"),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
    path('add_favorit/<int:id>/', views.add_favorit, name='add_favorit'),
    path('delete_favorit/<int:id>/', views.delete_favorit, name='delete_favorit'),
]