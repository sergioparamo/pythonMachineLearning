import matplotlib.pyplot as plt
import numpy as np

valors = np.linspace(-2,2,15)
print(valors)

plt.plot(valors,valors, "-", label='linear')  # Imprimim els punts
plt.show()



