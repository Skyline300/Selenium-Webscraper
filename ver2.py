from email import header
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os.path



df = pd.read_csv('url.csv');

for i, row in df.iterrows():
    s=Service('\web scraper\chromedriver_win32\chromedriver');
    driver = webdriver.Chrome(service=s);
    url = row['URL'];
    print("getting URL: "+ str(url));
    driver.get(url);
    if os.path.exists('result.csv'):
        
        result  = driver.find_elements(By.CLASS_NAME,'something');
        result_list = [];
        
        for p in range(len(result)):
            result_list.append(result[p].text);
        print(result_list);
        data_tuples = list(zip(result_list[0:]));
        # print(data_tuples);
        temp_df = pd.DataFrame(data_tuples);
        temp_df.to_csv('result.csv', mode='a',index=False,header=False);
        print("action completed");
        driver.close();

    
    else:

        result  = driver.find_elements(By.CLASS_NAME,'something');
        result_list = [];

        for p in range(len(result)):
            result_list.append(result[p].text);

        data_tuples = list(zip(result_list[0:]));
        temp_df = pd.DataFrame(data_tuples, columns=['result']);
        temp_df.to_csv('result.csv',index=False);
        print("action completed");
        driver.close();


print("script completed");
