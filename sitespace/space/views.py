from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

# Create your views here.
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Новости", 'url_name': 'news'},
        {'title': "Компании", 'url_name': 'company'},
        {'title': "Ракеты", 'url_name': 'rockets_categories'},
        {'title': "Войти", 'url_name': 'login'}]

data_company = [{'id':1, 'title': 'SpaceX', 'content': 'О компании SpaceX', 'is_published': True},
        {'id':2, 'title': 'Роскосмос', 'content': 'О компании Роскосмос', 'is_published': False},
        {'id':3, 'title': 'NASA', 'content': 'О компании NASA', 'is_published': True}
]

def index(request):
    data = {'title': "Главная страница",
            'menu': menu,
            'company': data_company}
    return render(request, 'space/index.html', context=data) # ответ клиенту на запрос на сайт

def about(request):
    return render(request, 'space/about.html')

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')

def news(request):
    return render(request, 'space/news.html') # {'title': "Новости", 'menu': menu})

def company(request):
    return render(request, 'space/company.html')

def space_x(request):
    return render(request, 'space/space_x.html')

def northrop_grumman(request):
    return render(request, 'space/northrop_grumman.html')

def rocket_lab(request):
    return render(request, 'space/rocket_lab.html')

def rockets_categories(request):
    return render(request, 'space/rockets_categories.html')


#def rockets_categories_by_slug(request, rockets_categories_slug):
    #if request.GET:
        #print(request.GET)
    #return HttpResponse(f'<h1>Ракеты по категориям</h1><p>slug: {rockets_categories_slug}</p>')

def login(request):
    return render(request, 'space/login.html')
    #return HttpResponse('Войти')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Упс, страница не найдена :(</h1>')


