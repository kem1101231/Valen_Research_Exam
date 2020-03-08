from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Models.models import CarType, CarBrand, Color, Car
from django.http import JsonResponse
import json


# === Dislpays ===================
# Function that basically dipslay the page and provides the required data of the page

def index(request):
	all_cars = Car.objects.order_by('order')
	return render(request, 'index.html', {'cars': all_cars})

def brands(request):
	car_brands = CarBrand.objects.all()
	return render(request, 'brand.html', {'brands':car_brands})

def types(request):
	car_types = CarType.objects.all()
	return render(request, 'type.html', {'types':car_types})

def colors(request):
	car_colors = Color.objects.all()
	return render(request, 'color.html', {'colors':car_colors})


# ====== Get Functions =======================
# Functions that are use to fill data on a datalist on there repective fields for provide suggestions to the user

# Find matching brand name base on input 
def find_brand(request):
	if request.method == 'POST':
		brand_ref = request.POST['input_data']

		results = CarBrand.objects.filter(brand_name__icontains=brand_ref)
		outpput_list = []
		for line in results:
			outpput_list.append({
									'name':line.brand_name,
									'id':line.id,

							})

		return HttpResponse(json.dumps({'data_result':outpput_list}), content_type="application/json")

# Find matching car type name base on input 
def find_type(request):
	if request.method == 'POST':
		type_ref = request.POST['input_data']

		results = CarType.objects.filter(type_description__icontains=type_ref)
		outpput_list = []
		for line in results:
			outpput_list.append({
									'name':line.type_description,
									'id':line.id,

							})


		return HttpResponse(json.dumps({'data_result':outpput_list}), content_type="application/json")

# Find matching color name base on input 
def find_color(request):
	if request.method == 'POST':
		color_ref = request.POST['input_data']

		results = Color.objects.filter(color_description__icontains=color_ref)
		outpput_list = []
		for line in results:
			outpput_list.append({
									'name':line.color_description,
									'id':line.id,

							})

		return HttpResponse(json.dumps({'data_result':outpput_list}), content_type="application/json")

# Find matching car name base on input 
def find_car(request):
	if request.method == 'POST':
		car_ref = request.POST['input_data']

		results = Car.objects.filter(car_name__icontains=car_ref)
		outpput_list = []
		for line in results:
			outpput_list.append({
									'name':line.car_name,
									'id':line.id,

							})


		return HttpResponse(json.dumps({'data_result':outpput_list}), content_type="application/json")


# Find matching car name base on the field name and field value 
def find_car_by_group(request):
	if request.method == 'POST':
		reference_type = request.POST['reference_type']
		reference_input = request.POST['reference_input']

		cars = []

		if reference_type == 'Type':
			car_type = CarType.objects.get(id=reference_input)
			result_cars = Car.objects.filter(car_type=car_type).order_by('order')
			
			cars = generate_car_list(result_cars)
		
		if reference_type == 'Color':
			car_color = Color.objects.get(id=reference_input)
			result_cars = Car.objects.filter(car_color=car_color).order_by('order')
			
			cars = generate_car_list(result_cars)
		
		if reference_type == 'Brand':
			car_brand = CarBrand.objects.get(id=reference_input)
			result_cars = Car.objects.filter(car_brand=car_brand).order_by('order')
			
			cars = generate_car_list(result_cars)
		

		return HttpResponse(json.dumps({'cars':cars}), content_type="application/json")

# Generate a array of dictionary based on aist of queryset of cars
def generate_car_list(result):
	output_data = []
	for line in result:
		output_data.append({
								'name':line.car_name,
								'brand':line.car_brand.brand_name,
								'type':line.car_type.type_description,
								'color':line.car_color.color_description,
						})
	return output_data

# ==== Add Functions ==================
# Functions that add or update data on the database

# adds a new brand
def add_brand(request):
	if request.method == 'POST':
		brand_code = request.POST['brand_code']
		brand_name = request.POST['brand_name']

		car_brand = CarBrand(brand_abbv = brand_code, brand_name= brand_name)
		car_brand.save()

		return HttpResponseRedirect('/brands')

# adds a new car_type
def add_type(request):
	if request.method == 'POST':
		type_code = request.POST['type_code']
		type_name = request.POST['type_name']

		car_type = CarType(type_abbv = type_code, type_description= type_name)
		car_type.save()


		all_types = CarType.objects.all()

		return HttpResponseRedirect('/types')

# adds a new color
def add_color(request):
	if request.method == 'POST':
		color_code = request.POST['color_code']
		color_name = request.POST['color_name']

		car_color = Color(color_abbv = color_code, color_description= color_name)
		car_color.save()

		return HttpResponseRedirect('/colors')

# adds a new car to the list
def add_car(request):
	if request.method == 'POST':

		brand_input = request.POST['brand_input']
		type_input = request.POST['type_input']
		color_input = request.POST['color_input']
		model_input = request.POST['model_input']

		car_brand = CarBrand.objects.filter(id=brand_input)
		car_type = CarType.objects.filter(id=type_input)
		car_color = Color.objects.filter(id=color_input)
		
		last_car = Car.objects.order_by('-order')

		new_car = Car(		car_name = car_brand[0].brand_name+" - "+model_input,
							car_model = model_input, 
							car_type = car_type[0], 
							car_brand = car_brand[0],
							car_color = car_color[0],
					)


		new_car.save()
		id_value = new_car.id
		new_car.order = id_value
		new_car.save()

		outpput_data = {
							'name':new_car.car_name,
							'brand':new_car.car_brand.brand_name,
							'type':new_car.car_type.type_description,
							'color':new_car.car_color.color_description,
						}

		return HttpResponse(json.dumps({'new_car':outpput_data}), content_type="application/json")

# ===== Move functions =======================

# move a car to either before or after another specified car 
def move_car(request):
	if request.method == 'POST':
		car_to_move = request.POST['car_to_move']
		position = request.POST['position']
		move_to = request.POST['move_to']

		car_to_move_data = Car.objects.get(id=car_to_move)
		ref_car_data = Car.objects.get(id=move_to)
		
		the_car_order = car_to_move_data.order
		ref_car_order = ref_car_data.order
		
		operator = 'minus' if ref_car_order > the_car_order else 'plus'
		
		#the value of the order where the update would start 
		start_order	= the_car_order + 1 if operator == 'minus' else 0

		#the value of the order where the update would end
		end_order = the_car_order - 1 if operator == 'plus' else 0

		if position == 'Before':
			if operator == 'minus':
				end_order = ref_car_order - 1
			else:
				start_order = ref_car_order
		else:
			if operator == 'minus':
				end_order = ref_car_order
			else:
				start_order = ref_car_order + 1

		# Saves sa the order value of the car to be moved
		the_car_order = end_order if operator == 'minus' else start_order
		
		#update all cars with order value within start_order value up to end_order value
		update_order(start_order, end_order, operator)
		
		#updates the new order value of the recently moved car
		car_to_move_data.order = the_car_order
		car_to_move_data.save()

		return HttpResponse('')


def update_order(start_order, end_order, operator):

	car_list = Car.objects.exclude(order__lt=start_order).exclude(order__gt=end_order)
	for car in car_list:
		if operator == 'minus':
			car.order -= 1
		else:
			car.order += 1
		car.save()
