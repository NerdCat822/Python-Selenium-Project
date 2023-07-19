from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# option to be kept open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

KEYWORD = "buy domain"

browser = webdriver.Chrome(
    ChromeDriverManager().install(), options=chrome_options)

browser.get("https://google.com")

search_bar = browser.find_element_by_class_name("gLFyf")

search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements_by_class_name("g")

for index, search_result in enumerate(search_results):
    class_name = search_result.get_attribute("class")
    if "kno-kp mnr-c g-blk" not in class_name:
        search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")


browser.quit()
