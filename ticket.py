# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, threading
import win32ui

def msg(msg):
    threading.Thread(target=win32ui.MessageBox, args=(msg, time.ctime(),)).start()

url = 'http://pass.rzd.ru/timetable/public/ru?STRUCTURE_ID=735&layer_id=5354&refererVpId=1&refererPageId=704&refererLayerId=4065#dir=0|tfl=3|checkSeats=1|st0=%D0%9C%D0%9E%D0%A1%D0%9A%D0%92%D0%90|code0=2000000|dt0=30.04.2015|ti0=20-24|st1=%D0%9A%D0%90%D0%9D%D0%90%D0%A8|code1=2060630|dt1=18.03.2015'

driver = webdriver.Firefox()
driver.get(url)
while True:
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="trlist"]'))
        )
    except:
        print ('Cant load ticket page')
        driver.save_screenshot('screen.png')
        driver.refresh()
        continue
    trains = driver.find_elements_by_xpath('//*[@class="trlist"]/tbody/tr')

    train_name = []
    for train in trains:
        name = train.find_element_by_xpath('.//td[3]/div[@class="trlist__cell-pointdata__tr-num train-num-0"]').text
        train_time = train.find_element_by_xpath('.//td[4]/div/span[1]').text
        places = train.find_elements_by_xpath('.//td[9]/table/tbody/tr')
        for place in places:
            place = place.text.split(' ')
            if place[0] == 'Плацкартный':
                message = 'Купить срочно {0} билет на поезд {1} по цене {2} р. Время отправления {3}'.format(place[0], name, place[2], train_time)
                print(message, ' ', time.ctime())
                msg(message)
            if place[0] == 'Купе' and int(place[2]) <= 3000:
                message = 'Купить срочно {0} билет на поезд {1} по цене {2} р. Время отправления {3}'.format(place[0], name, place[2], train_time)
                print(message, ' ', time.ctime())
                msg(message)
        train_name.append(name)
        print('-'*60)

    print(train_name)

    #print 'На 30 апреля с 20-00 до 24-00 доступно {0} поезда: {1}'.format(len(trains), ', '.join(train_name))



    time.sleep(5)
    driver.refresh()
