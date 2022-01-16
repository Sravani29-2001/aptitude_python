#A train of length 400 meters is running at a speed of 98 km/hr. The train takes 40 seconds to cross a tunnel. Find the length of the tunnel.
length_of_train = int(input("Enter the length of train:"))
speed_of_train = int(input("Enter the speed of train"))
time_taken_to_cross_tunnel = int(input("Enter the time taken to cross the tunnel:"))
speed_in_ms = speed_of_train*(5/18)
lenth_of_tunnel = (time_taken_to_cross_tunnel*speed_in_ms)-length_of_train
print(f'The length of tunnel is {lenth_of_tunnel}m')