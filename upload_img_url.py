import requests

def upload_image_for_content(file_path, access_token):
    url = f"https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token={access_token}"
    with open(file_path, 'rb') as f:
        files = {'media': f}
        resp = requests.post(url, files=files)
    return resp.json()
