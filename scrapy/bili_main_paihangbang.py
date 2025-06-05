import csv
import requests

url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all&web_location=333.934&w_rid=a7e3807b5a8f384231c2c518387645fe&wts=1715169374"
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}
response = requests.get(url, headers=head)
response_json = response.json()
# print(response_json)

response_json_datas = response_json["data"]["list"]
# print(response_json_data)
rank = 1
with open(f'统计学.csv','w',encoding='utf-8',newline='') as filename:
    dictwriter = csv.DictWriter(filename,fieldnames=[
        "排名",
        "UP主",
        "UP主头像",
        "标题",
        "视频链接",
        "封面图",
        "作品分布ip",
        "作品类别",
        "评论数量",
        "播放量",
        "点赞数量",
        "弹幕数量",
    ])
    dictwriter.writeheader()
    for response_json_data in response_json_datas:
        pub_location = response_json_data.get("pub_location", "")  # 使用 get 方法获取 pub_location，如果不存在则默认为空字符串
        dic = {
            "排名": rank,
            "UP主": response_json_data["owner"]["name"],
            "UP主头像": response_json_data["owner"]["face"],
            "标题": response_json_data["title"],
            "视频链接": response_json_data["short_link_v2"],
            "封面图": response_json_data["pic"],
            "作品分布ip": pub_location,  # 使用变量 pub_location
            "作品类别": response_json_data["tname"],
            "评论数量": response_json_data["stat"]["danmaku"],
            "播放量": response_json_data["stat"]["view"],
            "点赞数量": response_json_data["stat"]["like"],
            "弹幕数量": response_json_data["stat"]["reply"],
        }
        dictwriter.writerow(dic)
        print(dic)
        rank += 1