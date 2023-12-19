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
x4 = [0, 40]
y4 = [0, 0]
plt.plot(x4, y4, c='k', marker='>')
x5 = [0, 0]
y5 = [0, 30]
plt.plot(x5, y5, c='k', marker='^')
x = [0, 0, 14, 19]
y = [0, 17, 17, 13]
plt.fill_between(x, y, color='peachpuff')
plt.arrow(0, 0, 4, 5, color='orange', shape='full',width=0.3, head_width=1)
xL = [-5, 0, 5]
yL = [4, 0, -4]
plt.plot(xL, yL, c='k', linewidth=1)
plt.savefig('График.png', dpi=300)
plt.show()