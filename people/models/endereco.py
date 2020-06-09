from django.db import mode
from django.apps import ap

# Create your models here.
class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100, null=True)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.nome} (id={self.id})"

    def detalhar(self):
        result = Endereco.objects.filter(pessoa__id = self.id)
        if(result):
            return result[0]