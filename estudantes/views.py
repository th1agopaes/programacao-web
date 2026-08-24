from django.shortcuts import redirect, render
from django.http import HttpResponse

from estudantes.forms import EstudanteForm
from estudantes.models import Estudante

#-- O arquivo views é onde definimos as nossas regras de negocios

#-- método/função para listagem
#-- de estudantes

def editarEstudantes(request):
    return HttpResponse('<h2> Editando o estudante fulano de tal </h2>')

#-- regra de negócio para adicionar estudante
def adicionarEstudante(request):
    form = EstudanteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    dicionario = {
        'form' : form
    }

    return render(request, 'estudante.html', dicionario)

def listarEstudantes(request):
    estudantes = Estudante.objects.all()
    contexto = {
        'listaEst' : estudantes,
    }

    return render(request, 'listagem.html', contexto)