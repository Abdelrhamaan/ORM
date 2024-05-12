from core.models import Restaurant, Rating, Sale, Staff, StaffRestauarant, Product
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection, transaction
from django.db.models import Count, Avg, Max, Min, Sum, Variance, StdDev, CharField, Value, F, Q, Case, When, DecimalField, BooleanField, Subquery, OuterRef, Exists
from django.db.models.functions import Length, Upper, Concat, Coalesce
from pprint import pprint
from django.db.models.functions import Lower, Upper
import random
import itertools


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
    # res = Restaurant.objects. ('date_opened')
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
    # concatenation = Concat(
    #     'name', Value(' [Rating: '), Avg('rating__rating'), Value(' ]'),
    #     output_field=CharField()
    # )
    # total_sales = Concat(
    #     'name', Value('[total_sales : '), Sum(
    #         'sale_related__income'), Value(' ]'),
    #     output_field=CharField()
    # )
    # # this will make for every instance in database then will appear this values in values method
    # res = Restaurant.objects.annotate(msg=concatenation,
    #                                   total_sales=total_sales,
    #                                   avg_rating=Avg('rating__rating')
    #                                   ).values('msg', 'total_sales', 'avg_rating'
    #                                            ).order_by('total_sales')
    # # will make group by every name field in database then will make annotate on it
    # res2 = Restaurant.objects.values('name').annotate(
    #                                 msg=concatenation,
    #                                 total_sales=total_sales,
    #                                 avg_rating=Avg('rating__rating')
    #                                 ).order_by(
    #                                     'total_sales'
    #                                 )
    # print(res)
    # print(res2)
    # print(connection.queries)
    # ===============================
    # using F experssions to make arthemtric operations on database level
    # rating = Rating.objects.filter(rating=3).first()
    # # this will happen in python memory
    # rating.rating += 1
    # rating.save(update_fields=['rating'])
    # print(connection.queries)

    # this will happen on database level instead of get value to python memory
    # rate = Rating.objects.filter(rating=3).first()

    # rate.rating = F('rating') + 1

    # rate.save(update_fields=['rating'])

    # ===============================
    # Rating.objects.update(
    #     rating=F('rating') * 2
    # )
    # Rating.objects.update(
    #     rating=F('rating') / 2
    # )
    # ===============================
    # sales = Sale.objects.all()
    # for sale in sales:
    # sale.expenditure = random.uniform(5, 100)

    # update many instances in one query
    # Sale.objects.bulk_update(sales, ['expenditure'])
    # ===================================
    # using F experssion to compare column with another in the same model
    # sales = Sale.objects.filter(expenditure__gt=F('income'))
    # print(sales)
    # ==================================
    # using f experssion with annotation
    # profits = Sale.objects.annotate(
    #     profits = (F('income') - F('expenditure'))
    # ).values('profits').order_by('-profits')
    # print(profits)
    # ==================================
    # using f expressions with aggregate
    # data = Sale.objects.aggregate(
    #     profits=Count('id', filter=Q(income__gt=F('expenditure'))),
    #     loss=Count('id', filter=Q(income__lt=F('expenditure')))
    # )

    # print(data)
    # print(connection.queries)
    # ==================================
    # rating = Rating.objects.filter(rating=3).first()
    # refresh data base to prevent saving  f expression
    # print(rating.rating)
    # rating.rating = F('rating') + 1
    # rating.save(update_fields=['rating'])
    # print(rating.rating)  # F(rating) + Value(1) is still saved
    # ==================================
    # rating = Rating.objects.filter(rating=3).first()
    # # refresh data base to prevent saving  f expression
    # print(rating.rating)
    # rating.rating = F('rating') + 1
    # rating.save(update_fields=['rating'])
    # rating.refresh_from_db()
    # print(rating.rating)  # F(rating) + Value(1) is still saved

    # ===============================
    # using Q experssion for or and xor operators
    # it = Restaurant.TypeChoices.ITALIAN
    # ch = Restaurant.TypeChoices.CHINESE
    # res = Restaurant.objects.filter(
    #     (Q(restaurant_type=it) | Q(restaurant_type=ch)) & Q(name="ablabn"))

    # res2= Restaurant.objects.filter(name__icontains="a")
    # print(res2)
    # print("res", res)
    # =================================
    # balabn_orsobhy = Q(name="asobhy") | Q(name="ablabn")
    # recently_opened = Q(date_opened__gt=timezone.now() -
    #                     timezone.timedelta(days=40))
    # not_recently_opened = ~Q(date_opened__gt=timezone.now() -
    #                          timezone.timedelta(days=40))
    # res = Restaurant.objects.filter(
    #     balabn_orsobhy | recently_opened
    # )
    # res = Restaurant.objects.filter(
    #     balabn_orsobhy & recently_opened
    # )
    # res = Restaurant.objects.filter(
    #     balabn_orsobhy & not_recently_opened
    # )
    # print(res)
    # ================================
    # find sale for restausrants which
    # rest name contains number and res profit is more than
    # ependiture
    # res_contains_num = Q(restaurant__name__regex=r"[0-9]+")
    # sale = Sale.objects.filter(
    #     res_contains_num & Q(income__gt=F('expenditure'))
    #                            ).values('restaurant__name')
    # sale = Sale.objects.filter(
    #     res_contains_num & Q(income__gt=F('expenditure'))
    # )
    # sale = Sale.objects.select_related('restaurant').filter(
    #     res_contains_num & Q(income__gt=F('expenditure'))
    # )
    # for sa in sale:
    #     print(sa.restaurant.name)
    # ================================
    # handle null values
    # res = Restaurant.objects.filter(capacity__isnull=True)

    # Restaurant.objects.filter(name__startswith="ab").update(
    #     capacity=10
    # )
    # res = Restaurant.objects.filter(capacity__isnull=False)
    # print("res", res)
    # ===============================
    # how django handle null values ordering

    # res = Restaurant.objects.order_by(
    #     'capacity').values('id', 'name', 'capacity')
    # res = Restaurant.objects.order_by(
    #     F('capacity').desc(nulls_last=True)).values('id', 'name', 'capacity')
    # res2 = Restaurant.objects.order_by(
    #     F('capacity').asc(nulls_last=True)).values('id', 'name', 'capacity')
    # print(res2)

    # print(connection.queries)
    # ================================
    # using coalesce values
    # Restaurant.objects.filter(capacity__isnull=False).update(
    #     capacity=None
    # )
    # another way to handle null values on database
    # res2 = Restaurant.objects.aggregate(
    #     total_capc=Sum('capacity', default=1))
    # res2 = Restaurant.objects.aggregate(
    # total_capc=Coalesce(Sum('capacity'), Value(1)))
    # print(res2)
    # print(Rating.objects.filter(
    #     rating__lt=0
    # ).aggregate(
    #     avg_rating=Coalesce(Avg('rating'), 0.0)
    # ))
    # ================================
    # using Coalesce with annotate and F
    # Restaurant.objects.filter(id=1).update(nickname="hamada")
    # res = Restaurant.objects.annotate(
    #     nick_name=Coalesce(F('nickname'), F('name'))
    # ).values('nick_name')
    # print(res)
    # print(connection.queries)
    # ================================
    # italian = Restaurant.TypeChoices.ITALIAN
    # annotate any italian rest..
    # res = Restaurant.objects.annotate(
    #     is_italian=Case(
    #         When(restaurant_type=italian, then=True), default=False
    #     )
    # ).values('name', 'is_italian')
    # res = Restaurant.objects.annotate(
    #     is_italian=Case(
    #         When(restaurant_type=italian, then=True), default=False
    #     )
    # ).filter(is_italian=True).values('name', 'is_italian')
    # print(res)
    # ================================
    # res = Restaurant.objects.annotate(nsales=Count('sale_related'))
    # restaurants = res.annotate(
    #     is_popular=Case(When(
    #         nsales__gt=4, then=True
    #     ), default=False)
    # ).values('name', 'nsales', 'is_popular').filter(
    #     is_popular=True
    # )
    # print(restaurants)
    # print(connection.queries)

    # ================================
    # annotate sales more than 80000

    # good example
    # res = Sale.objects.annotate(
    #     sale_more_8=Case(
    #         When(income__gt=80000, then=F('income')),
    #         default=Value(0),
    #         output_field=DecimalField()  # Set output_field to DecimalField
    #     )
    # ).filter(
    #     sale_more_8__gt=80000
    # ).values(
    #     'restaurant__name', 'sale_more_8'
    # )
    # print(res)
    # print(connection.queries)
    # =================================
    # res = Restaurant.objects.annotate(
    # avg_rating=Avg('rating__rating'),
    # num_ratings=Count('rating__pk')
    # )
    # res2 = res.annotate(
    #     more_than_3=Case(
    #         When(avg_rating__gt=3.4, then=F('avg_rating')),
    #         default=0.0,
    #         output_field=DecimalField()
    #     ),
    #     rating_more19=Case(
    #         When(num_ratings__gt=19, then=F('num_ratings'))
    #     )
    # ).values('name', 'more_than_3', 'num_ratings')
    # res2 = res.annotate(
    # high_res=Case(
    # When(avg_rating__gt=3.4, num_ratings__gte=19, then=True),
    # default=False,
    # output_field=BooleanField()  # Set output_field to BooleanField
    # )
    # ).values('name', 'avg_rating', 'num_ratings', 'high_res').filter(high_res=True)
    # print(res.values('name', 'avg_rating', 'num_ratings'))
    # print(res2)
    # ===========================================
    # res = Restaurant.objects.annotate(
    #     avg_rating=Avg('rating__rating')
    # )

    # res2 = res.annotate(
    #     rating_bucket=Case(
    #         When(avg_rating__gt=3.4, then=Value('Highly rated')),
    #         When(avg_rating__range=(2.4, 3.4), then=Value('Average rated')),
    #         When(avg_rating__lt=2.4, then=Value('Bad rated'))
    #     )
    # ).values('name', 'rating_bucket', 'avg_rating')
    # print(res2)
    # ===========================================
    # types = Restaurant.TypeChoices
    # res = Restaurant.objects.annotate(
    #     continent=Case(
    #         When(Q(restaurant_type=types.ITALIAN) | Q(
    #             restaurant_type=types.GREEK), then=Value('Europe')),
    #         When(Q(restaurant_type=types.CHINESE) | Q(
    #             restaurant_type=types.INDIAN), then=Value('Asia')),
    #         When(restaurant_type=types.MEXICAN, then=Value('North America')),
    #         default=Value('N/A')
    #     )
    # )
    # europian = Q(restaurant_type=types.ITALIAN) | Q(
    #     restaurant_type=types.GREEK)
    # asian = Q(restaurant_type=types.CHINESE) | Q(
    #     restaurant_type=types.INDIAN)
    # north_americain = Q(restaurant_type = types.MEXICAN)
    # res = Restaurant.objects.annotate(
    #     continent=Case(
    #         When(europian, then=Value('Europe')),
    #         When(asian, then=Value('Asia')),
    #         When(north_americain, then=Value('North America')),
    #         default=Value('N/A')
    #     )
    # )
    # print(res.values('name', 'continent'))
    # print(connection.queries)
    # ============================================
    # first_sale = Sale.objects.aggregate(first_sale_date=Min('datatime'))[
    #     'first_sale_date']
    # last_sale = Sale.objects.aggregate(last_sale_date=Max('datatime'))[
    #     'last_sale_date']

    # count = itertools.count()
    # dates = []
    # while (dt := first_sale + timezone.timedelta(days=10*next(count))) <= last_sale:
    #     dates.append(dt)
    # whens = [
    #     When(
    #         datatime__range=(dt, dt+timezone.timedelta(days=10)), then=Value(dt.date())
    #     )for dt in dates
    # ]

    # case = Case(
    #     *whens,
    #     output_field=CharField()
    # )

    # print(
    #     Sale.objects.annotate(
    #         daterange=case
    #     ).values('daterange').annotate(total_sales=Sum('income'))
    # )
    # =============================================
    # restaurants = Restaurant.objects.filter(restaurant_type__in=['IN', 'IT']).values('pk')
    # sales = Sale.objects.filter(restaurant__in=Subquery(restaurants)).values('income')
    # print(sales)
    # print(len(sales))
    # print(len(Sale.objects.filter(
    #     restaurant__restaurant_type__in=['IN', 'IT']).values('income')))
    # =============================================
    # sale = Sale.objects.filter(restaurant=OuterRef('pk')).order_by('-datatime')
    # res = Restaurant.objects.all()
    # restaurants = res.annotate(
    #     last_sale_income=Subquery(sale.values('income')),
    #     last_sale_expenditure=Subquery(sale.values('expenditure')),
    #     last_sale_profit=F('last_sale_income') - F('last_sale_expenditure'),
    # ).values(
    #     'pk', 'last_sale_income',
    #     'last_sale_expenditure',
    #     'last_sale_profit',
    # )
    # print(restaurants)

    # for res in restaurants:
    #     print(f"{res.pk} : {res.last_sale}")
    # ==============================================
    # res = Restaurant.objects.filter(
    #     Exists(Sale.objects.filter(restaurant = OuterRef('pk'), income__gte = 70000))
    # ).count()
    # exists is boolean so this will return all res which its rating is equal to 5
    # res = Restaurant.objects.filter(
    #     Exists(Rating.objects.filter(restauarant=OuterRef('pk'), rating=5))
    # ).values('name', 'capacity')

    # exists is boolean so this will return all res which its rating is not equal to 5
    # res = Restaurant.objects.filter(
    #     ~Exists(Rating.objects.filter(restauarant=OuterRef('pk'), rating=5))
    # )
    # print(res.count())
    # ============================================
    # get all res with sales in the last five days

    # last_five_days_date = timezone.now() - timezone.timedelta(days=29)

    # sales = Sale.objects.filter(
    #     datatime__gt = last_five_days_date,
    #     restaurant = OuterRef('pk')
    # )
    # res = Restaurant.objects.filter(
    #     ~Exists(sales)
    # ).values('name')
    # print(res)
    # print(connection.queries)
    # ==========================================
    # we will try to change in book while in transaction by openinig another python shell
    # import time
    # with transaction.atomic():
    #     # select for update lock this row until transaction is finishing  in it
    #     book = Product.objects.select_for_update().get(name='Book')
    #     time.sleep(60)
    # ===========================================
    # content types frame work
    from django.contrib.contenttypes.models import ContentType

    models = ContentType.objects.filter(app_label='core')
    models_list = [
        c.model for c in models
    ]
    print("models_list", models_list)

    # get the actual model

    content_type = ContentType.objects.get(
        app_label='core', model='restaurant'
    )
    rest_class = content_type.model_class()
    print("rest_class", rest_class)
    # retrive all data for that class
    all_rest_data = rest_class.objects.all()
    print("all_rest_data", all_rest_data)

    # get method
    ablabn_rest = content_type.get_object_for_this_type(name='ablabn')
    print("ablabn_rest", ablabn_rest)
    print("ablabn_rest", ablabn_rest.website)
    print("ablabn_rest", ablabn_rest.latitude)
    print("ablabn_rest", ablabn_rest._meta.fields)
    for record in ablabn_rest._meta.fields:
        print("rec", record.name)
        # print("rec", ablabn_rest.record.name)

    # get content type inst for any model from content type mananger methods

    rating_content_type = ContentType.objects.get_for_model(Rating)
    print("rating_content_type", rating_content_type)
    print("rating_content_type", rating_content_type.model)
    print("rating_content_type", rating_content_type.app_label)
    print("rating_content_type", rating_content_type.model_class().objects.all())
    ratings_content_type = ContentType.objects.get_for_models(
        Rating, Restaurant)
    print("ratings_content_type", ratings_content_type)
