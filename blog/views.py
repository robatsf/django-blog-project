from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin



class PostListView(LoginRequiredMixin, ListView):
  model=Post
  template_name='blog/index.html'
  context_object_name='posts'
  ordering=["-date_posted"]


class postDetailView(LoginRequiredMixin, DetailView):
  model=Post


class postCeateView(LoginRequiredMixin, CreateView):
  model=Post
  fields=['title','content']

  def form_valid(self,form):
    form.instance.author=self.request.user
    return super().form_valid(form)
  
  
class postUpdateview(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
  model=Post
  fields=['title','content']

  def form_valid(self,form):
    form.instance.author=self.request.user
    return super().form_valid(form)
  
  def test_func(self):
    post=self.get_object()
    if self.request.user==post.author:
      return True
    return False
  
class postDeleteView(DeleteView):
  model=Post
  success_url='/'
  
  def test_func(self):
    post=self.get_object()
    if self.request.user==post.author:
      return True
    return False