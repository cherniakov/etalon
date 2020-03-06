from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"


class Brand(models.Model):
    """Производитель"""
    name = models.CharField("Поизводитель", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поизводитель"


class Product(models.Model):
    """Товар"""
    article = models.CharField("Артикул", max_length=15)
    name = models.CharField("Товар", max_length=150)
    brand = models.ForeignKey(Brand, verbose_name="Поизводитель", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name="Поизводитель", on_delete=models.SET_NULL, null=True)
    description_bf = models.TextField("Краткое описание")
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    images = models.ImageField("Изображения", upload_to="product_img/")
    publication = models.BooleanField("Публиковать", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

