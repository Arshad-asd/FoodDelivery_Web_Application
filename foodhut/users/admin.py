from django.contrib import admin
from django.contrib.auth import get_user_model
from users.models import Category, Product, ProductSize
from users.models import CustomUser
# Register your models here.
class CustomUser(admin.ModelAdmin):
    list_display = ('name','email', 'password','mobile')
admin.site.register(get_user_model())
admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(Category)