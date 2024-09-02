from .models import CardModel
import requests
import os


class Card(CardModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = '/cards'
        self.__get_environment_vars()

    @classmethod
    def get(cls, id: int):
        card = cls()
        card.__get_environment_vars()
        url = f'{card.__url}/{id}'
        response = requests.get(url=url, headers=card.__headers)
        card_content = response.json()
        return cls(**card_content) if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    @classmethod
    def get_all(cls, page: int = 1):
        card = cls()
        card.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=card.__url, headers=card.__headers, params=params)
        cards = [cls(**card) for card in response.json()['data']]
        return cards if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    def post(self):
        if not self.pipeline_id:
            raise ValueError("pipeline_id is required to post a card.")
        if not self.pipeline_stage_id:
            raise ValueError("pipeline_stage_id is required to post a card.")
        if not self.name:
            raise ValueError("name is required to post a card.")
        card_json = self.model_dump(exclude_none=True)
        response = requests.post(url=self.__url, headers=self.__headers, json=card_json)
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response.reason}'

    def update(self):
        if not self.id:
            raise ValueError("id is required to update a card.")
        url = f'{self.__url}/{self.id}'
        card_json = self.model_dump(exclude_none=True)
        response = requests.put(url=url, headers=self.__headers, json=card_json)
        return f'{response.status_code} - {response.reason}'

    def delete(self):
        if not self.id:
            raise ValueError("id is required to delete a card.")
        url = f'{self.__url}/{self.id}'
        response = requests.delete(url=url, headers=self.__headers)
        return f'{response.status_code} - {response.reason}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_python_sdk.auth.login()')
        self.__url = os.getenv("API_URL") + self.__endpoint
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}
