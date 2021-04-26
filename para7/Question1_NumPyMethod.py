import numpy as np
import matplotlib.pyplot as plt
import math 

canvas = plt.figure()

x = np.linspace(0, 5 , 256 )
s = (math.e**(-x))*np.cos(x*math.pi*2)
c = np.cos(x*math.pi*2)

convas1 = canvas.add_subplot(2,1,1)
plt.plot(x,s,color="red",linewidth=2.5,linestyle="-",label="e**(-x)cos(2*x*pi)",zorder=-2)
convas2 = canvas.add_subplot(2,1,2)
plt.plot(x,c,color="blue",linewidth=2.5,linestyle="-",label="cos(2*x*pi)",zorder=-1)
plt.show()
# y=(e**(-x))*cos(2*pi*x)