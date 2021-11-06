from matplotlib import pyplot as plt
import numpy as np

x = np.array([0,0.5,0.7,1])
y = np.array([-15,-40,-35,-30])
m, b = np.polyfit(x, y, 1)


plt.title("White Yam Mass Percent Change after 24 Hours")
plt.xlabel("Water Concentration (mole)")
plt.ylabel("Percentage Decrease of Mass (-%)")
plt.scatter(x, y)
plt.plot(x, m*x+b)
plt.show()

