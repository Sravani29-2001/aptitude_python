#A train of length 200 meters crosses a man running at 10 km/hr in the same direction in 10 seconds. What is the speed of the train?


lenght_of_train = int(input("Enter the length of train: "))
speed_of_man = int(input("Enter the speed of man: "))
Relative_speed = (lenght_of_train/speed_of_man)*(18/5)
x = Relative_speed +10 # where x is speed of train
print(f'{x} Km/hr')