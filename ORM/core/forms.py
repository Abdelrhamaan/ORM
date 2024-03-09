from django import forms
from core.models import Rating , Restaurant 
from django.core.validators import MinValueValidator, MaxValueValidator

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