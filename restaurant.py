class Restaurant:
	def __init__(self,restaurant_name,cusine_type):
		self.restaurant_name = restaurant_name
		self.cusine_type = cusine_type
		self.number_served = 0
	def describe_restaurant(self):
		print(f"{self.restaurant_name} is the name, and provide {self.cusine_type}")
	def open_restaurant(self):
		print(f"{self.restaurant_name} now open")

restaurant = Restaurant('Jim R','Chinese')
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cusine_type}")
restaurant.describe_restaurant()
restaurant.open_restaurant()