class Vehicle:
	def weight_per_passenger(self): # Define a function in the class
		return self.weight / self.passengers
	def passenger_economy(self): # Define another class function
		return self.vehicle_economy * self.passengers
titanic = Vehicle()
titanic.weight=54000
titanic.passengers=2400
titanic.vehicle_economy=0.75
print(titanic.weight_per_passenger())
print(titanic.passenger_economy())

