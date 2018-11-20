from django.db import models
from django.utils import timezone

# Create your models here.
class Cours(models.Model):
    
    titre=models.CharField(max_length=100)
    auteur=models.TextField(null=True)
    type=models.ForeignKey('Type',null=True,on_delete=models.SET_NULL)
    matiere=models.ForeignKey('Matiere',null=True,on_delete=models.SET_NULL)
    file=models.TextField(null=True)
    partager=models.BooleanField(default=False)

    class Meta:
        verbose_name="cours"
        ordering=['matiere']
	
    def __str__(self):
        return self.titre
	
class Matiere(models.Model):
    matiere=models.CharField(max_length=50)
    
    def __str__(self):
        return self.matiere

class Type(models.Model):
    type=models.CharField(max_length=10)
    
    def __str(self):
        return self.type