#python fysiikka 4
import math
import matplotlib.pyplot as plt

g = 9.81
vn= 13
an=45
hn=2.1
rad=57.2957795
#alkunopeudet
vnx=(vn*math.cos(an/rad))
vny=(vn*math.sin(an/rad))
print(str(vnx))
print(str(vny))
t = 0
xkoord =[]
ykoord= []
y = 0
while y >= 0:
    x = vnx * t
    y = vny * t - (1/2)*g*t**2 + hn
    print ("x is " + str(x) + " and y is " + str(y))
    xkoord.append(x)
    ykoord.append(y)
    t = t + 0.01

plt.plot([xkoord], [ykoord], 'go')
plt.axis([0, 20, 0, 10])
plt.xlabel("X-suunnassa kuljettu matka")
plt.ylabel("Y-suunnassa kuljettu matka")
plt.show()
