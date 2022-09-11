from msilib.schema import Class
from django.db import models

class cliente (models.Model):
    documento=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.CharField(max_length=100)
    celular=models.CharField(max_length=15)
    def __str__(self):
        #return self.documento, self.nombre, self.apellido, self.correo, self.celular
        return f'{self.documento} {self.nombre} {self.apellido} {self.correo} {self.celular}'

class Lineas_De_Credito (models.Model):
    codigo=models.IntegerField(primary_key=True)
    plazo_maximo=models.IntegerField()
    monto_maximo=models.IntegerField()
    def __str__(self):
        return f'{self.codigo} {self.plazo_maximo} {self.monto_maximo}'

class credito (models.Model):
    codigo_credito=models.IntegerField(primary_key=True)
    monto_prestado=models.IntegerField()
    fecha=models.DateField()
    documento=models.ForeignKey(cliente, on_delete=models.CASCADE)
    codigo=models.ForeignKey(Lineas_De_Credito, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.codigo_credito} {self.monto_prestado} {self.fecha} {self.documento} {self.codigo}'