"""
 # Project Name: Abdal Youtube Downloader
 # Programmer: Ebrahim Shafiei
 # Programmer WebSite: https://hackers.zone/
 # Programmer Email: Prof.Shafiei@Gmail.com
 # License : MIT
 # Current Date : 2023-02-09
 # Current Time : 8:14 AM
 # File Description: no description
"""
import requests
import re
from bs4 import BeautifulSoup
import validators


class LinkScrap:

    @staticmethod
    def url_validator(link):
        valid = validators.url(link)
        if valid:
            return True
        else:
            return False

    @staticmethod
    def video_unavailable_checker(link):
        try:
            if LinkScrap.url_validator(link):
                req = requests.get(link)
                if "Video unavailable" in req.text:
                    return True
                else:
                    return False
        except:
            pass

    def get_channel_links_by_id24(self):
        # txt = """
        #  "=1\026utuid=QSqpl0NJPpLSecnfFsJCzg","externalId":"UCQfqpl0NJPpLSecnfFsJCzg","doubleclickTrackingUsername":"","keywords":"","ownerUrls":["http://www.youtube.com/@amirtataloo"
        #  """
        my_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

        get_page_source = requests.get("https://www.youtube.com/@amirtataloo", headers=my_headers).text
        print(get_page_source)
        x = re.findall('"([a-zA-Z0-9\d]{24})"', get_page_source)
        print("https://www.youtube.com/channel/" + str(x))

    def link_scraper(self, channel_link):
        url = channel_link
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        urls = []
        for link in soup.find_all('a'):
            print(link.get('href'))
            urls.append(link.get('href'))
        return urls
