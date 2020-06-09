from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from ..models import Pessoa, Endereco

# Create your views here.
@require_http_methods(["GET", "POST"])
def home(request):
    return HttpResponse("Ola, requisição feita com sucesso!")

@csrf_exempt
@require_http_methods(["GET", "POST"])
def listar(request):
    result = Pessoa.objects.all()
    template = loader.get_template('listar.html')
    context = {
        'lista': result,
    }
    return HttpResponse(template.render(context, request))

def detalhar(request, id_pessoa):
    pessoa = Pessoa.objects.get(id = id_pessoa)
    context = {'pessoa': pessoa}
    return render( request, 'detalhar.html', context)

#queryfilterage
def queryfilterage(request):
	pessoa = Pessoa.objects.filter(idade = 40)
	context = {'pessoa': pessoa}
	return render(request, 'detalhar.html', context)

#queryfilterdateofbirth
def queryfilterdateofbirth(request):
	pessoa = Pessoa.objects.filter(data_nascimento = '1980-01-01')
	context = {'pessoa': pessoa}
	return render(request, 'detalhar.html', context)

#queryfilterfirstrecords
def queryfirstrecords(request):
	result = Pessoa.objects.all()[:3]
	template = loader.get_template('listar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

#queryfiltername
def queryfiltername(request):
	pessoa = Pessoa.objects.get(nome__contains='Luiz')
	context = {'pessoa': pessoa}
	return render(request, 'detalhar.html', context)


def excluir(request, id_pessoa):
    try:
        pessoa = Pessoa.objects.get(id = id_pessoa)
        pessoa.delete()
        return HttpResponse (f"Registro: {pessoa.nome} de (id={pessoa.id}) foi excluído com sucesso.")
    except ObjectDoesNotExist:
        return HttpResponse("Pessoa não encontrada")

def cadastro(request):
    genero = ['Masculino','Feminino','Binario','Não informado']
    template = loader.get_template('cadastrar.html')
    context = {
        'genero': genero,
    }
    return HttpResponse(template.render(context, request))

def cadastrar(request):
    dataNascimento = datetime.strptime(request.POST['dataNascimento'], "%d/%m/%Y").date()
	p = Pessoa.objects.nova(
			request.POST['nome'],
			request.POST['idade'],
			dataNascimento,
			request.POST['cpf'],
			request.POST['logradouro'],
			request.POST['numero'],
			request.POST['bairro'],
			request.POST['cep'])

	return HttpResponse(f"{p} cadastrado com sucesso")