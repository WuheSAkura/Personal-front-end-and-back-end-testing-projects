from matplotlib import pyplot as plt
import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
import jieba
from collections import Counter
import string
from wordcloud import WordCloud, STOPWORDS
import imageio

# 读取数据集到 DataFrame
data = pd.read_csv('数据集.csv', encoding='utf-8', on_bad_lines='skip')

# 将所有评论文本合并为一个长字符串，并移除标点符号
all_comments = ' '.join(str(comment).translate(str.maketrans('', '', string.punctuation)) for comment in data['评论内容'])

# 使用 jieba.cut_for_search 进行分词
words = jieba.cut_for_search(all_comments)

# 去除停用词并统计词频
word_list = []
stop_words = set(['就是','这是','但是','虽然','一部','觉得','还是','没有'])  # 假设这是您的停用词列表
for word in words:
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
bar = Bar(init_opts=opts.InitOpts(width="1200px", height="600px"))

# 添加 X 轴和 Y 轴数据
bar.add_xaxis(attr)
bar.add_yaxis("出现次数", value)

# 设置全局配置项，如标题等
bar.set_global_opts(title_opts=opts.TitleOpts(title="评论区出现频率最高的词汇"))

# 创建词云对象，并设置背景图
wc = WordCloud(background_color='white', max_words=200, stopwords=stop_words, font_path="C:\\Windows\\Fonts\\simhei.ttf", width=800, height=400)
back_color = imageio.imread(r'C:\Users\Administrator\Desktop\27\元气骑士背景图.jpg')

# 生成词云
wordcloud = wc.generate(all_comments)

# 显示词云图像
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存词云图像
wordcloud.to_file('wordcloud_with_background.png')
# 无背景版
# import pandas as pd
# from pyecharts.charts import HeatMap
# from pyecharts import options as opts

# # 假设CSV文件名为 data.csv，包含 'datetime', 'commenter', 'count' 列
# # 读取CSV文件
# df = pd.read_csv('数据集.csv')

# # 将日期时间列转换为datetime对象
# df['评论时间'] = pd.to_datetime(df['评论时间'])

# # 分离日期和时间
# df['日期'] = df['评论时间'].dt.date
# df['小时'] = df['评论时间'].dt.hour

# # 对评论者进行分类编码
# df['评论者_id'] = pd.Categorical(df['评论者']).codes

# # 创建热力图数据
# data = [(小时, 日期, 评论者_id) for 小时, 日期, 评论者_id in zip(df['小时'], df['日期'], df['评论者_id'])]

# # 初始化热力图
# heatmap = HeatMap()

# heatmap = HeatMap(init_opts=opts.InitOpts(width="1200px",height="600px"))

# # 添加X轴数据（时间）
# heatmap.add_xaxis([str(hour) for hour in range(24)])

# # 添加Y轴数据（日期）
# heatmap.add_yaxis("评论数量", [date.strftime("%Y-%m-%d") for date in df['日期'].unique()], data)

# # 设置全局配置项
# heatmap.set_global_opts(
#     title_opts=opts.TitleOpts(title="评论-时间分布"),
#     visualmap_opts=opts.VisualMapOpts(is_show=True,
#         max_=150,  
#         min_=0,
#         pos_right="1%",  # 假设的设置，具体值取决于库的 API
#     pos_top="bottom")
# )

# # 渲染图表到HTML文件
# heatmap.render('heatmap11.html')