from scipy import exp, sqrt
from numpy import linspace, zeros
from math import pi# where pi= 3.1415...
from scipy import interpolate
import matplotlib.pyplot as plt 

mime=1840.# Where mime is the proton to electron mass ratio.
L=zeros(6)
ww=zeros(6)

vshat=1.
L[0]=0.1; L[1]=1.; L[2]=10.;L[3]=100.; L[4]=1000.; L[5] = 10000.

for m in [0,1,2,3,4,5]:    
     
    def F2ode(state, time):  
           
        E = state[0]
        y = state[1]
        v = state[2]
         
        dEdt = vshat/v -exp(y)
        dydt = -E  
        dvdt = E/v- v/L[m]
                          
        return [dEdt, dydt,dvdt]
    
    from scipy.integrate import odeint
    
    function0 = [0.001, 0.,1.]       
    t = linspace(0, 40.0, 100)  
                                                                    
    function = odeint(F2ode, function0, t)
                    
    j = (sqrt(mime/(2*pi))*exp(function[:,1]))-1.0 
        
    xn = j; yn = t
    f = interpolate.interp1d(xn[::-1], yn[::-1])
    zero = f(0.0)
    
    vw=function[:,2]
    plt.plot (t-zero,vw, label="L={var}".format(var=L[m]), linewidth=3.0) 
    
    xw = t-zero; yw = vw
    fw = interpolate.interp1d(xw[::-1], yw[::-1])
    
    zerow = fw(0.0)
    ww[m]=zerow
        
    plt.grid(True)
    plt.xlabel("x [Debye lengths]", fontsize=20)
    plt.ylabel("Ion velocity [Normalised]", fontsize=20)
    plt.title('Ion velosity as a function of the distance from the wall', fontsize=24)        
    plt.legend()
    plt.show()
    
a = plt.axes([0.20, 0.6, .2, .2], axisbg='y')
plt.semilogx(L,ww,linewidth=2.0)
plt.title('Vi at wall as a function of collision length')
plt.xlim(-2., 20000)
plt.xlabel("Collision length [Normalised]", fontsize=16)
plt.ylabel("Vi at wall", fontsize=16)
plt.grid(True)

plt.legend()
plt.show()