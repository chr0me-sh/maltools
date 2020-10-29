from maltools import API
import json
import requests


class Malshare(API):
    URL_BASE = "https://malshare.com/api.php"

    def info(self, h):
        return self._get('details', hash=h).text

    def status(self):
        return self._get('getlimit').text

    def daily(self):
        return self._get('getlist').text

    def _get_sample(self, h):
        return self._get('getfile', hash=h).content

    def _get(self, action, h):
        query = {'api_key': self.key, 'action': action, 'hash': h}
        return requests.get(self.URL_BASE, params=query)
