from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView

# Create your views here.

class PostLV(ListView):
    model = Post
    context_object_name = 'posts'

