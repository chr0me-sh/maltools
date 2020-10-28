from maltools import API
from io import BytesIO
from zipfile import ZipFile
import json
import requests


class VirusShare(API):
    URL_BASE = "https://virusshare.com/apiv2/"

    def info(self, h):
        info = self._get('file', h).json()
        sources = self._get('source', info['sha256']).json()
        return json.dumps(info | sources, indent=4)

    def _get_sample(self, h):
        data = BytesIO(self._get('download', h).content)
        with ZipFile(data) as zp:
            fname = zp.namelist()[0]
            return zp.read(fname, pwd='infected')

    def _get(self, action, h):
        ep = self.URL_BASE + action
        params = {'apikey': self.key, 'hash': h}
        return requests.get(ep, params)