from django.shortcuts import render
# from .forms import RatingForm
from .forms import RestaurantForm
from .models import Restaurant, Rating, Sale
from django.db.models import Sum, Prefetch
from django.utils import timezone


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
    month_ago = timezone.now() - timezone.timedelta(days=30)
    month_lookup = Prefetch(
        'sale_related',
        # to control the related selected object
        queryset=Sale.objects.filter(datatime__gte=month_ago)
    )
    res = Restaurant.objects.prefetch_related(
        'rating', month_lookup).filter(rating__rating=5)
    print(res)
    rest = res.annotate(total=Sum('sale_related__income'))
    print([r.total for r in rest])
    # context = {'ratings' : ratings}
    return render(request, 'index.html')
