from django.contrib import admin
from .models import Product, ProductVariant, Category, Attribute, AttributeValue

admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
