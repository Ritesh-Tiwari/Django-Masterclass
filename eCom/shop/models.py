from django.db import models

# Create your models here.
class Products(models.Model):
    title       = models.CharField(max_length=250)
    price       = models.FloatField()
    discount_pice = models.FloatField()
    category    = models.CharField(max_length=250)    
    description = models.TextField()
    image       = models.CharField(max_length=300)


    
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Products'
        verbose_name_plural = 'Products'


class Order(models.Model):
    items   = models.CharField(max_length=1000)
    name    = models.CharField(max_length=250)
    email   = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city    = models.CharField(max_length=50)
    state   = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    total   = models.CharField(max_length=50,default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True  
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'