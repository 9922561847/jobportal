from django.db import models

# Create your models here.
class register(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField(max_length=100)
    file = models.FileField(upload_to='files/',null=True,verbose_name="")
