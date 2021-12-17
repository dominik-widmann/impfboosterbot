from random import random

from selenium import webdriver
import time
import logging
import platform
import os

from selenium.webdriver.firefox.service import Service

from src.utils import is_appointment_until, parse_user_required_date

logging.basicConfig(format='%(asctime)s %(message)s')
from selenium.webdriver.common.by import By

GECKO_MAC_x86_64 = './include/macOS/x86_64/geckodriver'
GECKO_MAC_arm64 = './include/macOS/arm64/geckodriver'
GECKO_LINUX = './include/linux64/geckodriver'
GECKO_WINDOWS = './include/win64/geckodriver.exe'
GECKO_COMPILED = 'geckodriver'

def get_gecko_driver_for_OS(iscompiled):
    """
    Returns the path to the gecko executable. If in doubt, assume win64.
    :return:
    """
    if iscompiled:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), GECKO_COMPILED)

    if platform.system() == 'Darwin':
        if platform.machine() == 'x86_64':
            return GECKO_MAC_x86_64
        else:
            return GECKO_MAC_arm64
    elif platform.system() == 'Linux':
        return GECKO_LINUX
    else:
        return GECKO_WINDOWS


def run_bot(username, password, person_number, earliest_date, latest_date, iscompiled):
    """

    :param username:
    :param password:
    :param person_number:
    :param earliest_date:
    :param latest_date:
    :param iscompiled:
    :return:
    """

    # Prepare logging
    logging.root.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('Impfterminbucher')

    # Check that input makes sense
    assert parse_user_required_date(earliest_date) <= parse_user_required_date(latest_date), \
        "'latest_date' must be equal to or after 'earliest_date'"

    # Start browser
    firefox_service = Service(get_gecko_driver_for_OS(iscompiled))
    browser = webdriver.Firefox(service=firefox_service)
    url = 'https://ciam.impfzentren.bayern/auth/realms/C19V-Citizen/protocol/openid-connect/auth?client_id=c19v-frontend&redirect_uri=https%3A%2F%2Fimpfzentren.bayern%2Fcitizen%2F&state=c5c6e344-a034-4bfc-8a16-82d223932875&response_mode=fragment&response_type=code&scope=openid&nonce=15b8b742-4fd4-487b-a5de-759ffdb44008&ui_locales=de'

    # open the website
    browser.get(url)

    # login
    username_xpath = '//*[@id="username"]'
    password_xpath = '//*[@id="password"]'
    login_button_xpath = '//*[@id="kc-login"]'
    browser.find_element('xpath', username_xpath).send_keys(username)
    browser.find_element('xpath', password_xpath).send_keys(password)
    browser.find_element('xpath', login_button_xpath).click()

    # wait for redirect
    time.sleep(2)

    # Choose person
    person_xpath = "//*[@id='main']/div/div/div[1]/div[" + str(person_number) + "]/section/a"
    person_button = browser.find_element(By.XPATH, person_xpath)
    browser.execute_script("arguments[0].click();",
                           person_button)  # use this executor to click as normal way doesnt work
    time.sleep(1)

    # Choose appointment
    termin_waehlen_xpath = '//*[@id="main"]/div/div[2]/div[2]/section[2]/section[1]/button'
    termin_wahl_button = browser.find_element('xpath', termin_waehlen_xpath)
    browser.execute_script("arguments[0].click();", termin_wahl_button)
    time.sleep(1)

    termin_verfuegbar = False
    while not termin_verfuegbar:
        try:
            # Select date filter
            termin_xpath = '//*[@id="earliestDate"]'
            termin_element = browser.find_element(By.XPATH, termin_xpath)
            termin_element.click()
            termin_element.send_keys(earliest_date)

            # Show next appointment
            naechster_termin_anzeigen_xpath = '//*[@id="main"]/div/div/form/div/button'
            temrin_anzeigen_button = browser.find_element('xpath', naechster_termin_anzeigen_xpath)
            browser.execute_script("arguments[0].click();", temrin_anzeigen_button)
            time.sleep(1)

            try:
                impftermin_moeglich_xpath = '//*[@id="main"]/div/div/form/div/div[3]/div/div[2]/dd[1]'
                termin_text = browser.find_element(By.XPATH, impftermin_moeglich_xpath).text
                logger.warning("Found Appointment: " + termin_text)

                # Check if Termin is convenient
                is_convenient = is_appointment_until(termin_text, latest_date)

                if is_convenient:
                    # book
                    termin_buchen_xpath = '//*[@id="main"]/div/div/form/nav/button[2]'
                    termin_buchen_button = browser.find_element('xpath', termin_buchen_xpath)
                    browser.execute_script("arguments[0].click();", termin_buchen_button)

                    # If we got until here, assume we were successful
                    logging.warning("Booked.")
                    termin_verfuegbar = True
                    break
                else:
                    logger.warning("Skipping this appointment, since it is after " + latest_date)

            except:
                # no Termin found
                pass


        except Exception as e:
            logger.warning(str(e))

        # refresh page and try again
        browser.refresh()
        random_wait = random()
        time.sleep(1 + random_wait)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Find and book a vaccination appointment at the Bavarian Vaccination Center.')
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('person_number', help='Number of the person in the Impfzentrumsaccount. Starts with 1.')
    parser.add_argument('earliest_date', help="Earliest date to book an appointment at. Needs to be of the form "
                                              "'YYYY-MM-DD'")
    parser.add_argument('latest_date', help="Latest date to book an appointment at. Needs to be of the form "
                                            "'YYYY-MM-DD'")
    args = parser.parse_args()

    run_bot(args.username, args.password, args.person_number, args.earliest_date, args.latest_date, iscompiled=False)
