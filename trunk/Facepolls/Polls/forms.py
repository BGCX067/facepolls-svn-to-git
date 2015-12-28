from Polls.models import Enquete, Votacao

__author__ = 'Wouker'
from django import forms

class EnqueteForm(forms.ModelForm):
    class Meta:
        model=Enquete
        exclude = ('data','votado')

class VotacaoForm(forms.ModelForm):
    class Meta:
        model = Votacao
        foto = forms.ImageField
        exclude = ('perguntaEnquete','quantidadevotos')