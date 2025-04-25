import requests
from PIL import Image
from io import BytesIO
import random

PEXELS_API_KEY = 'xO81XPn02LcKhFu5Xx97bBXR4vMseJeNpM9opufBuPqxilsE6YMXFxep'

def get_cover_image(query='girl', width_crop_ratio=2.35):
    headers = {
        "Authorization": PEXELS_API_KEY
    }

    # 随机页码（例如最多 10 页）
    page = random.randint(1, 10)

    params = {
        "query": query,
        "per_page": 10,              # 一页多取几张，提高随机性
        "page": page,
        "orientation": "landscape"
    }

    response = requests.get("https://api.pexels.com/v1/search", headers=headers, params=params)

    if response.status_code != 200:
        raise Exception("Failed to fetch image:", response.text)

    data = response.json()

    if not data["photos"]:
        print("没有找到相关图片。")
        return

    # 从当前页随机取一张
    photo = random.choice(data["photos"])
    photo_url = photo["src"]["original"]
    print("图片原始链接：", photo_url)

    # 下载图片
    img_response = requests.get(photo_url)
    image = Image.open(BytesIO(img_response.content))

    # 裁剪为 2.35:1 比例
    width, height = image.size
    new_height = int(width / width_crop_ratio)
    top = (height - new_height) // 2
    cropped_image = image.crop((0, top, width, top + new_height))

    # 保存本地
    cropped_image.save("wechat_cover.jpg")
    print("封面图片已保存为 wechat_cover.jpg")

# 示例调用
get_cover_image("girl")
