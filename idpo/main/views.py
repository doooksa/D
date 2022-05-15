from datetime import datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .models import Entry, Category, News, Slider, Grid, Сourses, Schedule, Payment


def index(request):
    category = Category.objects.all()
    entry = Entry.objects.all()
    slider = Slider.objects.all()
    grid = Grid.objects.all()
    courses = Сourses.objects.all()[:4]
    schedule = Schedule.objects.all()
    payment = Payment.objects.all()

    now = datetime.now()
    news = News.objects.filter(date__lte=now)[:4]



    context ={
        'category': category,
        'cat_selected': 0,
        'entry' : entry,
        'slider': slider,
        'cat_selected':0,
        'grid': grid,
        'courses': courses,
        'news': news,
        'schedule': schedule,
        'payment': payment,
        'news': news

    }

    return render(request, 'main/index.html', context=context)


def cats(request, slug):
    category = Category.objects.all()
    get_artc = Category.objects.get(slug=slug)
    schedule = Schedule.objects.all()


    context ={
        'category': category,
        'get_artc': get_artc,
        'schedule': schedule,
    }

    return render(request, 'main/page.html', context=context)


def slide(request,slug):
    category = Category.objects.all()
    get_artc = Slider.objects.get(slug=slug)
    context = {
        'category': category,
        'get_artc': get_artc
    }
    template ='main/page.html'

    return render(request, template, context)

def grid(request,slug):
    category = Category.objects.all()
    get_artc = Grid.objects.get(slug=slug)
    context = {
        'category': category,
        'get_artc': get_artc
    }
    template ='main/page.html'

    return render(request, template, context)

def courses(request,slug):
    category = Category.objects.all()
    get_artc = Сourses.objects.get(slug=slug)

    cour_object = Сourses.objects.get(slug=slug)
    cour_object.c_views = cour_object.c_views + 1
    cour_object.save()
    context = {
        'category': category,
        'get_artc': get_artc,
        'cour_object': cour_object
    }
    template ='main/page.html'

    return render(request, template, context)

def news(request,slug):
    category = Category.objects.all()
    get_artc = News.objects.get(slug=slug)

    context = {
        'category': category,
        'get_artc': get_artc
    }
    template ='main/page.html'

    return render(request, template, context)


def all_courses(request):
    courses = Сourses.objects.all()
    paginator = Paginator(courses, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        'page_obj': page_obj,

    }
    template = 'main/courses.html'

    return render(request, template, context)

def all_news(request):
    now = datetime.now()
    news = News.objects.filter(date__lte=now)
    paginator = Paginator(news, 10)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    context = {
        'page_obj': page_obj,

    }
    template = 'main/news.html'

    return render(request, template, context)

def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        courses = Сourses.objects.filter(Q(name__icontains=search_query) | Q(post__icontains=search_query))
        now = datetime.now()
        news_filter = News.objects.filter(date__lte=now)

        news = news_filter.filter(Q(name__icontains=search_query) | Q(post__icontains=search_query) )
    context = {
        'courses': courses,
        'news': news,
        'search_query': search_query

    }
    template = 'main/search.html'

    return render(request, template, context)

