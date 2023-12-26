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