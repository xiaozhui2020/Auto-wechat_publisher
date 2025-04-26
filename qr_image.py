from PIL import Image, ImageDraw, ImageFont
import qrcode
from PIL import ImageFilter

def generate_qr_image(url, size=200):
    qr = qrcode.QRCode(box_size=10, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize((size, size))

def draw_qr_table(urls, labels, output_path='qr_table.jpg'):
    assert len(urls) == len(labels)

    # 参数
    qr_size = 240
    padding = 20
    header_height = 60
    font_path = "C:/Windows/Fonts/msyh.ttc" 
    font_size = 35

    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print("⚠️ 字体加载失败，请检查字体路径")
        font = ImageFont.load_default()

    # 生成二维码
    qr_images = [generate_qr_image(url, qr_size) for url in urls]

    # 创建整张图
    width = len(qr_images) * (qr_size + padding) + padding
    height = header_height + qr_size + padding * 2

    img = Image.new('RGBA', (width, height), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    assert len(urls) == len(labels)

    # 样式参数
    qr_size = 240
    padding = 30
    shadow_offset = 8
    header_height = 60
    border_thickness = 2

    # 加载字体
    try:
        font = ImageFont.truetype(font_path, font_size)
    except:
        font = ImageFont.load_default()

    
    qr_images = [generate_qr_image(url, qr_size) for url in urls]
    width = len(qr_images) * (qr_size + padding) + padding
    height = header_height + qr_size + padding * 2

    img = Image.new('RGBA', (width + 2 * border_thickness, height + 2 * border_thickness), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 样式色彩（与下方卡片一致）
    border_color = (48, 117, 153, int(255 * 0.34))       # rgba(48,117,153,0.34)
    header_bg_color = (230, 244, 249, 255)               # #e6f4f9 淡蓝背景
    font_color = (69, 160, 176, 255)                     # 表头字体颜色

    # 外边框
    draw.rectangle([(0, 0), (img.width - 1, img.height - 1)], outline=border_color, width=border_thickness)

    # 表头背景
    draw.rectangle(
        [(border_thickness, border_thickness),
         (img.width - border_thickness, border_thickness + header_height)],
        fill=header_bg_color
    )

    # 表头文字（上移使其更居中）
    for i, label in enumerate(labels):
        bbox = draw.textbbox((0, 0), label, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = border_thickness + padding + i * (qr_size + padding) + (qr_size - text_w) // 2
        y = border_thickness + header_height // 8 - text_h // 8  # 垂直居中
        draw.text((x, y), label, fill=font_color, font=font)


    # 插入二维码及其阴影
    for i, qr in enumerate(qr_images):
        shadow = Image.new('RGBA', (qr_size, qr_size), color=(0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rectangle([0, 0, qr_size, qr_size], fill=(0, 0, 0, 80))
        shadow = shadow.filter(ImageFilter.GaussianBlur(4))

        x = border_thickness + padding + i * (qr_size + padding)
        y = border_thickness + header_height + padding

        img.paste(shadow, (x + shadow_offset, y + shadow_offset), shadow)
        img.paste(qr, (x, y))

    img.save(output_path, format='PNG')
    print(f"✅ 表格风格二维码图已保存：{output_path}")
    return output_path

# # 示例数据
# urls = [
#     "https://example.com/a", 
#     "https://example.com/b", 
#     "https://example.com/c", 
#     "https://example.com/d"
# ]
# labels = ["刷题本", "数分基础", "高代基础", "快捷打印"]

# draw_qr_table(urls, labels)