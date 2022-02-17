from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def index(request):
    principais = Post.objects.filter(principal=True)[:2]
    outros_favs = Post.objects.filter(principal=True)[2:]
    posts = Post.objects.all().order_by('data_postagem')

    paginator = Paginator(posts, 1)

    pagina = request.GET.get('page')

    posts_por_pagina = paginator.get_page(pagina)

    contexto = {
        'posts': posts_por_pagina,
        'principais': principais,
        'favs': outros_favs
    }
    return render(request, 'conteudos/index.html', contexto)
