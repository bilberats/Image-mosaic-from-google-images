from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time 


def dlimages(search,folder_size):
    driver = webdriver.Chrome("C:/fernand/python/pictures/chromedriver.exe")
    driver.get('https://www.google.ca/imghp?hl=en&tab=ri&authuser=0&ogbl')

    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    box.send_keys(search)
    box.send_keys(Keys.ENTER)
    
    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

    rootpath = os.getcwd()
    if not os.path.exists(os.path.join(rootpath,"download")):
        os.mkdir(os.path.join(rootpath,"download"))
    os.mkdir(os.path.join(rootpath,"download",search))


    for i in range(1, folder_size):
        try:
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('C:/fernand/python/pictures/download/'+search+'/'+str(i)+'.png')
        except:
            pass
    
    path = os.path.join(rootpath,"download",search)

    return path

    