from django.db import models
from django.apps import apps

# Create your models here.
class PessoaDAO(models.Manager):
	def retorna_C(self):
    		return self.filter(nome__startswith="C")

	def nova(self, nome, idade, dataNascimento, cpf,
		logradouro, numero, bairro, cep):
		p = Pessoa(nome=nome, idade=idade,
			dataNascimento = dataNascimento, cpf = cpf)
		end = Endereco(pessoa=p,
			logradouro=logradouro, numero=numero,
			bairro=bairro, cep=cep)
		p.save()
		end.save()
		return p

class Pessoa(models.Model):
    cpf = models.CharField('CPF', max_length=11, unique=True)
    nome = models.CharField(max_length=200)
    dataNascimento = models.DateField(null = True)
    idade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} (id={self.id})"
    
    def detalhar(self):
        result = Endereco.objects.get(pessoa__id=self.id)
        if(result):
            return result

    objects = PessoaDAO()

class Endereco(models.Model):
	pessoa = models.ForeignKey("Pessoa", on_delete=models.CASCADE)
	logradouro = models.CharField(max_length=200)
	numero = models.IntegerField()
	bairro = models.CharField(max_length=100,null=True)
	cep = models.CharField(max_length=9)
	
	def __str__(self):
		detalhar = f"""{self.logradouro}, {self.numero}.
			Bairro {self.bairro}. CEP: {self.cep}
		"""
		return detalhar