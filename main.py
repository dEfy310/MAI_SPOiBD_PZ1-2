#PZ №1

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

x1 = [0, 35.25]
y1 = [28.2, 0]
plt.title('Графическое решение задачи линейного программирования')
plt.scatter(x1, y1, c='k')
plt.plot(x1, y1, c='k')
plt.grid()
x2 = [19, 19]
y2 = [0, 17]
plt.scatter(x2, y2, c='indianred')
plt.plot(x2, y2, c='indianred')
x3 = [0, 19]
y3 = [17, 17]
plt.scatter(x3, y3, c='indianred')
plt.plot(x3, y3, c='indianred')



plt.show()