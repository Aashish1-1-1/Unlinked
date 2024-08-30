import requests
import beautifulsoup

class crawler:
    def __init__(self,startlink:str):
        self.startlink=startlink
        self.crawstack=[]
        self.contexttext=[]
    def parsedom(self):
    #Fetch html of the link provided and parse to get links and tags befor that anchor tag
        html = requests.get(self.startlink)


    def extracttext():
    #Extract the text and link out of the div or paragraph in which anchor tag is in and save it as list in out crawstack

    def fetchlink(self):
    #Iterate through stack and fetch that html and contextual text with which a page can be judged save them in contexttext list as a list of list and at last return it 
    
