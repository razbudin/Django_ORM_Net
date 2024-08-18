from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Car, Sale


def home(request):
    return redirect(reverse('list'))


def cars_list_view(request):
    q = request.GET.get('q')
    if q is None:
        cars = Car.objects.all()
    else:
        cars = Car.objects.filter(model__icontains=q)
    context = {'cars': cars}
    template_name = 'main/list.html'
    return render(request, template_name, context)


def car_details_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car_id)
        context = {'car': car, 'sales': sales}
        template_name = 'main/details.html'
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sales = Sale.objects.filter(car=car_id)
        context = {'car': car, 'sales': sales}
        template_name = 'main/sales.html'
        return render(request, template_name, context)
    except Car.DoesNotExist:
        raise Http404('Car not found')
