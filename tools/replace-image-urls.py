#!/usr/bin/env python3
"""
Replace <img src> values in an HTML file with WeChat CDN URLs, in document order.

Usage:
    python replace-image-urls.py article.html urls.txt article.wechat.html
"""
from pathlib import Path
import sys
from bs4 import BeautifulSoup

if len(sys.argv) != 4:
    raise SystemExit("Usage: python replace-image-urls.py INPUT.html URLS.txt OUTPUT.html")

src, urls_file, out = map(Path, sys.argv[1:])
urls = [line.strip() for line in urls_file.read_text(encoding="utf-8").splitlines() if line.strip()]
soup = BeautifulSoup(src.read_text(encoding="utf-8"), "html.parser")
imgs = soup.find_all("img")

if len(imgs) != len(urls):
    raise SystemExit(f"Image count mismatch: HTML has {len(imgs)} images, URL list has {len(urls)} URLs.")

for img, url in zip(imgs, urls):
    img["src"] = url
    img["data-src"] = url

out.write_text(str(soup), encoding="utf-8")
print(f"Wrote {out} with {len(urls)} WeChat CDN image URLs.")
