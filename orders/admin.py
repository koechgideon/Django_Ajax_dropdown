from django.contrib import admin



from .models import Model, Car,Order

admin.site.register(Model)
admin.site.register(Car)
admin.site.register(Order)