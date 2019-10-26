from django.utils import timezone
from datetime import datetime
from django.db import models

class controle(models.Model):
    TIPO_GASTO =[
        ("Remedio","Remedio"),
        ("Roupa","Roupa"),
        ("Alimentação","Alimentação"),
        ("Educação","Educação"),
        ("Transporte","Transporte"),
        ("Outros","Outros"),
    ]
    PAGAMENTO =[
        ('CAD', 'cartao de debito'),
        ('CAC', 'cartao de credito'),
        ('CRE', 'cartao Crediario'),
        ('CHE', 'cheque'),
        ('DI', 'dinheiro'),
    ]
    data_criacao = models.DateTimeField('Data Criação',auto_now_add=True)
    tipo_despesa = models.CharField('Tipo Despesa',max_length=10,choices=TIPO_GASTO,default='6')
    descricao = models.TextField('Descrição')
    forma_pagamento = models.CharField('forma pagamento',max_length=3,choices=PAGAMENTO,default='DI')
    vencimento = models.DateField('Data vencimento')
    quitacao = models.BooleanField('Quitação')

    class Meta:
        verbose_name_plural = 'Controles de gastos'
        verbose_name = 'Controle de gasto'

    def __str__(self):
        return "{} - {}".format(
            self.data_criacao.strftime('%d/%m/%Y'),
            self.tipo_despesa
        )
    def expira(self):
        data_atual = datetime.now().date()
        data = self.vencimento - data_atual
        if data.days < 0 and self.quitacao == False:
            return 'Fatura vencida!'

        elif data.days < 0 and self.quitacao == True:
            return 'Fatura já foi paga!'

        elif data.days == 0:
            return 'Sua fatura se vence hoje!'

        elif data.days <= 2:
            return 'Fatura com menos de 2 dias para o vencimento, por favor efetuar o pagamento!'

        else:
            return '{} dias para o vencimento'.format(data.days)

    a_vencer = property(expira)
