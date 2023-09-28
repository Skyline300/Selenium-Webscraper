from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options();
options.add_experimental_option('excludeSwitches', ['enable-logging']);
commands = {};
url = "https://track.mydronefleets.com/playback/64fd5648e98213f5d3f5b415";
#s=Service('chromedriver_win32/chromedriver');
driver  = webdriver.Chrome(options=options);
driver.get(url);


try:
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//div/button')))
finally:
    res = driver.find_element(By.XPATH,'//div/h4')
    print("the string:")
    print(res.text)
    
   # driver.quit()



def _cock(*args):
    print("balls")


commands["cock"] = _cock

def _login(*args):
    driver.find_element(By.XPATH,'//div/button').click()
    try: 
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'email_login')));
    finally: 
        print("there is a login input")

commands["login"] = _login

def _exit(*args):
    driver.quit()

commands["exit"] = _exit

def repl():
    while True:
        raw_input = input("> ").split()
        command = raw_input[0]
        args = raw_input[1:]
        try:
            commands[command](args)
        except KeyError:
            print(f"syntax error: {command}")
        # should probably handle exception from _set somehow too

if __name__ == "__main__":
    repl()