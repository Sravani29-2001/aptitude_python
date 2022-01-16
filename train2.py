#A train moving at 108 km/hr crosses a platform in 30 seconds. Then it crosses a man running at 12 km/hr in the same direction of train in 9 seconds.
#  What is the length of train and platform?


speed_of_train = int(input("Enter the speed of train in km/hr: "))
speed_of_man = int(input("Enter the speed of man: "))
time_to_cross_platform = int(input("Enter the time taken to cross the platform: "))
time_to_cross_man= int(input("Enter the time taken to cross the man: "))
relative_speed_man = (speed_of_train - speed_of_man)*(5/18) 
x = relative_speed_man*time_to_cross_man # x is length of train
speed_of_train = speed_of_train* (5/18)
y = (time_to_cross_platform *speed_of_train) - x # y is lenth of platform
print(f'lenght of train is {x}m and length of platform is {y}m')
