from django.contrib import admin

from .models import *# импоррт моделей из файла

class WomenAdmin(admin.ModelAdmin):#для отображения полей в админ панели
    list_display = ('id', 'title', 'time_create','photo', 'is_published')# заголовки
    list_display_links = ('id','title')#отображение ссылок
    search_fields = ('title','content')# поле поиска
    list_editable = ('is_published',)#галочка и публикация
    list_filter = ('is_published','time_create')#фильтрацию делаем
    prepopulated_fields = ({'slug': ('title',)})# сдаг для админки и заполенеия урл адреса

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = ({'slug':('name',)})
admin.site.register(Women, WomenAdmin)#регистрация в админке
admin.site.register(Category,CategoryAdmin)
# Register your models here.
