from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"id {self.id} - {self.name} - cena: {self.price/100}zł "