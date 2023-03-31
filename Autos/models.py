from django.db import models

class Auto(models.Model):
  marca = models.CharField(max_length=20,verbose_name='Marca')
  nombre = models.CharField(max_length=30,verbose_name='Nombre')
  modelo = models.IntegerField(verbose_name='Modelo')
  color = models.CharField(max_length=20,verbose_name='Color')
  
  class Meta:
    db_table = 'auto'
  def __str__(self):
    return self.marca

class Cliente(models.Model):
  nombre = models.CharField(max_length=20)
  apellido = models.CharField(max_length=30)
  direccion = models.CharField(max_length=200)
  email = models.EmailField(max_length=100)
  telefono = models.CharField(max_length=20)
  
  class Meta:
    db_table='cliente'

  def __str__(self):
    return self.nombre
  
# from Autos.models import *
# Auto.objects.create(marca='abarth',nombre='spider',modelo=500,color='negro')
# Auto.objects.create(marca='alfa romeo',nombre='mito',modelo=2023,color='blanco')
# Auto.objects.create(marca='aston martin',nombre='vantage',modelo=2022,color='gris')
# Auto.objects.create(marca='audi',nombre='allroad',modelo=2021,color='blanco')
# Auto.objects.create(marca='bentley',nombre='mulsanne',modelo=2022,color='gris')
# Cliente.objects.create(nombre='kenier',apellido='guerrero',direccion='cra 2b #12-65',email='kenier@gmail.com',telefono='+57 3214587456')
# Cliente.objects.create(nombre='jhon',apellido='sanchez',direccion='cra 3b #09-12',email='jhon@gmail.com',telefono='+57 3547845965')
# Cliente.objects.create(nombre='alejo',apellido='vidal',direccion='cra 2b #23-15',email='alejo@gmail.com',telefono='+57 3124789562')
# Cliente.objects.create(nombre='daniel',apellido='isma',direccion='cra 4b #07-15',email='daniel@gmail.com',telefono='+57 3236547895')
# Cliente.objects.create(nombre='breynner',apellido='isgay',direccion='cra 2c #23-05',email='breynner@gmail.com',telefono='+57 3151458745')