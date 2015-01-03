import numpy as np 
import matplotlib.pyplot as plt 

t= np.arange(0,5,0.2)
plt.plot(t,t,'r--',t,t*t,'bs',t,t**3,'g^');
plt.show()