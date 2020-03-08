from django.urls import path, include
from . import views

urlpatterns = [
    # == Displays ======================
    path('', views.index, name="index" ),
    path('brands', views.brands, name="brands"),
    path('types', views.types, name="types"),
    path('colors', views.colors, name="colors"),

    # == Functions =====================
    path('add/brand', views.add_brand, name="add_brand"),
    path('add/type', views.add_type, name="add_type"),
    path('add/color', views.add_color, name="add_color"),
    path('add/car', views.add_car, name="add_car"),

    path('find/brand', views.find_brand, name="find_brand"),
    path('find/type', views.find_type, name="find_type"),
    path('find/color', views.find_color, name="find_color"),
    path('find/car', views.find_car, name="find_car"),
    path('find/car/by_group', views.find_car_by_group, name="find_car_by_group"),

    path('move/car', views.move_car, name="move_car"),
]
