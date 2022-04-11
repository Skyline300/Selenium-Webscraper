from email import header
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os.path

url = 'enter url here';
s=Service('\web scraper\chromedriver_win32\chromedriver');
driver = webdriver.Chrome(service=s);
driver.get(url);


if os.path.exists('result.csv'):
    
    email  = driver.find_elements_by_xpath('//entertaghere[@class="enter class here (optional)"]');
    email_list = [];
    for p in range(len(email)):
        email_list.append(email[p].text);
    print(email_list);
    data_tuples = list(zip(email_list[0:]));
    temp_df = pd.DataFrame(data_tuples);
    temp_df.to_csv('result.csv', mode='a',index=False,header=False);
    print("action success");
    driver.close();

    
else:

    email  = driver.find_elements_by_xpath('//entertaghere[@class="enter class here (optional)"]');
    email_list = [];
    for p in range(len(email)):
        email_list.append(email[p].text);

    data_tuples = list(zip(email_list[0:]));
    temp_df = pd.DataFrame(data_tuples, columns=['Result']);
    temp_df.to_csv('result.csv',index=False);
    print("action success");
    driver.close();