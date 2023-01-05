from django.shortcuts import render
from base.forms import CadastroForm

# Create your views here.
def cadastrar(request):
    sucesso = False
    if request.method == 'GET':
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            sucesso = True
    contexto = {
        'responsavel': 'William Santos',
        'telefone': '(71) 9 9999-9999',
        'form': form
    }
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'cadastrar.html', contexto)