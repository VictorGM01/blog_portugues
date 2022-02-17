from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    legenda = models.CharField(max_length=200)
    conteudo = RichTextField()
    mapa_mental = models.ImageField(upload_to='imagens/%d/%m')
    data_postagem = models.DateField(default=datetime.today)
    principal = models.BooleanField(default=False)
