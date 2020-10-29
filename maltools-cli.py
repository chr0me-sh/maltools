from pathlib import Path
import maltools
import sys
import argparse
import json

CONF_FILE = 'maltools.conf'

apis = maltools.api_list.keys()
opts = ['download', 'info', 'status', 'daily']

parser = argparse.ArgumentParser(
    description='MalTools: A Malware Repo API Frontend'
)

parser.add_argument('-k', action='store', default=False, dest='key',
                    help='API key for the chosen provider')

parser.add_argument('-i', action='store', dest='hash', metavar='HASH',
                    help='Hash value of sample to query/download.')

parser.add_argument(action='store', metavar='repo', dest='api',
                    choices=maltools.api_list.keys(),
                    help='the repo provider to connect to. '
                         'Allowed values are: ' + ', '.join(apis) + '.')

parser.add_argument(action='store', metavar='action',
                    dest='action', help='API request to perform. '
                    'Allowed values are: ' + ', '.join(opts) + '.')


def gen_config(path):
    '''Creates the config file and returns an empty config'''
    c_obj = {a: '' for a in apis}
    with open(path, 'w+') as fp:
        json.dump(c_obj, fp, indent=4)
    return c_obj


def load_config(path):
    try:
        with open(path, 'r') as fp:
            c = json.load(fp)
    except (FileNotFoundError, json.JSONDecodeError):
        print('[x] Failed to load config file. Rebuilding...')
        c = gen_config(path)
    return c


def main(args):
    conf = load_config(CONF_FILE)

    if args.key:
        api_key = args.key
    elif conf[args.api]:
        api_key = conf[args.api]
    else:
        print(f'[x] No API key for {args.api} '
              'specified or present in config file.')
        return 1

    api = maltools.api_list[args.api](api_key)

    if args.action in ('download', 'info') and not args.hash:
        print(f'[x] {args.action.title()} requires a hash to be specified.')
        return 1

    try:
        if args.action == 'download':
            api.download(args.hash)
        elif args.action == 'info':
            print(api.info(args.hash))
        elif args.action == 'status':
            print(api.status())
        elif args.action == 'daily':
            print(api.daily())
    except NotImplementedError:
        print(f'[x] {args.api.title()} does not support action: {args.action}')
        print(f'[x] Available actions: {", ".join(api.actions)}')
        return 1


if __name__ == "__main__":
    args = parser.parse_args()
    ret = main(args)
    sys.exit(ret)