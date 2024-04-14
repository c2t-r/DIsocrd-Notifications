import requests
from random import random
from . import util

suffixes = ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th"]

async def main() -> tuple[bool, list[dict]]:
    name = "fortune_teller"

    url = "http://worldtimeapi.org/api/timezone/Asia/Tokyo"

    response = requests.get(url)

    obj = response.json()
    day = obj["day_of_year"]

    data = util.load(name)
    if not data:
        data = {"latest": 0}
        util.save(name, data)

    if day == data["latest"]:
        return False, None

    data["latest"] = day
    util.save(name, data)

    if random() > 0.7: # 30% lucky
        luck = "lucky!"
        color = 0x64FF00
    else:
        luck = "unlucky..."
        color = 0x0000FF

    suffix = suffixes[int(str(day)[-1])]

    data = {
        "username": "certain fortune teller",
        "avatar_url": "https://i.imgur.com/w44p22m.png", # sorry for use
        "embeds": [
            {
                "color": color,
                "title": "Today is...",
                "description": f'{day}{suffix} of this year! Your luck today is ||{luck}||',
                "timestamp": obj["datetime"]
            }
        ]
    }

    return True, [data]
