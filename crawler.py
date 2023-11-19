from bs4 import BeautifulSoup
import requests


class linkcrawler():

    def crawling(self, number):
        url = "https://www.tagesschau.de/"
        url_start = "https://www.tagesschau.de"
        r = requests.get(url)
        #print(number)

        linkliste =[]
        doc = BeautifulSoup(r.text, "html.parser")

        i=0
        for link in doc.find_all("a", class_="teaser__link"):
            link3=(link.get('href'))
            link3=url_start+link3
            i=i+1
            if i < 11:
               linkliste.append(link3)
        #rint(linkliste)
        #print(len(linkliste))

        return linkliste[number]

class Webcrawler():

    def crawl(self):

        url = "https://www.tagesschau.de/"
        r = requests.get(url)

        headlines=[]


        doc = BeautifulSoup(r.text, "html.parser")


        for teaser in doc.select(".teaser__head"):
            content = teaser.select_one(".teaser__headline").text
            headlines.append(content)

        #print(headlines)
        return headlines





