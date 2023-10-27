import matplotlib.pyplot as plt
import math as m
x = [i for i in range(11)]
y = [m.pow(x[i],3) for i in range(11)]
plt.plot(x,y,color="blue")
plt.title("y = x^3")
plt.xlabel("Ось Х")
plt.ylabel("Ось Y")
plt.show()
