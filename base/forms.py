from django import forms

class CadastroForm(forms.Form):
    Nome = forms.CharField()
    email = forms.EmailField()
    telefone = forms.CharField()
    cpf = forms.CharField()
    data_nascimento = forms.DateField()
    observacoes = forms.CharField(widget=forms.Textarea)