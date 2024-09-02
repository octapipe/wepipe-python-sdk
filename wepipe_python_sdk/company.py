from .models import CompanyModel
import requests
import os


class Company(CompanyModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = '/companies'
        self.__get_environment_vars()

    @classmethod
    def get(cls, id: int):
        company = cls()
        company.__get_environment_vars()
        url = f'{company.__url}/{id}'
        response = requests.get(url=url, headers=company.__headers)
        company_content = response.json()
        return cls(**company_content) if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    @classmethod
    def get_all(cls, page: int = 1):
        company = cls()
        company.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=company.__url, headers=company.__headers, params=params)
        companies = [cls(**company) for company in response.json()['data']]
        return companies if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    def post(self):
        if not self.company:
            raise ValueError("company is required to post a company.")
        company_json = self.model_dump(exclude_none=True)
        response = requests.post(url=self.__url, headers=self.__headers, json=company_json)
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response.reason}'

    def update(self):
        if not self.id:
            raise ValueError("id is required to update a company.")
        url = f'{self.__url}/{self.id}'
        company_json = self.model_dump(exclude_none=True)
        response = requests.put(url=url, headers=self.__headers, json=company_json)
        return f'{response.status_code} - {response.reason}'

    def delete(self):
        if not self.id:
            raise ValueError("id is required to delete a company.")
        url = f'{self.__url}/{self.id}'
        response = requests.delete(url=url, headers=self.__headers)
        return f'{response.status_code} - {response.reason}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_python_sdk.auth.login()')
        self.__url = os.getenv("API_URL") + self.__endpoint
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}
