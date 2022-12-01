from django.contrib import admin
from . models import Truck, Product, InfoByDate, Archive

admin.site.register(Truck)
admin.site.register(Product)
admin.site.register(InfoByDate)
admin.site.register(Archive)