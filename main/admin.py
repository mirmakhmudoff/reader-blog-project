from django.contrib import admin

from .models import *


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"name": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"name": ("name",)}


class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 1  # Yangi rasm qo'shish uchun qo'shimcha maydon


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "date_posted",
        "editors_pick",
        "trending_post",
        "popular_post",
    )
    list_filter = (
        "author",
        "date_posted",
        "editors_pick",
        "trending_post",
        "popular_post",
        "category",
        "tags",
    )
    search_fields = ("title", "content")
    prepopulated_fields = {"title": ("title",)}
    date_hierarchy = "date_posted"
    filter_horizontal = ("tags",)
    inlines = [PostImagesInline]

    fieldsets = (
        ("Asosiy Ma'lumotlar", {"fields": ("title", "content", "author")}),
        ("Qo'shimcha Ma'lumotlar", {"fields": ("tags", "category", "date_posted")}),
        (
            "Post Xususiyatlari",
            {"fields": ("editors_pick", "trending_post", "popular_post")},
        ),
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "author",
        "post",
        "content",
    )
    list_filter = (
        "post",
        "author",
    )
    search_fields = ("author__username", "content")


class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ("id", "picture")
    search_fields = ("id",)


admin.site.register(Post, PostAdmin)
admin.site.register(InstagramPost, InstagramPostAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reply)
admin.site.register(Contact)
