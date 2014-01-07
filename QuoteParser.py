from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

class QuoteParser(HTMLParser):

    def _init_(self):
        HTMLParser._init_(self)
        self.inQuote = False
        self.inDiv = False
        self.inP = False
        self.inAuthor = False
        self.lasttag = None
        self.foundQuote = False
        self.foundAuthor = False
        self.quote = []
        

    def getQuote(self, url):
        self.foundQuote = False
        self.foundAuthor = False
        self.quote = []
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html; charset=UTF-8':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return self.quote
            

    def handle_starttag(self, tag, attr):
        self.inAuthor = False
        if tag == 'dailyquote':
            self.inQuote = True
            self.lasttag = tag
        if tag == 'div':
            self.inDiv = True
            self.lasttag = tag
        if tag == 'p':
            self.inP = True
            self.lasttag = tag
        if tag == 'p':
            for (key, value) in attr:
                if key == 'class' and value == 'author':
                    self.inAuthor = True
                    self.lasttag = tag
            
    def handle_data(self, data):
        if self.lasttag == 'p' and self.inQuote and data.strip() and self.inDiv and self.inAuthor and not self.foundAuthor:
            #print("The author is: ",data)
            self.quote.append(data)
            self.foundAuthor = True
        elif self.lasttag == 'p' and self.inQuote and data.strip() and self.inDiv and self.inP and not self.foundQuote:
            #print("The quote is: ",data)
            self.quote.append(data)
            self.foundQuote = True
        

    def handle_endtag(self, tag):
        if tag == 'dailyquote':
            self.inQuote = False
            self.inDiv = False
            self.inP = False
            self.inAuthor = False

def spider(url):
    parser = QuoteParser(HTMLParser)
    quote = parser.getQuote(url)
    f = open('qotd.txt', 'w')
    i = 0
    for i in range (0,2):
        f.write(quote[i])
        f.write("\n")


        


    
            
                    
                    
