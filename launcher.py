import os
from main import run_bot

if __name__ == '__main__':
    # get user inputs
    print(
        "\nHello there!:)\nI'm the impfboosterbot. To be able to book a vaccination appointment for you, please help me out "
        "with the necessary account details of your account at the Bayrisches Impfzentrum. Don't worry, I won't use it "
        "for anything other than booking an appointment for you. I promise! Please make sure you type everything "
        "correctly. To submit your input, press ENTER.\n")

    # username
    username = input("Username (e.g. santa@claus.com): ")

    # password
    password = input("Password: ")

    # person_number
    person_number = input(
        "Please enter the number of the person in your account that you want to book an appointment for: ")

    # earliest_date
    earliest_date = input("Please enter the earliest date that works for you in the format 'YYYY-MM-DD': ")

    # latest_date
    latest_date = input("Please enter the latest date that works for you in the format 'YYYY-MM-DD': ")

    print("Thank you. Let me get you an appointment...")

    # start the bot
    run_bot(username, password, person_number, earliest_date, latest_date, iscompiled=True)
