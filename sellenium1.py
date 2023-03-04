from selenium import webdriver
import time

#driver - nasza nazwa dla okna przeglądarki

driver = webdriver.Chrome()
driver.get('https://google.com')
print('Nazwa strony: ', driver.title)
time.sleep(5)
button1_accept = driver.find_element('id','L2AGLb')
print(button1_accept)
button1_accept.click()

field_search1 = driver.find_element('name','q')
print(field_search1)
field_search1.send_keys('czy jutro jest niedziela handlowa?')
push_button = driver.find_element('name','btnK')
#field_search1.send_keys(keys.ENTER) do spradzenia ? klika Enter
push_button.submit()

time.sleep(5)

driver.quit()
