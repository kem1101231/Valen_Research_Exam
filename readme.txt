A simple CRUD application written in  Django, a Python framework for development.
Basic Functions:
	1. Adds basic car information:
		a. Brand 
				- brand of cars. Companies that have produced a car. Companies may be existing or just a product of imagination. Ex. Ford.
		b. Car Type
				- known types of cars. Ex. Muscle.
		c. Color
				- any color that could be painted to a car. Ex. Midnight Purple

	2. Add car.
		- together with the information above and model name, a car is added to the list.
		- each saved car were given with a order value. This value increments as new cars were being recorded.


	- the car list is displayed with the value of the car's order on an acending order, which means, the car with a lower order is going to be diplayed above the car with a higher order.

	- cars can be moved on the list either before or after another car.
	- if a car is being moved, the order value of the car will be updated. The value may differ depending on the conditions on where the car was moved.

	- cars can be group based on their brands, types or colors. The resulting list display a list of cars grouped together on an ascending order based on the cars order value.


