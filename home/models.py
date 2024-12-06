from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # AbstractUser already includes fields like username, password, email, first_name, last_name

    # Qo'shimcha maydonlar
    rate = models.IntegerField(default=0, null=True, blank=True, verbose_name="Reyting")
    age = models.IntegerField(null=True, blank=True, verbose_name="Yosh")
    phoneNumber = models.CharField(max_length=20, verbose_name="Telefon raqam", unique=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True, verbose_name="Foydalanuvchi rasmi")
    role = models.CharField(max_length=50, null=True, blank=True, verbose_name="Rol")

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username




# Product model - Mahsulot ma'lumotlari
class Product(models.Model):

    # Mahsulot nomi (char - belgilar)
    name = models.CharField(max_length=255, verbose_name="Mahsulot nomi")

    # Mahsulot narxi (float - suzuvchi nuqta soni)
    price = models.FloatField(verbose_name="Mahsulot narxi")

    # Mahsulot qo'shilgan sana (date - sana turi)
    date = models.DateTimeField(verbose_name="Qo'shilgan sana", auto_now_add=True)

    # Mahsulot haqida batafsil ma'lumot (text - matnli ma'lumot)
    description = models.TextField(verbose_name="Mahsulot tavsifi")

    # Mahsulot miqdori (int - butun son)
    quantity = models.IntegerField(verbose_name="Mahsulot miqdori")

    # Mahsulot rasmi (ImageField - tasvir saqlash)
    image = models.ImageField(upload_to='products/', verbose_name="Mahsulot rasmi")

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name

# Income model - Daromad ma'lumotlari
class Income(models.Model):

    # Daromad nomi (char - belgilar)
    name = models.CharField(max_length=255, verbose_name="Daromad nomi")

    # Miqdor (bigint - katta butun son)
    quantity = models.BigIntegerField(verbose_name="Miqdor")

    # Narx (bigint - katta butun son)
    price = models.BigIntegerField(verbose_name="Narx")

    # Qo'shilgan sana (datetime - vaqt va sana turi)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt")

    class Meta:
        db_table = "income"

    def __str__(self):
        return self.name

# Cost model - Xarajatlar ma'lumotlari
class Cost(models.Model):

    # Xarajat nomi (char - belgilar)
    name = models.CharField(max_length=255, verbose_name="Xarajat nomi")

    # Narx (bigint - katta butun son)
    price = models.BigIntegerField(verbose_name="Narx")

    # Xarajat haqida batafsil ma'lumot (text - matnli ma'lumot)
    description = models.TextField(verbose_name="Tavsif")

    # Mahsulot qo'shilgan sana (date - sana turi)
    date = models.DateTimeField(verbose_name="Qo'shilgan sana", auto_now_add=True)

    
    class Meta:
        db_table = "cost"

    def __str__(self):
        return self.name


class Staffdailywork(models.Model):
   
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    price = models.FloatField(verbose_name="Narx")

    class Meta:
        db_table = "staffdailywork"

    def __str__(self):
        return f"{self.name.username}"
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity