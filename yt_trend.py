import requests
from bs4 import BeautifulSoup


url = 'https://www.youtube.com/feed/trending'

def get_yt_trend(url=url):
    # BASED OFF:
    # https://gist.github.com/ggqq12356/71a7b658271867832733435e81640a07
    # BY ggqq12356
    Req = requests.get(url)

    Soup = BeautifulSoup(Req.text, 'html.parser')

    return [str(i.h3.a.get('title')) for i in Soup.select('.yt-lockup-content')] # VIDEO TITLES
	    