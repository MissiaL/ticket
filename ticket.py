# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'http://pass.rzd.ru/timetable/public/ru?STRUCTURE_ID=735&layer_id=5354&refererVpId=1&refererPageId=704&refererLayerId=4065#dir=0|tfl=3|checkSeats=1|st0=%D0%9C%D0%9E%D0%A1%D0%9A%D0%92%D0%90|code0=2000000|dt0=30.04.2015|ti0=20-24|st1=%D0%9A%D0%90%D0%9D%D0%90%D0%A8|code1=2060630|dt1=18.03.2015'


#driver = webdriver.PhantomJS(executable_path="C:\\Python\\phantomjs-2.0.0-windows\\bin\\phantomjs.exe")
driver = webdriver.Firefox()
driver.get(url)
while True:
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="trlist"]'))
        )
    except:
        print 'Cant load ticket page'
        driver.refresh()
        continue
    trains = driver.find_elements_by_xpath('//*[@class="trlist"]/tbody/tr')

    train_name = []
    for train in trains:
        name = train.find_element_by_xpath('.//td[3]/div[@class="trlist__cell-pointdata__tr-num train-num-0"]').text
        places = train.find_elements_by_xpath('.//td[9]/table/tbody/tr')
        print places
        for place in places:
            #print place.get_attribute('innerHTML')
            print place.text
            train_name.append([name, place.text])
        print '-'*60

    r = []
    print train_name
    for i in train_name:
        for t in i:
            r.append(t.decode('cp1251'))
    print r
    #print 'На 30 апреля с 20-00 до 24-00 доступно {0} поезда: {1}'.format(len(trains), ', '.join(train_name))



    time.sleep(5)
    driver.refresh()
