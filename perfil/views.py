from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .forms import PessoaForm

from .models import Pessoa

class CreatePersonView(LoginRequiredMixin, generic.CreateView):
    login_url = "/login"
    template_name = 'perfil/index.html'
    context_object_name = 'pessoa'
    model = Pessoa
    form_class = PessoaForm
    success_url = 'perfil.edit'

    def form_valid(self, form: PessoaForm) -> HttpResponseRedirect:
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())        

class UpdatePersonView(LoginRequiredMixin, generic.UpdateView):
    login_url = "/login"
    template_name = 'perfil/index.html'
    context_object_name = 'pessoa'
    model = Pessoa
    form_class = PessoaForm
    success_url = 'perfil.edit'

    def get_queryset(self):
        return self.request.user.pessoa.all()

@login_required(login_url='/login')
def index(request):

    try:
        pessoa = Pessoa.objects.get(user=request.user)
    except Pessoa.DoesNotExist:
        pessoa = Pessoa()
        pessoa.user = request.user

    if request.method == "POST":
        form = PessoaForm(request.POST or None, instance=pessoa)
        
        if form.is_valid():
            form.save()

        return redirect("/perfil")
    else:
        form = PessoaForm(instance=pessoa)

    return render(request,'perfil/index.html',{'form': form})
