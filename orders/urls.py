from django.urls import path
from .views import (
    main_view,
    get_json_car_data
    )





app_name="orders"


urlpatterns = [
    path('', main_view, name='main-view'),
    path('cars-json/', get_json_car_data, name= 'cars-json')
]