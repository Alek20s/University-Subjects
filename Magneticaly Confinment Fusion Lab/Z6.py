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
average=np.ones(302)
sigma[100] = 0.001
Nw=148
i=0
while i<190:
	sigma[i]=1.
	i=i+1

i=190
while i<201:
	sigma[i]=1700.
	i=i+1
i=201
while i<224:
	sigma[i]=1.
	i=i+1

i=224
while i<236:
	sigma[i]=1700.
	i=i+1

i=236
while i<302:
	sigma[i]=1.
	i=i+1

print (intensity[9,77])

print ( intensity.shape)
print (wavelength.shape)
print (radius.shape)
print (angle.shape)

k=0
average[:]=0
while k<30:
	average[:]=average[:]+intensity[Nw+k,:]
	k=k+1
average[:]=(average[:])/k



#average[:]=(intensity[Nw,:] + intensity[Nw+1,:]+ intensity[Nw+2,:]+intensity[Nw+3,:])/4


guesses = [1000, 7000, 170]
from scipy.optimize import curve_fit
def func(x, a, b, c):
        return a*exp(-(0.5*(xdata-b)/c)**2)
        
        
xdata=wavelength[Nw,:]
ydata = average[:]
        
popt, pcov = curve_fit(func, xdata, ydata, guesses, sigma)

a=popt[0]
b=popt[1]
c=popt[2]

print ( "a", a, "b", b, "c", c)

print ("sigma[100]", sigma[100])

j=0
indices=[]
for j in range(302):
    k = 301-j
    indices.append(k)
    j=j+1

print (indices)

g=a*exp(-(0.5*(xdata-b)/c)**2)
plt.figure(52),

plt.plot(xdata,average[:], "g", linewidth=2., label="Average Actual data")


plt.plot(xdata,g, "r", linewidth=4., label="Gaussian function")
plt.plot(xdata, sigma)

plt.plot(xdata,sigma, "b", linewidth=3., label="Sigma line")
plt.xlim([5500,8500])

plt.xlabel("Wavelength", fontsize=20)
plt.ylabel("Intensity", fontsize=20)

plt.title('Intensity Destribution', fontsize=20)        
plt.legend()
plt.show() 

plt.grid(True)
plt.show() 


i=0
while i<302:
	print ("i", i, "wave", wavelength[150,i], "intensity", intensity[150,i])
	i=i+1

print ("sigma", c)
