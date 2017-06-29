# coding=utf-8
"""
=========================================================
柱状图
=========================================================

一些可选参数:

    * Setting the number of data bins
    * The ``normed`` flag, which normalizes bin heights so that the
      integral of the histogram is 1. The resulting histogram is an
      approximation of the probability density function.
    * Setting the face color of the bars
    * Setting the opacity (alpha value).

Selecting different bin counts and sizes can significantly affect the
shape of a histogram. The Astropy docs have a great section on how to
select these parameters:
http://docs.astropy.org/en/stable/visualization/histogram.html
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

np.random.seed(0)

# 示例数据
mu = 100  # 分布均值
sigma = 15  # 标准差
# 随机产生的数据作为X
x = mu + sigma * np.random.randn(500)
print len(x)
#50个分桶
num_bins = 50

# 得到对象
fig, ax = plt.subplots()

# 柱状图
n, bins, patches = ax.hist(x, num_bins, normed=1)

# 添加最佳的拟合线
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')

# 横坐标
ax.set_xlabel('Smarts')
# 纵坐标
ax.set_ylabel('Probability density')
# 标题
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# 调整间距
fig.tight_layout()
#展示
plt.show()