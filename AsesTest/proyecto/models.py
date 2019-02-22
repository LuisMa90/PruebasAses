from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Contratista(models.Model):
    contratista = models.CharField(verbose_name="Razon social del Contratista", max_length=200)

    class Meta:
        verbose_name = "Contratista"
        verbose_name_plural = "Contratistas"
    
    def __str__(self):
        return self.contratista

class Promovete(models.Model):
    promovente = models.CharField(verbose_name="Razon social del Promovente", max_length=200)
    contratista = models.ForeignKey(Contratista,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Promovente"
        verbose_name_plural = "Promoventes"
    
    def __str__(self):
        return self.promovente
          

class Estudios(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Estudio", max_length=200)
    fecha_de_inicio = models.DateField(verbose_name="Fecha de inicio")
    fecha_de_entrega = models.DateField(verbose_name="Fecha de entrega")
    opc = (("mia","MIA"),("etj","ETJ"),("po","POEL"),("poet","POET"),("pdu","PDU"),("pac","PACMUN"),("scoo","SCOOPING"),("scr","SCREENING"))
    tipo = models.CharField(max_length=20,choices=opc,default='mia')
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    tareas = models.TextField(verbose_name="Tareas")

    class Meta:
        verbose_name = "Estudio"
        verbose_name_plural = "Estudios"
    
    def __str__(self):
        return self.nombre

class TiposProyectos(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Tipo de Proyecto", max_length=200)

    class Meta:
        verbose_name = "Tipo de Proyecto"
        verbose_name_plural = "Tipos de Proyectos"
    
    def __str__(self):
        return self.nombre

class Proyectos(models.Model):
    nombre = models.CharField(verbose_name="Nombre del Proyecto", max_length=200)
    promoventes = models.ForeignKey(Promovete,on_delete=models.CASCADE)
    contratistas =  models.ForeignKey(Contratista,on_delete=models.CASCADE)
    fecha_de_inicio = models.DateField(verbose_name="Fecha de inicio")
    tipo_de_proyecto =  models.ForeignKey(TiposProyectos,on_delete=models.CASCADE)
    estudios = models.ManyToManyField(Estudios,verbose_name="Estudios")
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
    
    def __str__(self):
        return self.nombre

