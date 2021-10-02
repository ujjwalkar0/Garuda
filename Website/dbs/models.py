from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField
# Create your models here.

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

class UploadImageTest(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')