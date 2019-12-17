import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
  rw = RandomWalk(50000)
  rw.fill_walk()
  #画布尺寸
  plt.figure(dpi=128, figsize=(10, 6))

  point_numbers = list(range(rw.num_points))
  #添加色彩
  plt.scatter(rw.x_values, rw.y_values,
              c=point_numbers, cmap=plt.cm.Blues,
              edgecolors='none', s=1)
  #起始点 标为绿色
  plt.scatter(0, 0, c='green',
              edgecolors='none', s=100)
  #终点 标为红色
  plt.scatter(rw.x_values[-1], rw.y_values[-1],
              c='red', edgecolors='none',
              s=100)
  # 隐藏坐标轴
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)

  plt.show()