# impfboosterbot
Bot that books booster vaccines at the Bayerische Impfzentrum.

Please use with care and at your own risk!

## Requirements
* A user account at https://impfzentren.bayern/ 
* Firefox installed
* Geckodriver installed: install the firefox selenium driver and make sure it is on your path (e.g. by installing it to /usr/local/bin/). https://github.com/mozilla/geckodriver/releases

## Installation
Make sure all packages from requirements.txt are available in your environment. You can use venv for that like so:

```bash
python3 -m venv impfenv
source impfenv/bin/activate
```

## Usage
Make sure you followed all installation steps and activated your venv. Then from within your venv run main.py. The usage is as follows:

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
