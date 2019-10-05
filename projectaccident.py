from math import *
avg_rotation=asin(0.72)
chk_rotation=0
temp=0
data=[]
x=0.508
y=0.762
Ptot=0
Px=0
Py=0
Pyy=0
Pxy=0
for row in range(row):
	for col in range(col):
		if data[row,col]>0.0:
			temp=1
		else
			temp=0
		Ptot=Ptot+temp
		Px=Px+(x*col*y/2)*temp
		Py=Py+(y*row+y/2)*temp	
		Pxx=Pxx+(x*y*y*y/12+x*y*(row*y+y/2)*(row*y+y/2))*temp
		Pyy=Pyy+(y*x*x*x/12+x*y*(col*x+x/2)*(col*x+x/2))*temp
		Pxy=Pxy=(x*y*(row*y+y/2)*(row*x+x/2))*temp
CoPY=Py/Ptot
CoPX=Px/Ptot
CoP=[CoPX,CoPY]
Ixx=Pxx-Ptot*self.x*self.y*CoPY*CoPX
Iyy=Pyy-Ptot*self.y*self.x*CoPY*CoPX
Ixy=Pxy-Ptot*self.y*self.x*CoPY*CoPX
angle=(math.atan(2*Ixy/(Iyy-Ixx)))/2

Ixp=Ixx+cos(angle)*cos(angle)+Iyy*sin(angle)*sin(angle)-2*Ixy*sin(angle)*cos(angle)
Iyp=Ixx+cos(angle)*cos(angle)+Ixx*sin(angle)*sin(angle)-2*Ixy*sin(angle)*cos(angle)
RotationMatrix=[[cos(angle),sin(angle)], [-sin(angle),cos(angle)]]



