# DIsocrd-Notifications
a sample code to create a simple notification bot for discord

## How to run
1. clone this repo
2. edit `settings.json`
3. run `py main.py`

note: do not edit `data.json` by yourself. it will be generated automatically.

## How to add modules
1. write code based on `module/manga_fgo3.py` (sample module)
2. add your module on `settings.json`

## settings.json
```json
[
    {
        "name": "manwaka_3",                                             // just a name to manage modules
        "enabled": true,                                                 // if this module is enabled
        "module": "manga_fgo3",                                          // the module name (file name)
        "args": [],                                                      // main() function's argments to run
        "webhook": "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"   // discord webhook url
    }
]
```
