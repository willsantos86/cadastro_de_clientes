from django.db import models

class Dados(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    email = models.EmailField(max_length=75, verbose_name="Email")
    telefone = models.CharField(max_length=14, verbose_name="Telefone")
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name="Data Nascimento")
    data = models.DateTimeField(verbose_name="Data de Criação", auto_now=True)
    observacoes = models.TextField(verbose_name="Observações")
    aprovado = models.BooleanField(verbose_name="Aprovado", default=False, blank=True)
    
    def __str__(self):
        return f'Nome: {self.nome} - Tel: {self.telefone} - Email: {self.email}'
    class Meta:
        verbose_name = "Cadastro de Cliente"
        verbose_name_plural = "Cadastros de Clientes"
        ordering = ['nome']


