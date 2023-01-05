from django.shortcuts import render
from base.forms import CadastroForm
from base.models import Dados

# Create your views here.
def cadastrar(request):
    sucesso = False
    if request.method == 'GET':
        form = CadastroForm(request.POST or None)
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'responsavel': 'William Santos',
        'telefone': '(71) 9 9999-9999',
        'form': form,
        'sucesso' : sucesso
    }
    return render(request, 'cadastrar.html', contexto)