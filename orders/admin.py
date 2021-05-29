from django.contrib import admin
from .models import Post, Profile, Relationship, Item_Category, Item, Topping

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
admin.site.register(Item_Category)
admin.site.register(Item)
admin.site.register(Topping)