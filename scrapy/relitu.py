import pandas as pd
from pyecharts.charts import HeatMap
from pyecharts import options as opts

# 假设CSV文件名为 data.csv，包含 'datetime', 'commenter', 'count' 列
# 读取CSV文件
df = pd.read_csv('数据集.csv')

# 将日期时间列转换为datetime对象
df['评论时间'] = pd.to_datetime(df['评论时间'])

# 分离日期和时间
df['日期'] = df['评论时间'].dt.date
df['小时'] = df['评论时间'].dt.hour

# 对评论者进行分类编码
df['评论者_id'] = pd.Categorical(df['评论者']).codes

# 创建热力图数据
data = [(小时, 日期, 评论者_id) for 小时, 日期, 评论者_id in zip(df['小时'], df['日期'], df['评论者_id'])]

# 初始化热力图
heatmap = HeatMap()

heatmap = HeatMap(init_opts=opts.InitOpts(width="1200px",height="600px"))

# 添加X轴数据（时间）
heatmap.add_xaxis([str(hour) for hour in range(24)])

# 添加Y轴数据（日期）
heatmap.add_yaxis("评论数量", [date.strftime("%Y-%m-%d") for date in df['日期'].unique()], data)

# 设置全局配置项
heatmap.set_global_opts(
    title_opts=opts.TitleOpts(title="评论-时间分布"),
    visualmap_opts=opts.VisualMapOpts(is_show=True,
        max_=150,  
        min_=0,
        pos_right="1%",  # 假设的设置，具体值取决于库的 API
    pos_top="bottom")
)

# 渲染图表到HTML文件
heatmap.render('heatmap11.html')