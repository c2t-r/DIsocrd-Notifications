# Discord-Notifications
a sample code to create a simple notification bot for discord  

## How to run
1. clone this repo
2. edit [`settings.json`](settings.json)
3. run `py main.py`

note: do not edit `data.json` by yourself. it will be generated automatically.  

## How to add modules
1. write code based on [`module/fortune.py`](module/fortune.py) (sample module)
2. add your module on [`settings.json`](settings.json)

## settings.json
```json
[
    {
        "name": "fortune_teller",    // just a name to manage modules
        "enabled": true,             // if this module is enabled
        "module": "fortune",         // the module name (file name)
        "args": [],                  // main() function's argments to run
        "cool": 120,                 // cool time (mins)
        "webhook": "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"   // discord webhook url
    }
]
```

## Example
output for example module [`module/fortune.py`](module/fortune.py)  
![image](https://github.com/c2t-r/DIsocrd-Notifications/assets/80561604/570fe00e-4e04-4e68-aa1f-d27499fe9e3c)
