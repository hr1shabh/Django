from django.contrib import admin
from .models import Cars, CarReviews, Store, CarCertificate
# Register your models here.

class CarReviewsInline(admin.TabularInline):
    model = CarReviews
    extra = 2

class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [CarReviewsInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('car',)

class CarCertificateAdmin(admin.ModelAdmin):
    list_display = ('car', 'certificate_number')

admin.site.register(Cars, CarsAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(CarReviews)
admin.site.register(CarCertificate, CarCertificateAdmin)


