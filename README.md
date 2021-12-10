# impfboosterbot
Bot that books booster vaccines at the Bayerische Impfzentrum

## Installation

1) Make sure the firefox browser is installed 
2) Install the firefox selenium driver and make sure it is on your path (e.g. by installing it to /usr/local/bin/). https://github.com/mozilla/geckodriver/releases
3) Make sure all packages from requirements.txt are available in your environment

## Usage
```bash
python main.py -h
usage: main.py [-h] username password person_number

positional arguments:
  username
  password
  person_number  Number of the person in the Impfzentrumsaccount. Starts with 1.

optional arguments:
  -h, --help     show this help message and exit

```