# MalTools
MalTools is a frontend for interacting with popular malware repository APIs.

Supported repositories:
* MalShare
* VirusTotal
* VirusShare

Currently the tool can download or get information on a specified hash, show the status of the API (e.g. limits) and retrieve daily sample listings.
Sadly, only MalShare supports all of the tools capabilities at the moment.

## Usage

`./maltools-cli.py [-h] [-k KEY] [-i HASH] <api> <action>`

When first running the program, a config file `maltools.conf` will be created in the CWD. API keys can alternativley be specified here.