import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self,startlink:str):
        self.startlink=startlink
        self.crawstack=[]
        self.contexttext=[]

    def printy(self):
        print(self.startlink)

    #Fetch html of the link provided and parse to get links and tags befor that anchor tag
    def parsedom(self):
        html = requests.get(self.startlink)
        soup = BeautifulSoup(html.content, "html.parser")
        print(soup)

    #Extract the text and link out of the div or paragraph in which anchor tag is in and save it as list in out crawstack
    def extracttext(self):
        pass

    #Iterate through stack and fetch that html and contextual text with which a page can be judged save them in contexttext list as a list of list and at last return it
    def fetchlink(self):
        pass

if __name__ == "__main__":
    print("This is Crawler")    
