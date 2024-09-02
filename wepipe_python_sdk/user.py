from .models import UserModel
import requests
import os


class User(UserModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = '/users'
        self.__get_environment_vars()

    @classmethod
    def get(cls, id: int):
        user = cls()
        user.__get_environment_vars()
        url = f'{user.__url}/{id}'
        response = requests.get(url=url, headers=user.__headers)
        user_content = response.json()
        return cls(**user_content) if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    @classmethod
    def get_all(cls, page: int = 1):
        user = cls()
        user.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=user.__url, headers=user.__headers, params=params)
        users = [cls(**user) for user in response.json()['data']]
        return users if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    def post(self):
        if not self.first_name:
            raise ValueError("first_name is required to post a user.")
        if not self.last_name:
            raise ValueError("last_name is required to post a user.")
        if not self.password:
            raise ValueError("password is required to post a user.")
        if not self.role:
            raise ValueError("role is required to post a user.")
        if not self.email:
            raise ValueError("email is required to post a user.")
        user_json = self.model_dump(exclude_none=True)
        response = requests.post(url=self.__url, headers=self.__headers, json=user_json)
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response.reason}'

    def update(self):
        if not self.id:
            raise ValueError("id is required to update a user.")
        url = f'{self.__url}/{self.id}'
        user_json = self.model_dump(exclude_none=True)
        response = requests.put(url=url, headers=self.__headers, json=user_json)
        return f'{response.status_code} - {response.reason}'

    def delete(self):
        if not self.id:
            raise ValueError("id is required to delete a user.")
        url = f'{self.__url}/{self.id}'
        response = requests.delete(url=url, headers=self.__headers)
        return f'{response.status_code} - {response.reason}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_python_sdk.auth.login()')
        self.__url = os.getenv("API_URL") + self.__endpoint
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}
