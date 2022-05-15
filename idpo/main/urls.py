from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('category/<slug:slug>/', views.cats, name='category'),
    path('slide/<slug:slug>/', views.slide, name='slide'),
    path('grid/<slug:slug>/', views.grid, name='grid'),
    path('course/<slug:slug>/', views.courses, name='courses'),
    path('news/<slug:slug>/', views.news, name='news'),
    path('courses/', views.all_courses, name='all_courses'),
    path('all_news/', views.all_news, name='all_news'),
    path('search/', views.search, name='search'),


]
