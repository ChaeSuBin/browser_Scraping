from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')
#크롬을 통해서 스크래핑 진행, 크롬 드라이버 로드
driver.get('https://oneline.kr/bbs/?boardCode=1&seq=704')
#open naver

print(driver.current_url)

title = driver.find_element_by_xpath('//*[@id="contentsArea"]/div[1]/h1')
# xpath 기반으로 요소를 찾아라 
print(title.text)
# //*[@id="cSub"]/div/h3
# //*[@id="harmonyContainer"]/section/p[1]

driver.quit()