import requests
from opcua import Client

class Sensor:
    host: str
    rest_port: str
    opcua_port: str
    name: str
    rest_base_url: str
    opcua_url: str

    def __init__(self, host: str, port: str, opcua_port:str, name: str):
        self.host = host
        self.rest_port = port
        self.name = name
        self.rest_base_url = f"http://{host}:{port}/"
        self.opcua_url = f"opc.tcp://{host}:{opcua_port}"

# REST

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
        response = self._post("measurement.start.single.measurement")
        self._check_status(response.status_code)

    def get_raw(self, link: str):
        request = requests.get(link)
        return request.json()

# OPCUA

    def write_opcua(self, node_path: str, value):
        client = Client(self.opcua_url)
        try:
            client.connect()
            node = client.get_node(f"ns=2;s={node_path}")
            node.set_value(value)
            print(f"[{self.name}] {node_path} -> {value}")
        finally:
            client.disconnect()

    def read_opcua(self, node_path: str) -> None:
        client = Client(self.opcua_url)
        try:
            client.connect()
            node = client.get_node(f"ns=2;s={node_path}")
            return node.get_value()
        finally:
            client.disconnect()

    def get_link(self) -> str:
        return f"{self.read_opcua('Acceleration.Data.RawData.DataLink')}"