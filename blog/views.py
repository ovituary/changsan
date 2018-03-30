from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.

class PostLV(ListView):
    model = Post
    context_object_name = 'posts'

class PostDV(DetailView):
    model = Post

