import spacy

class Attention:
    def __init__(self,data,title):
        self.result = []
        self.titlemain=title
        self.data = data
    #Call fetchlink from crawler which will return list of list of text and embedded them
    def CalculateSimilarity(self):
        nlp = spacy.load("en_core_web_md")
        maintext=nlp(str(self.titlemain))
        for i in range(len(self.data)):
            linktext=nlp(str(self.data[i][1]))
            similarity = maintext.similarity(linktext)
            self.result.append((self.data[i][0],similarity))
        return self.result

if __name__ == "__main__":
    print("Attention")    
