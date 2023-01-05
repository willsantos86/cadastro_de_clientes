from django import forms
from base.models import Dados

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome', 'email', 'telefone', 'cpf', 'data_nascimento']