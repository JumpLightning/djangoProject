from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'), #http://127.0.0.1:8000/
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('company/', views.company, name='company'),
    path('rockets/', views.rockets_categories, name='rockets_categories'), #http://127.0.0.1:8000/ships
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    #path('rockets/<slug:rockets_categories_slug>/', views.rockets_categories_by_slug, name='rockets_cats_slug') # http://127.0.0.1:8000/ships/df

]