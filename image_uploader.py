import requests
from config import UPLOAD_IMAGE_URL

def upload_image(file_path, access_token):
    url = UPLOAD_IMAGE_URL.format(access_token)
    with open(file_path, 'rb') as f:
        files = {'media': f}
        resp = requests.post(url, files=files)
    return resp.json()

