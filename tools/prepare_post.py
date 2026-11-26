#!/usr/bin/env python3
"""通常投稿の準備: 写真を Instagram API 用の JPEG にして posts/ に置き、日付の JSON を書く。
使い方: python3 -I tools/prepare_post.py YYYY-MM-DD キャプションのファイル 写真1 [写真2 ...]
  - 写真は向きを直し、長辺1440px以内の JPEG(q92, sRGB)にする。切り取りや加工はしない。
  - 縦横比が 4:5(0.8)〜1.91:1 の外なら、止まる(Instagram が受け付けないため)。
  - 画像は posts/YYYY-MM-DD-1.jpg ... 、投稿の中身は posts/YYYY-MM-DD.json に書く。
"""
import sys, json, os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    date, cap_path, *photos = sys.argv[1:]
    if len(photos) > 10:
        sys.exit("写真は10枚まで")
    caption = open(cap_path, encoding="utf-8").read().strip()
    if not caption:
        sys.exit("キャプションが空")
    if len(caption) > 2200:
        sys.exit("キャプションが2200字を超えています: %d" % len(caption))
    if caption.count("#") > 30:
        sys.exit("ハッシュタグが30個を超えています")
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(os.path.dirname(here), "posts")
    os.makedirs(out, exist_ok=True)
    names = []
    for i, p in enumerate(photos, 1):
        im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
        w, h = im.size
        r = w / h
        if not (0.8 <= r <= 1.91):
            sys.exit("%s: 縦横比 %.3f は 0.8〜1.91 の外です(%dx%d)" % (p, r, w, h))
        s = 1440 / max(w, h)
        if s < 1:
            im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
        name = "%s-%d.jpg" % (date, i)
        im.save(os.path.join(out, name), "JPEG", quality=92, optimize=True)
        names.append(name)
        print(name, im.size, os.path.getsize(os.path.join(out, name)) // 1024, "KB")
    with open(os.path.join(out, date + ".json"), "w", encoding="utf-8") as f:
        json.dump({"caption": caption, "images": names}, f, ensure_ascii=False, indent=2)
    print("wrote posts/%s.json (%d枚, 本文%d字)" % (date, len(names), len(caption)))

main()
