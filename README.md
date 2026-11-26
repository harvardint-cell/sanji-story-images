# sanji-story-images

酒肆 参事の Instagram 自動投稿（Cloudflare Worker `sanji-story`）が読む公開リポジトリ。
毎営業日（火〜土）18:00〜18:30（JST）に Worker が投稿する。

- `stories/YYYY-MM-DD.jpg` … その日のストーリーズ（1080x1920 JPEG）
- `posts/YYYY-MM-DD.json` と `posts/YYYY-MM-DD-N.jpg` … その日の通常投稿（写真1枚、または2〜10枚のカルーセル）。
  JSON は `{"caption": "...", "images": ["YYYY-MM-DD-1.jpg", ...]}`。
- ファイルが無い日は、何も投稿しない。投稿を取りやめるときはファイルを消す（18:00 まで）。
- `tools/prepare_post.py` … 写真を JPEG にして JSON を作る。
