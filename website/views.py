from django.shortcuts import render
from vagas.models import Vaga

def home(request):
    vagas_disponives = Vaga.objects.all().filter(aberta=True)

    return render(request, 'website/home.html', { 'vagas_disponiveis': vagas_disponives } )


def quemsomos(request):
    return render(request, 'website/quemsomos.html')