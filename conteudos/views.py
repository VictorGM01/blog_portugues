from django.shortcuts import render, get_object_or_404
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


def detalhar(request, id_post):
    post = get_object_or_404(Post, pk=id_post)

    contexto = {
        'post': post
    }

    return render(request, 'conteudos/post.html', contexto)


def mapas_mentais(request):
    mapas = Post.objects.all()

    contexto = {
        'mapas': mapas
    }

    return render(request, 'conteudos/mapas_mentais.html', contexto)
