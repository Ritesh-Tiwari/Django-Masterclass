from django.db import models

# Create your models here.
class Expense(models.Model):
    

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'