from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    principais = Post.objects.filter(principal=True)[:2]
    outros_favs = Post.objects.filter(principal=True)[2:]
    posts = Post.objects.all().order_by('-data_postagem')
    tema = request.GET.get('tema')

    if tema:
        posts_pesquisa = Post.objects.filter(Q(titulo__icontains=tema) | Q(legenda__icontains=tema))
        return render(request, 'conteudos/resumos_e_mapas.html', {'todos': posts_pesquisa})

    paginator = Paginator(posts, 2)

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
    tema = request.GET.get('tema')

    if tema:
        posts_pesquisa = Post.objects.filter(Q(titulo__icontains=tema) | Q(legenda__icontains=tema))
        return render(request, 'conteudos/mapas_mentais.html', {'mapas': posts_pesquisa})

    contexto = {
        'mapas': mapas
    }

    return render(request, 'conteudos/mapas_mentais.html', contexto)


def resumos(request):
    resumo = Post.objects.all()
    tema = request.GET.get('tema')

    if tema:
        posts_pesquisa = Post.objects.filter(Q(titulo__icontains=tema) | Q(legenda__icontains=tema))
        return render(request, 'conteudos/resumos.html', {'resumos': posts_pesquisa})

    contexto = {
        'resumos': resumo
    }

    return render(request, 'conteudos/resumos.html', contexto)


def resumos_e_mapas(request):
    todos = Post.objects.all()
    tema = request.GET.get('tema')

    if tema:
        posts_pesquisa = Post.objects.filter(Q(titulo__icontains=tema) | Q(legenda__icontains=tema))
        return render(request, 'conteudos/resumos_e_mapas.html', {'todos': posts_pesquisa})

    contexto = {
        'todos': todos
    }

    return render(request, 'conteudos/resumos_e_mapas.html', contexto)


def criadores(request):
    return render(request, 'conteudos/criadores.html')
