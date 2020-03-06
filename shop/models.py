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
    model_product = models.CharField("Модель/Серия", max_length=20, null=True)
    brand = models.ForeignKey(Brand, verbose_name="Поизводитель", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    description_bf = models.TextField("Краткое описание", max_length=500)
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    poster = models.ImageField("Изображение поста", upload_to="product_img/")
    publication = models.BooleanField("Публиковать", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ImagesProduct(models.Model):
    """Изображения товара"""
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.CASCADE)
    title = models.CharField("Заголовок", max_length=150)
    image = models.ImageField("Изображение", upload_to="product_img/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
