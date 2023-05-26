from django.db import models

# Create your models here.


class ccv_pessoa(models.Model):
    id = models.BigAutoField(primary_key=True)
    pessoa = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=10, null=True, blank=True)


class ccv_animal(models.Model):
    id = models.BigAutoField(primary_key=True)
    nomeanimal = models.CharField(max_length=42)
    raca = models.CharField(max_length=25, null=True, blank=True)
    idpessoa = models.ForeignKey(ccv_pessoa, on_delete=models.CASCADE)
    dt_nascimento = models.DateTimeField(blank=True, null=True)


class ccv_vacinas(models.Model):
    id = models.BigAutoField(primary_key=True)
    vacina_nome = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)


class ccv_agenda(models.Model):
    id = models.BigAutoField(primary_key=True)
    dt_agenda = models.DateTimeField(blank=True, null=True)
    idanimal = models.ForeignKey(ccv_animal, on_delete=models.CASCADE)
    idvacina = models.ForeignKey(ccv_vacinas, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=34, blank=True, null=True)
