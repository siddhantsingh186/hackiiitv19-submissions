from math import sin, cos, radians, pi, atan2, degrees
import datetime
from datetime import timedelta
import random
import time


#the function for checking overspeeding
def timeandspeed():
	speed=random.randint()
	max_speed = 120
	if speed>max_speed:
		p = 1
	else:
		p = 0
	if p == 1:
		print("Light on")
	return p


#the function for monitoring axel rotation

def position():
	angle = float(input("Value from accelerometer")) #input from accelerometer
	c = 0
	if angle<0:
		angle= -(angle)
	if angle > 27:
		c = 1
	return c

#the function for calculation of acceleration at time of crash
def accident():
	accl=input()
	fix_accl = 20.0
	if accl<0:
		accl=-accl
	if accl>fix_accl:
		return 1
	else:
		return 0

def acceleration():
	accl = int(input())
	return accl

#snippet to check the violation of rules and accordingly upload the data to the cloud based server
accl_previous = acceleration()
counter_speed = 1;
counter_axel_rotation = 1
counter_acceleration_var = 1
while True:
	accl_present = acceleration()
	pos = position()
	if pos == 1:
		counter_axel_rotation+=1
		print("Beep On")
	if counter_axel_rotation>=5:
		s="beep on"
		print(s + s)
		counter_axel_rotation=0
		#pass on information to cloud based server
	acc=acceleration()
	if (accl_present-accl_previous) >= 3:
                print("Beep on")
		counter_acceleration_var += 1
	if counter_acceleration_var >= 5
		counter_acceleration_var = 0
		#pass on information to cloud based server
	speed_check = timeandspeed()
	if speed_check:
           	counter_speed += 1
	if counter_speed >= 5:
                counter = 0
              #pass on information to cloud based server
	accl_previous = accl_present;
	acci = accident()
	if acci == 1:
		print("Light ON")
		#pass on information to cloud based server
		counter_acceleration_var + =  1
	if counter_acceleration_var >= 5
		#pass on information to cloud based server
	time.sleep(1.5)
