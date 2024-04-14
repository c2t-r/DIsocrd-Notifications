import requests
import re
from bs4 import BeautifulSoup
from . import util

async def main() -> tuple[bool, list[dict]]:
    name = "manga_fgo3"

    url = "https://www.fate-go.jp/manga_fgo3/index.html"

    response = requests.get(url)

    html = response.content.decode()
    soup = BeautifulSoup(html, 'html.parser')

    data = util.load(name)
    if not data:
        data = {"latest": 0}
        util.save(name, data)

    news = soup.select_one("ul.hero_news li")
    latest = int(re.findall(r'第(\d+?)話', news.next)[0])
    title = news.next.next.next

    if latest == data["latest"]:
        return False, None

    data["latest"] = latest
    util.save(name, data)

    data = {
        "embeds": [
            {
                "color": 0xFF7100,
                "author": {
                    "name": "リヨ",
                    "icon_url": "https://www.fate-go.jp/manga_fgo2/images/common/author.png"
                },
                "title": f'第{latest}話 {title}',
                "url": f'https://www.fate-go.jp/manga_fgo3/comic{latest}.html',
                "image": {
                    "url": f'https://www.fate-go.jp/manga_fgo3/images/comic{latest}/comic.png'
                }
            }
        ]
    }

    return True, [data]
