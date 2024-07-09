from django.db import models
from immobiles.choices import TypeImmobile

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-id']
    
class Immobile(models.Model):
    code = models.CharField(max_length=100)
    type_item = models.CharField(max_length=100, choices=TypeImmobile.choices)
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_locate = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {}".format(self.code, self.type_item)
    
    class Meta:
        verbose_name = 'Immobile'
        verbose_name_plural = 'Properties'
        ordering = ['-id']

class ImmobileImage(models.Model):
    image = models.ImageField('Images', upload_to='images')
    immobile = models.ForeignKey(Immobile, related_name='immobile_images', on_delete=models.CASCADE)

    def __str__(self):
        return self.immobile.code

class RegisterLocation(models.Model):
    immobile = models.ForeignKey(Immobile, on_delete=models.CASCADE, related_name='reg_location')
    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dt_start = models.DateTimeField('Start')
    dt_end = models.DateTimeField('End')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    update_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.client, self.immobile)
    
    class Meta: 
        verbose_name = 'Register Location'
        verbose_name_plural = 'Register Locations'
        ordering = ['-id']