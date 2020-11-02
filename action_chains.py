from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def main():
    opts = Options()
    opts.add_argument("--disable-extensions")
    opts.add_argument("--headless")
    driver = Firefox(executable_path=r'My computers path')
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    driver.implicitly_wait(5) #same as time.sleep
    cookie = driver.find_element_by_id('bigCookie')
    cookie_count = driver.find_element_by_id('cookies')
    items = [driver.find_element_by_id(f'productPrice{str(i)}') for i in range(1,-1,-1)]
    actions = ActionChains(driver)
    actions.click(cookie)
    for i in range(5000):
        actions.perform()   
        count = int(cookie_count.text.split(' ')[0])
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()
if __name__ == '__main__':
    main()      