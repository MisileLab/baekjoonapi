from requests import get
from bs4 import BeautifulSoup

class BaekjoonProb:
    def __init__(self, number):
        soup = BeautifulSoup(get(f"https://www.acmicpc.net/problem/{number}").text, "lxml")
        self.number = number
        self.question = soup.select_one("#problem_description > p").text
        self.input = soup.select_one("#problem_input > p").text
        self.output = soup.select_one("#problem_output > p").text
        self.sample_input = []
        for i in soup.select("#sample-input"):
            self.sample_input.append(i.text)
        self.sample_output = []
        for i in soup.select("#sample-output"):
            self.sample_output.append(i.text)
        self.correct_rate = soup.select_one("#problem-info > tbody > tr > td:nth-child(6)").text
        self.time_limit = soup.select_one("#problem-info > tbody > tr > td:nth-child(1)").text
        self.memory_limit = soup.select_one("#problem-info > tbody > tr > td:nth-child(2)").text

