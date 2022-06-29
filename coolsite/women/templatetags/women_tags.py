from django import template
from women.models import *

register = template.Library()#регистрация собственных тегов

@register.simple_tag(name='getcats')#превращает функцию в тег
def get_categories(filter = None):#фунция тега для возврата значений категорий
    if not filter:

        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html') #возвращает в этот шаблон функцию
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}