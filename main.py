import sys
from PIL import Image
from PyQt5.QtGui import QPixmap
from qtpy import QtWidgets
from mainwindow import Ui_MainWindow
from crawler import Webcrawler
from crawler import linkcrawler
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import webbrowser
from functools import partial

#from urllib.parse import urljoin
#image = Image.open("images.jfif")

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testprojekt")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.graphicsView_2=image

        #### Top 10 Tagesschau Artikel anzeigen
        self.ui.crawler = Webcrawler()
        Liste = self.ui.crawler.crawl()
        for i in range(0, 10):
            self.item = self.ui.listWidget.item(i)
            self.item.setText(Liste[i])

        #### Link selektierte Artikel Tagesschau öffnen

        self.ui.crawler2 = linkcrawler()

        self.item1 = self.ui.crawler2.crawling(0)
        self.item2 = self.ui.crawler2.crawling(1)
        self.item3 = self.ui.crawler2.crawling(2)
        self.item4 = self.ui.crawler2.crawling(3)
        self.item5 = self.ui.crawler2.crawling(4)
        self.item6 = self.ui.crawler2.crawling(5)
        self.item7 = self.ui.crawler2.crawling(6)
        self.item8 = self.ui.crawler2.crawling(7)
        self.item9 = self.ui.crawler2.crawling(8)
        self.item10 = self.ui.crawler2.crawling(9)

        #print(self.linkliste)

        self.listlist = []

        self.ui.checkBox.toggled.connect(self.link01)
        self.ui.checkBox_2.toggled.connect(self.link02)
        self.ui.checkBox_3.toggled.connect(self.link03)
        self.ui.checkBox_4.toggled.connect(self.link04)
        self.ui.checkBox_5.toggled.connect(self.link05)
        self.ui.checkBox_6.toggled.connect(self.link06)
        self.ui.checkBox_7.toggled.connect(self.link07)
        self.ui.checkBox_8.toggled.connect(self.link08)
        self.ui.checkBox_9.toggled.connect(self.link09)
        self.ui.checkBox_10.toggled.connect(self.link010)


        self.ui.pushButton.clicked.connect(self.linksoeffnen)


        ##### online Produkt-Suche, siehe unten
        self.ui.pushButton_2.clicked.connect(self.produktfinden)

        ##### Website des günstigsten Produktes aufrufen, siehe unten
        self.ui.pushButton_3.clicked.connect(lambda: self.shoppen(self.produktfinden()))

        #print(self.listlist)

    def linksoeffnen(self, list3):

        list3=self.listlist
      #  print(list3)

        if len(list3)<2:
            url2 = list3[0]
            webbrowser.open(url2)
        if len(list3) > 1:
            url2 = list3[0]
            webbrowser.open(url2)
            for i in range(1, len(list3)):
                url3=list3[i]
                webbrowser.open_new_tab(url3)

        while True:
            list3.pop()
            if len(list3) == 0:
                break
      #  print(list3)


    def link01(self):
      #  print(self.listlist)
        self.link1(self.listlist, self.item1)

    def link02(self):
        self.link2(self.listlist, self.item2)

    def link03(self):
        self.link3(self.listlist, self.item3)

    def link04(self):
        self.link4(self.listlist, self.item4)

    def link05(self):
        self.link5(self.listlist, self.item6)

    def link06(self):
        self.link6(self.listlist, self.item6)

    def link07(self):
        self.link7(self.listlist, self.item7)

    def link08(self):
        self.link8(self.listlist, self.item8)

    def link09(self):
        self.link9(self.listlist, self.item9)

    def link010(self):
        self.link10(self.listlist, self.item10)

    def link1(self, item, list1):
        list1 = self.listlist
        item = self.item1
        list1.append(item)
        return list1

    def link2(self, item, list1):
        list1 = self.listlist
        item = self.item2
        list1.append(item)
        return list1

    def link3(self, item, list1):
        list1 = self.listlist
        item = self.item3
        list1.append(item)
        return list1

    def link4(self, item, list1):
        list1 = self.listlist
        item = self.item4
        list1.append(item)
        return list1

    def link5(self, item, list1):
        list1 = self.listlist
        item = self.item5
        list1.append(item)
        return list1

    def link6(self, item, list1):
        list1 = self.listlist
        item = self.item6
        list1.append(item)
        return list1

    def link7(self, item, list1):
        list1 = self.listlist
        item = self.item7
        list1.append(item)
        return list1

    def link8(self, item, list1):
        list1 = self.listlist
        item = self.item8
        list1.append(item)
        return list1

    def link9(self, item, list1):
        list1 = self.listlist
        item = self.item9
        list1.append(item)
        return list1

    def link10(self, item, list1):
        list1 = self.listlist
        item = self.item10
        list1.append(item)
        return list1

        #### günstigstes Produkt zur Suche finden (schließt nur die Ergeisse der ersten Seite der Suche mit ein)

    def produktfinden(self):
        eingabe = self.ui.textEdit.toPlainText()
        #print(eingabe)


        url = f"https://www.ebay.de/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw={eingabe}&_sacat=0&LH_TitleDesc=0&rt=nc&_odkw=Air+Up+10+Euro+Gutschein+f%C3%BCr+Neukunden+&_osacat=0&LH_BIN=1"
        #print(url)
        r2 = requests.get(url)
        produkte = []
        preise = []
        links=[]

        kat = BeautifulSoup(r2.text, "html.parser")

        #### Artikelnamen der ersten Seite herausfinden
        artikel = kat.select(".s-item__title")  # ("span").text
        for i in range(1, len(artikel) - 1):
            x = artikel[i].select("span")[0].text
            produkte.append(x)
            #print(produkte)

        ####Preise herausfinden
        euro = kat.select(".s-item__price")
        for j in range(1, len(euro) - 1):
            preise.append(euro[j].text)
        # print(preise)

            #### bei " von - bis" Preisen nur den niedrigsten Preis filtern und in Zahl umwandeln

        for k in range(0, len(preise)):
            preise[k] = preise[k].split(" ")[1]
            preise[k] = preise[k].replace(",", ".")
            if len(preise[k]) > 6:
                preise[k] = preise[k].replace(".", "", 1)
            preise[k]=float(preise[k])
            preise[k] = round(preise[k],1)

            #print(preise)

        ####kleinsten Preis und zugehörigen Artikel finden und anzeigen

        minimum = min(preise)
        #print(minimum)

        a = preise.index(minimum)
        #print(a)
        art_min = produkte[a]
        #print(art_min)
        mini = str(minimum)
        mini_komma=mini.replace(".", ",")


        if len(preise) != len(produkte):
            print("Fehler!!)")
            print(len(preise))
            print(len(produkte))

        self.ui.label_8.setText(art_min)
        self.ui.label_9.setText(mini_komma)

        #### Histogramm Preisverteilung siehe unten
        self.ui.tabWidget.currentChanged.connect(partial(self.histogramm, preise))


        #### Bild des günstigsten Produktes runterladen
        file = open('Produkt.jpeg', 'wb')

        img= kat.find("img", alt=art_min)

        bild = img.get('src')
        #print(img)
        #print(bild)

        response = requests.get(bild)
        file.write(response.content)
        file.close()

        #print("download successful")

        self.ui.label_10.setPixmap(QPixmap('Produkt.jpeg'))

        # Link zu Produkt öffnen
        aufstieg = img.parent
        aufstieg2 = aufstieg.parent
        #print(aufstieg2)
        adresse=aufstieg2.get("href")
        #print(adresse)

        ### neu gelöscht  ##   self.ui.pushButton_3.clicked.connect(lambda: self.shoppen(adresse))
        return adresse


    def shoppen(self, adr):
        webbrowser.open(adr)


    #### Histogramm Preisverteilung
    def histogramm(self, preise):

        plt.clf()
        plt.hist(preise, bins=30)
        plt.title("Preisverteilung der günstigsten Varianten")
        plt.xlabel("Preis")
        plt.ylabel("Häufigkeit")
        # plt.show()
        plt.savefig('Figure_1.png')

        self.ui.label_7.setPixmap(QPixmap('Figure_1.png'))


window = MainWindow()
window.show()


sys.exit(app.exec_())


