import requests
import json
from config import APP_ID, APP_SECRET, TOKEN_URL, DRAFT_ADD_URL
from image_uploader import upload_image
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
    article = {
        "article_type": "news",
        "title": meta["title"],
        "author": meta["author"],
        "digest": meta["digest"],
        "content": content,
        "thumb_media_id": meta["thumb_media_id"],
        "need_open_comment": 1,
        "only_fans_can_comment": 0
    }
    data = {"articles": [article]}
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    json_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
    resp = requests.post(url, data=json_data, headers=headers)
    return resp.json()

def create_article_content(qr_img_url, content_img_url=None):
    # 文章样式模板
    html_content = f"""
    <section style="font-family: 微软雅黑;">
        <!-- 头图部分 -->
        <section style="text-align: center; margin-bottom: 20px;">
            <img src="{content_img_url}" style="max-width: 100%; height: auto;" />
        </section>
        
        <!-- 二维码部分 -->
        <section style="margin: 20px 0;">
            <img src="{qr_img_url}" alt="二维码合集" style="max-width: 100%; height: auto;" />
        </section>
        
        <!-- 温馨提示部分 -->
        {get_tip_block()}
        
        <!-- 共享解析部分 -->
        <section style="margin: 20px 0; padding: 15px; background: #f8f8f8; border-radius: 5px;">
            <h2 style="color: #333; font-size: 18px; margin-bottom: 15px;">公众号共享解析：</h2>
            <ul style="list-style: none; padding-left: 0;">
                <li style="margin: 10px 0;">
                    <a href="https://mp.weixin.qq.com/s/l_P96x1FognjcVxQ1Byasg" style="color: #07C160; text-decoration: none;">
                        ▶ 湖南大学 2025 年数学分析试题解析
                    </a>
                </li>
                <li style="margin: 10px 0;">
                    <a href="https://mp.weixin.qq.com/s/l_P96x1FognjcVxQ1Byasg" style="color: #07C160; text-decoration: none;">
                        ▶ 湖南大学 2024 年数学分析试题解析
                    </a>
                </li>
            </ul>
        </section>
        
        <!-- 网盘资源部分 -->
        <section style="margin: 20px 0; padding: 15px; background: #f8f8f8; border-radius: 5px;">
            <h2 style="color: #333; font-size: 18px; margin-bottom: 15px;">网盘共享解析：</h2>
            <ol style="padding-left: 20px; color: #666;">
                <li>2000-2025年湖南大学数学分析真题</li>
                <li>2000-2025年湖南大学高等代数真题</li>
                <li>2000-2025年湖南大学数学分析解析</li>
                <li>2000-2025年湖南大学数学分析解析</li>
            </ol>
            <p style="margin: 15px 0; color: #666;">
                📁 夸克网盘：<a href="https://pan.quark.cn/s/fe2822d0b031" style="color: #07C160;">点击下载</a><br>
                📁 百度网盘：<a href="https://pan.baidu.com/s/1SHCo0WTVtjNTmMjl5n4UxQ?pwd=4b69" style="color: #07C160;">点击下载</a>（提取码：4b69）
            </p>
        </section>
    </section>
    """
    return html_content

def main():
    print("🔑 获取 Access Token...")
    token = get_access_token()
    print("✅ Token 获取成功:", token)

    # 可选：自动生成封面图（也可以关闭）
    # get_cover_image(query="数学分析")

    print("🖼️ 上传封面图...")
    image_result = upload_image("wechat_cover.jpg", token)
    media_id = image_result.get("media_id")
    if not media_id:
        print("❌ 上传封面失败")
        return

    print("🧾 生成二维码横排图...")
    qr_img_path = draw_qr_table(urls, labels, "qr_table.png")

    print("🌐 上传二维码横图...")
    qr_img_result = upload_image_for_content(qr_img_path, token)
    qr_img_url = qr_img_result.get("url")

    print("📤 上传正文插图（复用封面图）...")
    content_img_result = upload_image_for_content("wechat_cover.jpg", token)
    content_img_url = content_img_result.get("url")

    # 文章信息
    title = "湖南大学数学分析（610）历年试题解析"
    author = "木林儿"
    digest = "本文搜集分享了湖南大学数学分析（610）历年试题，详细讲解了重要知识点和解题方法。"

    html_content = create_article_content(qr_img_url, content_img_url)

    meta = {
        "title": title,
        "author": author,
        "digest": digest,
        "thumb_media_id": media_id
    }

    print("📝 创建草稿...")
    draft_result = create_draft(html_content, meta, token)
    print("📤 草稿上传结果:", json.dumps(draft_result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
