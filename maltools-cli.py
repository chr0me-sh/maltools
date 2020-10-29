import maltools
import argparse

apis = maltools.api_list.keys()
opts = ['download', 'info', 'status', 'daily']

parser = argparse.ArgumentParser(
    description='MalTools: A Malware Analysis Tool & Repo API Frontend'
)
parser.add_argument(action='store', metavar='REPO', dest='api',
                    help='the repo provider to connect to. '
                         'Allowed values are: ' + ', '.join(apis) + '.')
parser.add_argument(action='store', metavar='ACTION',
                    dest='ACTION', help='API request to perform. '
                    'Allowed values are: ' + ', '.join(opts) + '.')


def main():
    args = parser.parse_args()


if __name__ == "__main__":
    main()