from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    data_de_nascimento = models.DateField()
    email = models.EmailField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pessoa", null=True)

    def __str__(self) -> str:
        return self.nome
    
class Emprego(models.Model):
    Pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    nome_da_organizacao = models.CharField(max_length=200)
    data_de_inicio = models.DateField()
    data_de_termino = models.DateField(null=True)
    descricao_das_principais_atividades = models.TextField()

    def __str__(self) -> str:
        return self.nome_da_organizacao
    
    class Meta:
        verbose_name_plural = 'Empregos'

class Formacao(models.Model):
    EM_ANDAMENTO = 'A'
    INTERROMPIDO = 'I'
    SUSPENSO = 'S'
    CONCLUIDO = 'C'
    SITUACAO_DO_CURSO_CHOICES = [
        (EM_ANDAMENTO, 'Em Andamento'),
        (INTERROMPIDO, 'Interrompido/Desistiu'),
        (SUSPENSO, 'Suspenso/Trancado'),
        (CONCLUIDO, 'Concluído')
    ]

    Pessoa = models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    nome_da_instituicao = models.CharField(max_length=200)
    data_de_inicio = models.DateField()
    date_de_termino = models.DateField(null=True)
    situacao_atual_do_curso = models.CharField(max_length=1,choices=SITUACAO_DO_CURSO_CHOICES,default=CONCLUIDO)

    def __str__(self) -> str:
        return self.nome_da_instituicao
    
    class Meta:
        verbose_name = 'Formação'
        verbose_name_plural = 'Formações'