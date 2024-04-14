from os.path import isfile
import json

name = "data.json"

if not isfile(name):
    with open(name, "w") as f: f.write('{}')

def load(key):
    with open(name, "r") as f:
        data = json.load(f)
    if not key in data:
        data[key] = {}
        save(key, data)
    return data[key]

def save(key, obj):
    with open(name, "r") as f:
        data = json.load(f)
    data[key] = obj
    with open(name, "w") as f:
        json.dump(data, f, indent=4)
    return
