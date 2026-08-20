## 실행방법: python practice1.py

## 솔루션 결과
"""
!!STARTED!!

--- XPath Axes 문제 ---
xpath 문제 1 완료(html): <li class="item">Item B</li>
xpath 문제 2 완료(text): Item A
xpath 문제 3 완료(text): Item C

!!FINISHED!!
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.add_argument("--guest")
options.add_argument("--disable-features=PasswordLeakDetection,AutofillServerCommunication,OptInRelaunch")

def xpath_axes_problems(driver, wait):
    print("\n--- XPath Axes 문제 ---")
    # 1. id='xpath-head' 인 h3 >> 다음에 오는 형제들 중, 첫번재 형제(ul) >> 의 자식 중, 두번재 자식(li) 선택
    locator_1 = "//h3[@id='xpath-head']/following-sibling::ul[1]/li[2]"
    second_li = wait.until(EC.presence_of_element_located((By.XPATH, locator_1)))
    print("xpath 문제 1 완료(html):", second_li.get_attribute("outerHTML"))

    # 2. text()='Item B'인  li >> 바로 이전 형제 li
    locator_xpath_2 = "//li[text()='Item B']/preceding-sibling::li"
    prev_li = wait.until(
        EC.presence_of_element_located((By.XPATH, locator_xpath_2))
    )
    print("xpath 문제 2 완료(text):", prev_li.text)

    # 3. text()='Item B'인  li >> 바로 이후 형제 li
    locator_xpath_3 = "//li[text()='Item B']/following-sibling::li"
    next_li = wait.until(
        EC.presence_of_element_located((By.XPATH, locator_xpath_3))
    )
    print("xpath 문제 3 완료(text):", next_li.text)

print("!!STARTED!!")
with webdriver.Chrome(options=options) as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://jinny-dev-anything.github.io/locator_ex_webpage")

    xpath_axes_problems(driver, wait)

    print("\n!!FINISHED!!")
    driver.quit()
