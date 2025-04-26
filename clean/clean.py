import requests

APP_ID = 'wx08729cb52d68c691'
APP_SECRET = '6067ce7db984ae5de21901b878c85995'
TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token"
GET_MATERIAL_LIST_URL = "https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token={}"
GET_DRAFT_LIST_URL = "https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token={}"
DELETE_DRAFT_URL = "https://api.weixin.qq.com/cgi-bin/draft/delete?access_token={}"
DELETE_MATERIAL_URL = "https://api.weixin.qq.com/cgi-bin/material/del_material?access_token={}"


def get_access_token():
    params = {
        "grant_type": "client_credential",
        "appid": APP_ID,
        "secret": APP_SECRET
    }
    resp = requests.get(TOKEN_URL, params=params)
    data = resp.json()
    if data.get("access_token"):
        return data["access_token"]
    else:
        print(f"获取access_token失败，错误信息: {data}")
        return None


def get_material_list(type="image", offset=0, count=20):
    access_token = get_access_token()
    if not access_token:
        print("无法获取access_token，无法获取素材列表")
        return

    url = GET_MATERIAL_LIST_URL.format(access_token)
    data = {
        "type": type,
        "offset": offset,
        "count": count
    }
    resp = requests.post(url, json=data)
    result = resp.json()
    if result.get("errcode") is None:
        print("素材列表获取成功")
        return result
    else:
        print(f"素材列表获取失败，错误信息: {result}")
        return None


def get_draft_list(offset=0, count=20):
    access_token = get_access_token()
    if not access_token:
        print("无法获取access_token，无法获取草稿列表")
        return

    url = GET_DRAFT_LIST_URL.format(access_token)
    data = {
        "offset": offset,
        "count": count
    }
    resp = requests.post(url, json=data)
    # 手动设置编码为 utf-8
    resp.encoding = 'utf-8'
    result = resp.json()
    if result.get("errcode") is None:
        print("草稿列表获取成功")
        return result
    else:
        print(f"草稿列表获取失败，错误信息: {result}")
        return None


def delete_draft(media_id):
    access_token = get_access_token()
    if not access_token:
        print("无法获取access_token，无法删除草稿")
        return

    url = DELETE_DRAFT_URL.format(access_token)
    data = {
        "media_id": media_id
    }
    resp = requests.post(url, json=data)
    result = resp.json()
    if result.get("errcode") == 0:
        print("草稿删除成功")
    else:
        print(f"草稿删除失败，错误信息: {result}")
    return result


def delete_permanent_material(media_id):
    access_token = get_access_token()
    if not access_token:
        print("无法获取access_token，无法删除永久素材")
        return

    url = DELETE_MATERIAL_URL.format(access_token)
    data = {
        "media_id": media_id
    }
    resp = requests.post(url, json=data)
    result = resp.json()
    if result.get("errcode") == 0:
        print("永久素材删除成功")
    else:
        print(f"永久素材删除失败，错误信息: {result}")
    return result


# 获取素材列表
material_list = get_material_list()
if material_list:
    print("素材列表：")
    for item in material_list.get("item", []):
        print(f"Media ID: {item['media_id']}, Name: {item.get('name', '未命名')}")

    media_id_to_delete = input("请输入要删除的素材的 Media ID（若不删除则直接回车）：")
    if media_id_to_delete:
        delete_permanent_material(media_id_to_delete)

# 获取草稿列表
draft_list = get_draft_list()
if draft_list:
    print("草稿列表：")
    for item in draft_list.get("item", []):
        print(f"Media ID: {item['media_id']}, Title: {item['content']['news_item'][0]['title']}")

    draft_media_id_to_delete = input("请输入要删除的草稿的 Media ID（若不删除则直接回车）：")
    if draft_media_id_to_delete:
        delete_draft(draft_media_id_to_delete)