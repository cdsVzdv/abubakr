from django.db import models

# Create your models here.
class Kirish(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.CharField(max_length=150)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi

class Biz_haqimizda(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.CharField(max_length=150)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi

class Biz(models.Model):
    nomi = models.CharField(max_length=100)
    def __str__(self):
        return self.nomi

class Biz_a(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.CharField(max_length=150)
    rasm = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.nomi

class Testimular_rasm(models.Model):
    rasm = models.ImageField(upload_to='media/')
  

class Testimullar(models.Model):
    nomi = models.CharField(max_length=100)
    haqida = models.CharField(max_length=150)
    ismi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi

class Contact(models.Model):
    adressi = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.adressi