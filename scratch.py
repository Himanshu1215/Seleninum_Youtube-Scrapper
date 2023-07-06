import requests
from bs4 import BeautifulSoup
YOUTUBE_TRENDING = 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl'
# Does Not load java Scrpit
responce = requests.get(YOUTUBE_TRENDING)
print('status_code' ,responce.status_code)
print('output',responce.text[:100])
with open('trending.html','w') as f :
  f.write(responce.text)
doc = BeautifulSoup(responce.text,'html.parser')
print('pageTitle',doc.title)
# find all the video divs
video_div = doc.find_all('div',class_='style-scope ytd-video-renderer')
print(f'Found {len(video_div)} videos')