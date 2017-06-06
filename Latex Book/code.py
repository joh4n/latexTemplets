# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 12:39:12 2014

@author: johan
"""
from  __future__  import division
from  scipy       import *
from  matplotlib.pyplot import *

##### Projectile: Baseball ####
x0=0 # inital x position
y0=2.2 # inital y position

### Reigon of velocity and angle beeing used in Brutefore
#angle = linspace(1,60,100) #inital guess
#vRange=linspace(0,50,100) #intal guess
angle = linspace(19,19.7,100) # angles 
vRange=linspace(20.5,21.5,100) #velocity

dt=1e-3 # timestep in iteration of DE
N=1e6 #break iteration
g=9.82 #Gravitaional konstant
wind=[5,0] #in a cordiante system(x,z) with z perpundicualr to x and y
H=4.6 # measure meaximum hight
R=30.5 #measured distance

#### Store values from brute fore algoritm
ProR=[] #projectile distance
fAngle=[] #found angle for vRange that produces R
fvelocity=[] # found velocity for R and fAngle
fH=[] #found H values
Limit=[0.99,1.01] # intervall of H and R that beeing accepted in bruteforce
countAngle=0 #iteration counter
for s in vRange:
    for i in angle:
        theta=0.0174532925*i #angle in degrees
        x=[x0]
        y=[y0]
        Vx=[s*cos(i)]
        Vy=[s*sin(i)]
        count = 0
        while y[-1] > 0 :
            V=sqrt(Vx[-1]**2+Vy[-1]**2)
            B=0.0039+0.0058/(1+exp((V-35)/5)) #B2/m according to textbook
            Vwind=sqrt((Vx[-1]-wind[0])**2+(Vy[-1])**2+wind[1]**2)
            x.append(x[-1]+Vx[-1]*dt)
            Vx.append(Vx[-1]-B*Vwind*(Vx[-1]-wind[0])*dt)
            y.append(y[-1]+Vy[-1]*dt)
            Vy.append(Vy[-1]-g*dt-B*Vwind*Vy[-1]*dt)
            count = count + 1
            if count == N:
                break
        if Limit[0]*R < x[-1] < Limit[1]*R and Limit[0]*H < max(y) < Limit[1]*H :
            ProR.append(x[-1]) #projectile distance
            fAngle.append(i)
            fvelocity.append(s)
            fH.append(max(y))
        countAngle = countAngle+1
        print countAngle
figure(1)
plot(ProR,fH,'+')
ylabel('H [m]')
xlabel('R [m]')

figure(2)
plot(fAngle,fvelocity,'+')
xlabel('Angle [degrees]')
ylabel('velocity [m/s]')

figure(3)
plot(fvelocity,fAngle,'+')
ylabel('Angle [degrees]')
xlabel('velocity [m/s]')

print 'ProR: ', ProR
print 'fAngle: ', fAngle
print 'fvelocity: ', fvelocity
print 'vRange: ', vRange