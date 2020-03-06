from django.contrib import admin
from .models import Product, Category, Brand, ImagesProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


class ImagesProductInline(admin.StackedInline):
    model = ImagesProduct
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("article", "name", "category", "publication")
    list_display_links = ("name",)
    list_filter = ("category",)
    search_fields = ("article", "category__name")
    save_on_top = True
    save_as = True
    list_editable = ("publication",)
    inlines = [ImagesProductInline]


@admin.register(ImagesProduct)
class ImagesProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "title", "image")
    list_display_links = ("product",)
    search_fields = ("product", "title")

# admin.site.register(ImagesProduct)

admin.site.site_header = "Эталон"
# admin.site.site_title = "Django Movies"
