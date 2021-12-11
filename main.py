from random import random

from selenium import webdriver
import time
import logging

logging.basicConfig(format='%(asctime)s %(message)s')
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('person_number', help='Number of the person in the Impfzentrumsaccount. Starts with 1.')
    parser.add_argument('earliest_date', help="Earliest date to book an appointment. Needs to be of the form "
                                              "'YYYY-MM-DD'")
    args = parser.parse_args()

    logging.root.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('Impfterminbucher')
    browser = webdriver.Firefox()
    url = 'https://ciam.impfzentren.bayern/auth/realms/C19V-Citizen/protocol/openid-connect/auth?client_id=c19v-frontend&redirect_uri=https%3A%2F%2Fimpfzentren.bayern%2Fcitizen%2F&state=c5c6e344-a034-4bfc-8a16-82d223932875&response_mode=fragment&response_type=code&scope=openid&nonce=15b8b742-4fd4-487b-a5de-759ffdb44008&ui_locales=de'

    # open the website
    browser.get(url)

    # login
    username_xpath = '//*[@id="username"]'
    password_xpath = '//*[@id="password"]'
    login_button_xpath = '//*[@id="kc-login"]'
    browser.find_element('xpath', username_xpath).send_keys(args.username)
    browser.find_element('xpath', password_xpath).send_keys(args.password)
    browser.find_element('xpath', login_button_xpath).click()

    # wait for redirect
    time.sleep(2)

    # Person auswählen
    person_xpath = "//*[@id='main']/div/div/div[1]/div[" + str(args.person_number) + "]/section/a"
    person_button = browser.find_element(By.XPATH, person_xpath)
    browser.execute_script("arguments[0].click();",
                           person_button)  # use this executor to click as normal way doesnt work
    time.sleep(1)

    # Termin wählen
    termin_waehlen_xpath = '//*[@id="main"]/div/div[2]/div[2]/section[2]/section[1]/button'
    termin_wahl_button = browser.find_element('xpath', termin_waehlen_xpath)
    browser.execute_script("arguments[0].click();", termin_wahl_button)
    time.sleep(1)

    termin_verfuegbar = False
    while not termin_verfuegbar:
        try:
            # Wünsche wählen
            termin_xpath = '//*[@id="earliestDate"]'
            termin_element = browser.find_element(By.XPATH, termin_xpath)
            termin_element.click()
            termin_element.send_keys(args.earliest_date)

            # Nächsten Termin anzeigen
            naechster_termin_anzeigen_xpath = '//*[@id="main"]/div/div/form/div/button'
            temrin_anzeigen_button = browser.find_element('xpath', naechster_termin_anzeigen_xpath)
            browser.execute_script("arguments[0].click();", temrin_anzeigen_button)
            time.sleep(1)

            try:
                impftermin_moeglich_xpath = '//*[@id="main"]/div/div/form/div/div[3]/div/div[2]/dd[1]'
                termin_text = browser.find_element(By.XPATH, impftermin_moeglich_xpath).text
                logger.warning("Found Termin: " + termin_text)

                # if there is a Termin, click on Termin buchen
                termin_buchen_xpath = '//*[@id="main"]/div/div/form/nav/button[2]'
                termin_buchen_button = browser.find_element('xpath', termin_buchen_xpath)
                browser.execute_script("arguments[0].click();", termin_buchen_button)

                # If we got until here, assume we were successful
                logging.warning("Booked.")
                termin_verfuegbar = True
                break

            except:
                # no Termin found
                pass


        except Exception as e:
            logger.warning(str(e))

        # refresh page and try again
        browser.refresh()
        random_wait = random()
        time.sleep(1 + random_wait)
