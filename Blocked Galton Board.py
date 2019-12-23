"""
Galton board with block in middle
Author: Oscar Chou
Date: 2019/12/23
"""
import matplotlib.pyplot as plt
import random
import scipy.stats as scs
import numpy as np
import math

TOTAL_BALLS = 30000
TOTAL_LINES = 29
number = list()

#在正中央放置覆蓋(BLOCK)個針的檔版
BLOCK=10 #0~line，BLOCK==0 和 BLOCK==1 相等

#改變向右機率，p趨近0.5曲線才會趨近高斯分布
p=0.3

#向左
u1=(TOTAL_LINES)*p+0.5-(BLOCK-1)*p
s1=math.sqrt((TOTAL_LINES+1-BLOCK)*p*(1-p))
#向右
u2=(TOTAL_LINES)*p+1.5+(BLOCK-1)*(1-p)
s2=math.sqrt((TOTAL_LINES+1-BLOCK)*p*(1-p))

xx = np.linspace(0, TOTAL_LINES+1, 90)
#向左
yy1 = ((TOTAL_BALLS*(1-p)) / (np.sqrt(2 * np.pi * s1 * s1))) * np.exp(-(((xx+1 - u1) ** 2) / (2 * s1 * s1)))
#向右
yy2=((TOTAL_BALLS*p) / (np.sqrt(2 * np.pi * s2 * s2))) * np.exp(-(((xx+1 - u2) ** 2) / (2 * s2 * s2)))
#合併
yy=yy1+yy2

labels = [0] * (TOTAL_LINES + 1)
for i in range(0, TOTAL_LINES + 1):
    labels[i] = i + 1

x = np.arange(TOTAL_LINES + 1)  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()


def galton(balls, lines) -> list:
    dist = [0] * ((lines * 2) + 1)

    for ball in range(0, balls):
        outcome = random.uniform(0, 1)

        #向右
        if (outcome < p):
            total = 0
            for line in range(1, lines-BLOCK+1):
                outcome = random.uniform(0, 1)
                if (outcome < p):
                    total += 1
                else:
                    total -= 1
            dist[total + lines+BLOCK] += 1

        # 向左
        else:
            total = 0
            for line in range(1, lines-BLOCK+1):
                outcome = random.uniform(0, 1)
                if (outcome < p):
                   total += 1
                else:
                    total -= 1
            dist[total + lines - BLOCK] += 1

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

    # https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    # Attach a text label above each bar in *rects*, displaying its height.
    for rect in rects1:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

dist = galton(TOTAL_BALLS, TOTAL_LINES)
plot_galton(dist, TOTAL_LINES)

# 綠線
plt.plot(xx, yy1, '--', color='#00b015')
plt.plot(xx, yy2, '--', color='#00b015')
# 紅線
plt.plot(xx, yy, '-', color='#A60628')

plt.show()
