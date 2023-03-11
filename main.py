import requests

TOKEN = 


class YaUploader:
    def __init__(self, disk_token: str):
        self.token = disk_token

    # https://yandex.ru/dev/disk/poligon/
    def upload(self, file_path: str, filename: str, file_format: str):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        # URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path={'smartest_hero.txt'}&overwrite={True}'
        # Получаем ответ на запрос загрузки файла в облако
        response = requests.get(f"{URL}/upload?path={filename}{file_format}&overwrite={True}", headers=headers).json()

        if 'href' not in response.keys():
            #  Если в ответе от Яндекс диска не было ссылки, возвращаем код ошибки
            print(f"Got an error: {response['error']}")
        else:
            #  Если ошибок не возникло, загружаем файл в облако
            with open(file_path, 'r') as file:
                # with open(file_path, 'rb') as file:
                requests.put(response['href'], files={'file': file})
            print(f"File was successfully uploaded")


if __name__ == '__main__':
    # Ссылка на облако и токен
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    # Загрузка реультата в облако
    yandex_loader = YaUploader(TOKEN)
    yandex_loader.upload(r"C:/Users/Владислав Сергеевич/Desktop/APXH/idпреложения.txt", 'коля', ".jpg")
