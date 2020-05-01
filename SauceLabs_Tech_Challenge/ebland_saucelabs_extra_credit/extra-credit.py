from selenium import webdriver
import time

desired_cap = {
    'tags':['extra-credit', '1',],
    'platform': 'Windows 10',
    'browserName': 'chrome',
    'version': 'latest',
    'screenResolution':'1920x1080',
}

remote_url = "https://ebland:492fec24-6252-43cf-b537-d26f613814a6@ondemand.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_cap)


driver.get("https://www.amazon.com")
time.sleep(3)

Search = driver.find_element_by_id("twotabsearchtextbox")
Search.send_keys("i","P","h","o","n","e","X" )
Search.submit()
time.sleep = 2

driver.find_element_by_id("a-autoid-0").click()
time.sleep = 2

driver.find_element_by_id("s-result-sort-select_2").click()

products = driver.find_elements_by_css_selector("#search > div.sg-row > div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.s-right-column.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 > div > span:nth-child(4) > div.s-result-list.s-search-results.sg-row > div")

for product in products:
    title = product.find_element_by_css_selector("a.a-link-normal.a-text-normal")
    print(title.text)
    price = driver.find_element_by_css_selector(".a-price.a-text-price")
    print(price.text)
    print(title.get_attribute('href'))

driver.quit()
