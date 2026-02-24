import requests


def get_api(link:str):
    try:
        req = requests.get(link)
        req.raise_for_status()
        if req:
            data = req.json()
            return data
    except requests.exceptions.RequestException as e:
        print(f"error al hacer la conexion: {e}")
        return []
    
    
