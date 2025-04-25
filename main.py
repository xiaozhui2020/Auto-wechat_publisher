import requests
import json
from config import APP_ID, APP_SECRET, TOKEN_URL, DRAFT_ADD_URL
from image_uploader import upload_image
from upload_img_url import upload_image_for_content

def get_access_token():
    params = {
        "grant_type": "client_credential",
        "appid": APP_ID,
        "secret": APP_SECRET
    }
    res = requests.get(TOKEN_URL, params=params)
    return res.json().get("access_token")

def create_draft(access_token, title, content, thumb_media_id):
    url = DRAFT_ADD_URL.format(access_token)

    article = {
        "title": title,
        "content": content,
        "thumb_media_id": thumb_media_id
    }

    data = {
        "articles": [article]
    }

    headers = {'Content-Type': 'application/json'}
    resp = requests.post(url, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers)
    return resp.json()

def main():
    print("🔑 获取 Access Token...")
    token = get_access_token()
    print("✅ Token:", token)

    print("🖼️ 上传封面图...")
    image_result = upload_image("wechat_publisher/cover.jpg", token)
    print("📦 上传结果:", image_result)

    media_id = image_result.get("media_id")
    if not media_id:
        print("❌ 上传封面失败")
        return
    
    # 上传一张图文正文图
    img_result = upload_image_for_content("wechat_publisher/cover.jpg", token)
    img_url = img_result.get("url")

    print("📝 创建草稿...")
    # 构造图文内容
    html = f"<h1>这是标题</h1><p>这是正文</p><img src='{img_url}' />"

    draft_result = create_draft(token, "测试文章", html, media_id)
    print("📤 草稿上传结果:", draft_result)

if __name__ == "__main__":
    main()
