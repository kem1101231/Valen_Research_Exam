from django.db import models


# List of Car Types
class CarType(models.Model):
	type_abbv = models.CharField(max_length=10)
	type_description = models.CharField(max_length=50)
	
	def __str__(self):
		return self.type_description

#List of Car Brands
class CarBrand(models.Model):
	brand_abbv = models.CharField(max_length=10)
	brand_name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.brand_name	

#List of color that might painted on the car
class Color(models.Model):
	color_abbv = models.CharField(max_length=10)
	color_description = models.CharField(max_length=20)
	
	def __str__(self):
		return self.color_description	


# The list of cars
class Car(models.Model):

	car_name = models.CharField(max_length=50)
	order = models.FloatField(default=0, null=True)
	car_model = models.CharField(max_length=50)

	car_type = models.ForeignKey(CarType, on_delete=models.CASCADE, related_name='car_type', null=True)
	car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='car_brand', null=True)
	car_color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='car_color', null=True)

	def __str__(self):
		return self.car_name	