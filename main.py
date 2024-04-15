from importlib import import_module
from concurrent import futures
from module.util import requests
from module.util import env
import asyncio
from time import sleep
import datetime
import json
import os
from sys import exit

env.set_name_space(globals())

def sendDiscord(webhook_url, content: dict):
    response = requests.post(webhook_url, data=json.dumps(content), headers={
        "Accept": "application/json",
        "Content-Type": "application/json",
    })
    return response

def runModule(m: dict):
    module = import_module("module." + m["module"])
    status, content = asyncio.run(module.main(*m["args"]))

    if not status: return

    for i in content:
        response = sendDiscord(m["webhook"], i)
        print(timeStr, response)

data = {}
if not os.path.isfile("data.json"):
    with open("data.json", "w", encoding="utf-8") as f:
        f.write("{}")
else:
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

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

    future_list = []
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        for m in modules:
            future = executor.submit(runModule, m)
            future_list.append(future)
        _ = futures.as_completed(future_list)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f'last checked: {timeStr}      ', end="\r")

    sleep(60)
