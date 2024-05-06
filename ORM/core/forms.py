from typing import Any
from django import forms
from core.models import Rating, Restaurant, Order
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# for model form validation
# class RatingForm (forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ('user', 'restauarant', 'rating')

# for form validation
# class RatingForm(forms.Form):
#     rating = forms.IntegerField(validators=[MinValueValidator, MaxValueValidator])


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name',)


class ProductExceptionError(Exception):
    pass


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'number_of_items')

    def save(self, commit=True) -> Any:
        """
        check to see if product has enough items in stock
        """
        order = super().save(commit=False)
        if order.number_of_items > order.product.num_in_stock:
            raise ProductExceptionError(
                f'you cannot make order because product items stock {order.product.num_in_stock} are less than ordered items {order.number_of_items} '
            )
            # raise ValidationError(
            #     f'you cannot make order because product items stock {order.product.num_in_stock} are less than ordered items {order.number_of_items} '
            # )

        if commit:
            order.save()

        return order
