from maltools import API
import requests


class VirusTotal(API):
    URL_BASE = "https://www.virustotal.com/api/v3"
    actions = ['info', 'download']

    def info(self, h):
        return self._get('files', h).text

    def _get_sample(self, h):
        return self._get('files', h, 'download').content

    def _get(self, obj, id, act=None):
        ep = self.URL_BASE + f'/{obj}/{id}'
        if act:
            ep += f'/{act}'
        return requests.get(ep, headers={'x-apikey': self.key})
