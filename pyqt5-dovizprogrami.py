import sys

import requests

from bs4 import BeautifulSoup

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Pencere(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.baglanti()
        
        self.init_ui()
        
    def baglanti(self):
        
        try:
            url = "https://www.doviz.com/"
            
            response = requests.get(url)
            
            icerik = response.content
            
            self.soup = BeautifulSoup(icerik,"html.parser")
        
        except:
            sys.stderr.write("internet baglantisi saglanamadi")
            sys.stderr.flush()
            sys.exit()
    
        
    def init_ui(self):
        
        self.a = True
        
        self.altin = QPushButton("Altin")
        self.dolar = QPushButton("Dolar")
        self.euro = QPushButton("Euro")
        self.cevir = QPushButton("Çevir")
        self.yazialani = QLabel("")
        self.miktar = QLineEdit()
        self.yazialani2 = QLabel("")
        
        h_box = QHBoxLayout()
        h_box.addWidget(self.altin)
        h_box.addWidget(self.dolar)
        h_box.addWidget(self.euro)
        
        h1_box = QHBoxLayout()
        h1_box.addWidget(self.miktar)
        h1_box.addWidget(self.cevir)
        
        v_box = QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addWidget(self.yazialani)
        v_box.addLayout(h1_box)
        v_box.addWidget(self.yazialani2)
        v_box.addStretch()
        
        self.setLayout(v_box)
        
        self.setWindowTitle("Döviz Programı")
        
        self.altin.clicked.connect(self.kurcevir)
        
        self.dolar.clicked.connect(self.kurcevir)
        
        self.euro.clicked.connect(self.kurcevir)
        
        self.cevir.clicked.connect(self.kurcevir)
        
        self.show()
        
        
    def kurcevir(self):
        
        
        sender = self.sender()
        
        if sender.text() == "Altin":
            
            self.yazialani.setText("Gram Altın "+self.soup.find_all("span",{"class":"value","data-socket-key":"gram-altin"})[0].text+" TL")
            
            self.value = self.soup.find_all("span",{"class":"value","data-socket-key":"gram-altin"})[0].text
            
            if "." in self.value:
            
                self.value = self.value.replace(".","")

            if "," in self.value:

                self.value = self.value.replace(",",".")
            
            self.a = False
            
        elif sender.text() == "Dolar":
            
            self.yazialani.setText("1 Dolar "+self.soup.find_all("span",{"class":"value","data-socket-key":"USD"})[0].text+" TL")
            
            self.value = self.soup.find_all("span",{"class":"value","data-socket-key":"USD"})[0].text
            
            if "." in self.value:
            
                self.value = self.value.replace(".","")

            if "," in self.value:

                self.value = self.value.replace(",",".")
            
            self.a = False
        
        elif sender.text() == "Euro":
            
            self.yazialani.setText("1 Euro "+self.soup.find_all("span",{"class":"value","data-socket-key":"EUR"})[0].text+" TL")
            
            self.value = self.soup.find_all("span",{"class":"value","data-socket-key":"EUR"})[0].text
            
            if "." in self.value:
            
                self.value = self.value.replace(".","")

            if "," in self.value:

                self.value = self.value.replace(",",".")
            
            self.a = False
            
        else:
            
            try:
                
                if self.a:
                    
                    self.yazialani2.setText("bir seçenek giriniz")
                
                else:
                    
                    sonuc = float(self.miktar.text())*float(self.value)
                
                    self.yazialani2.setText(str(sonuc)+" TL")
                    
                
            
            except:
                
                self.yazialani2.setText("doğru girdi verilmedi")
    
app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
