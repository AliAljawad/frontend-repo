import yaml
import os

class Client:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            self.server_ip = config.get('ServerIPAddress', 'localhost')

    def connect(self):
        print(f"Connecting to server at {self.server_ip}")

if __name__ == "__main__":
    client = Client()
    client.connect()
