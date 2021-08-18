from django.urls import path
from .views import BlogDetailView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
