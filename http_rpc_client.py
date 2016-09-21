import requests


class Client:
    def __init__(self, host):
        self.host = host

    def get(self, resource, payload=None):
        try:
            return requests.get(self.host + "/" + resource, params=payload).json()
        except:
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
        if isinstance(a, int) is False or isinstance(b, int) is False:
            raise Exception("not an integer")
        r = self.get("add", {'a': a, 'b': b})
        return r['result']

    def sub(self, a, b):
        if isinstance(a, int) is False or isinstance(b, int) is False:
            raise Exception("not an integer")
        r = self.get("sub", {'a': a, 'b': b})
        return r['result']

    def json_to_xml(self, json_str):
        r = self.get("json_to_xml", {'json_str': json_str})
        return r['result']
