from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=20,verbose_name='Mã', unique=True)
    name = models.CharField(max_length=100, verbose_name='Tên')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Nhóm sản phẩm", 
                            on_delete=models.PROTECT)
    code = models.CharField(max_length=20, verbose_name="Mã", unique=True)
    name = models.CharField(max_length=100, verbose_name="Tên")
    price = models.IntegerField(verbose_name="Giá")
    image = models.ImageField(upload_to='static/images', blank=True,
                            null=True, verbose_name="Ảnh")

class Order(models.Model):
    class Status:
        PENDING = 0
        DELIVERED = 1
        CANCELED = 2
    color= models.CharField(max_length=100 ,default='DEFAULT VALUE')
    size= models.CharField(max_length=100,default='DEFAULT VALUE')
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    orderDate = models.DateTimeField()
    deliverDate = models.DateTimeField(null=True)
    status = models.IntegerField()
   