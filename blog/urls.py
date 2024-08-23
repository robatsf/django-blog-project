from django.urls import path
from .import views
from .views import PostListView,postDetailView,postCeateView,postUpdateview,postDeleteView

urlpatterns = [
    path('',PostListView.as_view(),name='index'),
    path('post/<int:pk>',postDetailView.as_view(),name='blog_detail'),
    path('post/new',postCeateView.as_view(),name='new_post'),
    path('post/<int:pk>/update',postUpdateview.as_view(),name='blog_update'),
    path('post/<int:pk>/delete',postDeleteView.as_view(),name='blog_delete'),
]
