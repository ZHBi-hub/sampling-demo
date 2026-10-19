# -*- coding: utf-8 -*-
import sys
from pathlib import Path
import qrcode
from PIL import Image, ImageDraw, ImageFont

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else input("请输入工具的公开链接：").strip()
    if not url:
        raise SystemExit("链接不能为空")
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    w, h = img.size
    canvas = Image.new("RGB", (w, h + 90), "white")
    canvas.paste(img, (0, 0))
    draw = ImageDraw.Draw(canvas)
    font_path = r"C:\Windows\Fonts\msyh.ttc"
    try:
        font = ImageFont.truetype(font_path, 30)
    except Exception:
        font = ImageFont.load_default()
    text = "扫码运行抽样定理仿真工具"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((w - tw) / 2, h + 20), text, font=font, fill=(23, 59, 87))
    out = Path(__file__).resolve().parent / "tool_qrcode.png"
    canvas.save(out, quality=95)
    print(out)

if __name__ == "__main__":
    main()
