from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserMeta)
admin.site.register(Category)


@admin.register(Post)
class PostAdmin( admin.ModelAdmin):
    list_display = ('title', 'category', 'date_created')
