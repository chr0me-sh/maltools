class API:
    URL_BASE = None

    def __init__(self, key):
        self.key = key

    def download(self, hash, path):
        raise NotImplementedError

    def info(self, hash):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError

    def daily(self):
        raise NotImplementedError