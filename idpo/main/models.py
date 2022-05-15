from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=50)
    post = models.TextField('Описание', blank=True)
    sub_categories = models.ManyToManyField("self", blank=True)
    main = models.BooleanField('Главное меню')
    add = models.BooleanField('Доп. меню')
    url = models.URLField('Ссылка', max_length=200, null=True, blank=True)
    slug = models.SlugField('Slug', max_length=255, unique=True, db_index=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Карегория'
        verbose_name_plural = '3. Меню'

class Entry(models.Model):
    name = models.CharField(max_length=60)
    post = models.TextField('Описание', blank=True)
    category = models.ManyToManyField(Category)
    slug = models.SlugField('Slug', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Slider(models.Model):
    name = models.TextField('Заголовок',max_length=100)
    shortpost = models.TextField('Короткое описание', null=True, blank=True,)
    post = models.TextField('Описание')
    photo = models.ImageField('Изображение',null=True, blank=True, upload_to='slider/')
    slug = models.SlugField('Slug', max_length=255, unique=True, db_index=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = '4. Слайдер'

class Grid(models.Model):
    name = models.TextField('Название', max_length=100)
    post = models.TextField('Описание')
    photo = models.ImageField('Изображение',null=True, blank=True, upload_to='slider/grid/')
    publish = models.BooleanField('Опубликовать', default=True)
    slug = models.SlugField('Slug', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = '5. Блоки под слайдером'

class Сourses(models.Model):
    name = models.CharField('Название', max_length=70)
    shortpost = models.TextField('Короткое описание')
    post = models.TextField('Описание')
    price = models.IntegerField('Цена', null=True, blank=True,)
    image = models.ImageField(null=True, blank=True, upload_to='courses/',
                                      verbose_name=u'Изображение', )
    publish = models.BooleanField('Опубликовать',default=True)
    c_views = models.IntegerField('Просмотры', default=0)
    slug = models.SlugField('Slug', max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = '1. Курсы'
        ordering = ['-id']


class News(models.Model):
    date = models.DateTimeField('Дата')
    name = models.CharField('Название', max_length=70)
    post = models.TextField('Описание')
    publish = models.BooleanField('Опубликовать',default=True)
    slug = models.SlugField('Slug', max_length=255, unique=True, db_index=True)


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = '2. Новости'
        ordering = ['-date']

class Schedule(models.Model):
    day = models.CharField('День недели', max_length=2)
    time = models.TimeField('С',null=True,blank=True)
    time2 = models.TimeField('До', null=True,blank=True)
    weekend = models.BooleanField('Выходной')

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = '6. График работы'
        ordering = ['id']

class Payment(models.Model):
    name = models.CharField('Название', max_length=50)
    url = models.URLField('Ссылка')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = '7. Оплата'

