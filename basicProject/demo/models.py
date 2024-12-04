from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Cars(models.Model):
    car_type = [
        ('S', 'Sedan'),
        ('Su', 'SUV'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='demos/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=car_type)
    desciption = models.TextField(default='')

    def __str__(self):
        return self.name


## One to many car - many reviews
## Foreign key means one to many
class CarReviews(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.car.name}'

## many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    car = models.ManyToManyField(Cars, related_name='stores')

    def __str__(self):
        return self.name   
    
## one to one

class CarCertificate(models.Model):
    car = models.OneToOneField(Cars, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'certificate for {self.car}'