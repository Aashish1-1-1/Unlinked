from crawler.crawler import Crawler
import transformer.transformer


if __name__=="__main__":
    test = Crawler("https://stackoverflow.com/questions/15765366/how-does-git-track-file-changes-internally")
    #test.printy()
    test.parsedom()
