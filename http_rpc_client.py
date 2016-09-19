import requests


class Client:
    def __init__(self, host):
        self.host = host

    def get(self, resource):
        try:
            return requests.get(self.host + "/" + resource).json()
        except requests.exceptions.ConnectionError:
            raise

    def time(self):
        return self.get("time")['time']

    def ram(self):
        r = self.get("ram")
        return r['total'], r['used']

    def hdd(self):
        r = self.get("hdd")
        return r['total'], r['used']