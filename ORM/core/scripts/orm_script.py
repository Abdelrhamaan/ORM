from core.models import Restaurant, Rating, Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from pprint import pprint
def run():
    # restaurant = Restaurant()
    # restaurant.name = 'sobhy'
    # restaurant.date_opened = timezone.now()
    # restaurant.latitude = 50.2
    # restaurant.longitude = 50.2
    # restaurant.restaurant_type = restaurant.TypeChoices.GREEK

    # restaurant.save()
    # print("Hello from running script....")
    # ===============
    # restaurants = Restaurant.objects.all()[0]
    # restaurants = Restaurant.objects.first()
    # print("Restaurants: ", restaurants)
    # ===============

    # Restaurant.objects.create(
    #     name = "blabn", 
    #     date_opened = timezone.now(),
    #     latitude = 25.5,
    #     longitude = 25.5,
    #     restaurant_type = Restaurant.TypeChoices.CHINESE,
    # )
    # ================
    # restaurant = Restaurant.objects.count()
    # print("Restaurant", restaurant) 
    # print(connection.queries)
    # ================
    # restaurant = Restaurant.objects.first()
    # user = User.objects.first()
    # Rating.objects.create(restauarant=restaurant,
    #                        user=user,
    #                        rating = 4.5,
    # )
    # ================

    # print(Rating.objects.filter(rating=4.5))
    # print(Rating.objects.filter(rating=5))
    # print(Rating.objects.filter(rating__lte=5))
    # print(Rating.objects.exclude(rating__gte=4.6))
    # print(Rating.objects.filter(restauarant__name='blabn'))
    # rate = Rating.objects.filter(rating=4)[0]
    # print(rate)
    # print(rate.rating)
    # rate.rating = 5
    # print(rate.rating)
    # rate.save()      
    # pprint(connection.queries)
    # =================
    # rate = Rating.objects.first()
    # print(rate.restauarant)
    # pprint(connection.queries)
    # =================
    # restaurant = Restaurant.objects.first()
    # restaurant.rating_set.all()# this is default related name you can customize it in models  
    # # restaurant.rating.all()# related_name = "rating"  
    # pprint(restaurant)
    # pprint(restaurant.rating_set.all())
    # pprint(connection.queries)
    # ===================

    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=2.5,
    #     datatime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=3,
    #     datatime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant=Restaurant.objects.first(),
    #     income=2.4,
    #     datatime=timezone.now()
    # )
    # =====================
    # res = Restaurant.objects.first()
    # print(res.sale_related.all())
    # =====================
    # user = User.objects.last()
    # res = Restaurant.objects.last()
    # rating, created = Rating.objects.get_or_create(
    #     user=user,
    #     restauarant=res, 
    #     rating=4.7,
    # )
    # if created :
    #     # send user email 
    #     pass
    # pprint(connection.queries)  
    # ======================
    # user = User.objects.last()
    # res = Restaurant.objects.last()
    # rating = Rating.objects.create(
    #     user=user,
    #     restauarant=res, 
    #     rating=9)
    # print(rating)
    # ======================
    user = User.objects.last()
    res = Restaurant.objects.last()
    rating = Rating(
        user=user,
        restauarant=res, 
        rating=9)
    rating.full_clean()
    rating.save()
    print(rating)