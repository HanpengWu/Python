hello_world = 'start 123'

f = open('hello_world.txt', mode='w')     # 以写入的形式打开文件
f.write(hello_world)                      # 将数据写入至已打开的文件
f.close()     # 关闭文件
