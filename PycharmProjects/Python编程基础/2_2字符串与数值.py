#单双引号都可以，三引号被用于长段文字，或引号不停止可以任意换行
string1 = 'Python1'
string2 = 'PYthon2'
string3 = '''1.35
Python3
Python4
2.44'''
print(string3)

#字符串基本操作
string1 + string2#合并字符串
string1*3#复制字符串
int('9')#将字符串转化为数值类型

#字符串索引及切片操作
print(string1)
string1[1]#正序索引，从0开始
string1[-6]#逆序索引，从-1开始
string1[0:3]#切片操作，左闭右开
string1[:3]#从开头取



# 1. 创建一个字符串变量“Apple's unit price is 9 yuan.”
applePriceStr = "Apple's unit price is 9 yuan"
# 2. 提取出里面的数字9并赋值给新的变量
applePrice = applePriceStr[-6]
print(applePrice)
# 3. 查看新变量的数据类型
print(type(applePrice))
# 4. 将提取的数字9转成整型（int）
applePriceInt = int(applePrice)
# 5. 确认数据类型是否转换成功。
print(type(applePriceInt))