from django.db import models

class Endereco(models.Model):
    endereco = models.CharField(max_length=150)
    complemento = models.CharField(max_length=150, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    longitude = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.endereco

