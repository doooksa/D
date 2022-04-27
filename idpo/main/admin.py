from django import forms
from django.contrib import admin
from .models import Entry, Category, Slider, Grid, Сourses, Schedule, News, Payment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class СoursesAdminForm(forms.ModelForm):
    post = forms.CharField(widget=CKEditorUploadingWidget ())
    class Meta:
        model = Сourses
        fields = '__all__'

class СoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'post')
    form = СoursesAdminForm




admin.site.register(Entry)

admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Grid)
admin.site.register(Сourses,СoursesAdmin)
admin.site.register(Schedule)
admin.site.register(News)
admin.site.register(Payment)

admin.site.site_title = 'ИДПО'
admin.site.site_header = 'Администрирование ИДПО'

