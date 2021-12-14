# Bavarian Booster Bot
##### This is a bot that conveniently books COVID vaccination appointments at the Bayrisches Impfzentrum for you.  

[![unittests](https://github.com/dominik-widmann/impfboosterbot/actions/workflows/unittests.yaml/badge.svg)](https://github.com/dominik-widmann/impfboosterbot/actions/workflows/unittests.yaml)

The Bayrisches Impfzentrum provides only a very limited number of COVID vaccination slots that are often fully booked very quickly. To avoid having to sit in front of the website hiting refresh until you are lucky to get a slot, you can use this bot to do the work for you.

The bot logs into your account at the Bayrisches Impfzentrum and automatically books the next free slot in the time frame you specified. _If you cannot attend the appointment, it is possible to cancel and re-run the bot to book a different slot._ 

Please use this bot responsibly and at your own risk.

## Requirements
* **User account at [impfzentren.bayern](https://impfzentren.bayern):** You will need to supply the bot with your username and password.
* **Person registrated:** In your account, you need to click `+ Person hinzufügen` to register a person. Later, you will need to supply the bot with a number to reference which person you want to book the appointment for. Numbers start from 1 and increase by 1 from left to right as the persons are shown in your account.
* **Impfzentrum selected:** For this person, you need to have the vaccination site (Impfzentrum) selected at which you want to book an appointment (`Person auswählen > Impfzentrum auswählen`).
* **Firefox:** Get it [here](https://www.mozilla.org/en-US/firefox/new/).
* **Python:** Get it [here](https://www.python.org/downloads/).
* **Geckodriver:** Install the firefox selenium driver following these [instructions](https://github.com/mozilla/geckodriver/releases) and make sure it is on your path (e.g. by installing it to `/usr/local/bin/`).

## Installation
Open your favorite command line tool and run the following commands to download the impfboosterbot and install all packages from `requirements.txt`:

```bash
git clone https://github.com/dominik-widmann/impfboosterbot.git
cd impfboosterbot
python3 -m venv impfenv
source impfenv/bin/activate
pip install -r requirements.txt 
```

## Usage
If you followed the installation steps above, provide the bot with the following arguments:
* `username` and `password` from your user account at [impfzentren.bayern](https://impfzentren.bayern).
* `person_number` of the person in your user account you want to book the appointment for as one account can contain mutiple persons.
* the `earliest_date` and `latest_date` of the time frame you want to book an appointment in (in the format `YYYY-MM-DD`).

Then from within the impfboosterbot folder execute it as follows: 
```bash
python main.py username password person_number earliest_date latest_date
```
Once the bot has found an appointment, it will terminate and print the appointment on the command line. It should also be visible in your account now. _Note that the Bayrisches Impfzentrum often only provides appointments in the next 1-2 weeks._

## Example 
Let's assume that Santa Claus has two people registered in his account, Nikolaus and Rudolf. Rudolf is shown as the second person on Santa's account. He wants to have his Corona vaccination appointment between December 24th and December 26th 2021. Thus, Santa runs the bot as follows:
```bash
python main.by santa@claus.com secretpassword 2 2021-12-24 2021-12-26
```

## Thanks
Thank you for getting vaccinated. Feel free to [buy me a coffee](https://ko-fi.com/dominikwidmann) if you enjoyed using the bot :)
