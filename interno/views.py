from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime

from interno.forms import CategoriaForm
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
    nome = request.POST.get("nome").strip().captalize()
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
     if request.method == "POST":
        nome = request.POST.get("nome")
        sigla = request.POST.get("sigla")
        estado = models.Estado(
            nome=nome,
            sigla=sigla,
        )
        estado.save()
        return redirect("estados")
   



def estado_apagar(request):
    estado = models.Estado.objects.get(pk=id)
    estado.delete()
    
    return redirect("estados")

def estado_editar(request, id: int):
    estado = models.Estado.objects.get(pk=id)
    if request.method == "GET":
        contexto = {"estado": estado}
        return render(request, "estados/editar.html", context=contexto)

    estado.nome = request.POST.get("nome").strip()
    estado.save()
    return redirect("estados")


def categoria_form_index(request, id: int):
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias": categorias
    }
    return render(request, "categorias_forms/index.html", context=contexto)

def categoria_form_cadastrar(request):
    # Verificando se a request é do tipop POST
    if request.method == "POST":
        # Contruindo o form com os dados que o usuário preencheu
        form = CategoriaForm(request.POST)
        # valida se os dados preenchidos que estão no form são válidos
        if form.is_valid():
            # Criar a categoria nesse caso
            form.save()
            # redirecionar para a lista de categorias
            return redirect("categorias_form")
    # caso da requisição do tipo GET
    else:
        # Criando o form vazio
        form = CategoriaForm()
        # criando o contexto passando o form
        contexto = { 
            "form": form
        }
        # retornar o html do form
        return render(request, "categorias_forms/cadastrar.html", context=contexto)

def categoria_form_apagar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect("categorias_form")

def categoria_form_editar(request, id:int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("categorias_form")
    else:
        form = CategoriaForm(instance=categoria)
    contexto = {
        "form": form,
        "categoria": categoria,
    }
    return render(request, "categorias_forms/editar.html", contexto)


def produto_index(request):
    produtos = models.Produto.objects.all()
    contexto = {"produtos": produtos}
    return render(request, "produtos/index.html", context=contexto)


def produto_cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")
        id_categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        produto = models.Produto(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria_id=id_categoria, 
        )
        produto.save()
        return redirect("produtos")
    categorias = models.Categoria.objects.all()
    contexto = {"categorias": categorias}
    return render(request, "produtos/cadastrar.html", context=contexto)


def produto_apagar(request, id: int):
    produto = models.Produto.objects.get(pk=id)
    produto.delete()
    return redirect("produtos")


def produto_editar(request, id: int):
    produto = models.Produto.objects.get(pk=id)
    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")
        id_categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        produto.nome = nome
        produto.preco = preco
        produto.descricao = descricao
        produto.categoria_id = id_categoria
        produto.save()
        return redirect("produtos")
    
    categorias = models.Categoria.objects.order_by("nome").all()
    contexto = {
        "categorias": categorias,
        "produto": produto,
    }
    return render(request, "produtos/editar.html", contexto)


def cidade_index(request):
    cidades = models.Cidade.objects.all()
    contexto = {"cidades": cidades}
    return render(request, "cidades/index.html", context=contexto)

def cidade_cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        quantidade_habitantes = request.POST.get("quantidade_habitantes")
        clima = request.POST.get("clima")
        data_fundacao = request.POST.get("data_fundacao")
        id_estado = request.POST.get("estado")
        cidade = models.Cidade(
            nome=nome,
            quantidade_habitantes=quantidade_habitantes,
            clima=clima,
            data_fundacao=data_fundacao,
            estado_id=id_estado, 
        )
        cidade.save()
        return redirect("cidades")
    estados = models.Estado.objects.all()
    contexto = {"estados": estados}
    return render(request, "cidades/cadastrar.html", context=contexto)

def cidade_apagar(request, id: int):
    pass

def cidade_editar(request, id: int):
    pass