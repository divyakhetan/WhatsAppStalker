import time
from datetime import datetime
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')

#list_names = input('Enter the contact names: ')
#list_names = list_names.split(" ")
list_names = list()
n = input('Enter number of contacts')
for i in range(int(n)):
    xyz = input('name: ')
    list_names.append(xyz)
    
print (list_names)

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

t = dt.datetime.now()

started = False
file = open("lastseendata.txt", "w")
file.write("")
file.close()
while True:
    delta = dt.datetime.now() -t
    if delta.seconds >= 2:
        
        for names in list_names:
            print(names)
            #user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(names))
            #user.click()
            search_field = driver.find_element_by_class_name('jN-F5') 
            search_field.send_keys(names + Keys.ENTER)
            try:
                time.sleep(5)
                last_seen = driver.find_element_by_class_name('O90ur').text
                
                if len(last_seen) > 0:
                    print (names + " is online at " +  str(datetime.now()) + "\n")
                    file = open("lastseendata.txt", "a")
                    
                    if(last_seen == "online"):
                        if(started == False):
                            file.write(names + " came online at " +  str(datetime.now()) + "\n")
                            started = True
                        
                    else:
                        file.write(names + " : " + last_seen + "\n")
               
                    file.close()
            except Exception as e:
                if(started == True):
                    print(names + " went offline at " +  str(datetime.now()) + "\n")
                    file = open("lastseendata.txt", "a")
                    file.write(names + " went offline at " +  str(datetime.now()) + "\n")
                    file.close()
                    started = False
                pass
            t = dt.datetime.now()



