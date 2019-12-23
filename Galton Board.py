"""
Author: Oscar Chou
Date: 2019/12/23
"""
import matplotlib.pyplot as plt
import random
import scipy.stats as scs
import numpy as np
import math

TOTAL_BALLS = 40000
TOTAL_LINES = 30
number = list()

#改變向右機率
p=0.5

u=(TOTAL_LINES)*p+1 #曲線位置修正項
s=math.sqrt(u*(1-p))
xx = np.linspace(0, TOTAL_LINES+1, 64)
yy = (TOTAL_BALLS/ (np.sqrt(2 * np.pi * s * s))) * np.exp(-(((xx+1 - u) ** 2) / (2 * s * s)))


labels = [0] * (TOTAL_LINES + 1)
for i in range(0, TOTAL_LINES + 1):
    labels[i] = i + 1

x = np.arange(TOTAL_LINES + 1)  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()


def galton(balls, lines) -> list:
    dist = [0] * ((lines * 2) + 1)

    for ball in range(0, balls):
        total = 0

        for line in range(1, lines + 1):
            outcome = random.uniform(0, 1)
            if (outcome < p):
                total += 1
            else:
                total -= 1
        dist[total + lines] += 1

    for i in range(0, TOTAL_LINES + 1):
        dist[i] = dist[i * 2]
    print(dist[0:lines + 1])
    return dist[0:lines + 1]


def plot_galton(dist, lines):
    rects1 = ax.bar(x , dist, width)

    ax.set_ylabel('Balls')
    ax.set_title('Galton Board')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    for rect in rects1:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


# Attach a text label above each bar in *rects*, displaying its height.
# https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py


dist = galton(TOTAL_BALLS, TOTAL_LINES)
plot_galton(dist, TOTAL_LINES)

# add Gaussian distribution curve
plt.plot(xx, yy, '-', color='#A60628')


plt.show()
