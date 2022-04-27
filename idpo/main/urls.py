from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:id>/', views.cats, name='category'),
    path('entry/<int:id>/', views.entry, name='entry'),
    path('slide/<int:id>/', views.slide, name='slide'),
    path('grid/<int:id>/', views.grid, name='grid'),
    path('course/<int:id>/', views.courses, name='courses'),
    path('news/<int:id>/', views.news, name='news'),


]
