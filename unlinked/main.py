from crawler.crawler import Crawler
from attention.attention import Attention

if __name__=="__main__":
    test = Crawler("https://stackoverflow.com/questions/15765366/how-does-git-track-file-changes-internally","post-layout")
    #test.printy()
    title = test.getdomandextract()
    array = test.fetchlink()
    test1 = Attention(array,title)
    result = test1.CalculateSimilarity()
    for i in result:
        print(i)
