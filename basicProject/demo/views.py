from django.shortcuts import render
from .models import Cars
from django.shortcuts import get_object_or_404
# Create your views here.
def all_demo(requests):
    cars = Cars.objects.all() #return an array
    return render(requests, 'all_demo.html', {'cars': cars}) #by default path template/ 

def car_details(requests, car_id):
    car = get_object_or_404(Cars, pk = car_id)
    return render(requests, 'car_details.html', {'car': car})