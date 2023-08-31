# for循环语句
for i in range(10):
    print(i)      # 代码块（循环体）通过缩进进行限制
print(0.001)

s = 0
while s < 10:
    print(s)
    s += 1

# 任务实现
# 实现一组数的连加操作
vec = list(range(1, 11))    # 创建列表
m = 0
for i in vec:
    m += i
print(m)

# 实现一组数的连乘操作
x = list(range(1, 11))
n = 1
for i in x:
    n *= i
print(n)



