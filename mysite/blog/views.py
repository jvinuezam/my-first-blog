from django.shortcuts import render
from django.utils import timezone
# el signo . indica el directorio actual o la aplicación actual
from . models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
