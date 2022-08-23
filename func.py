import requests

def get_ip_info(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            '[IP]': response.get('query'),
            '[COUNTRY]': response.get('country'),
            '[CITY]': response.get('regionName'),
            '[ZIP]': response.get('zip')
        }
        for k, v in data.items():
            print(f"{k}: {v}")
    except Exception as exception:
        print(exception)