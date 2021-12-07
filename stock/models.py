from django.db import models


class Car(models.Model):
    thumbnail = models.ImageField(upload_to="car_thumbnails")
    thumbnail_description = models.CharField(max_length=500, default="")

    img1 = models.ImageField(upload_to="car_covers")
    img2 = models.ImageField(upload_to="car_covers", blank=True, null=True)
    img3 = models.ImageField(upload_to="car_covers", blank=True, null=True)
    img4 = models.ImageField(upload_to="car_covers", blank=True, null=True)
    img5 = models.ImageField(upload_to="car_covers", blank=True, null=True)
    img6 = models.ImageField(upload_to="car_covers", blank=True, null=True)

    brand = models.CharField(max_length=40)

    model = models.CharField(
        max_length=100, blank=True, null=True)
    attribute = models.CharField(
        max_length=100, blank=True, null=True)

    description = models.TextField(default="")

    price = models.IntegerField()

    car_type = models.CharField(max_length=40, default="Hatchback")
    gear_type = models.CharField(max_length=40, default="Manual")
    colour = models.CharField(max_length=40)
    petrol_type = models.CharField(max_length=40, default="Diesel")
    mileage = models.IntegerField()
    year_of_car = models.IntegerField()

    model_series = models.CharField(max_length=50, blank=True, null=True)
    gross_weight_kg = models.IntegerField(blank=True, null=True)
    acceleration_zeroToSixty = models.FloatField(blank=True, null=True)
    fuel_consumption_MPG = models.FloatField(blank=True, null=True)
    foward_gears = models.IntegerField(blank=True, null=True)
    max_power_BHP = models.IntegerField(blank=True, null=True)
    max_speed_MPH = models.IntegerField(blank=True, null=True)
    number_of_cylinders = models.IntegerField(blank=True, null=True)
    length_metres = models.FloatField(blank=True, null=True)
    height_metres = models.FloatField(blank=True, null=True)

    slug = models.SlugField(
        default="please-input-in-this-format", max_length=100)

    def __str__(self):
        return f"{self.brand}, {self.model}"


class PromotionalCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,)

    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="promotional")

    def __str__(self):
        return self.title
