import requests


def new_folder(folder_name):
    token_ya = 'тут должен быть токен'
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {
        "Accept": "application/json",
        "Authorization": "OAuth " + token_ya
    }
    params = {
        'path': folder_name,
        "Accept": "application/json",
        "Authorization": "OAuth " + token_ya
    }
    res = requests.put(url=url, params=params, headers=headers)
    if res.status_code == 201:
        return res.status_code
    if res.status_code == 409:
        raise ValueError('Папка с таким названием уже существует')


if __name__ == '__main__':
    print(new_folder('345435'))
