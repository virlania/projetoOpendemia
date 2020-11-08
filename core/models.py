from django.db import models

# Create your models here.

class AmigosFacebook(models.Model):
    name = models.CharField(max_length=50)
    idFacebook = models.CharField(max_length=15)
    doencas = models.TextField()

    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'amigos'