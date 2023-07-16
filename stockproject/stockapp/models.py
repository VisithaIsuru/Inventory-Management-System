from django.db import models

# Create your models here.
CATEGORY = (
    ('Womens', 'Womens' ),
    ('Mens', 'Mens' ),
    ('Kids', 'Kids' ),
)

SIZE = (
    ('XS', 'XS' ),
    ('S', 'S' ),
    ('M', 'M' ),
    ('L', 'L' ),
    ('XL', 'XL' ),
    ('XXL', 'XXL' ),
    ('XXXL', 'XXXL' ),
)

class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    item_code = models.CharField(max_length=100, null=True)
    item_brand = models.CharField(max_length=100, null=True)
    colour = models.CharField(max_length=20, null=True)
    size = models.CharField(max_length=20, choices=SIZE, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)




