import argparse
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

parser = argparse.ArgumentParser()

parser.add_argument("-u","--username", help="Username for Mozzart Bet", type=str, default="")
parser.add_argument("-p","--password", help="Password for Mozzart Bet", type=str, default="")

args = parser.parse_args()

username, password = args.username, args.password

driver = webdriver.Chrome()
driver.get("https://www.mozzartbet.com/sr#/mozz-app?mozzAppConversation=64e5a8ae85ad0bdcc91e36eb")

driver.find_element(By.XPATH, '//*[@id="gdpr-wrapper-new"]/div/div[3]/div[2]/button').click()
sleep(5)

driver.find_element(By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]').click()

try:
    driver.find_element(By.CSS_SELECTOR, '#pageWrapper > div > header > section.nav-top > article.nav-group.min-width-400.user-part.mozzart_sr > section > section > div > div.bottom-part > span').click()
except:


driver.find_element(By.XPATH, '//*[@id="pageWrapper"]/section/div/p[4]').click()

sleep(3)

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

driver.find_element(By.CSS_SELECTOR, '#pageWrapper > div > header > section.nav-top > article.nav-group.min-width-400.user-part.mozzart_sr > section > article > div:nth-child(2) > div > div > div > div.modal__body > form > button').click()
sleep(4)
driver.find_element(By.XPATH, '//*[@id="pageWrapper"]/section/div/div/div/div/div[1]/div/div/div/div[3]').click()

# breakpoint()
while True:
    message_cards = driver.find_elements(By.CLASS_NAME, "MozzAppMessageCard")
    for message_card in message_cards:
        free_spins_buttons = message_card.find_elements(By.CLASS_NAME, "MozzAppMessageCard__right--free")
        for i, fsb in enumerate(free_spins_buttons):
            try:
                free_spins_buttons[i].click()
                game = message_card.find_element(By.CLASS_NAME, "MozzAppFreeCard__header").text
            except:
                pass
            sleep(.5)
    sleep(10)
