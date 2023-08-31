
class Human:
    def __init__(self, age, gender):   # 构造函数
        self.age = age                 # 类的属性
        self.gender = gender

    def sqrt(self, x):
        return x**2


zhangfei = Human(age=23, gender='男')      # 类的实例化，得到一个具体对象
zhangfei.age         # 对象的属性
zhangfei.gender
zhangfei.sqrt(10)    # 调用对象的方法

caocao = Human(age=36, gender='男')       # 类的实例化，得到一个具体对象
all_in_list = [0.2, 0.25]
all_in_list.append(3.56)

# zhangfei.append(0.3)     # 非法操作，Human对象没有append方法
print(zhangfei)
print(all_in_list)