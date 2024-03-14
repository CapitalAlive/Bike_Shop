from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from . import models
from . import forms
from django import forms as f
# Create your views here.


def available_bikes(request):
    model = models.Bike
    bikes = model.objects.all()
    context = {"bikes": bikes}

    return render(request, "shop/bikes.html", context)


def bike_details(request, pk):
    context = {}
    bike = models.Bike.objects.filter(pk=pk).first()
    if bike:
        frame = models.Frame.objects.filter(color=bike.frame).first()
        seat = models.Seat.objects.filter(color=bike.seat).first()
        tire = models.Tire.objects.filter(type=bike.tire).first()
        basket = models.Basket.objects.all().first()
        is_available = False
        if frame.quantity and seat.quantity and (tire.quantity > 1):
            is_available = True
            if bike.has_basket:
                if not basket.quantity:
                    is_available = False
        form = forms.OrderForm(initial={'bike': bike})
        context = {"bike": bike, "is_available": is_available, "form": form}

    if request.method == "GET":
        return render(request, "shop/bike_details.html", context=context)
    elif request.method == "POST":
        post_data = request.POST.copy()  # Make a mutable copy
        post_data['status'] = "P"
        post_data['bike'] = bike
        form = forms.OrderForm(post_data)

        if form.is_valid():
            print("1:", frame.quantity, seat.quantity, tire.quantity, bike.has_basket, basket.quantity)
            frame.quantity -= 1
            frame.save()
            seat.quantity -= 1
            seat.save()
            tire.quantity -= 2
            tire.save()
            if bike.has_basket:
                basket.quantity -= 1
                basket.save()
            form.save()
            print("2:", frame.quantity, seat.quantity, tire.quantity, bike.has_basket, basket.quantity)

        return redirect(f"/order/{pk}")


def order_details(request, pk):
    order = models.Order.objects.filter(pk=pk).first()
    context = {"order": order}
    return render(request, "shop/order_details.html", context=context)