from django.contrib import admin
from Polls.models import Enquete, Votacao

class AdminVotacaoOpcao(admin.TabularInline):
    model = Votacao
    extra = 2

class AdminEnquete(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': ['pergunta','data','votado']}),
    ]
    inlines = [AdminVotacaoOpcao]

admin.site.register(Enquete,AdminEnquete)
