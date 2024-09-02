from .models import ContactModel
import requests
import os


class Contact(ContactModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = '/contacts'
        self.__get_environment_vars()

    @classmethod
    def get(cls, id: int):
        contact = cls()
        contact.__get_environment_vars()
        url = f'{contact.__url}/{id}'
        response = requests.get(url=url, headers=contact.__headers)
        contact_content = response.json()
        return cls(**contact_content) if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    @classmethod
    def get_all(cls, page: int = 1):
        contact = cls()
        contact.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=contact.__url, headers=contact.__headers, params=params)
        contacts = [cls(**contact) for contact in response.json()['data']]
        return contacts if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    def post(self):
        if not self.first_name:
            raise ValueError("first_name is required to post a contact.")
        contact_json = self.model_dump(exclude_none=True)
        response = requests.post(url=self.__url, headers=self.__headers, json=contact_json)
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response.reason}'

    def update(self):
        if not self.id:
            raise ValueError("id is required to update a contact.")
        url = f'{self.__url}/{self.id}'
        contact_json = self.model_dump(exclude_none=True)
        response = requests.put(url=url, headers=self.__headers, json=contact_json)
        return f'{response.status_code} - {response.reason}'

    def delete(self):
        if not self.id:
            raise ValueError("id is required to delete a contact.")
        url = f'{self.__url}/{self.id}'
        response = requests.delete(url=url, headers=self.__headers)
        return f'{response.status_code} - {response.reason}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_python_sdk.auth.login()')
        self.__url = os.getenv("API_URL") + self.__endpoint
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}
