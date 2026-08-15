# WeChat Official Account HTML: Fix Missing Images, Broken Image Sizes, and Stripped CSS

> A field-tested guide for pasting **AI-generated / ChatGPT-generated / custom HTML** into WeChat Official Account articles.
>
> **Core fix: WeChat CDN (`mmbiz.qpic.cn`) + fully inline CSS.**

[中文完整指南](README.md)

## The problem

A custom HTML article can look perfect in Chrome or Edge but break after you paste it into the WeChat Official Account editor:

- Base64 images disappear.
- Images show up but lose their intended width and position.
- Two-column or staggered galleries break.
- `<style>` blocks and CSS classes are stripped or overridden.
- Pseudo-elements such as `::before` / `::after` disappear.
- HTML imported into third-party editors such as Xiumi may keep text/layout but lose images.

This is particularly common when an AI assistant generates a normal web page and you later try to paste it into WeChat.

## The tested solution

Treat image resources and CSS compatibility as **two separate problems**.

### 1. Move images into WeChat's own image system

Upload final images to a temporary WeChat draft, obtain the resulting `mmbiz.qpic.cn` URLs, and replace Base64/local sources:

```html
<img src="https://mmbiz.qpic.cn/...">
```

Do not rely on this as the final form:

```html
<img src="data:image/jpeg;base64,...">
```

### 2. Inline critical CSS

Do not leave important sizing/layout rules only in `<style>` or CSS classes.

Prefer:

```html
<section style="display:inline-block;width:39%;vertical-align:top;">
  <img
    src="https://mmbiz.qpic.cn/..."
    style="
      display:block;
      width:100% !important;
      max-width:100% !important;
      height:auto !important;
    "
  >
</section>
```

Critical properties to inline include `width`, `max-width`, `height`, `margin`, `padding`, `display`, `border`, `border-radius`, `box-shadow`, `transform`, `background`, typography, and `box-sizing`.

For important decorative elements, use real HTML nodes instead of relying only on `::before` / `::after`.

## Failure path observed in practice

```text
Base64 HTML
→ images disappear

MHT / MHTML
→ image resources may appear broken

WeChat CDN + normal stylesheet
→ images appear, but size/position may be wrong

WeChat CDN + partially inline CSS
→ some styling still gets stripped

WeChat CDN + fully inline CSS
→ successful
```

## Recommended AI-assisted workflow

```text
AI creates the visual HTML
→ refine in browser
→ upload final images to WeChat
→ replace image URLs with mmbiz.qpic.cn
→ inline critical CSS
→ replace critical pseudo-elements with real nodes
→ copy final HTML-rendered page
→ paste into WeChat Official Account editor
→ save as draft and verify on mobile
```

## Related search terms

WeChat Official Account HTML, WeChat HTML paste, WeChat HTML import, WeChat image missing, WeChat Base64 image, WeChat CSS stripped, WeChat inline CSS, WeChat CDN, mmbiz.qpic.cn, AI WeChat article, ChatGPT WeChat article, AI-generated WeChat HTML, Xiumi HTML images missing.

> This repository documents engineering observations from real editing tests. It is not an official WeChat specification, and editor behavior may change over time.
