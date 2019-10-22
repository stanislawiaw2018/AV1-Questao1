from datetime import timezone

from django.db import models

class controle(models.Model):
    TIPO_GASTO =[
        ("1","Remedio"),
        ("2","Roupa"),
        ("3","Alimentação"),
        ("4","Educação"),
        ("5","Transporte"),
        ("6","Outros"),
    ]
    PAGAMENTO =[
        ('CAD', 'cartao de debito'),
        ('CAC', 'cartao de credito')
        ('CRE', 'cartao Crediario')
        ('CHE', 'cheque'),
        ('DI', 'dinheiro'),
    ]
    data_criacao = models.DateTimeField('Data_Criação',default=timezone.now)
    tipo_despesa = models.CharField('Tipo_Despesa',max_length=1,choices=TIPO_GASTO,default='6')
    descricao = models.TextField('Descrição')
    forma_pagamento = models.CharField('forma_pagamento',max_length=3,choices=PAGAMENTO,default='DI')
    vencimento = models.DateField('Data_vencimento')
    quitacao = models.BooleanField('Quitação')
