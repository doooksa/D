from django.shortcuts import render
from .models import Entry, Category, News, Slider, Grid, Сourses, Schedule, Payment


def index(request):
    category = Category.objects.all()
    entry = Entry.objects.all()
    slider = Slider.objects.all()
    grid = Grid.objects.all()
    courses = Сourses.objects.all()
    news = News.objects.all()
    schedule = Schedule.objects.all()
    payment = Payment.objects.all()



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
    }

    return render(request, 'main/index.html', context=context)


def cats(request,id):
    category = Category.objects.all()
    get_artc = Category.objects.get(id=id)
    entry = Entry.objects.filter(category=id)
    schedule = Schedule.objects.all()


    context ={
        'category': category,
        'entry' : entry,
        'get_artc': get_artc,
        'schedule': schedule,
    }

    return render(request, 'main/news.html', context=context)

def entry(request,id):
    category = Category.objects.all()
    get_artc = Entry.objects.get(id=id)
    context = {
        'category': category,
        'get_artc': get_artc
    }
    template ='main/news.html'

    return render(request, template, context)

def slide(request,id):
    category = Category.objects.all()
    get_artc = Slider.objects.get(id=id)
    context = {
        'category': category,
        'get_artc': get_artc
    }
    template ='main/news.html'

    return render(request, template, context)

def grid(request,id):
    category = Category.objects.all()
    get_artc = Grid.objects.get(id=id)
    context = {
        'category': category,
        'get_artc': get_artc
    }
    template ='main/news.html'

    return render(request, template, context)

def courses(request,id):
    category = Category.objects.all()
    get_artc = Сourses.objects.get(id=id)

    cour_object = Сourses.objects.get(id=id)
    cour_object.c_views = cour_object.c_views + 1
    cour_object.save()
    context = {
        'category': category,
        'get_artc': get_artc,
        'cour_object': cour_object
    }
    template ='main/news.html'

    return render(request, template, context)

def news(request,id):
    category = Category.objects.all()
    get_artc = News.objects.get(id=id)
    context = {
        'category': category,
        'get_artc': get_artc
    }
    template ='main/news.html'

    return render(request, template, context)

