from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import csv

#Using Selenium without launching the browser (headless).
chrome_options = Options()
chrome_options.add_argument("--headless")
driver=webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

#User input.
search = input("Please enter your City or Zip Code: ")

#Webdriver will navigate to weather.com, click the search bar, and enter the users input.
driver.get('https://weather.com/')
time.sleep(2)
driver.find_element_by_id('LocationSearch_input').click()
driver.find_element_by_id('LocationSearch_input').send_keys(search)
time.sleep(2)
driver.find_element_by_id('LocationSearch_input').send_keys(Keys.RETURN)
time.sleep(2)
print("")
print("")
city = driver.find_element_by_class_name('CurrentConditions--location--kyTeL').text
temp = driver.find_element_by_class_name('CurrentConditions--tempValue--3a50n').text
tod = driver.find_element_by_class_name('CurrentConditions--timestamp--23dfw').text

print(city)
print("")
print(tod)
print("")
print(temp)

#Saves the output to data.csv. 
with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["City: ", city, "Time of Day:  ", tod, "Temperature:   ", temp])
    
#Close Selenium webdriver.
driver.quit
