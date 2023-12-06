from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  age = models.IntegerField(default=50)
  
  def __str__(self):
    return f"{self.firstname} {self.lastname}{self.age}"
  
class Court(models.Model):
  name = models.CharField(max_length=255)
  Type = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  def __str__(self):
    return f"{self.name} {self.Type} {self.city}"