import re
# 读取文本文件
f = open('walden.txt', mode='r')  # 按照指定的方式打开文件
txt = f.read()                    # 读取具体文件数据
f.close()                         # 关闭文件

# f = open('walden.txt', mode='r')  # 按照指定的方式打开文件
# txt = f.readlines()                    # 读取具体文件数据
# f.close()

# 任务实现
# 1.读取数据
f = open('walden.txt', mode='r')  # 按照指定的方式打开文件
txt = f.read()                    # 读取具体文件数据
f.close()                         # 关闭文件
# 2.去除多余符号
lyric = txt.lower()      # 将大写字母转换成小写形式
lyric_new = re.sub('[,.:"\'?\n;-]', '', lyric)  # 去除多余的标点符号
# 3.单词分割
words = lyric_new.split()
# 4.词频统计
word_freq = {}                          # 构建一个空字典，用于后续记录各单词的频次
for word in words:
    if word not in word_freq.keys():    # 判断当前访问的单词是否在字典中
        word_freq[word] = 1             # 若不在则以该单词为键创建一个键值对，且赋值为一
    else:
        word_freq[word] += 1            # 若在，则将该单词对应键的值加一
# 5.排序
result = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# 6.写出结果
result_string = str(result)    # 将结果转换成字符串形式

with open('word_freq.txt', mode='w') as f:
    f.write(result_string)     # 将结果数据写入至指定文件中
