from django.db import models

# Create your models here.
class Team(models.Model):
    full_name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=255
    )
    work = models.CharField(
        max_length=50
    )
    image = models.ImageField(
        upload_to="team_images/"
    )
    
    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        