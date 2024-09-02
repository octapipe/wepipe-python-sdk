from .models import FileModel
import requests
import os


class File(FileModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = '/files'
        self.__get_environment_vars()

    @classmethod
    def get_all(cls, card_id: int):
        file = cls()
        file.__get_environment_vars()
        params = {'entity': 'deal', 'record_id': card_id}
        response = requests.get(url=file.__url, headers=file.__headers, params=params)
        files = [cls(**file) for file in response.json()]
        return files if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    def post(self):
        if not self.record_id:
            raise ValueError("card_id is required to post a file.")
        if not self.entity:
            raise ValueError("entity is required to post a file.")
        if not self.name:
            raise ValueError("name is required to post a file.")
        if not self.url:
            raise ValueError("url is required to post a file.")
        if not self.mime:
            raise ValueError("mime is required to post a file.")
        if not self.size:
            raise ValueError("size is required to post a file.")
        url = f'{self.__url}/copy'
        file_json = self.model_dump(exclude_none=True)
        response = requests.post(url=url, headers=self.__headers, json=file_json)
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response.reason}'

    def delete(self):
        if not self.id:
            raise ValueError("id is required to delete a file.")
        url = f'{self.__url}/{self.id}'
        response = requests.delete(url=url, headers=self.__headers)
        return f'{response.status_code} - {response.reason}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_python_sdk.auth.login()')
        self.__url = os.getenv("API_URL") + self.__endpoint
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}
