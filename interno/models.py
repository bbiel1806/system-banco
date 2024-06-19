from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=100)