# Impfboosterbot

[![Run unittests](https://github.com/dominik-widmann/impfboosterbot/actions/workflows/unittests.yaml/badge.svg)](https://github.com/dominik-widmann/impfboosterbot/actions/workflows/unittests.yaml)

Bot that books vaccination appointments at the Bayerisches Impfzentrum.

Please use with care and at your own risk!

## Requirements
* A user account at https://impfzentren.bayern/ with your username and password. You need to have the Impfzentrum selected at which you want to book an appointment.
* Firefox installed
* Geckodriver installed: install the firefox selenium driver and make sure it is on your path (e.g. by installing it to /usr/local/bin/). https://github.com/mozilla/geckodriver/releases

## Installation
Make sure all packages from requirements.txt are available in your environment. You can use venv for that:

```bash
python3 -m venv impfenv
source impfenv/bin/activate
pip install -r requirements.txt 
```

## Usage
Make sure you followed all installation steps and activated your venv. Then from within your venv run main.py. The usage is as follows:

```bash
 python main.py -h
usage: main.py [-h] username password person_number earliest_date latest_date

Find and book a vaccination appointment at the Bavarian Vaccination Center.

positional arguments:
  username
  password
  person_number  Number of the person in the Impfzentrumsaccount. Starts with 1.
  earliest_date  Earliest date to book an appointment at. Needs to be of the form 'YYYY-MM-DD'
  latest_date    Latest date to book an appointment at. Needs to be of the form 'YYYY-MM-DD'

optional arguments:
  -h, --help     show this help message and exit


```

Example run:
```bash
python main.py user@somemail.de dummypassword 1 '2022-01-04' '2022-01-12'
```
