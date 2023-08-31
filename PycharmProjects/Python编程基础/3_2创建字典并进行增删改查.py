dict_first = {
    'the': 2,
    3.4: [3.5, 4],
    'hello': 'world'
}
# 字典增删改查
dict_first['the']  # 通过键来对应值
dict_first['the'] = 101  # 修改
dict_first['woeld'] = 2.5  # 赋值新增键值对
dict_first.update({'hello world': 3, 4.5: 2})  # 值可以为字典，键不可以，因为键不可变
del dict_first['world']

dict_first.keys()  # 访问所有键
dict_first.values()  # 访问所有值
dict_first.items()  # 访问所有元素

second_dict = {i: i ** 2 for i in range(1, 11)}
# 统计单词词频
lyric = 'The night begin to shine, the night begin to shine'
# 1. 处理字符串（大小写转换）
lyric = lyric.lower()  # 转为小写

# 2. 将句子拆分成各单词
words = lyric.split()

# 3. 统计每个单词频次
word_freq = {}
for word in words:

    if word in word_freq.keys():  # 判定当前访问的键是否在语句中，在则当前值加一
        word_freq[word] += 1
    else:
        word_freq[word] = 1
        print(word)
# 4. 记录汇总
