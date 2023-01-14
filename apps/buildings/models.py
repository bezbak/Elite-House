from django.db import models
from apps.team.models import Team
# Create your models here.
class Building(models.Model):
    title = models.CharField(
        max_length=100
    )
    description = models.TextField(
        max_length=255
    )
    location = models.CharField(
        max_length=255
    )
    price = models.IntegerField()
    architetor = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        related_name='architetor'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
    
class Media(models.Model):
    image = models.ImageField(
        upload_to='building_images/'
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='media'
    )
    
    def __str__(self):
        return self.building.title
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
    