# -*-coding:utf-8-*-
from datetime import datetime
from django.db import models

class Enquete(models.Model):
    pergunta = models.CharField(max_length=100)
    data = models.DateTimeField(default=datetime.now())
    votado = models.IntegerField(default=0,blank=True,null=True)
    def __unicode__(self):
        return self.pergunta

    class Meta:
        verbose_name = 'Enquete'
        verbose_name_plural = 'Enquetes'

class Votacao(models.Model):
    perguntaEnquete = models.ForeignKey(Enquete,null=True)
    foto = models.ImageField(upload_to= 'media')
    opcao = models.CharField(max_length=100,blank=True,null=True)
    quantidadevotos = models.IntegerField(default=0,blank=True,null=True)
    def __unicode__(self):
        return self.opcao

    class Meta:
        verbose_name = 'Votação'
        verbose_name_plural = 'Votações'
