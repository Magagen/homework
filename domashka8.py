import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

## 1
# x1 = [1, 5, 10, 15, 20]
# y1 = [1, 7, 3, 5, 11]
# x2 = [1, 5, 10, 15, 20]
# y2 = [4, 3, 1, 8, 12]

# plt.plot(x1, y1, "r", marker="o", label="line 1")
# plt.plot(x2, y2, "-.g", marker="o", label="line 1")

# plt.legend()


## 2
# x = [1, 2, 3, 4, 5]
# y1 = [1, 7, 6, 3, 5]
# y2 = [9, 4, 2, 4, 9]
# y3 = [-7, -4, 2, -4, -7]

# plt.subplot(2, 2, (1, 2))
# plt.plot(x, y1)

# plt.subplot(2, 2, 3)
# plt.plot(x, y2)

# plt.subplot(2, 2, 4)
# plt.plot(x, y3)


## 3
# fig, ax = plt.subplots()
# x = np.linspace(-5, 5, 11)
# y = x**2

# ax.plot(x, y)

# ax.annotate(
#     "min",
#     xy=(0, 0),
#     xytext=(0, 10),
#     arrowprops=dict(facecolor="green"),
# )


## 4
# x = np.random.randint(0, 10, size=100)
# y = np.random.randint(0, 10, size=100)

# plt.hist2d(x, y)
# plt.colorbar()


## 5

# x = np.linspace(0, 5, 100)
# y = np.cos(x * np.pi)

# plt.plot(x, y, 'r')
# plt.fill_between(x, y)


## 6
# fig, ax = plt.subplots()

# x = np.linspace(0, 5, 100)
# y = np.cos(x * np.pi)
# y_masked = np.where(y >= -0.5, y, np.nan)

# ax.plot(x, y_masked, linewidth=3)

# ax.set_xlim(-0.2, 4.9)
# ax.set_ylim(-1, 1)


## 7
# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0, 1, 2, 3, 4, 5, 6]

# plt.subplot(1, 3, 1)
# plt.step(x, y, "g", where="pre", linewidth=2, marker="o")
# plt.grid(True)

# plt.subplot(1, 3, 2)
# plt.step(x, y, "g", where="post", linewidth=2, marker="o")
# plt.grid(True)

# plt.subplot(1, 3, 3)
# plt.step(x, y, "g", where="mid", linewidth=2, marker="o")
# plt.grid(True)


## 8
# fig, ax = plt.subplots()
# x = np.arange(0, 11, 1)
# y1 = (-0.2)*x**2+2*x
# y2 = (-0.4)*x**2+4*x
# y3 = 2*x

# ax.stackplot(x, y1, y2, y3, labels=["y1", "y2", "y3"])
# ax.legend(loc='upper left')


## 9
# vals = [24, 17, 53, 21, 35]
# labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]

# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, explode=(0, 0, 0.15, 0, 0))
# ax.axis("equal")


## 10
# vals = [24, 17, 53, 21, 35]
# labels = ["Ford", "Toyota", "BMV", "AUDI", "Jaguar"]

# fig, ax = plt.subplots()
# ax.pie(vals, labels=labels, wedgeprops=dict(width=0.5))

plt.show()
