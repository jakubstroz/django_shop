from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self) -> str:
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name = 'Producent'
        verbose_name_plural = 'Producenci'

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    price = models.IntegerField()
    producer = models.ForeignKey(Producer,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return f"id {self.id} - {self.name} - cena: {self.price/100}zł, {self.category} "
    
