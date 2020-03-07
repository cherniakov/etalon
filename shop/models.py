from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    """Производитель"""
    name = models.CharField("Поизводитель", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поизводитель"
        verbose_name_plural = "Производители"


class Product(models.Model):
    """Товар"""
    article = models.CharField("Артикул", max_length=15, unique=True)
    name = models.CharField("Наименование", max_length=150)
    model_product = models.CharField("Модель/Серия", max_length=20, null=True, blank=True)
    brand = models.ForeignKey(Brand, verbose_name="Поизводитель", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    publication = models.BooleanField("Публиковать", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Parameters(models.Model):
    """Характеристики"""
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    name = models.CharField("Наименование", max_length=150)
    values = models.CharField("Значения", max_length=150)
    short = models.BooleanField("Добавить в краткие характеристики", default=False)
    title = models.BooleanField("Добавить в заголовок", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Характиристика"
        verbose_name_plural = "Характиристики"


class ImagesProduct(models.Model):
    """Изображения товара"""
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=150)
    image = models.ImageField("Изображение", upload_to="product_img/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
