from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Estado(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2)
    
class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
class Cidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    quantidade_habitantes = models.DecimalField(max_digits=3,decimal_places=3)
    clima = models.CharField(max_length=40, unique=True)
    data_fundacao = models.CharField(max_length=40, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    
def __str__(self)-> str:
   return f"Nome: {self.nome} Categoria: {self.categoria.nome}"