from django.db import models
from django.utils import timezone
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
