from django.db import models
from perfil.models import Pessoa

class Departamento(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nome

class Vaga(models.Model):
    nome = models.CharField(max_length=200)
    detalhes = models.TextField()
    aberta = models.BooleanField(default=True)
    data_de_publicacao = models.DateTimeField(auto_now_add=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.nome
    
class Candidatura(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    def __str__(self) :
        return "Candidato %s à vaga: %s" %(self.pessoa.nome, self.vaga.nome)