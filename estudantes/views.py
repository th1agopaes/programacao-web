from django.shortcuts import render
from django.http import HttpResponse

#-- O arquivo views é onde definimos as nossas regras de negocios

#-- método/função para listagem
#-- de estudantes

def listarEstudantes(request):
    return HttpResponse('<h2> Olá estudantes, está é a listagem </h2>')

def editarEstudantes(request):
    return HttpResponse('<h2> Editando o estudante fulano de tal </h2>')