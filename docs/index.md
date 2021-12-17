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
* **Github account:** Create it [here](https://github.com) to be able to download the bot executable.

## Installation
Download the executable for your platform. You need to create a user account at https://github.com
* Windows 11: TODO
* MacOS Big Sur (or higher): TODO
* Linux: TODO

## Usage
### MacOS
* Double-click the downloaded executable
* MacOS will probably refuse to launch the app at the first attempt since it are not able to verify it
* This can be solved as follows: go to "system preferences" -> "Security & Privacy" -> "General" and click on "Open Anyway"

### Linux
* Just run the downloaded executable. Since you are using linux, you might also be interested in having a look at the [code](https://github.com/dominik-widmann/impfboosterbot). ;)

### Windows 11
* Extract the downloaded folder
* Double-click impfboosterbot_win64.exe (In the extracted folder)  
* After double-clicking the exe, a dialog opens. Go to "more info" -> "Run anyway"

One the bot is started, it will say hi to you in the terminal and start prompting you for the required inputs to book a 
vaccination appointment. Type them correctly and submit them by pressing ENTER.
If you submitted a mistake, just restart the bot by closing the terminal and double-clicking the executable again.

Once the bot has found an appointment, it will terminate and print the appointment on the command line. It should also be visible in your account now. _Note that the Bayrisches Impfzentrum often only provides appointments in the next 1-2 weeks._

## Thanks
Thank you for getting vaccinated. Feel free to [buy me a coffee](https://ko-fi.com/dominikwidmann) if you enjoyed using the bot :)

## For software developers
The impfboosterbot is open source and is available in this github [repo](https://github.com/dominik-widmann/impfboosterbot). 
Should you experience problems with the dowloaded binary, the impfboosterbot can also be run like any other python program.
