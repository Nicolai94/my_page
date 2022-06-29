from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy

from .forms import AddPostForm
from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .utils import *

menu =[
    {'title':'О сайте', 'url_name': 'about'},
    {'title':"Добавить статью", 'url_name': 'add_page'},
    {'title':"Обратная связь", 'url_name': 'contact'},
    {'title':"Войти", 'url_name': 'login'},

]

class WomenHome(DataMixin,ListView):#класс представлений и отвечате за главную страницу
    model = Women#назначаем модель
    template_name = 'women/index.html' # указываем путь к файлу
    context_object_name = 'posts' # указываем имя файла

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)#обращаемся к базовому и получаем параметры
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items())+list(c_def.items()))


    def get_queryset(self):# указать что именно выбирть и отображать из списка
        return Women.objects.filter(is_published = True)
# def index(request):
#     posts = Women.objects.all()
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request,'women/index.html',context=context)
def about(request):
    return render(request,'women/about.html',{'menu': menu,'title':'О сайте'})
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')





class AddPage(CreateView):#добавили новую страниц и категории в ней, как снизу
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')#функция выполняет построение только тогда когда понадоьится

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)#обращаемся к базовому и получаем параметры
        context['menu'] = menu
        context['title'] = 'post'
        return context

# def add_page(request):# далее чтобы форма не исчезала полсе ввода
#     if request.method == 'POST':# сверяем передачи серверу
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():# проверка корректности данных
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#
#         form = AddPostForm()
#     return render(request, 'women/addpage.html',{'form': form, 'menu': menu,'title':'Добавление статьи'})
def contact(request):
    return HttpResponse('Обратная связь')
def login(request):
    return HttpResponse('Войти')

class ShowPost(DetailView): #функция для отобраддения, как снизу
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)#обращаемся к базовому и получаем параметры
        context['menu'] = menu
        context['title'] = context['post']
        return context


#def show_post(request, post_slug):
#    post = get_object_or_404(Women,slug=post_slug)
#    context = {
#        'post': post,
#        'menu': menu,
#        'title': post.title,
#        'cat_selected': 1,
#    }
 #   return render(request,'women/post.html', context=context)

class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'  # указываем путь к файлу
    context_object_name = 'posts'  # указываем имя файла
    allow_empty = False

    def get_queryset(self):# указать что именно выбирть и отображать из списка
        return Women.objects.filter(cat__slug = self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)#обращаемся к базовому и получаем параметры
        context['menu'] = menu
        context['title'] = 'Категория - '+str(context['posts'][0].cat)#возвращает нахвание категории
        context['cat_selected'] = context['posts'][0].cat_id
        return context
#def show_category(request, cat_id):
#    posts = Women.objects.filter(cat_id=cat_id)
#
 #   if len(posts) == 0:
#        raise Http404()
#
 #   context = {
  #      'posts': posts,
   #     'menu': menu,
    #    'title': 'Отображение по рубрикам',
     #   'cat_selected': cat_id,
    #}

    #return render(request, 'women/index.html', context=context)
