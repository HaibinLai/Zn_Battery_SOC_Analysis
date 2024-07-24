import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('SDM-101-赖海斌csv.csv')

# 提取前5000行的第一列和第六列数据（注意Python中索引是从0开始的）
x = df.iloc[:2500, 0]
y = df.iloc[:2500, 5]

# 使用Matplotlib作图
plt.figure(figsize=(8, 6))  # 可选的，设置图的大小

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data points')  # 绘制折线图
plt.scatter(x, y, color='r', label='Scatter points')  # 绘制散点图，如果需要

plt.title('Plot of Data from Database')  # 设置图的标题
plt.xlabel('3 Second / period')  # 设置X轴标签
plt.ylabel('Voltage')  # 设置Y轴标签
plt.legend()  # 显示图例

plt.grid(True)  # 添加网格线，可选

plt.show()  # 显示图形
