import requests
import json
from config import APP_ID, APP_SECRET, TOKEN_URL, DRAFT_ADD_URL
from image_uploader import upload_image
from temple.page import create_article_content
from upload_img_url import upload_image_for_content
from my_photo import get_cover_image  # 可选：生成封面图
from qr_image import draw_qr_table
from temple.tip_block_html import get_tip_block

# 示例数据
labels = ["刷题本", "数分基础", "高代基础", "快捷打印"]
urls = [ "https://www.xiaohongshu.com/goods-detail/680238ed4d5fd500010a5512?t=1744976934013&xsec_token=ABm_M_o_4WDvAMLXm9dTuzDPlEUUA067ibdyAbdULCmu8%3D&xsec_source=pc_arkselfshare",
    "https://www.xiaohongshu.com/goods-detail/67f270ebe8f2430001fdc29b?t=1744594568067&xsec_token=ABhdhZXXQSR75z-XObMXq4iOBpKMg4zlo6W7ArhPthRz0%3D&xsec_source=pc_arkselfshare",
    "https://www.xiaohongshu.com/goods-detail/67f26f085d35ce0001a44547?t=1744594859287&xsec_token=AB9lsbSshua_s_XaQbQJPTR4t3zuDVblBlqWZVEiapq_M%3D&xsec_source=pc_arkselfshare",
    "https://printh5.xiaohouyunyin.com/channel/to-mini?channel_id=13063"
    ]
def get_access_token():
    params = {
        "grant_type": "client_credential",
        "appid": APP_ID,
        "secret": APP_SECRET
    }
    res = requests.get(TOKEN_URL, params=params)
    return res.json().get("access_token")

def create_draft(content, meta, token):
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}"
    
    # 增加更多文章配置
    article = {
        "title": meta["title"],
        "author": meta["author"],
        "digest": meta["digest"],
        "content": content,
        "thumb_media_id": meta["thumb_media_id"],
        "need_open_comment": 1,  # 开启评论
        "only_fans_can_comment": 0,  # 所有人可评论
        #"content_source_url": "",  # 原文链接，可选
        #"article_type": "news",  # 图文消息类型
        #"show_cover_pic": 1,  # 显示封面
    }
    
    data = {"articles": [article]}
    headers = {
        'Content-Type': 'application/json; charset=utf-8'
    }
    
    try:
        json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
        resp = requests.post(url, data=json_data, headers=headers)
        result = resp.json()

        # 添加更详细的错误信息输出
        print(f"API 响应结果：{json.dumps(result, ensure_ascii=False, indent=2)}")
            
    except Exception as e:
        print(f"❌ 发生错误：{str(e)}")
        return None


def main():
    # 1. 获取 access token
    print("🔑 获取 Access Token...")
    token = get_access_token()
    if not token:
        print("❌ 获取 Token 失败")
        return
    print("✅ Token 获取成功")

    # 2. 生成/上传封面图
    print("🖼️ 处理封面图...")
    #get_cover_image(query="数学分析", width_crop_ratio=2.35)  # 生成封面
    image_result = upload_image("wechat_cover.jpg", token)
    media_id = image_result.get("media_id")
    if not media_id:
        print("❌ 上传封面失败")
        return
    print("✅ 封面图上传成功")

    # 3. 生成并上传二维码图片
    print("🧾 生成二维码表格...")
    qr_img_path = draw_qr_table(urls, labels, "qr_table.png")
    qr_img_result = upload_image_for_content(qr_img_path, token)
    qr_img_url = qr_img_result.get("url")
    if not qr_img_url:
        print("❌ 二维码图片上传失败")
        return
    print("✅ 二维码图片上传成功")

    # 4. 上传文章内容图片
    print("📤 上传文章内容图片...")
    content_img_result = upload_image_for_content("wechat_cover.jpg", token)
    content_img_url = content_img_result.get("url")
    if not content_img_url:
        print("❌ 文章内容图片上传失败")
        return
    print("✅ 文章内容图片上传成功")

    # 5. 准备文章信息
    meta = {
        "title": "湖南大学数学分析（610）历年试题解析",
        "author": "木林儿",
        "digest": "本文搜集分享了湖南大学数学分析（610）历年试题，详细讲解了重要知识点和解题方法。",
        "thumb_media_id": media_id
    }

    # 6. 生成文章内容
    html_content = create_article_content(qr_img_url, content_img_url)

    # 7. 创建草稿
    print("📝 创建草稿...")
    draft_result = create_draft(html_content, meta, token)
    # if draft_result:
    #     print("✅ 草稿创建成功")
    #     print("📤 草稿详情:", json.dumps(draft_result, indent=2, ensure_ascii=False))
    # else:
    #     print("❌ 草稿创建失败")

if __name__ == "__main__":
    main()
