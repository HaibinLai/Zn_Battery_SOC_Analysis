import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('CC_Chg7.csv')

# 提取第一列和第二列数据
x = df.iloc[:, 0]
y = df.iloc[:, 5]

# 使用Matplotlib作图
plt.figure(figsize=(8, 6))  # 可选的，设置图的大小

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data points')  # 绘制折线图
plt.scatter(x, y, color='r', label='Scatter points')  # 绘制散点图，如果需要

plt.title('Plot of Data from CSV')  # 设置图的标题
plt.xlabel('Second')  # 设置X轴标签
plt.ylabel('Voltage')  # 设置Y轴标签
plt.legend()  # 显示图例

plt.grid(True)  # 添加网格线，可选

plt.show()  # 显示图形
