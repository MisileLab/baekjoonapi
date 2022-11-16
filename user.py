import requests
from bs4 import BeautifulSoup

class AcmicpcUser:
    def __init__(self, user_name):
        soup = BeautifulSoup(requests.get('https://www.acmicpc.net/user/' + user_name).text, 'lxml')
        self.user_name = user_name
        self.status = soup.find('blockquote', {'class': 'no-mathjax'}).text
        self.bojrank = soup.find('#statics > tbody > tr:nth-child(1) > td').text
        self.correct_q = soup.find('#u-solved').text

