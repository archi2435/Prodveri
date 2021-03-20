from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()
# Create your models here.

class category(models.Model):

    title = models.CharField(verbose_name='Название категории', max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class sub_category(models.Model):

    category = models.ForeignKey(category, verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Подкатегория', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sub_category", kwargs={"sub_category_slug": self.slug})

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'



class catalog(models.Model):

    category = models.ForeignKey(category, verbose_name='Категория', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_category, verbose_name="Подкатегория", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(unique=True)
    price = models.CharField(verbose_name='Цена', max_length=20)
    image = models.ImageField()
    sub_name = models.TextField(verbose_name='Описание / назваие коллекции')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
    
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталог'



class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE)
    product = models.ForeignKey(catalog, verbose_name='Товар', on_delete=models.CASCADE, related_name='related_products')
    qty = models.PositiveIntegerField(default=1)
    sum_price = models.DecimalField(verbose_name='Общая цена', max_digits=15, decimal_places=2)

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.product.title)



class cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    sum_price = models.DecimalField(verbose_name='Общая цена', max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.id)



class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер телефона', max_length=15)

    def __str__(self):
        return "Покупатель {}".format(self.user.first_name)



class Sizes(models.Model):
    f_name = models.CharField(verbose_name='Имя', max_length=50)
    l_name = models.CharField(verbose_name='Отчество', max_length=50)
    phone = models.CharField(verbose_name='Номер телефона', max_length=15)

    def __str__(self):
        return '{} {}'.format(self.Sizes.f_name, self.Sizes.l_name)



class Furnite_category(models.Model):

    title = models.CharField(verbose_name='Название', max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("furnite_category", kwargs={"furnite_category_slug": self.slug})
    
    


class Furnite_sub_category(models.Model):

    
    category = models.ForeignKey(Furnite_category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Подкатегория', max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("furnite_sub_category", kwargs={"furnite_sub_category_slug": self.slug})    



class Furnite(models.Model):
    
    category = models.ForeignKey(Furnite_category, verbose_name='Категория', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Furnite_sub_category, verbose_name="Подкатегория", on_delete=models.CASCADE,)
    title = models.CharField(verbose_name='Название', max_length=50)
    image = models.ImageField()
    dist = models.TextField(verbose_name='Описание / назваие коллекции')
    price = models.CharField(verbose_name='Цена', max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("furnite", kwargs={"furnite_slug": self.slug})

    class Meta:
        verbose_name = 'Фурнитура'
        verbose_name_plural = 'Фурнитура'
