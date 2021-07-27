from selenium import webdriver
driver = webdriver.Chrome('./chromedriver')
# AIA 생명 치아보험 견적 페이지에서 보장 내역과 보험료 가져와서 출력을한다

def getAIAdata(birth):
    driver.get(
        'https://www.aia.co.kr/ko/our-products/medical-protection/non-par-denteal-health-plan.html#')
    seButton = driver.find_element_by_xpath(
        '//*[@id="calculator-container-form"]/div[1]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/label')
    seButton.click()
    birthInpyt = driver.find_element_by_xpath('//*[@id="aia644363719"]')
    birthInpyt.send_keys(birth)
    resultButton = driver.find_element_by_xpath('//*[@id="btn806817556"]')
    resultButton.click()

    driver.implicitly_wait(1)
    amountText = driver.find_element_by_xpath('//*[@id="premium-by-timespan-value"]')
    print(amountText.text)

    tableBody = driver.find_element_by_xpath(
        '//*[@id="collapse-large-724022276"]/div[1]/div/table').find_element_by_tag_name('tbody')
    driver.find_element_by_xpath(
        '//*[@id="the_fine_print"]/div[2]/div[1]/div[2]/div/a[2]').click()
    rows = tableBody.find_elements_by_tag_name("tr")
    contentsList = []

    for index, value in enumerate(rows):
        if index != 0:
            print(value.find_elements_by_tag_name('td')[0].text)
            contentsList.append(value.find_elements_by_tag_name('td')[
                                0].text)
    
getAIAdata('19980124')