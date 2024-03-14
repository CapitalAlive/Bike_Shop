from django.urls import path
from . import views

urlpatterns = [
    path("bikes/", views.available_bikes, name="available_bikes"),
    path("bikes/<int:pk>/", views.bike_details, name="bike_details_url"),
    path("order/<int:pk>/", views.order_details, name="order_details_url"),

]
