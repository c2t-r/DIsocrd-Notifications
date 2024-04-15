import requests

def get(url: str, headers={}):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print("[NETWORK-ERROR]", response)
        print(e)
        return response
    except Exception as e:
        print("[ERROR]")
        print(e)
        return

def post(url: str, data, headers={}):
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print("[NETWORK-ERROR]", response)
        print(e)
        return response
    except Exception as e:
        print("[ERROR]")
        print(e)
        return
