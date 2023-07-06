from selenium import webdriver
from selenium.webdriver.chrome.options import Options




YOUTUBE_TRENDING = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
def get_driver():
 chrome_options=Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--disable-dev-shm-usage')
 chrome_options.add_argument('--headless')
 driver = webdriver.Chrome( options=chrome_options)
 return driver 


if __name__=="__main__":
 driver.get(YOUTUBE_TRENDING)
 print ('page title ', driver.title)