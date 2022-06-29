from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):# чтобы в селектре было написано категория не выбрана
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Women#связь формы мс моделю вумен
        fields = '__all__' # какие поля нужно отобразить
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),#сделали заголовок вид
            'content': forms.Textarea(attrs={'cols':60, 'rows':10}),#сделали окощшко ввода ширину и длину
        }

    def clean_title(self):# добавили проверку на непревышение 200 символов в заголовке
        # собственный валидатор
        title = self.cleaned_data['title']
        if len(title)>200:
            raise ValidationError('Длина превышает 200 символов')
        return title