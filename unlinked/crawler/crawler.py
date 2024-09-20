import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self,startlink:str):
        self.startlink=startlink
        self.crawlstack=[]
        self.title=""
        self.contexttext=[]

    def printy(self):
        print(self.startlink)

    #Fetch html of the link provided and parse to get links and tags befor that anchor tag
    #Extract the text and link out of the div or paragraph in which anchor tag is in and save it as list in out crawstack
    def getdomandextract(self):
        html = requests.get(self.startlink)
        html.encoding = html.apparent_encoding
        soup = BeautifulSoup(html.content, "html.parser")
        self.title=soup.title.string
        postcontainers=soup.find_all('div',class_="post-layout")
        for postcontainer in postcontainers:
            links = postcontainer.find_all('a',rel=lambda x: x in ['nofollow','noreferrer'])
            for link in links:
                href=link.get('href')
                if href.startswith('http') or href.startswith('http'): 
                    self.crawlstack.append(link['href'])
        return self.title

    #Iterate through stack and fetch that html and contextual text with which a page can be judged save them in contexttext list as a list of list and at last return it
    def fetchlink(self):
        while self.crawlstack:
            link = self.crawlstack.pop()
            html = requests.get(link)
            html.encoding = html.apparent_encoding
            soup = BeautifulSoup(html.content, "html.parser")
            text = soup.title.string if soup.title and soup.title.string else "404 Notfound"
            self.contexttext.append((link,text.lower()))
        return self.contexttext

if __name__ == "__main__":
    print("This is Crawler")    
