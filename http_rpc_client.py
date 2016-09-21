import requests


class Client:
    def __init__(self, host):
        self.host = host

    def get(self, resource, payload=None):
        try:
            return requests.get(self.host + "/" + resource, params=payload).json()
        except requests.exceptions.ConnectionError:
            raise Exception("server unreachable")

    def time(self):
        return self.get("time")['time']

    def ram(self):
        r = self.get("ram")
        return r['total'], r['used']

    def hdd(self):
        r = self.get("hdd")
        return r['total'], r['used']

    def add(self, a, b):
        try:
            a += 1
            b += 1
            r = self.get("add", {'a': a, 'b': b})
            return r['result']
        except TypeError:
            raise Exception("not an integer")

    def sub(self, a, b):
        try:
            a += 1
            b += 1
            r = self.get("sub", {'a': a, 'b': b})
            return r['result']
        except TypeError:
            raise Exception("not an integer")
