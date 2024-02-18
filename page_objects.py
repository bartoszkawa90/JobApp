from selenium import webdriver
from selenium .webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import sys
from copy import deepcopy
from bs4 import BeautifulSoup
import time
import requests
from source import *
from resources import *


class PageOperations:
    def __init__(self, page_obj):
        self.page_obj = page_obj
        self.driver = webdriver.Chrome()

        # setup  // open page and get rid of pop-ups
        self.driver.get(self.page_obj.page)
        self.click_xpath(self.page_obj.Xpath.accept_button)

    def click_xpath(self, xpath: str):
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def click_css(self, css: str):
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, css)
        element.click()

    def set_value_by_xpath(self, xpath: str, value: str):
        element = self.driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(value)


class Pracujpl(PageOperations):

    def search_front_page(self, position: str = None, category: str = None, localization: str = None, range_in_km: str = None):
        if self.page_obj.page == Pages.pracujpl:
            self.set_value_by_xpath(self.page_obj.Xpath.position_front, position)
            time.sleep(2)
            self.set_value_by_xpath(self.page_obj.Xpath.localization_front, localization)
            self.click_xpath(self.page_obj.Xpath.select_localization_front)
        else:
            raise Exception('Some wrong Page was requested')

        self.click_xpath(self.page_obj.Xpath.search_front)

    def search_standard_page(self, position: str = None, category: str = None, localization: str = None, range_in_km: str = None):
        if self.page_obj.page == Pages.pracujpl:
            self.clear_search_bar(self.page_obj.Css.clear_bar_list)
            self.set_value_by_xpath(self.page_obj.Xpath.position_standard, position)
            time.sleep(2)
            self.set_value_by_xpath(self.page_obj.Xpath.localization_standard, localization)
            self.click_xpath(self.page_obj.Xpath.category_standard)
        else:
            raise Exception('Some wrong Page was requested')

        self.click_xpath(self.page_obj.Xpath.search_standard)

    def clear_search_bar(self, clear_search_bar_list):
        for css in clear_search_bar_list:
            for _ in range(2):
                try:
                    time.sleep(1)
                    element = self.driver.find_element(By.CSS_SELECTOR, css)
                    time.sleep(1)
                    element.click()
                except:
                    print('--- Except but may work ---')

    def get_job_offer(self, link: str = ''):
        self.driver.get(link)
        url = self.driver.current_url
        reqs = requests.get(url)

        soup = BeautifulSoup(reqs.text, 'html.parser')
        title = ''.join(soup.title.string.strip().split()[:-5])
        job_offer = soup


    def get_offers_list(self) -> list[JobOffersPracuje]:
        url = self.driver.current_url
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        links = [link.get('href') for link in soup.find_all('a')]
        job_links = list(
            set([link for link in links if link is not None and "https://www.pracuj.pl/praca/" in link and 'wp' not in link]))

        # get data about offers
        list_of_job_offers = []
        for link in job_links:
            time.sleep(2)
            offer = self.get_job_offer(link)
            list_of_job_offers.append(offer)

        return list_of_job_offers

print('')
