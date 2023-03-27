from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.contrib.auth.models import User


from perfil.models import Pessoa
from .models import Vaga, Candidatura

from .forms import CandidatarForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@login_required(login_url='/login')
def candidatarse(request, vaga_id):
    # user = get_object_or_404(User,pk=request.user.id)
    vaga = get_object_or_404(Vaga, pk=vaga_id)

    try:
        pessoa = Pessoa.objects.get(user=request.user)
    except Pessoa.DoesNotExist:
        return redirect("perfil:meus_dados")
    
    
    if not request.user.is_authenticated:
        return redirect("/login");

    if request.method == "POST":
        candidatura = Candidatura.objects.create(pessoa,vaga=vaga)
        candidatura.save()
        return redirect('website:home')
    
    form = CandidatarForm()

    return render(request,'vagas/candidatarse.html',{'vaga': vaga, 'form': form})