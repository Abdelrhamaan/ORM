from core.models import Rating, Restaurant, Sale
from django.contrib.auth.models import User
import random
from datetime import datetime
# res_list = [1, 2, 3, 4, 5, 6]


def run():
    for _ in range(30):
        Rating.objects.create(
            user=User.objects.get(pk=1),
            restauarant=Restaurant.objects.get(pk=random.randint(1, 6)),
            rating=random.randint(1, 5)
        )

    for _ in range(30):
        Sale.objects.create(
            income=random.randint(50000, 100000),
            restaurant=Restaurant.objects.get(pk=random.randint(1, 6)),
            expenditure=0,
            datatime=datetime.now()
        )
