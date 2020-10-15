import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10)
y = x # Funció linial


x_cuadrat = x**2
x_cubo = x**3


plt.plot(x,y, "-", label='linear')  # Imprimim els punts
plt.plot(x,x_cuadrat, "o", label='linear')  # Imprimim els punts
plt.plot(x,x_cubo, ".", label='linear')  # Imprimim els punts




plt.show()



