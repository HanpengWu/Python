if 1 < 2:
    print('hello')
elif 2 > 3:
    pass
# 多路分支elif


try:
    print(hello)
except NameError:
    print('hello')  # 假设出现什么错误则执行什么操作
# 1. 创建一个变量，输入任意数值作为成绩并赋予该变量。
try:
    score = input('请输入考试成绩：')
    score = float(score)     # 将数据转为浮点类型
    if score >= 90:
        print('A')
    elif 80 <= score < 90:
        print('B')
    elif 70 <= score < 80:
        print('C')
    elif 60 <= score < 70:
        print('D')
    else:
        print('E')
except:
    print('输入的成绩是非数值型的！')


# 2. 检测输入的内容是否为数值型的数据。
# 3. 设置条件分支判断成绩属于哪个等级。
# 4. 打印结果
