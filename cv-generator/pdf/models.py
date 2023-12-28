from django.db import models

# Create your models here.
class Profile(models.Model):
    name        = models.CharField(max_length=250)
    email       = models.CharField(max_length=250)
    phone       = models.CharField(max_length=250)
    summary     = models.TextField(max_length=2500)
    degree      = models.CharField(max_length=250)
    school     = models.CharField(max_length=250)
    university  = models.CharField(max_length=250)
    previous_work= models.TextField(max_length=1000)
    skills      = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'