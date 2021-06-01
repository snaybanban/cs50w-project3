from django.contrib import admin
from .models import Post, Profile, Item_Category, Item, Topping, Cart

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Item_Category)
admin.site.register(Item)
admin.site.register(Topping)
admin.site.register(Cart)