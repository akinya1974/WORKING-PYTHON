

import requests
from pprint import pprint

files_url =
upload_url =

def get_token():
    with open('token.txt') as file:
        token = file.readline()
    return token


class YandexDisc:
    files_url: str =
    upload_url: str =

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Autorization': f'OAuth {self.token}'
        }

    @property
    def header(self):
        return self.get_headers()

    '''Получаем список файлов'''

    def get_files(self):
        responce = requests.get(self.files_url, headers=self.header)
        return responce.json()

    def _get_upload_link(self, file_path: str):
        params = {'path': file_path, 'overwrite': 'true'}
        response = requests.get(self.upload_url, params=params,  headers=self.header)
        pprint(response.json())
        return response.json()

    def upload(self, file_path: str, file_name: str):
        href = self._get_upload_link(file_path).get('href')
        if not href:
            return False

        response = requests.put(href, data=open(file_name, 'rb'))
        if response.status_code == 201:
            print('Файл загружен')
            return True

'''Загрузка файлов'''
    ya = YandexDisc(get_token())
    ya.upload('file.txt', 'file.txt')

    '''Получение списка файлов'''
    ya = YandexDisc(get_token())
    result = ya.get_files()
    pprint(result)


# import requests
# from pprint import pprint
#
# url = 'https://vk.com/sergiyakinshin'
#
# responce = requests.get(url, headers={'User-agent': 'netology'})
# pprint(responce.json())