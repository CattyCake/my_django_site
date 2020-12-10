from django.contrib import admin
from .models import Delivery_number
from .models import Order
from .models import Courier

admin.site.register(Delivery_number)
admin.site.register(Order)
admin.site.register(Courier)

# Register your models here.
