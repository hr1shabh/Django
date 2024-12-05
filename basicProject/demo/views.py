from django.shortcuts import render
from .models import Cars, Store
from django.shortcuts import get_object_or_404
from .forms import CarsForm
# Create your views here.
def all_demo(requests):
    cars = Cars.objects.all() #return an array
    return render(requests, 'all_demo.html', {'cars': cars}) #by default path template/ 

def car_details(requests, car_id):
    car = get_object_or_404(Cars, pk = car_id)
    return render(requests, 'car_details.html', {'car': car})

def car_stores(request):
    stores = None
    # print("lol")
    # print(request.method)
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            car_variety = form.cleaned_data['car_variety']
            print('car')
            print(car_variety)
            stores = Store.objects.filter(car = car_variety)
    else:
        form = CarsForm()
    return render(request, 'car_stores.html', {'stores' : stores, 'form': form})

