from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=1000, null=True)
    address = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
