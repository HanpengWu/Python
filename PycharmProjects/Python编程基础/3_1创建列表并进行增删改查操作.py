# 创建列表
all_in_list = [0.25, 'hello', True, [2.3, 1.5]]  # 任意Python变量都可以
list_example = list('AB1.5D')
print(all_in_list)

# 列表的索引及切片操作
print(all_in_list)
all_in_list[1]
all_in_list[-3]
all_in_list[0:3]
all_in_list[-4:-2]  # 从左往右去切片，不是大小
all_in_list[:]  # 取所有值

# 为列表新增元素
print(all_in_list)
all_in_list.append(0.78)  # 末尾新增
all_in_list.extend([1, 2])  # 将列表整体及列表里的元素也添加至末尾
all_in_list.insert(1, 'world')  # 选择第几个添加，指定位置
all_in_list + all_in_list  # 两个列表中元素合并

# 删除
print(all_in_list)

all_in_list.remove('hello')  # 删除指定元素
del all_in_list[0:2]  # 删除多个元素
del all_in_list  # 删除列表本身

# 修改
all_in_list[0] = 123

# 列表推导式
x = []
for i in range(1, 11):
    x.append(i)
X_new = [i for i in range(1, 11)]  # 通过列表推导式来构建一个具有特定规则的列表
[i ** 2 for i in range(1, 11)]  # 构建平方值

# 1. 将图形等份划分，得到若干小矩形（构建x序列）。

import math

n = 1000
width = 2 * math.pi / n  # 每个小矩形的宽
# x = [0*width,1*width,...(n-1)*width]
x = [i * width for i in range(0, n)]
# 2. 求出各小矩形的高度。
[abs(math.sin(x[i]) for i in range(n))]  # abs绝对值，求高度在n个矩形中遍历
# [abs(math.sin(i)*width for i in x)]#直接在x列表中遍历，与上面方法一样
# 3. 将各高度乘以宽度，得各小矩形面积，最后求和。
s = [abs(math.sin(i) * width for i in x)]
sum(s)
