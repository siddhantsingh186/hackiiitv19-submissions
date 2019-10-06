from math import sin, cos, radians, pi, atan2, degrees
import datetime
from datetime import timedelta
import random
import time


#the function for checking overspeeding
def timeandspeed():
	speed=random.randint()
	max_speed=120	
	if speed>max_speed:
		p=1	
	else:
		continue
	if p==1:
		print("Light on")
	return p


#the function for monitoring axel rotation

def position():
	angle=float(input("Value from accelerometer")) #input from accelerometer
	c=0    	
	if angle<0:
		angle= -(angle)
	if angle > 33.7:
		c=1
	return c


