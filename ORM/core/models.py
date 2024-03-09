from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

def validate_name_startswith_a(name):
    if not name.startswith('a'):
        raise ValidationError("Restaurant name must start with a letter...")

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        ITALIAN = 'IT', 'Italian'
        CHINESE = 'CH', 'Chinese'
        GREEK = 'G', 'Greek'
        MEXICAN = 'M', 'Mexican'
        FASTFOOD = 'F', 'Fast Food'
        OTHER = 'OT', 'Other'
    name = models.CharField(max_length=100, validators=[validate_name_startswith_a])
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    def __str__(self) -> str:
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restauarant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    # rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"Rating: {self.rating}"
    



class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sale_related')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datatime = models.DateTimeField() 
                                              