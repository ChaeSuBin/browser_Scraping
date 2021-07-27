from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.eum.go.kr/web/am/amMain.jsp')

sidoSelect = Select(driver.find_element_by_xpath('//*[@id="selSido"]'))
sidoSelect.select_by_visible_text('전라남도')
driver.implicitly_wait(1)
selsgg = Select(driver.find_element_by_xpath('//*[@id="selSgg"]'))
selsgg.select_by_visible_text('고흥군')
driver.implicitly_wait(1)
selumd = Select(driver.find_element_by_xpath('//*[@id="selUmd"]'))
selumd.select_by_visible_text('고흥읍')
driver.implicitly_wait(1)
selri = Select(driver.find_element_by_xpath('//*[@id="selRi"]'))
selri.select_by_visible_text('남계리')
driver.implicitly_wait(1)
idInput = driver.find_element_by_xpath('//*[@id="bobn"]')
idInput.send_keys('45')
driver.implicitly_wait(1)
bubninput = driver.find_element_by_xpath('//*[@id="bubn"]')
bubninput.send_keys('1')

resultButton = driver.find_element_by_xpath('//*[@id="frm"]/fieldset/div[3]/p/span/a')
resultButton.click()
