from django.db import models
from django.db.models.signals import post_save


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
    description = models.TextField("Описание", null=True, blank=True)
    price = models.DecimalField("Цена", max_digits=12, decimal_places=2)
    publication = models.BooleanField("Публиковать", default=True)

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
    image = models.ImageField("Изображение", upload_to="shop/product_img/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Order(models.Model):
    """Заказ"""
    name = models.CharField("Имя", max_length=20)
    phone = models.CharField("Телефон", max_length=20)
    comment = models.TextField("Комментарии", max_length=500, null=True, blank=True, default=None)
    total_price = models.DecimalField("Сумма заказа", max_digits=12, decimal_places=2, null=True, blank=True, default=None)
    created = models.DateField("Дата", auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return 'Заказ {}'.format(self.id)


class ProductInOrder(models.Model):
    """Список товаров в заказе"""
    order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Товар", blank=True, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField("Количество", default=1)
    price_product = models.DecimalField("Цена товара", max_digits=12, decimal_places=2, null=True, blank=True, default=None)
    total_product = models.DecimalField("Сумма товара", max_digits=12, decimal_places=2, null=True, blank=True, default=None)

    class Meta:
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        price_product = self.product.price
        self.price_product = price_product
        self.total_product = self.quantity * price_product
        super(ProductInOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_product
    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)
