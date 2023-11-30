from django.contrib import admin
from . import models

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    # Vai exibir um campo em branco a mais para facilitar para cadastrar uma nova variação
    extra = 1

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao_curta', 'preco_formatado', 'preco_promo_formatado']
    inlines = [
        VariacaoInline
    ]

admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
