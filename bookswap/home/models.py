from django.db import models

class Input(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name if self.name else 'Unnamed Input'