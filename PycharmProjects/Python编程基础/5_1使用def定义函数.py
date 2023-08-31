# Python内建函数
print('hello world')
int('101')

def def_sum(x, y):   # 自定义函数
    z = x + y
    print('hello world')
    # return z


def_sum(3, 4)        # 调用自定义的函数


# 任务实现：使用def关键字定义一个求列表均值的自定义函数
vec = [1, 2, 6, 0.3, 2, 0.5, -1, 2.4]


def def_mean(x):   # 定义函数
    m = 0
    for i in x:
        m += i
    return m/len(x)


def_mean(x=vec)    # 调用自定义的函数
