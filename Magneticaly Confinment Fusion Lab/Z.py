import numpy as np
from scipy import exp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# read in data
intensity  = np.loadtxt('intensity.dat')	# 2D array of CCD counts data
wavelength = np.loadtxt('lambda.dat')		# 2D array of wavelength data
radius     = np.loadtxt('radius.dat')		# 1D array of major radii
angle      = np.loadtxt('angle.dat')		# 1D array of scattering ang

sigma= np.ones(302)
sigma[100] = 0.001

i=0
while i<188:
	sigma[i]=1.
	i=i+1

i=188
while i<205:
	sigma[i]=1500.
	i=i+1
i=205
while i<225:
	sigma[i]=1.
	i=i+1

i=225
while i<242:
	sigma[i]=1500.
	i=i+1

i=242
while i<302:
	sigma[i]=1.
	i=i+1

print (intensity[9,77])

print (intensity.shape)
print (wavelength.shape)
print (radius.shape)
print ( angle.shape)


guesses = [1000, 7000, 170]
from scipy.optimize import curve_fit
def func(x, a, b, c):
        return a*exp(-(0.5*(xdata-b)/c)**2)
        
        
xdata=wavelength[150,:]
ydata = intensity[150,:]
        
popt, pcov = curve_fit(func, xdata, ydata, guesses, sigma)

a=popt[0]
b=popt[1]
c=popt[2]

print ("a", a, "b", b, "c", c)

print ("sigma[100]", sigma[100])

j=0
indices=[]
for j in range(302):
    k = 301-j
    indices.append(k)
    j=j+1

print (indices)

g=a*exp(-(0.5*(xdata-b)/c)**2)
plt.figure(52)
plt.plot(indices, intensity[150, :])
plt.plot(indices, g)
plt.plot(indices, sigma)
#plt.xlim([2000,9000])
plt.grid(True)
plt.show() 


#i=0
#while i<302:
#	print "i", i, "wave", wavelength[150,i], "intensity", intensity[150,i]
#	i=i+1

print ("sigma", c)
