from .models import ProductModel
import requests
import os


class Product(ProductModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = '/products'
        self.__get_environment_vars()

    @classmethod
    def get(cls, id: int):
        product = cls()
        product.__get_environment_vars()
        url = f'{product.__url}/{id}'
        response = requests.get(url=url, headers=product.__headers)
        product_content = response.json()
        return cls(**product_content) if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    @classmethod
    def get_all(cls, page: int = 1):
        product = cls()
        product.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=product.__url, headers=product.__headers, params=params)
        products = [cls(**product) for product in response.json()['data']]
        return products if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    def post(self):
        if not self.name:
            raise ValueError("name is required to post a product.")
        if not self.price:
            raise ValueError("price is required to post a product.")
        if not self.color:
            raise ValueError("color is required to post a product.")
        product_json = self.model_dump(exclude_none=True)
        response = requests.post(url=self.__url, headers=self.__headers, json=product_json)
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response.reason}'

    def update(self):
        if not self.id:
            raise ValueError("id is required to update a product.")
        url = f'{self.__url}/{self.id}'
        product_json = self.model_dump(exclude_none=True)
        response = requests.put(url=url, headers=self.__headers, json=product_json)
        return f'{response.status_code} - {response.reason}'

    def delete(self):
        if not self.id:
            raise ValueError("id is required to delete a product.")
        url = f'{self.__url}/{self.id}'
        response = requests.delete(url=url, headers=self.__headers)
        return f'{response.status_code} - {response.reason}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_python_sdk.auth.login()')
        self.__url = os.getenv("API_URL") + self.__endpoint
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}
