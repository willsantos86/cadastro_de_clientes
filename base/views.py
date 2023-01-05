from django.shortcuts import render

# Create your views here.
def cadastrar(request):
    contexto = {
        'responsavel': 'William Santos',
        'telefone': '(71) 9 9999-9999'
    }
    return render(request, 'cadastrar.html', contexto)