from .models import TaskModel
import requests
import os


class Task(TaskModel):
    __url: str
    __endpoint: str
    __bearer_token: str

    def __init__(self, **data):
        super().__init__(**data)
        self.__endpoint = '/tasks'
        self.__get_environment_vars()

    @classmethod
    def get(cls, id: int):
        task = cls()
        task.__get_environment_vars()
        url = f'{task.__url}/{id}'
        response = requests.get(url=url, headers=task.__headers)
        task_content = response.json()
        return cls(**task_content) if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    @classmethod
    def get_all(cls, page: int = 1):
        task = cls()
        task.__get_environment_vars()
        params = {'page': page}
        response = requests.get(url=task.__url, headers=task.__headers, params=params)
        tasks = [cls(**task) for task in response.json()]
        return tasks if response.status_code == 200 else f'{response.status_code} - {response.reason}'

    def post(self):
        if not self.task_type_id:
            raise ValueError("task_type_id is required to post a task.")
        if not self.start:
            raise ValueError("start is required to post a task.")
        if not self.end:
            raise ValueError("end is required to post a task.")
        if not self.responsible_user_id:
            raise ValueError("responsible_user_id is required to post a task.")
        task_json = self.model_dump(exclude_none=True)
        response = requests.post(url=self.__url, headers=self.__headers, json=task_json)
        self.__dict__.update(**response.json())
        return f'{response.status_code} - {response.reason}'

    def update(self):
        if not self.id:
            raise ValueError("id is required to update a task.")
        url = f'{self.__url}/{self.id}'
        task_json = self.model_dump(exclude_none=True)
        response = requests.put(url=url, headers=self.__headers, json=task_json)
        return f'{response.status_code} - {response.reason}'

    def delete(self):
        if not self.id:
            raise ValueError("id is required to delete a task.")
        url = f'{self.__url}/{self.id}'
        response = requests.delete(url=url, headers=self.__headers)
        return f'{response.status_code} - {response.reason}'

    def __get_environment_vars(self):
        bearer_token = os.getenv("BEARER_TOKEN")
        if bearer_token is None:
            raise ValueError('login was not done, try use: wepipe_python_sdk.auth.login()')
        self.__url = os.getenv("API_URL") + self.__endpoint
        self.__headers = {'Authorization': f'Bearer {bearer_token}'}
