# sanji-story-images

酒肆 参事（@shushi_sanji）のInstagramストーリーズ用の、日付入り画像（1080x1920、JPEG）です。

- `stories/YYYY-MM-DD.jpg` … その日の18:00（日本時間）に投稿される画像。
- 投稿は Cloudflare Worker（`sanji-story`）が、営業日（火〜土）の18:00〜18:30に行います。その日の画像が無いときは、投稿しません。
- 画像は公開されます（Instagramが取得するため）。個人情報や秘密は入れません。
