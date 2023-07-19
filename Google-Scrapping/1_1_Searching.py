from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# option to be kept open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)

browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys("hello!")
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements_by_class_name("g")

print(search_results)
