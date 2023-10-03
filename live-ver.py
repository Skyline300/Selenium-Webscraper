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
from dotenv import load_dotenv
import time

options = Options();
options.add_experimental_option('excludeSwitches', ['enable-logging']);
commands = {};
url = "https://track.mydronefleets.com/playback/64fd5648e98213f5d3f5b415";
#s=Service('chromedriver_win32/chromedriver');
driver  = webdriver.Chrome(options=options);
driver.get(url);

load_dotenv()

email = os.environ['email']
password = os.environ['password']

print(email)
print(password)
# try:
#     WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//div/button')))
# finally:
#     res = driver.find_element(By.XPATH,'//div/h4')
#     print(res.text)
#    # driver.quit()


def _cock(*args):
    print("balls")
    return


def _login(*args):
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//div/button')))
    driver.find_element(By.XPATH,'//div/button').click()
    try: 
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'email_login')));
    finally: 
        driver.find_element(By.ID,'email_login').send_keys(email)
        driver.find_element(By.ID,'nextButton').click()
        WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,'password')));
        driver.find_element(By.ID,'password').send_keys(password)
        driver.find_element(By.ID,'nextButton').click()


def _get(*args):
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.MuiGrid-root.MuiGrid-item.MuiGrid-grid-xs-6'))); 
    except:
        print("class not found")
    finally:
        insert() 
       

def _getTime(*args):
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="map"]/div[2]/div[3]'))); 
    except:
        print("Item not found")
    finally:
        print("Item found")
        data = driver.find_element(By.XPATH,'//*[@id="map"]/div[2]/div[3]')
        stopTime = driver.find_element(By.XPATH,'//*[@id="map"]/div[2]/div[2]/div/div[2]/span[2]')
        txtData = data.text
        listData = txtData.split()
        print(listData[1])
        print(stopTime.text)
        print(listData[1] == stopTime.text)

def _exit(*args):
    driver.quit()
    return

def insert():
    dataDict = {
        "Time" : driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[2]').text,
        "LocalTime": driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[4]').text,
        "Latitude":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[6]').text,
        "Longitude":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[8]').text,
        "Altitude":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[10]').text,
        "speed":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[12]').text,
        "acceleration":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[14]').text,
        "heading":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[16]').text,
        "vdop":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[24]').text,
        "hdop":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[26]').text,
        "roll":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[28]').text,
        "pitch":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[30]').text,
        "yaw":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[32]').text,
        "battery":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[34]').text,
        "voltage":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[36]').text,
        "temperature":driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div[3]/div[38]').text
    }
    print(dataDict)
    if os.path.exists("result.csv"):
            temp_df = pd.DataFrame(dataDict, index=[0])
            temp_df.to_csv('result.csv', mode='a')
    else:
        temp_df = pd.DataFrame(dataDict);
        temp_df.to_csv('result.csv');
    time.sleep(0.5)
    data = driver.find_element(By.XPATH,'//*[@id="map"]/div[2]/div[3]')
    stopTime = driver.find_element(By.XPATH,'//*[@id="map"]/div[2]/div[2]/div/div[2]/span[2]').text
    txtData = data.text
    listData = txtData.split()
    if (listData[1] != stopTime):
        insert()
    return


commands["exit"] = _exit
commands["cock"] = _cock
commands["login"] = _login
commands["get"] = _get
commands["timing"] = _getTime


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