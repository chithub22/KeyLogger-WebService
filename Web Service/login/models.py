from django.db import models

# Create your models here.
class Post(models.Model):
    immagine = models.ImageField()
    nomeSocial = models.CharField(max_length =20)
    descrizione_Box = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomeSocial