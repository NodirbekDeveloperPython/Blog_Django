from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Muallifi(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.PositiveSmallIntegerField()
    kasb = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=30)
    sana = models.DateField(auto_now_add=True)
    mavzu = models.CharField(max_length=50)
    matn = models.TextField(max_length=200)
    muallif = models.ForeignKey(Muallifi, on_delete=models.CASCADE)
    def __str__(self): return self.sarlavha