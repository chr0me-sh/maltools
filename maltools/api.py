from pathlib import Path


class API:
    URL_BASE = None

    def __init__(self, key):
        self.key = key

    def download(self, hash, path):
        data = _get_sample(hash)
        with Path(path) as p:
            if p.is_dir():
                p = p.joinpath(hash)
            with open(p, 'wb') as fp:
                fp.write(data)
            return str(p.resolve())

    def info(self, hash):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError

    def daily(self):
        raise NotImplementedError

    def _get_sample(self, hash):
        raise NotImplementedError
