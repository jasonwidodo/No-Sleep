from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('booking/', views.IndexView.as_view(), name='index'),
    path('booking/<int:pk>', views.SingleView.as_view(), name='single'),
    path('booking/add/', views.AddView.as_view(), name="add"),
    path('booking/posts/', views.PostsView.as_view(), name="posts"),
    path('booking/edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('booking/verify/<int:pk>/', views.VerifyView.as_view(), name='verify'),
    path('booking/cancel/<int:pk>/', views.CancelView.as_view(), name='cancel'),
    path('booking/delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]