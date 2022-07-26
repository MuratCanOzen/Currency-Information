from selenium import webdriver
from time import time, sleep
import pandas as pd
from openpyxl import Workbook
import xlsxwriter
import time

class Currency:
    def __init__(self, amount):
        self.url="https://anlikaltinfiyatlari.com/"
        self.browser=webdriver.Chrome(executable_path="C:\seleniumbrowserdriverSave\chromedriver.exe")
        self.amount=amount

    def currencyOns(self):
        #while True:
        self.browser.get(self.url)
        time.sleep(3)
        day=self.browser.find_element_by_xpath("//*[@id='content']/div/h3").text
        onsAltın=self.browser.find_element_by_xpath("//*[@id='spot']/ul/li[2]").text
        gramAltın=self.browser.find_element_by_xpath("//*[@id='spot']/ul/li[3]/a").text
        dolar=self.browser.find_element_by_xpath("//*[@id='spot']/ul/li[4]").text
        euro=self.browser.find_element_by_xpath("//*[@id='spot']/ul/li[5]").text
        euroDdolar=self.browser.find_element_by_xpath("//*[@id='spot']/ul/li[6]").text

        # time.sleep(10)
        print(f"{day} \n,{onsAltın} \n,{gramAltın} \n,{dolar} \n,{euro} \n,{euroDdolar} \n")

currency=Currency("Döviz Değişim")
currency.currencyOns()
