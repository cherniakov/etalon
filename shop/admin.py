from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Category, Brand, ImagesProduct, Parameters, Order, ProductInOrder


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class ParametersInline(admin.TabularInline):
    model = Parameters
    extra = 0


class ImagesProductInline(admin.TabularInline):
    model = ImagesProduct
    extra = 0
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        print(obj.image.url)
        return mark_safe(f'<img src={obj.image.url} width="80" height="60"')

    get_image.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("article", "name", "model_product", "brand", "category", "publication")
    list_display_links = ("name",)
    list_filter = ("category", "brand")
    search_fields = ("article", "category__name")
    save_on_top = True
    save_as = True
    list_editable = ("publication",)
    inlines = [ParametersInline, ImagesProductInline]
    fieldsets = (
            (None, {
                "fields": (("article", "publication"), )
            }),
            (None, {
                "fields": (("name", "model_product", "brand",), )
            }),
            (None, {
                "fields": ("category",)
            }),
            (None, {
                "fields": ("price",)
            }),
            (None, {
                "fields": ("description",)
            }),
    )


@admin.register(ImagesProduct)
class ImagesProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "name", "get_image")
    list_display_links = ("product",)
    search_fields = ("product__name", "name")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="50"')

    get_image.short_description = "Изображение"


@admin.register(Parameters)
class ParametersAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "name", "values")
    list_display_links = ("product",)
    list_filter = ("product",)
    search_fields = ("product__name",)


@admin.register(ProductInOrder)
class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity", "price_product")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "total_price", "created")
    inlines = [ProductInOrderInline]
    fieldsets = (
            (None, {
                "fields": (("name", "phone"), )
            }),
            (None, {
                "fields": ("comment",)
            }),
            (None, {
                "fields": ("total_price",)
            }),
    )


admin.site.site_header = "Эталон"
admin.site.site_title = "Эталон"
