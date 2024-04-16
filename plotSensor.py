import matplotlib.pyplot as plt
import numpy as np
fileData = "./dataset/100_1.txt"
# Mảng hoành độ tâm vòng tròn
x_pos = np.loadtxt(fileData, dtype=int)
N = len(x_pos)
# Mảng bán kính vòng tròn
radii = np.array(
    [17.0, 0, 0, 0, 0, 0, 0, 34.0, 0, 0, 0, 0, 34.0, 0, 0, 0, 0, 8.5, 0, 0, 0, 0, 0, 0, 24.5, 0, 0, 0,
     0, 0, 0, 0, 32.0, 0, 0, 0, 0, 32.0, 0, 0, 0, 0, 0, 24.5, 0, 0, 0, 24.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 27.5, 0, 0, 27.5, 0, 0, 0, 0, 0, 27.5, 0, 0, 0, 0, 0, 0, 30.5, 0, 0, 0, 30.5, 0, 0, 27.5, 27.5, 27.5, 0,
     0, 0, 0, 0, 0, 0, 0, 27.5, 0, 20.5, 23, 0, 0, 0, 27, 0]
)
fig, ax = plt.subplots()

# Vẽ các vòng tròn
for i in range(N):
    circle = plt.Circle((x_pos[i], 0), radii[i], color='blue', alpha=0.5)
    ax.add_patch(circle)
    if radii[i] > 0:
        ax.scatter(x_pos[i], 0, marker='o', color='red',
                   s=10)  # Chấm đỏ có kích thước 10
    else:
        ax.scatter(x_pos[i], 0, marker='x', color='black',
                   s=10)  # Chấm đen có kích thước 10
# Thiết lập trục
ax.set_xlim(0, 1000)  # Thiết lập giới hạn trục X
ax.set_ylim(-radii.max(), radii.max())  # Thiết lập giới hạn trục Y
ax.set_aspect('equal')  # Giữ tỷ lệ khung hình

# Thêm nhãn trục
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Hiển thị đồ thị
plt.show()
