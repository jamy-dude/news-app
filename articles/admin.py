from django.contrib import admin
from .models import Article, Comment # new

# class CommentInline(admin.StackedInline): # new
#     model = Comment
#     extra = 0 # new

class CommentInline(admin.TabularInline): # new
    model = Comment
    extra = 0 # new

class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]

# Register your models here.
admin.site.register(Article, ArticleAdmin) # new
admin.site.register(Comment) # new