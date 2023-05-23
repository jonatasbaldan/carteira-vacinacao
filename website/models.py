from django.db import models
from django.http import HttpResponse


# Create your models here.

class ccv_pessoa(models.Model):
    idpessoa = models.AutoField
    pessoa = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=10)

class ccv_animal(models.Model):
    idanimal = models.AutoField
    nomeanimal = models.CharField(max_length=42)
    raca = models.CharField(max_length=25)
    idpessoa = models.ForeignKey(ccv_pessoa, on_delete=models.CASCADE)
    dt_nascimento = models.DateTimeField()

class ccv_vacinas(models.Model):
    idvacina = models.AutoField
    vacina_nome = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=9, decimal_places=2)


class ccv_agenda(models.Model):
    idagenda = models.AutoField
    dt_agenda = models.DateTimeField(auto_now=True)
    idanimal = models.ForeignKey(ccv_animal, on_delete=models.CASCADE)
    idvacina = models.ForeignKey(ccv_vacinas, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=34)


