from django.shortcuts import render

# Create your views here.
def all_demo(requests):
    return render(requests, 'all_demo.html') #by default path template/
