from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower


def validate_name_startswith_a(name):
    if not name.startswith('a'):
        raise ValidationError("Restaurant name must start with a letter...")


class CustomValidators:
    """
        just will work if you save or update with save method 
        not update method if you want to customize it with update 
        you have to make new method on model level
    """
    @staticmethod
    def validate_name_startswith_a(name):
        if not name.startswith('a'):
            raise ValidationError(
                "Restaurant name must start with a letter...")

    @staticmethod
    def validate_name_contains_dot(name):
        if '.' in name:
            raise ValidationError("Restaurant name cannot contain a dot")


custom_validators = CustomValidators()


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        ITALIAN = 'IT', 'Italian'
        CHINESE = 'CH', 'Chinese'
        GREEK = 'G', 'Greek'
        MEXICAN = 'M', 'Mexican'
        FASTFOOD = 'F', 'Fast Food'
        OTHER = 'OT', 'Other'
    name = models.CharField(max_length=100,
                            # validators=[
                            # custom_validators.validate_name_startswith_a, custom_validators.validate_name_contains_dot]
                            )
    # name = models.CharField(max_length=100, validators=[validate_name_startswith_a])
    website = models.URLField(default='', null=True, blank=True)
    date_opened = models.DateField()
    latitude = models.FloatField(
        validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(
        validators=[MinValueValidator(-180), MaxValueValidator(180)])
    restaurant_type = models.CharField(
        max_length=2, choices=TypeChoices.choices)
    capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        # default ordering
        ordering = [Lower('name')]
        get_latest_by = 'date_opened'

    def clean(self) -> None:
        print("in clean")
        name = self.name
        # custom_validators = CustomValidators()
        # custom_validators.validate_name_contains_dot(name)
        # custom_validators.validate_name_startswith_a(name)

    def save(self, *args, **kwargs):
        self.full_clean()
        print(self._state.adding)
        super().save(*args, **kwargs)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restauarant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE,  related_name='rating')
    rating = models.PositiveSmallIntegerField()
    # rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return f"Rating: {self.rating}"


class Sale(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.SET_NULL, null=True, related_name='sale_related')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    expenditure = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)
    datatime = models.DateTimeField()


class Staff(models.Model):
    name = models.CharField(max_length=255)
    # restaurant = models.ManyToManyField(Restaurant)
    restaurant = models.ManyToManyField(Restaurant, through='StaffRestauarant')

    def __str__(self) -> str:
        return self.name


class StaffRestauarant(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    salary = models.FloatField(null=True)


class Product(models.Model):
    name = models.CharField(max_length=200)
    num_in_stock = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.number_of_items} x {self.product.name}'


class DummyModel(models.Model):
    name = models.CharField(max_length=200)
