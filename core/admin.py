
from django.contrib import admin
from core.models import controle

# default: "Administração do Django"
admin.site.site_header = 'Painel de Controle'
# default: "Administração do Site"
admin.site.index_title = 'Recursos'
# default: ”Site de administração do Django"
admin.site.site_title = 'Título HTML do Site'

class controleAdmin(admin.ModelAdmin):
    list_display = (
        'data_criacao','tipo_despesa','vencimento','quitacao','a_vencer'
    )
    list_filter = (
        'vencimento','quitacao',)



    class Meta:
        ordering = ('vencimento', 'forma_pagamento')
admin.site.register(controle,controleAdmin)
