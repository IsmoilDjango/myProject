# Register your models here.
from django.contrib import admin
from .models import Post, Tag, Category, Comment, Rating


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

def make_published(modeladmin, request, queryset):
    queryset.update(status = 'published')
make_published.short_description = "Make selection posts published"
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['title','content','created_at','updated_at','author','category','get_tags']
    inlines = [CommentInline]
    list_filter = ['created_at', 'category']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at','updated_at']
    actions = [make_published]
    fieldsets = (
        (None, {
            'fields':('title','content','author','category','tags')
        }),
        ('Tahrirlash vaqti',{
            'fields':('created_at','updated_at'),
            'classes':('collapse',),
        }),
    )
    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = 'Tags'
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['post','created_at', 'author','content']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    model = Rating
    list_display = ['post', 'user', 'value']