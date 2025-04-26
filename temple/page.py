import random

def create_article_content(qr_img_url, content_img_url=None):
    # 文末小标题池
    footer_titles = [
        "小尾巴叮嘱一下",
        "悄悄说几句",
        "留个好运给你",
        "说完这句就冲啦",
        "下次见面，愿你已上岸"
    ]

    # 文末祝福语池
    footer_messages = [
        "🐰 宝子这么乖还点赞，那我偷偷祝你一整年考试都顺顺顺哒～",
        "🌸 键盘敲敲，锦鲤到账～愿你下一套题，都会温柔以待！",
        "🎯 你点赞的样子像极了考试顺利的模样～继续冲鸭！",
        "✅ 今天点个赞，明天高分上岸不是梦！咱就是说，flag已立，不准退！",
        "🐟 被你看到这句话，就是暗号：你就是那个注定上岸的锦鲤宝宝～",
        "💌 你点个赞，我送颗糖，再加一朵好运小红花，一起走花路吧！",
        "🔥 你今天的努力我都看到了，放心冲！接下来每一科都是你的主场！",
        "🌟 你认真读到这里，我已经在偷偷许愿：你一定超棒，一定上岸！"
    ]

    footer_title = random.choice(footer_titles)
    footer_message = random.choice(footer_messages)

    # 模板结构
    html_content = f"""
    <section style="font-family: 微软雅黑; text-align: left;">
        <!-- 二维码部分 -->
        <section style="margin: 20px 0;">
            <img src="{qr_img_url}" alt="二维码合集" style="max-width: 100%; height: auto;" />
        </section>

        <!-- 温馨提示部分 -->
        <section style="margin-left:5px;font-family:'PingFangSC','微软雅黑',sans-serif;font-size:16px;line-height:1.5em;text-align:left;">
            <section style="border:1px solid rgba(48,117,153,0.34);margin:5px 0 10px;background-color:#fafafa;">
                <section style="border:1px solid rgba(48,117,153,0.34);padding:5px 15px;transform:translate3d(-5px,-5px,0);">
                    <h3 style="margin:5px 0;font-size:16px;color:rgb(69,160,176);font-weight:bold;">
                        <img src="http://mmbiz.qpic.cn/sz_mmbiz_png/ibiaWnrjbqlryIyBrzSXlqsHNEBAG5gjCoS1awVkvLVJG1QBdNicZsnGibicPHrRIbkvFY6EhmLI1YtwaJsIBcVk3Sw/0?from=appmsg" 
                            style="width:16px;height:16px;vertical-align:middle;margin-right:5px;" />
                        <span style="margin-left:5px;">温馨提示</span>
                    </h3>
                    <section style="margin:5px 0;padding-left:22px;">🔔 本文内容整理自公开资料，仅供学习交流，若有疏漏欢迎指正。</section>
                    <section style="margin:5px 0;padding-left:22px;">🔔 资料购自第三方，仅作分享使用，不涉及任何商业行为，如有侵权请联系删除。</section>
                    <section style="margin:5px 0;padding-left:22px;">🔔 若想获取更针对性的解析，欢迎在评论区留言，我们会视反馈持续优化。</section>
                    <section style="margin:5px 0;padding-left:22px;">🔔 文末可订阅专栏合集，后续资料持续更新中，记得关注哦～</section>
                </section>
            </section>
        </section>


        <!-- 共享解析部分 -->
        <section style="margin-left:5px;font-family:'PingFangSC','微软雅黑',sans-serif;font-size:16px;line-height:1.5em;text-align:left;">
            <section style="border:1px solid rgba(48,117,153,0.34);margin:5px 0 10px;background-color:#fafafa;">
                <section style="border:1px solid rgba(48,117,153,0.34);padding:5px 15px;transform:translate3d(-5px,-5px,0);">
                    <h3 style="margin:5px 0;font-size:16px;color:rgb(69,160,176);font-weight:bold;">
                        <img src="http://mmbiz.qpic.cn/sz_mmbiz_png/ibiaWnrjbqlryIyBrzSXlqsHNEBAG5gjCoS1awVkvLVJG1QBdNicZsnGibicPHrRIbkvFY6EhmLI1YtwaJsIBcVk3Sw/0?from=appmsg" 
                        style="width:16px;height:16px;vertical-align:middle;margin-right:5px;" />
                        <span style="margin-left:5px;">共享解析</span>
                    </h3>
                    <section style="margin:5px 0;padding-left:22px;">
                        <a href="https://mp.weixin.qq.com/s/l_P96x1FognjcVxQ1Byasg" style="color:#45a0b0;text-decoration:none;">📘 湖南大学 2025 年数学分析试题解析</a>
                    </section>
                    <section style="margin:5px 0;padding-left:22px;">
                        <a href="https://mp.weixin.qq.com/s/l_P96x1FognjcVxQ1Byasg" style="color:#45a0b0;text-decoration:none;">    🐟 版本2</a> 
                        <a href="https://mp.weixin.qq.com/s/l_P96x1FognjcVxQ1Byasg" style="color:#45a0b0;text-decoration:none;">    🐟 版本3</a>
                        <a href="https://mp.weixin.qq.com/s/l_P96x1FognjcVxQ1Byasg" style="color:#45a0b0;text-decoration:none;">    🐟 版本4</a>                    
                    </section>
                    <section style="margin:5px 0;padding-left:22px;">
                        <a href="https://mp.weixin.qq.com/s/l_P96x1FognjcVxQ1Byasg" style="color:#45a0b0;text-decoration:none;">📘 湖南大学 2024 年数学分析试题解析</a>
                    </section>
                </section>
            </section>
        </section>

        <!-- 共享网盘部分 -->
        <section style="margin-left:5px;font-family:'PingFangSC','微软雅黑',sans-serif;font-size:16px;line-height:1.5em;text-align:left;">
            <section style="border:1px solid rgba(48,117,153,0.34);margin:5px 0 10px;background-color:#fafafa;">
                <section style="border:1px solid rgba(48,117,153,0.34);padding:5px 15px;transform:translate3d(-5px,-5px,0);">
                    <h3 style="margin:5px 0;font-size:16px;color:rgb(69,160,176);font-weight:bold;">
                        <img src="http://mmbiz.qpic.cn/sz_mmbiz_png/ibiaWnrjbqlryIyBrzSXlqsHNEBAG5gjCoS1awVkvLVJG1QBdNicZsnGibicPHrRIbkvFY6EhmLI1YtwaJsIBcVk3Sw/0?from=appmsg" 
                        style="width:16px;height:16px;vertical-align:middle;margin-right:5px;" />
                        <span style="margin-left:5px;">共享网盘</span>
                    </h3>
                    <section style="margin:5px 0;padding-left:22px;">
                        <p style="margin:5px 0;">📌 2000-2025年湖南大学数学分析试题</p>
                        <p style="margin:5px 0;">📌 2000-2025年湖南大学数学分析解析</p>
                    </section>
                    <section style="margin:5px 0;padding-left:22px;">
                        <p style="margin:5px 0;">📁 夸克网盘 https://pan.quark.cn/s/fe2822d0b031</p>
                        <p style="margin:5px 0;">📁 百度网盘 https://pan.baidu.com/s/1SHCo0WTVtjNTmMjl5n4UxQ?pwd=4b69</p>
                    </section>
                </section>
            </section>
        </section>

        <!-- 随机引导祝福部分 -->
        <section style="margin-left:5px;font-family:'PingFangSC','微软雅黑',sans-serif;font-size:16px;line-height:1.5em;text-align:left;">
            <section style="border:1px solid rgba(48,117,153,0.34);margin:5px 0 10px;background-color:#fafafa;">
                <section style="border:1px solid rgba(48,117,153,0.34);padding:5px 15px;transform:translate3d(-5px,-5px,0);">
                    <h3 style="margin:5px 0;font-size:16px;color:rgb(69,160,176);font-weight:bold;">
                        <img src="http://mmbiz.qpic.cn/sz_mmbiz_png/ibiaWnrjbqlryIyBrzSXlqsHNEBAG5gjCoS1awVkvLVJG1QBdNicZsnGibicPHrRIbkvFY6EhmLI1YtwaJsIBcVk3Sw/0?from=appmsg" 
                        style="width:16px;height:16px;vertical-align:middle;margin-right:5px;" />
                        <span style="margin-left:5px;">{footer_title}</span>
                    </h3>
                    <section style="margin:5px 0;padding-left:22px;"><p style="margin:5px 0;">{footer_message}</p>
                    </section>
                </section>
            </section>
        </section>
    </section>
    """

    return html_content