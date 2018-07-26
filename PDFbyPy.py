import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def normal(power, mean, std, val):
    a = 1/(np.sqrt(2*np.pi)*std)
    diff = np.abs(np.power(val-mean, power))
    b = np.exp(-(diff)/(2*std*std))
    return a*b


array = np.arange(-4,4,0.001)
pdf_array = normal(2, 0, 0.5, array)
pdf_array1 = norm.cdf(array, 0, 0.5)



plt.plot(array, pdf_array,array,pdf_array1 )
#plt.ylabel('some numbers')
#plt.axis([-2, 2, 0, 100])
plt.show()


