from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=50
    )
    logo = models.FileField(
        upload_to='logo/' 
    )
    phone = models.CharField(
        max_length=20
    )
    email = models.EmailField()
    graphic = models.CharField(
        max_length=50
    )
    twitter = models.URLField()
    facebook = models.URLField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'