from django.shortcuts import render
from .models import Post


def index(request):
    principais = Post.objects.filter(principal=True)[:2]
    outros_favs = Post.objects.filter(principal=True)[2:]
    posts = Post.objects.filter(principal=False)
    contexto = {
        'posts': posts,
        'principais': principais,
        'favs': outros_favs
    }
    return render(request, 'conteudos/index.html', contexto)
