from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import datetime


def index(request) -> HttpResponse:
    response = HttpResponse(content="""
    <h1>Olá mundo</h1>
    <a href="contato">Contato</a>
    <a href="/exemplos-basicos/jogo">Jogo</a>
    <a href="/exemplos-basicos/calculadora-form">Calculadora</a>
    """) 
    return response


def contato(request) -> HttpResponse:
    # Obteve o arquivo contato.html e armazenou na variável template
    template = loader.get_template(template_name="contato.html")
    # Renderizar o template armazenando na variável html
    html = template.render(context={}, request=request)
    response = HttpResponse(content=html)
    return response

def jogo(request) -> HttpResponse:
    return render(request, "jogo.html")


def calculadora(request, numero1: int = 3, numero2: int = 8) -> HttpResponse:
    soma = numero1 + numero2
    contexto_dados = {
        "n1": numero1,
        "n2": numero2,
        "soma": soma
    }
    return render(request, "calculadora.html", context=contexto_dados)


def sobre(request) -> HttpResponse:
    return render(request, "sobre.html")


def sobre_form(request) -> HttpResponse:
    nome = request.GET.get("nome")
    sobrenome = request.GET.get("sobrenome")
    idade = int(request.GET.get("idade"))
    peso = float(request.GET.get("peso"))
    altura = float(request.GET.get("altura"))
    
    imc = float(peso / (altura * altura))
    nascimento = 2024- idade
    contexto_dados = {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "nome-completo": nome + sobrenome,
        "nascimento": nascimento,
        "imc": imc
    }
    exercicio = request.GET.get("exercicio")

    match(exercicio):
        case "nome-completo": nome + sobrenome
        case "nascimento": nascimento
        case "imc": imc
    return render(request, "sobre-form.html",context=contexto_dados)
    

def calculadora_form(request):
    if request.method == "POST":
        numero1 = int(request.POST.get("numero1"))
        numero2 = int(request.POST.get("numero2"))
        operacao = request.POST.get("operacao")

        match(operacao):
         case "soma": resultado = numero1 + numero2
         case "subtrair": resultado = numero1 - numero2
         case "multiplicar": resultado = numero1 * numero2
         case "dividir": resultado = numero1 / numero2
    else:
        resultado = None
        
    return render(request, "calculadora-form.html", context={"resultado": resultado})

def calcular(request) -> HttpResponse:
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    operacao = request.GET.get("operacao")

    match(operacao):
        case "somar": resultado = numero1 + numero2
        case "subtrair": resultado = numero1 - numero2
        case "multiplicar": resultado = numero1 * numero2
        case "dividir": resultado = numero1 / numero2
    return HttpResponse(f"Resultado: {resultado}")


def cadastro_form(request) -> HttpResponse:
    return render(request, "cadastro-form.html")

def cadastro(request) -> HttpResponse:
    modelo = (request.POST.get("modelo"))
    ano = int(request.POST.get("ano-fabricacao"))
    preco = float(request.POST.get("preco").replace(".", "").replace(",", "."))
    cor = request.POST.get("cor")
    
    contexto_dados = {
        "modelo": modelo,
        "ano": ano,
        "preco": preco,
        "cor": cor
    }
    return render(request, "cadastro.html", context=contexto_dados)

# Criar uma tela cadastro carro, com os seguintes campos
# modelo input text
# preço input text
# ano fabricação datetime
# cor select

# método: POST
# modelo = request.POST.get("modelo")

# Criar uma tela para visualizar esses daddos