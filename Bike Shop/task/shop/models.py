from django.db import models


class Frame(models.Model):
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Seat(models.Model):
    color = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.color


class Tire(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.type


class Basket(models.Model):
    quantity = models.IntegerField()


class Bike(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField()
    has_basket = models.BooleanField(blank=False)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE, blank=False)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, blank=False)
    tire = models.ForeignKey(Tire, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=50, blank=False)
    surname = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)
    status = models.CharField(max_length=50, choices=(("P", "pending"), ("R", "ready")), default="P")

    def __str__(self):
        return f"{self.name} {self.surname}"
