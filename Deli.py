sandwich_orders=['big mac','home made','special','tuna']
finished_sandwichs=[]
for sandwich_order in sandwich_orders:
	print(f"\n I made your {sandwich_order.title()} sandwich!")
	finished_sandwichs.append(sandwich_order)

for finished_sandwich in finished_sandwichs:
	print(f"\n finished {finished_sandwich.upper()} sandwich!")