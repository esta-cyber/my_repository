from django.db import models

class Studentlar(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
    

    def __str__(self):
        return f"{self.name} {self.surname}"