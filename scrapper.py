from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd 



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

def parse_video(video):
    title_element = video.find_element(By.ID, 'video-title')
    title_tag = title_element.text
    link = title_element.get_attribute('href')
    
    thumbnail_tags = video.find_elements(By.TAG_NAME, 'img')

    thumbnail_urls = [thumbnail.get_attribute('src') for thumbnail in thumbnail_tags]
    
    channel_div = video.find_element(By.CLASS_NAME , 'ytd-channel-name')
    channel_name= channel_div.text

    
    channel_description= video.find_element(By.ID , 'description-text')
    description = channel_description.text
    
    
    video_views = video.find_elements(By.CSS_SELECTOR, 'span.inline-metadata-item')
    view = video_views[0].text
    time = video_views[1].text
    return {
       'title': title_tag,
       'url'  : link,
       'thumbnail_tag':thumbnail_urls,
       'channel_name':channel_name,
       'description ' : description,
       'view' : view,
       'time':time


    }

if __name__ == "__main__":
    print('creating driver')

    driver = get_driver()
    print('Fetching the page ')

    
    print('trending Video')
    videos=get_video(driver)

    print(f'found {len(videos)} videos')
    
    print('Parsing The  Videos')
    # titile ,Views ,Uploaded, description, chanel ,url

    videos_data = [parse_video(video) for video in videos[:20] ]
    
    

    print('save data to csv')
    videos_df = pd.DataFrame(videos_data)
    print(videos_df)

    videos_df.to_csv('trending.csv', index=None)


    
