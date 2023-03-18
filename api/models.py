from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False, unique=True, )
    contacts = models.CharField(max_length=300, null=False, blank=False)
    address = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return f"{self.name} {self.address}"
    
class Section(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.name
    
# Product: price, quantity, type, description,
#  location, picture, is_promoted, is_discounted, is_new
class Product(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False, unique=True)
    type = models.CharField(max_length=60, blank=False, null=False, default='product')
    thumbnail = models.ImageField(upload_to='thumbnail/images', blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    description = models.CharField(max_length=600, blank=True, null=True)
    location = models.ForeignKey(Store, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title