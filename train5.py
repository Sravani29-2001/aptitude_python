#A train moving at speed of 90 km/hr crosses a pole in 7 seconds. Find the length of the train.


speed_of_train = int(input("Enter the speed of train: "))
speed = speed_of_train*(5/18)
time_to_cross_pole = int(input(" Enter the time taken to cross the pole: "))
distance = int(speed*time_to_cross_pole) 
print(f"The distance in meters:{distance} meters")
