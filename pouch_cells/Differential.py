import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np


def df_dx(x):
    return np.gradient(f(x), x)

# pg
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
print("Open database successfully")

cur = conn.cursor()

# sql
cur.execute("select * from output where c3 = 6 and c8 is not null")
rows = cur.fetchall()

data = pd.DataFrame(rows, columns=['idx', 'loop', 'cycle', 'situation', 'time', 'voltage','Q','2','3','4','5','6'])

print(rows)

conn.close()

df = data

x_data = df['time'].values.astype(float)
y_data = df['voltage'].values

# 使用线性插值
f = interp1d(x_data, y_data, kind='linear', fill_value='extrapolate')

x_interp = np.linspace(min(x_data), max(x_data), 1000)  # 生成1000个均匀分布的x值
y_interp = f(x_interp)  # 使用插值函数计算对应的y值

plt.figure(figsize=(10, 6))

# 绘制原始数据点
# plt.scatter(x_data, y_data, color='blue', label='Data Points')

# 绘制插值曲线
# plt.plot(x_interp, y_interp, color='green', label='Interpolated Curve')

# 计算微分方程的曲线
y_diff = df_dx(x_interp)
plt.plot(x_interp, y_diff, color='red', label='Differentiated Curve')

plt.xlabel('Q')
plt.ylabel('dV')
plt.title('Differential Voltage Curve')
plt.legend()
plt.grid(True)
plt.show()


# 例如，求解在某个特定点x=65的微分方程
# print("微分方程在 x=65 处的值:", df_dx(65))
