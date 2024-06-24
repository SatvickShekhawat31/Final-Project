from django.contrib import admin
from home.models import Input

# Register your models here.

class inputvalue(admin.ModelAdmin):
    list_display=('product_name','product_price','product_description',)

admin.site.register(Input, inputvalue)