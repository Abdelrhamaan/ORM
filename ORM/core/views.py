from django.shortcuts import render, redirect
# from .forms import RatingForm
from .forms import RestaurantForm, OrderForm, ProductExceptionError
from .models import Restaurant, Rating, Sale, StaffRestauarant, Product
from django.db.models import Sum, Prefetch
from django.utils import timezone
from django.db import transaction
from functools import partial


def index(request):
    # if request.method == 'POST':
    #     form = RestaurantForm(request.POST or None)
    #     if form.is_valid():
    #         print("form", form.cleaned_data)
    #         # form.save()
    #     else:
    #         return render(request, 'index.html', {'form': form})
    # print("herreee")
    # context = {'form' : RestaurantForm()}
    # ==========================================
    # prefetech realted reverese relation ship
    # restaurants = Restaurant.objects.all()
    # restaurants = Restaurant.objects.prefetch_related('rating')
    # restaurants = Restaurant.objects.prefetch_related('rating', 'sale_related')
    # restaurants = Restaurant.objects.filter(name__istartswith='m').prefetch_related('rating', 'sale_related')
    # restaurants = Restaurant.objects.filter(name__istartswith='m')
    # return render(request, 'index.html', {'restaurants':restaurants})
    # ===========================================
    # select related
    # ratings = Rating.objects.select_related('restauarant')
    # ratings = Rating.objects.only('rating',  'restauarant__name').select_related('restauarant')
    # context = {'ratings' : ratings}
    # return render(request, 'index.html', context)
    # ===========================================
    # get all restaurants with 5 stars and fetch sale and rating for them

    # res = Restaurant.objects.prefetch_related('rating', 'sale_related')\
    #         .filter(rating__rating=5)\
    #         .annotate(total=Sum('sale_related__income'))
    # print(res)
    # customize prefetch object
    # month_ago = timezone.now() - timezone.timedelta(days=30)
    # month_lookup = Prefetch(
    #     'sale_related',
    #     # to control the related selected object
    #     queryset=Sale.objects.filter(datatime__gte=month_ago)
    # )
    # res = Restaurant.objects.prefetch_related(
    #     'rating', month_lookup).filter(rating__rating=5)
    # print(res)
    # rest = res.annotate(total=Sum('sale_related__income'))
    # print([r.total for r in rest])
    # context = {'ratings' : ratings}
    # =============================================

    # jobs = StaffRestauarant.objects.all()
    jobs = StaffRestauarant.objects.prefetch_related('restaurant', 'staff')

    for job in jobs:
        job.restaurant.name
        job.staff.name
    return render(request, 'index.html')


def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    order = form.save()
                    # =======================
                    # solve the problem of selecting the same record in the same time 2 books
                    # prevent updating while the row is catching by select for update
                    # select_for_update(nowait=True) will prevent row locking and will raise exeception
                    # skip_locked=True will skip that row you make transaction on it and wil raise exception row not found
                    product = Product.objects.select_for_update().get(
                        id=form.cleaned_data['product'].pk
                    )
                    # try to consume it in the same time from django admin or python shell
                    import time
                    time.sleep(80)
                    # =======================
                    # the order will not created due to transaction
                    #  if you removed transaction the order will be created
                    # also if you didn't handle save method and an error occurs it will return back

                    # server crash summilating
                    # import sys
                    # sys.exit(1)
                    order.product.num_in_stock -= order.number_of_items
                    order.product.save()

                # send emails if transaction success
                transaction.on_commit(partial(send_emails, 'ahmed@gmail.com'))
            except ProductExceptionError:
                send_emails_refused()
            return redirect('order_form')
        else:

            context = {'form': form}
        return render(request, 'order_form.html', context)
    form = OrderForm(request.POST)
    context = {'form': form}

    return render(request, 'order_form.html', context)


def send_emails(user):
    print(f'Dear {user} thanks for making your order')


def send_emails_refused(user=''):
    print(f'Dear {user} your order not happened due to some errors ')


# with transaction.atomic():
#     product = Product.objects.select_for_update(skip_locked= True).get(id=1)
#     product.num_in_stock = 50

#     product.save()
