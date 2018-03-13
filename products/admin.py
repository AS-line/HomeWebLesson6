from django.contrib import admin
from .models import Product, Catalog


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class SlugFromTitleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CatalogAdmin(SlugFromTitleAdmin):
    inlines = (ProductInline,)


admin.site.register(Product, SlugFromTitleAdmin)
admin.site.register(Catalog, CatalogAdmin)
