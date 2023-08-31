import numpy as np

arr1 = np.array([0, 0.3, 0.5])
arr2 = np.array([[3, 4, 5], [0, 7, 8]])  # 创建二维数组
print(arr1.shape)  # 返回数组的尺寸
arr1.ndim  # 返回数组的维度
arr1.dtype  # 返回数组的类型
arr2.shape  # 返回数组中元素的类型

list1 = [0, 0.3, 0.5]  # 对比列表和数组
# list1**2不能实现
list1 = [i ** 2 for i in list1]
arr1 ** 2  # 数组具备向量化运算能力，列表就不可以

arr3 = np.arange(0, 10)
arr4 = np.arange(0, 1, 0.1)  # 从0到1以0.1为间隔来创建数组
arr5 = np.linspace(0, 1, 10)  # 等和序列
arr6 = np.zeros([3, 4, 5])  # 三维四列五行的全零数组
# 数组创建后，其中数据类型就定了


np.int32(arr1)

# 生成随机数
np.random.random(10)  # 无约束下的随机数
np.random.rand(3, 4)  # 生成指定shape下均匀分布的随机数，三行四列
np.random.randn(10)  # 正态分布的随机数

# 数组的索引
arr1 = np.array([0.3, 0.78, 0.24, 5, 3.2])
arr1[1]  # 取数组的值，不是一个结构
arr1[1:3]  # 切片，一维数组多个元素的索引

# 逻辑型索引
arr1[[False, False, True, False, True]]
index = arr1 > 2  # 比较操作，每个元素比较后返回bool型数值
arr1[index]

# 多维数组的索引
arr8 = np.arange(1, 13).reshape([3, 4])
arr8[0, 0]  # 从0开始
arr8[2, 0:]  # 第2行所有数据
arr8[1:3, 1:3]
arr8[2:, :]  # 切片，返回值为数组这个结构

arr8[arr8[:, 0] > 4, :]  # 取出第一列中大于4的所有行

# 修改数组中的元素
arr8[0, 0] = 11

# 欧氏距离
n = 10
x = np.linspace(1, 100, n)  # 样本横坐标
y = np.linspace(1, 100, n)  # 样本纵坐标

dist = np.zeros([n, n])
dist[0, 1] = np.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)  # 第0个点到第1个点的距离
