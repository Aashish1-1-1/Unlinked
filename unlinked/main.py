from crawler.crawler import Crawler
import transformer.transformer


if __name__=="__main__":
    test = Crawler("https://example.com/")
    test.printy()
    test.parsedom()
