from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models 
def home(request):
    return render(request, "home_setup.html")


def categoria_index(request):
    # Consultar os registros da tabela de categorias
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias": categorias
    }
    return render(request, "categorias/index.html", context=contexto)


def categoria_cadastrar(request):
    if request.method == "GET":
        return render(request, "categorias/cadastrar.html")
    # Obtendo os dados que o usuário preencheu nos campos
    nome = request.POST.get("nome").strip()
    # instanciando um objeto da classe Categoria
    # preenchendo os atributos (nome)
    categoria = models.Categoria(nome=nome)
    # Executando a rotin a de criar o registrro na tabela de Categorias (INSERT INTO)
    categoria.save()
    # redirecionar para lista de categorias
    return redirect("categorias")

# /categoria/apagar/<id>
def categoria_apagar(request, id: int):
    # Buscar a categoria que contém o id que veio na rota
    categoria = models.Categoria.objects.get(pk=id)
    # DELETE From categorias WHERE id = 2
    # Executar o delete na tabela de categoria filtrando por id
    categoria.delete()
    # Redireciona para a tela de listagem de categorias
    
    return redirect("categorias")
    


def categoria_editar(request, id:int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "GET":
        contexto = {"categoria": categoria}
        return render(request, "categorias/editar.html", context=contexto)

    categoria.nome = request.POST.get("nome").strip()
    categoria.save()
    return redirect("categorias")

def estado_index(request):
    estados = models.Estado.objects.all()
    contexto_estados = {
        "estados": estados
    }
    return render(request, "estados/index.html", context=contexto_estados)



def estado_cadastrar(request):
    if request.method == "GET":
        return render(request, "estados/cadastrar.html")
    
    nome = request.POST.get("nome").strip()
    estado = models.Estado(nome=nome)
    estado.save()
    
    return redirect("estados")


def estado_apagar(request):
    estado = models.Estado.objects.get(pk=id)
    estado.delete()
    
    return redirect("estados")

def estado_editar(request):
    estado = models.Estado.objects.get(pk=id)
    if request.method == "GET":
        contexto = {"estado": estado}
        return render(request, "estados/editar.html", context=contexto)

    estado.nome = request.POST.get("nome").strip()
    estado.save()
    return redirect("estados")