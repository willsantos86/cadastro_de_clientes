from django.contrib import admin
from django.contrib import messages

from base.models import Dados

@admin.action(description='Marcar Cadastros de Clientes como aprovados')
def marcar_como_aprovado(modeladmin, request, queryset):
    queryset.update(aprovado=True)
    modeladmin.message_user(request,'Cadastro(s) de Cliente(s) marcado(s) como aprovado(s)', messages.SUCCESS)


@admin.register(Dados)
class DadosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone', 'cpf', 'data_nascimento', 'aprovado']
    search_fields = ['nome', 'cpf']
    list_filter = ['nome', "aprovado"]
    actions = [marcar_como_aprovado]
