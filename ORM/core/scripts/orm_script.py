from core.models import Restaurant, Rating, Sale, Staff, StaffRestauarant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection
from django.db.models import Count, Avg, Max, Min, Sum, Variance, StdDev, CharField, Value
from django.db.models.functions import Length, Upper, Concat
from pprint import pprint
from django.db.models.functions import Lower, Upper
import random


def run():
    # restaurant = Restaurant()
    # restaurant.name = 'asobhy'
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
    #     name="ablabn",
    #     date_opened=timezone.now(),
    #     latitude=25.5,
    #     longitude=25.5,
    #     restaurant_type=Restaurant.TypeChoices.CHINESE,
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
    # user = User.objects.last()
    # res = Restaurant.objects.last()
    # rating = Rating(
    #     user=user,
    #     restauarant=res,
    #     rating=9)
    # rating.full_clean()
    # rating.save()
    # print(rating)
    # =================

    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name =  "new name"
    # restaurant.save()
    # print(connection.queries)

    #  to update the field just i want in sql query not update all fields
    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)
    # restaurant.name =  "new name"
    # restaurant.save(update_fields=['name'])
    # print(connection.queries)
    # ====================
    # restaurant1 = Restaurant.objects.first()
    # restaurant2 = Restaurant.objects.filter(id=32)
    # print(restaurant1)
    # print("s", type(restaurant1))
    # restaurant1.name="asdsa"
    # restaurant2[0].name="asdsa"
    # print(restaurant2[0].name)
    # restaurant2[0].save(update_fields=['name'])
    # restaurant1.save(update_fields=['name'])
    # print(restaurant1.name)
    # print(connection.queries)
    # ===================
    # restaurant2 = Restaurant.objects.filter(name="dsdsa")
    # print("s", type(restaurant2))
    # for res in restaurant2:
    #     res.name="ds.dsa"
    #     res.full_clean()
    #     res.save(update_fields=['name'])
    #     print(res.name)
    # print(connection.queries)
    # ====================
    # restaurant2 = Restaurant.objects.filter(name="asdsa")
    # print("s", type(restaurant2))
    # restaurant2.update(name="ds.dsa")
    # print(connection.queries)
    # ====================
    # res = Restaurant(
    #     name = "lamera",
    #     date_opened = timezone.now(),
    #     latitude = 55.2,
    #     longitude = 23.4,
    #     restaurant_type = 'CH'
    #     )

    # res.save()
    # print(connection.queries)

    # =================
    # update many records
    # res = Restaurant.objects.filter(latitude__lte=50.5).values('latitude')
    # print(res.update(
    #     latitude = 23
    # ))
    # print(res)
    # print(connection.queries)
    # =================
    # res = Restaurant.objects.first()
    # print(res.delete())
    # print(connection.queries)
    # =================

    # filters = {
    #     'restaurant_type' : Restaurant.TypeChoices.CHINESE,
    #     'latitude': 53.400002
    # }
    # print(Restaurant.objects.filter(**filters))
    # print(connection.queries)
    # =================
    # filters = {
    #     'restaurant_type' : Restaurant.TypeChoices.CHINESE,
    #     'latitude': 53.400002
    # }
    # res = Restaurant.objects.get(**filters)
    # print(res.date_opened)
    # print(connection.queries)
    # =================
    # filters = {
    #     'restaurant_type' : Restaurant.TypeChoices.CHINESE,
    #     # 'latitude': 53.400002,
    #     'name__startswith': 'c'
    # }
    # res = Restaurant.objects.filter(**filters)
    # print(res)
    # print(connection.queries)
    # =================
    # exclude_filters = [
    #     Restaurant.TypeChoices.CHINESE,
    #     Restaurant.TypeChoices.MEXICAN,
    #     Restaurant.TypeChoices.INDIAN,
    # ]

    # print(Restaurant.objects.exclude(restaurant_type__in=exclude_filters))
    # print(connection.queries)
    # ==================

    # print(Rating.objects.filter(restauarant__restaurant_type='CH'))
    # print(connection.queries)
    # ==================
    # print(Sale.objects.filter(income__range=(20, 50)).values('income').order_by('datatime'))
    # print(Sale.objects.filter(income__range=(20, 50)).values('income').order_by('datatime').reverse())
    # print(Sale.objects.filter(income__range=(20, 50)).values('income').order_by('-datatime'))
    # print(connection.queries)
    # ===================
    # res = Restaurant.objects.first()
    # res.name = res.name.lower()
    # res.save()
    # if not used lower p small will be the last element
    # print(Restaurant.objects.order_by(Lower('name')))
    # print(connection.queries)
    # ===================
    # print(Restaurant.objects.order_by('date_opened')[2:4])
    # print(Restaurant.objects.order_by('date_opened').last())
    # print(Restaurant.objects.order_by('date_opened').first())
    # print(connection.queries)
    # =================
    # print(Restaurant.objects.all())
    # print(connection.queries)

    # =================
    # res = Restaurant.objects.get(sale_related__income=58.91)
    # print(res)
    # print(res.sale_related.all())
    # print(connection.queries)
    # =================
    # res = Restaurant.objects.earliest('date_opened')
    # res = Restaurant.objects.latest('date_opened')
    # if made get_latest_by = 'date_opened' in class Meta
    # res = Restaurant.objects.latest()
    # print(res)
    # print(connection.queries)

    # =================
    # res = Rating.objects.filter(restauarant__name__startswith='C')
    # print(res)
    # print(connection.queries)
    # ==================
    # check validators class it just works with save not create
    # res_name = 'bc.rating'
    # res = Restaurant(
    #     name=res_name,
    #     date_opened=timezone.now(),
    #     latitude=100,
    #     longitude=85.5,
    #     restaurant_type='IN'
    # )
    # res.full_clean()
    # res.save()
    # print(connection.queries)

    # ====================
    # staff, create = Staff.objects.get_or_create(name="nader sha5a")
    # add, remove, all, count, set, clear  m2m relation
    # add and clear for one instance while set and clear for many instances
    # print(staff)
    # print(type(staff.restaurant))
    # print(staff.restaurant.all())
    # add staff to many restaurants
    # staff.restaurant.add(Restaurant.objects.last())
    # print(connection.queries)
    # staff.restaurant.remove(Restaurant.objects.last())
    # staff.restaurant.set(Restaurant.objects.all()[:6])
    # print(staff.restaurant.count())
    # =======================
    # staff, create = Staff.objects.get_or_create(name="nader sha5a")
    # staff.restaurant.set(Restaurant.objects.filter(restaurant_type="IT"))
    # italian = staff.restaurant.filter(
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN)
    # print(italian)
    # res = Restaurant.objects.get(pk=44)
    # print(res.staff_set.all())
    # ========================
    # staff, create = Staff.objects.get_or_create(name="nader sha5a")
    # rest = Restaurant.objects.first()
    # rest2 = Restaurant.objects.last()
    # StaffRestauarant.objects.create(
    #     staff=staff, restaurant=rest, salary=28000
    # )
    # StaffRestauarant.objects.create(
    #     staff=staff, restaurant=rest2, salary=24000
    # )
    # ==========================

    # rest = StaffRestauarant.objects.filter(
    #     restaurant__name='asobhy'
    # )

    # print(rest)
    # ==========================
    # staff, created = Staff.objects.get_or_create(name='nader sha5a')
    # rest = Restaurant.objects.first()
    #  this will create instance with empty salary
    # staff.restaurant.add(rest)
    # this will add for additional fields
    # staff.restaurant.add(rest, through_defaults={"salary":28_000})
    # ==========================
    # staff, created = Staff.objects.get_or_create(name='nader sha5a')
    # staff.restaurant.set(
    # Restaurant.objects.all()[:6],
    # through_defaults={
    # 'salary':random.randint(20_000, 80_000)
    # }
    # )
    # ==========================
    # rest = Restaurant.objects.values('name', 'date_opened')
    # rest = Restaurant.objects.values(upper_name=Upper('name'))
    # print(rest)
    # ==========================
    # IT = Restaurant.TypeChoices.ITALIAN
    # ratings = Rating.objects.filter(
    #     # restauarant__restaurant_type=IT).values('rating', 'restauarant__name')
    #     restauarant__restaurant_type=IT).values_list('rating', 'restauarant__name')
    # print(ratings)
    # print(connection.queries)
    # =========================
    # print(Restaurant.objects.count())
    # print(Restaurant.objects.filter(name__startswith='a').count())
    # print(connection.queries)
    # if not ids_num --- id__count
    # print(Restaurant.objects.aggregate(ids_num=Count('id')))
    # ===========================
    # print(Rating.objects.filter(
    #     restauarant__name__startswith='a'
    # ).aggregate(
    #     average_rating=Avg('rating')
    # ))
    # print(Rating.objects.filter(
    #     restauarant__name__startswith='a'
    # ).aggregate(
    #     max_rating=Max('rating')
    # ))
    # print(Rating.objects.filter(
    #     restauarant__name__startswith='a'
    # ).aggregate(
    #     min_rating=Min('rating')
    # ))
    # print(Rating.objects.filter(
    #     restauarant__name__startswith='a'
    # ).values('rating'))
    # =======================
    # print(Sale.objects.aggregate(
    #     max=Max('income'),
    #     min=Min('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income')
    # ))
    # sales = Sale.objects.filter(datatime__gte='2024-03-05')
    # sales.aggregate(
    #     max=Max('income'),
    #     min=Min('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income')
    # )
    # print(Sale.objects.filter(datatime__gte='2024-03-05').aggregate(
    #     max=Max('income'),
    #     min=Min('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income'),
    #     var=Variance('income'),
    #     std=StdDev('income'),
    # ))
    # print(sales)
    # print(connection.queries)
    # ============================
    # fetch all restaurants and count their names char'
    # annotate add an property to the object so you can access it by dot .
    # res = Restaurant.objects.annotate(len_name=Length('name')) # this will return objects
    # res2 = Restaurant.objects.values('name').annotate(len_name=Length('name')) # this will return dictinaries
    # # for rest in res:
    # #     print(rest.len_name)
    # for rest in res2:
    #     print(rest.get('len_name'))
    # # print(res)
    # print(connection.queries)
    # =============================
    # most important notes !!!!!!!!!!!!!!!!!!
    #  every returned object i add attribute to it to calc the length of name
    # after that i filtered this objects based on the len_name__gte=4
    # then i just returned two values name and len_name in dictionary
    # using values before annotate will make group by for unique values column values 
    # while making values after annotate will make for every model in the database 
    # you can aggregate the annotated values from 
    # ==============================
    # res = Restaurant.objects.annotate(len_name=Length('name')).filter(
    #     len_name__gte=4
    # ).values('name', 'len_name')
    # print(res)
    # print(connection.queries)
    # ============================
    # concat values on the database level
    concatenation = Concat(
        'name', Value(' [Rating: '), Avg('rating__rating'), Value(' ]'),
        output_field=CharField()
    )
    total_sales = Concat(
        'name', Value('[total_sales : '), Sum(
            'sale_related__income'), Value(' ]'),
        output_field=CharField()
    )
    # this will make for every instance in database then will appear this values in values method
    res = Restaurant.objects.annotate(msg=concatenation,
                                      total_sales=total_sales,
                                      avg_rating=Avg('rating__rating')
                                      ).values('msg', 'total_sales', 'avg_rating'
                                               ).order_by('total_sales')
    # will make group by every name field in database then will make annotate on it 
    res2 = Restaurant.objects.values('name').annotate(
                                    msg=concatenation,
                                    total_sales=total_sales,
                                    avg_rating=Avg('rating__rating')
                                    ).order_by(
                                        'total_sales'
                                    )
    print(res)
    print(res2)
    print(connection.queries)
