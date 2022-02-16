from django.db import models
from datetime import datetime


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    legenda = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=1000)
    mapa_mental = models.ImageField(upload_to='imagens/%d/%m')
    data_postagem = models.DateField(default=datetime.today)
