from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os.path


url = "https://track.mydronefleets.com/playback/64fd5648e98213f5d3f5b415";
s=Service('C:/Users/marcu/OneDrive/Documents/GitHub/Selenium-Webscraper/chromedriver_win32/chromedriver');
driver  = webdriver.Chrome(service=s);
driver.get(url);