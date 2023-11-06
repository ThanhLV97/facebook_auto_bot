import logging
import os
from time import sleep

import pandas as pd
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BASE_PATH = os.getcwd()


class PostBot():
    """TODO"""
    def __init__(self):
        self.driver = self._init_driver()

    def _init_driver(self):
        """TODO"""
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2} 
        chrome_options.add_experimental_option("prefs",prefs)

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def post_photo(self, photos: list):
        """TODO"""
        for photo in photos:
            photo_drag_element = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div[1]/div[2]')
            fake_drag = photo_drag_element.find_element(By.CSS_SELECTOR, "input[type='file']")
            fake_drag.send_keys(os.path.join(BASE_PATH, photo))
            sleep(5)

    def post_message(self, message: str):
        """TODO"""
        self.driver.switch_to.active_element.send_keys(message)
        sleep(1)

    def setup_account(self, email: str, password: str) -> None:
        """TODO"""
        self.driver.get('https://www.facebook.com')
        emailelement = self.driver.find_element(By.XPATH,'//*[@id="email"]')
        passelement = self.driver.find_element(By.XPATH,'//*[@id="pass"]')

        emailelement.send_keys(email)
        passelement.send_keys(password)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)

        sleep(1)

    def post_group(self, group: str, message: str, photos: list):
        """TODO"""
        self.driver.get(group)
        post_box = self.driver.find_element(By.XPATH, '//span[contains(text(), "Ảnh/video")]')
        post_box.click()
        sleep(1)

        # Post message and photo
        self.post_message(message=message)
        self.post_photo(photos)

        self.driver.switch_to.active_element.send_keys(Keys.COMMAND + Keys.ENTER)
        sleep(2)

    def posts(self, email: str, password: str, message: str, photos: list,  groups: list) -> None:
        """TODO"""
        self.setup_account(email=email, password=password)

        # Access group
        for group in groups:
            self.post_group(group=group, message=message, photos=photos)

        self.driver.close()


def main():
    # Set up Facebook login account name and password
    load_dotenv()
    email = os.getenv("EMAIL", None)
    password = os.getenv("PASSWORD", None)

    if not email or not password:
        logging.error('Please add .env with EMAIL and PASSWORD')

    # Set the test group    
    group_file = pd.read_csv('./data/groups.csv')
    groups = group_file['Groups'][0:1]

    photos = []
    for root, directories, files in os.walk('./data/images'):
        for filename in files:
            photo_path = os.path.join(root, filename)
            photos.append(photo_path)

    text_file = open("./data/status.txt", "r")
    message = text_file.read()
    text_file.close()
    
    # Login Facebook
    post_bot = PostBot()
    post_bot.posts(email, password, message, photos, groups)
    

if __name__ == '__main__':
    main()


