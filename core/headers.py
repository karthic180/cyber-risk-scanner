import requests

def get_headers(domain):
    try:
        response = requests.get(f"https://{domain}", timeout=3)
        return response.headers
    except:
        return {}