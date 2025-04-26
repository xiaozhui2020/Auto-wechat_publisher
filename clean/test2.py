from temple.tip_block_html import get_tip_block


def create_article_content(qr_img_url, content_img_url=None):
    # 文章样式模板
    html_content = f"""
    <section style="font-family: 微软雅黑;">
        
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
            <h3 style="color: #07C160; margin: 15px 0 10px 0;">网盘共享解析：</h3>
            <p>2000-2025年湖南大学数学分析真题</p>
            <p>2000-2025年湖南大学高等代数真题</p>
            <p>2000-2025年湖南大学数学分析解析</p>
            <p>2000-2025年湖南大学数学分析解析</p>
            <p>📁 夸克网盘：https://pan.quark.cn/s/fe2822d0b031<br></p>
            <p>📁 百度网盘：https://pan.baidu.com/s/1SHCo0WTVtjNTmMjl5n4UxQ?pwd=4b69</p>
        </section>
    </section>
    """
    return html_content
