import matplotlib.pyplot as plt
import math
import numpy as np

# plt.plot([1,3*3,math.sqrt(5),pow(7,2),21])
# plt.show()

x = np.array([1,2,3,4])
y = x**2
#
# plt.plot(x, y, 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()
#
# plt.plot(x,y, 'r')
# plt.plot(x,y,'o')
# plt.axis([0, 6, 0, 20])
# plt.show()

x = np.arange(0, 5, 0.2)

# plt.plot(x, x, 'r--', x, x**2, 'bo', x, x**3, 'g^')
# plt.legend(labels=['liniowy', 'kwadratowy', 'szescienny'])
# plt.show()

# plt.plot(x, x, 'r--', label='liniowy')
# plt.plot(x, x**2, 'or--', label='kwadratowa')
# plt.plot(x, x**3, 'g^', label='szescienna')
# plt.legend()
# plt.show()


#wykres funkcji sinus na przedziale x<0,10> wartosci zmieniaja sie co 0.1

x = np.arange(0, 10.1, 0.1)
y = np.sin(x)
plt.plot(x, y, 'b-', label='sinus')
plt.legend()
plt.show()





