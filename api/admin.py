from django.contrib import admin

# Register your models here.
from . models import Store, Section, Product

admin.site.register(Store)
admin.site.register(Section)
admin.site.register(Product)