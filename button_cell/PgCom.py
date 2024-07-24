import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# pg
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="127.0.0.1", port="5432")
print("Open database successfully")

cur = conn.cursor()

# sql
cur.execute("select * from output where  (c3 = 6 or c3 = 7) and c1%2 = 1;")
rows = cur.fetchall()

data = pd.DataFrame(rows,
                    columns=['idx', 'loop', 'cycle', 'situation', 'time', 'voltage', '1', '2', '3', '4', '5', '6']
                    )

print(rows)

conn.close()

# Visualize
df = data

# 提取数据
x = df.iloc[:, 0]
y = df.iloc[:, 5]

# 使用Matplotlib作图
plt.figure(figsize=(8, 6))  # 可选的，设置图的大小

plt.plot(x, y, marker='o', linestyle='-', color='b', label='Data points')  # 绘制折线图
plt.scatter(x, y, color='r', label='Scatter points')  # 绘制散点图，如果需要

plt.title('Plot of Data from Database')  # 设置图的标题
plt.xlabel('Second')  # 设置X轴标签
plt.ylabel('Voltage')  # 设置Y轴标签
plt.legend()  # 显示图例
plt.grid(True)  # 添加网格线，可选
plt.show()  # 显示图形

print("Operation done successfully")
