from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



YOUTUBE_TRENDING = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'

chrome_options=Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(YOUTUBE_TRENDING)
print ('page title ', driver.title)