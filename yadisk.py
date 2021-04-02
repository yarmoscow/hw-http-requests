import requests
import os
from pprint import pprint


host = 'https://cloud-api.yandex.net/'
token = '' # Вставить сюда свой токен
file_to_upload = 'test.txt'


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""
        filename = os.path.basename(file_path)
        params = {"path" : filename, "overwrite" : "true"}
        headers = {"Authorization" : "OAuth "+token}
        resp = requests.get(host+'v1/disk/resources/upload', params=params, headers=headers)
        if resp.status_code != 200:
            return 'Error requesting upload URL, HTTP status code: '+str(resp.status_code)
        resp_put = requests.put(resp.json()['href'], data=open(file_path, 'rb'))
        if resp_put.status_code != 201:
            return 'Error uploading file, HTTP status code: ' + str(resp_put.status_code)
        else:
            return 'Файл успешно загружен'


if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload(file_to_upload)
    print(result)