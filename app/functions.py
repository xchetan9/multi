# app/functions.py
import requests

api_configs = {
    "sendcm": {
        "key": "233675oewkgzcw80s21ibm",
        "url": "https://send.cm/api/upload/url"
    },
    "mediacm": {
        "key": "8475ait8co2ohk0mvhaf",
        "url": "https://media.cm/api/upload/url"
    },
    "filemoonapi": {
        "key": "49874pa34xr1tm3fkssf7",
        "url": "https://filemoonapi.com/api/remote/add"
    },
    "streamwish": {
        "key": "13582uc1lasxn8w58ygse",
        "url": "https://api.streamwish.com/api/upload/url"
    },
    "doodapi": {
        "key": "376614ml7l0hfanknuvyi2",
        "url": "https://doodapi.com/api/upload/url"
    },
    "upstream": {
        "key": "62199tturjoywvahvhobc",
        "url": "https://upstream.to/api/upload/url"
    }
}

def upload_to_api(api_config, url):
    try:
        full_url = f"{api_config['url']}?key={api_config['key']}&url={url}"
        response = requests.get(full_url)
        if response.status_code == 200:
            data = response.json()
            if data.get('result'):
                return data['result']['filecode']
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
