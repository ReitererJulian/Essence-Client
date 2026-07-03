import requests
import time
import json

class Sensor:
    host: str
    port: str
    name: str
    rest_base_url: str

    def __init__(self, host: str, port: str, name: str):
        self.host = host
        self.port = port
        self.name = name
        self.rest_base_url = f"http://{host}:{port}/"

    def _get(self, path: str):
        url = self.rest_base_url + path
        return requests.get(url)

    def _put(self, path: str, payload=None):
        url = self.rest_base_url + path
        return requests.put(url, json=payload)

    def _post(self, path: str, payload=None):
        url = self.rest_base_url + path
        return requests.post(url, json=payload)


    @staticmethod
    def _check_status(status_code: int) -> None:
        if status_code == 200:
            print("Status: OK | Code: 200")
        else:
            print(f"Status: Error | Code: {status_code}")

    def ping(self) -> None:
        response = self._get("status")
        self._check_status(response.status_code)

    def single_measurement(self) -> None:
        response = self._post("measurement.start.single.measurement", 10.0)
        self._check_status(response.status_code)

    def get_raw(self, data: str):
        request = self._get(data)
        return request.json()