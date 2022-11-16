import requests
from bs4 import BeautifulSoup

class BaekjoonUser:
    def __init__(self, user_name):
        soup = BeautifulSoup(requests.get('https://www.acmicpc.net/user/' + user_name).text, 'lxml')
        self.user_name = user_name
        self.status = soup.find('blockquote', {'class': 'no-mathjax'}).text
        self.rank = soup.select_one("#statics > tbody > tr:nth-child(1) > td").text
        self.correct_qs = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(1) > div.panel-body").text
        self.correct_q = soup.select_one("#u-solved").text
        self.unsolved_qs = soup.select_one("body > div.wrapper > div.container.content > div.row > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div.panel-body").text
        self.unsolved_q = soup.select_one("#u-failed").text
        self.submit_time = soup.select_one("#statics > tbody > tr:nth-child(4) > td").text

