#Number of cars
cars = 100
#space per car
space_in_a_car = 4.0
#total number of drivers available
drivers = 30
#number of passengers
passengers = 90
#cars not driven
cars_not_driven = cars - drivers
#number of cars driven
cars_driven = drivers
#total passenger that can be carried
carpool_capacity = cars_driven * space_in_a_car
#average passenger
average_passengers_per_car = passengers / cars_driven

#prints number of cars
print "There are",cars,"cars available."
#prints number of drivers
print "There are only",drivers,"drivers available."
#prints number of cars not driven
print "There will be",cars_not_driven,"empty cars today."
#total number of people that can be transported for the day
print "We can transport", carpool_capacity,"people today."
#total number of passengers for the day
print "We have",passengers, "to carpool today."
#prints average passengers per car
print "We need to put about", average_passengers_per_car, "in each car."

