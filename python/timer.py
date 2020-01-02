#!/usr/bin/env python3.6

#import time
from time import localtime, strftime, mktime

#start_time = time.localtime()
start_time = localtime()
#print(f"Started at {time.strftime('%X', start_time)}")
print(f"Started at {strftime('%X', start_time)}")
#print(f"Started at {time.mktime(start_time)}")
print(f"Started at {mktime(start_time)}")

#Wait for user to stop timer
input(f"Press 'Enter' to stop timer ")
#stop_time = time.localtime()
stop_time = localtime()
#time_difference = time.mktime(stop_time) - time.mktime(start_time)
time_difference = mktime(stop_time) - mktime(start_time)
#print(f"Stopped at {time.strftime('%X', stop_time)}")
print(f"Stopped at {strftime('%X', stop_time)}")
print(f"Total time {time_difference} seconds")
