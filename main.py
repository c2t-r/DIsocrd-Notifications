from importlib import import_module
import requests
import asyncio
from time import sleep
import datetime
import json
import os
from sys import exit

def sendDiscord(webhook_url, content: dict):
    response = requests.post(webhook_url, data=json.dumps(content), headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
    })
    return response

if not os.path.isfile("data.json"):
    with open("data.json", "w", encoding="utf-8") as f:
        f.write("{}")

with open("settings.json", "r") as f:
    settings = json.load(f)
    modules = [i for i in settings if i["enabled"]]
    if not modules:
        print("no module enabled, bye")
        exit()
    else:
        print(f'{len(modules)} module(s) found. \n{", ".join([i["name"] for i in modules])}')
        print()

while True:

    now = datetime.datetime.now()
    timeStr = now.isoformat(" ", timespec="seconds")

    if 23 <= now.hour or now.hour <= 6:
        print(f'it\'s night now... {timeStr}', end="\r")
        sleep(600)
        continue

    for m in modules:

        module = import_module("module." + m["module"])
        status, data = asyncio.run(module.main(*m["args"]))

        if not status: continue
        
        for i in data:
            try:
                response = sendDiscord(m["webhook"], i)
                print(timeStr, response)
                sleep(3)
            except Exception as e:
                print(timeStr, e)
                sleep(60)

        #sleep(10)

    print(f'last checked: {timeStr}      ', end="\r")
    
    sleep(60)
