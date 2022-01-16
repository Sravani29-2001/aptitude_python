# A man sitting in a train which is running at a speed of 100 km/hr saw a goods train which is running in opposite direction towards him.
#  The goods train crosses the man in 8 seconds. If the length of goods train is 300 meters, find its speed.

speed_of_man = int(input("Enter the speed of the train/man: "))
time_taken_by_goodstrain_to_cross_man = int(input("Enter the time taken to cross the goods train: "))
length_of_goods = int(input("Enter the lenth of the goods train:"))
relative_speed = length_of_goods/time_taken_by_goodstrain_to_cross_man
r = relative_speed *(18/5)
x = r  - speed_of_man # x is speed of goods train
print(f'The speed of goods train is: {x}Km/hr')