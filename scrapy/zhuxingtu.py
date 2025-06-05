import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
import jieba.posseg as psg
from collections import Counter
import string

# 假设 '数据集.csv' 文件中有一个名为 '评论内容' 的列
# 读取数据集到 DataFrame
data = pd.read_csv('数据集.csv', encoding='utf-8', on_bad_lines='skip')

# 将所有评论文本合并为一个长字符串，并移除标点符号
all_comments = ' '.join(str(comment).translate(str.maketrans('', '', string.punctuation)) for comment in data['评论内容'])

# 使用 psg.cut 进行分词
words = psg.cut(all_comments)

# 去除停用词并统计词频
word_list = []
stop_words = set(['的', '和', '是','没有'])  # 假设这是您的停用词列表
for word, flag in words:
    # 检查词的长度是否在两到三个字之间
    if 1 < len(word) < 4 and word not in stop_words:
        word_list.append(word)

# 使用 Counter 统计词频
word_counts = Counter(word_list)

# 获取出现频率最高的前10个词
most_common_words = word_counts.most_common(10)

# 提取词汇和对应的频率作为柱状图的数据
attr, value = zip(*most_common_words)

# 创建柱状图对象
bar = Bar(init_opts=opts.InitOpts(width="1000px", height="600px"))

# 添加 X 轴和 Y 轴数据
bar.add_xaxis(attr)
bar.add_yaxis("出现次数", value)

# 设置全局配置项，如标题等
bar.set_global_opts(title_opts=opts.TitleOpts(title="评论区出现频率最高的词汇"))

# 在 Jupyter Notebook 中渲染图表
#bar.render_notebook()  # 使用 render_notebook() 直接在 Notebook 中显示
bar.render("bar_chart1.html")  # 将图表保存为 HTML 文件