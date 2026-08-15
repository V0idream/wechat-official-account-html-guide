// Run this in the browser Console on a WeChat Official Account draft page.
// It collects unique WeChat CDN image URLs and copies them to the clipboard.
const urls = [...document.querySelectorAll('img')]
  .flatMap(img => [
    img.getAttribute('data-src'),
    img.getAttribute('src'),
    img.currentSrc
  ])
  .filter(Boolean)
  .map(url => url.replace(/&amp;/g, '&'))
  .filter(url => url.includes('mmbiz.qpic.cn'))
  .filter((url, i, arr) => arr.indexOf(url) === i);

console.table(urls.map((url, i) => ({
  index: String(i + 1).padStart(2, '0'),
  url
})));

copy(urls.join('\n'));
