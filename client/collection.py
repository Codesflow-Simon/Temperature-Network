#################################################################
# collection.py
#
# copyright
# August 2019
#
# Simon Little
# Rich Little
#
# This script is the main temperature collection script for the
# DS1818B20 temperature sensor used by raspberry pi
#
# It is called in the etc/profile file to auto start when the pi boots.
#
# It saves temperature reading and timestamp to a local file templog.
#
# It also sends reading to a server via the post function with argument
# to what the file / sensor is being uploaded to (outside, inside, slab)
# The post function is part of the post_request package which holds the
# server code and principal temperature reading collected from all client
# pis running collection.py.
#################################################################

import time
from w1thermsensor import W1ThermSensor
from post_request import post

node = 'inside'

sensor = W1ThermSensor()
f = open('/home/pi/Desktop/Temperature-Network/client/templog', 'a+')
t = time.asctime( time.localtime(time.time()) )
f.write("-- re-booted: " + str(t) + "\n")
f.close() 

while True:
    temperature = sensor.get_temperature()
    t = time.asctime( time.localtime(time.time()) )
    post({'temp':temperature, 'time':t}, node)
    print(t, temperature)
    x= str(t) + " " + str(temperature) + "\n"
    f = open('/home/pi/Desktop/Temperature-Network/client/templog', 'a+')
    f.write(x)  
    f.close()  
    time.sleep(300)
