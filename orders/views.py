from django.shortcuts import render
from .models import Order, Car, Model
from django.http import JsonResponse



def main_view(request):
    qs= Car.objects.all()
    return render(request, 'orders/main.html', {'qs':qs})


def get_json_car_data(request):
    qs_val=list(Car.objects.values()) 
    return JsonResponse({'data':qs_val})