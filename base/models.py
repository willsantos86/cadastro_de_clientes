from django.db import models

class Dados(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=14, verbose_name="Telefone")
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    data_nascimento = models.DateField(verbose_name="Data Nascimento")

    class Meta:
        verbose_name_plural = "Dados"

    def __str__(self):
        return f'Dados {self.id}'


