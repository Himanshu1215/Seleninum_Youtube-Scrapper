from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By




YOUTUBE_TRENDING = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'


def get_driver():
 chrome_options=Options()
 chrome_options.add_argument('--no-sandbox')
 chrome_options.add_argument('--disable-dev-shm-usage')
 chrome_options.add_argument('--headless')
 driver = webdriver.Chrome( options=chrome_options)
 return driver 



def get_video(driver):
   driver.get(YOUTUBE_TRENDING)
   elements = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
   return elements




if __name__ == "__main__":
    print('creating driver')

    driver = get_driver()
    print('Fetching the page ')

    
    print('trending Video')
    videos=get_video(driver)

    print(f'found {len(videos)} videos')
    
    print('Parsing The first Video')
    # titile ,Views ,Uploaded, description, chanel ,url 

    video = videos[0]
    title= video.find_element(By.ID,'video-title').text
    print(title)