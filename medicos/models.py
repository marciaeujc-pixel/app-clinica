from django.db import models

# Create your models here.
class Medico(models.Model):
    idmedico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    especializacao = models.CharField(max_length=50)
    crm = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome} - {self.especializacao} - {self.crm}"
