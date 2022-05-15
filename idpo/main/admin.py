from django import forms
from django.contrib import admin
from .models import Entry, Category, Slider, Grid, Сourses, Schedule, News, Payment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

#Category
class CategoryAdminForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorUploadingWidget ())
    class Meta:
        model = Category
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','main', 'add', )
    list_display_links = ('main', 'name')
    search_fields = ('name', 'post')
    form = CategoryAdminForm
    prepopulated_fields = {"slug": ("name",)}

#Сourses

class СoursesAdminForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorUploadingWidget ())
    class Meta:
        model = Сourses
        fields = '__all__'

class СoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publish')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'post')
    form = СoursesAdminForm
    prepopulated_fields = {"slug": ("name",)}

#Grid
class GridAdminForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorUploadingWidget ())
    class Meta:
        model = Grid
        fields = '__all__'

class GridAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'publish')
    list_display_links = ( 'name',)
    form = GridAdminForm
    prepopulated_fields = {"slug": ("name",)}


#Slider
class SliderAdminForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorUploadingWidget ())
    class Meta:
        model = Grid
        fields = '__all__'

class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm
    prepopulated_fields = {"slug": ("name",)}

#News

class NewsAdminForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorUploadingWidget ())
    class Meta:
        model = Сourses
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'publish')
    search_fields = ('name', 'post')
    form = NewsAdminForm
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Grid, GridAdmin)
admin.site.register(Сourses, СoursesAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Schedule)
admin.site.register(Payment)

admin.site.site_title = 'ИДПО'
admin.site.site_header = 'Администрирование ИДПО'

