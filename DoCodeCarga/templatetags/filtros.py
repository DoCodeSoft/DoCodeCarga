from django import template
register = template.Library()

# Colocar filtros de la aplicacion aqui
@register.filter(name='filtro')
def filtro(registro):
    registros = list()
    return registros

