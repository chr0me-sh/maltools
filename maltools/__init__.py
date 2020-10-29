import pkgutil
import importlib
import maltools.repos
from maltools.api import API


for _, m, _ in pkgutil.iter_modules(
                maltools.repos.__path__,
                'maltools.repos.'):
    importlib.import_module(m)

api_list = {
    sub.__name__: sub
    for sub
    in API.__subclasses__()
}
