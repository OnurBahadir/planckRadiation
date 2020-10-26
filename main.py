import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import Planck,speed_of_light,Boltzmann

h=Planck
c=speed_of_light
k=Boltzmann 
def planckRadiationFormula(v,T):  
    return  ( (8.0*np.pi*h) / (c**3) ) * ( (v**3) / (np.exp( (h*v)/(k*T) ) -1.0 ) ) 

freq=np.arange(1e10,1.2e15,1e13)

plt.plot( freq,planckRadiationFormula(freq,2000) ,'-', color=(0.6,0.3,0.1), label="2000 K" )
plt.plot( freq,planckRadiationFormula(freq,3000) ,'r-', label="3000 K" )
plt.plot( freq,planckRadiationFormula(freq,4000) ,'y-', label="4000 K" )
plt.plot( freq,planckRadiationFormula(freq,5000) ,'b-', label="5000 K" ) 

plt.xlabel(" Frequency (hz) ")
plt.ylabel(" Radiation Density ")
plt.legend()
plt.show()


