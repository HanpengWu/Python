import re

f = open('walden.txt', mode='r')
# f.seek(0)
# 1. 读取数据
# with open('walden.txt','r') as f :
#     f.seek(0)
#     txt = f.read()
#     f.close()
#     type(txt)

# f.seek(0)
txt = f.read()
f.close()
type(txt)

# f = open('walden.txt', mode='r')  # 按照指定的方式打开文件
# txt = f.readlines()                    # 读取具体文件数据
# f.close()

# 2. 去除多余符号
lyric = txt.lower()  # 转换为小写
lyric_new = re.sub('[,.:"\'?\n;-]', '', lyric)
# 3. 单词分割
words = lyric_new.split()
# 4. 词频统计
word_freq = {}
for word in words:
    if word not in word_freq.keys():
        word_freq[word] = 1
    else:
        word_freq[word] += 1
# 5. 排序
word_freq.items()
result = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
# 引用sorted排序，取字典中每一个键值，排序依据为lambda隐匿函数，取键值中的值为依据，由高至低
# 6. 写出结果
type(result)
result_string = str(result)

with open('word_freq.txt', mode='w') as f:  # 使用with open方法可以避免占用文件导致其他代码报错的问题
    f.write(result_string)

# pip install markdown -i http://pypi.douban.com/simple/
