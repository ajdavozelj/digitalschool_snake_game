#Python snake game z uporabo numpy
import random

#imamo razred "Polje", ki hrani 2D numpy matriko
#imamo razred "Kaca", ki hrani koordinate vseh polij na katerih kaca je in smer v katero kaca gleda

#najdi nacin, da neprestano spremljas kaj uporabnik pise v konzolo in ce vnese w, a, s, d, kaco obrni v pravo smer

#Razred Polje:

#Razred polje je glavni razred v katerem se igrica igra
#hrani razred kača, trenuten rezultat in koordinato polja, na katerem je hrana
#razred polje je tudi razred, ki spremlja kaj uporabnik piše v konzolo
#razred polje hrani igralno polje kot 2d numpy matriko; vse kkordinate so koordinate v tej matriki
#razred polje skrbi za izris igralnega polja

#Razred Kača
#razred kača hrani vse koordinate na kateriih kača je, smer v katero kača gleda, in boolean ali je kača živa ali mrtva
#razred ima funkcijo, ki prejme smer in ko se funkcija izvede, kačo obrne v to smer (če jo lahko)
#razred ima tudi funkcijo, ki preveri, ali je kača pojedla samo sebe in ali se je kača zabila v steno
#razded ima funkcijo, ki celo kačo premakne za 1 polje v smer katero gleda -> POMEMBNO NARIŠI SI
#razred ima funkcijo, ki kačo podaljša za 1 polje če ta poje hrano (to ali poje hrano se lahko spremlja iz razreda polje)

#osveževanje zaslova;
#vse igrice imajo neko frekvenco osveževanja zaslona (FPS)
#sami določite frekvenco osveževanja, in med vsako osvežitvijo izvedite komando "cls"
#|_> za to obstajajo tudi druge opcije, če najdeš katero, jo lahko tudi uporabiš
#frekvenco osveževanje določimo s time.sleep() -> za to ne pozabi import time

#Kako se take stvari lotit?
#1. začnemo z razredom polje
#   -> najprej napišemo konstruktor (__init__) in določimo katere vse podatke bo razred potreboval (kaca, 2d numpy matrika itd)
#   -> napišemo funkcijo za izris (__str__) -> ne pozabi da je treba izrisati tudi kačo in hrano
#   -> dopolnimo funkcijo za izris, da kombiniramo s time.sleep in cls
#   -> najdemo način, da lahko sproti spremljamo vse kar uporabnik vnese v konzolo (kaj se piše na tipkovnici)

#2. nadaljujemo z razredom kača
#   -> najprej naredimo konstruktor
#   -> naredimo funkcijo, ki preveri čeje kača živa ali mrtva
#   -> naredimo funkcijo, ki prejme smer in kačo obrne v to smer, če je možno
#   -> naredimo funkcijo, ki kačo premakne za 1 polje v smer gledanja
#   -> naredimo funkcijo ki kačo podaljša za 1 polje -> to je v laho v isti funckiji kot premik, samo da ne zradiramo repa


import keyboard
import time
import numpy as np
import os

from pygame.event import clear


class Polje:
    def __init__(self, kaca, mreza, koordinateHrana):
        self.kaca = kaca
        self.mreza = mreza
        self.koordinateHrana = koordinateHrana

    def __str__(self):
        izris = ""
        koordinateKace = self.kaca.koordinate
        for i in range(self.mreza.shape[0]):
            izris += "I"
            for j in range(self.mreza.shape[1]):
                trenutna_koordinata = [i,j]
                if trenutna_koordinata in koordinateKace:
                    izris += "o "
                elif trenutna_koordinata == self.koordinateHrana:
                    izris += "x "
                else:
                    izris += "  "
            izris += "I\n"

        return izris



    def game_loop(self):
        ziva = True
        while ziva:
            os.system("cls")
            print(self)
            print(kacica.smer)
            time.sleep(0.20)
            kacica.obracanje()
            kacica.seznamsmeri.append(kacica.smer)
            kacica.premaknikaco()
            kacica.hranjenje()

            ziva = kacica.preveristanje()
            print(kacica.koordinate)

class Kaca:
    def __init__(self, koordinate, smer, stanje):
        self.koordinate = koordinate
        self.smer = smer
        self.stanje = stanje
        self.seznamsmeri = ["right", "right", "right"]

    def obracanje(self):
        if keyboard.is_pressed("up") and self.smer != "down":
            self.smer = "up"

            print("up")
        elif keyboard.is_pressed("down") and self.smer != "up":
            self.smer = "down"

            print("down")
        elif keyboard.is_pressed("left") and self.smer != "left":
            self.smer = "right"

            print("right")
        elif keyboard.is_pressed("right") and self.smer != "right":
            self.smer = "left"

            print("left")

    def preveristanje(self):
        if self.koordinate[0][0] < 0 or self.koordinate[0][0] > 10 :
            self.stanje = False
            print("GAME OVER!")
            return False
        elif self.koordinate[0][1] < 0 or self.koordinate[0][1] > 25:
            self.stanje = False
            print("GAME OVER!")
            return False
        else:
            return True

    def premaknikaco(self):
        for i in range(len(self.koordinate)):
            if self.seznamsmeri[-(i+1)] == "up":
                self.koordinate[i][0] -= 1
            elif self.seznamsmeri[-(i+1)] == "down":
                self.koordinate[i][0] += 1
            elif self.seznamsmeri[-(i+1)] == "right":
                self.koordinate[i][1] -= 1
            elif self.seznamsmeri[-(i+1)] == "left":
                self.koordinate[i][1] += 1


    def hranjenje(self):
        if polje.koordinateHrana == self.koordinate[0]:
            if self.koordinate[-1][0] == self.koordinate[-2][0]:
                a = int(self.koordinate[-1][0])
                if self.seznamsmeri[-(len(self.koordinate))+1] == "left":
                    b = int(self.koordinate[-1][1] - 1)
                    self.koordinate.append([a,b])

                else:
                    b = int(self.koordinate[-1][1] + 1)
                    self.koordinate.append([a,b])
            else:
                a = int(self.koordinate[-1][1])
                if self.seznamsmeri[-(len(self.koordinate))+1] == "down":
                    b = int(self.koordinate[-1][0] - 1)
                    self.koordinate.append([b,a])
                else:
                    b = int(self.koordinate[-1][0] + 1)
                    self.koordinate.append([b,a])

            self.seznamsmeri.append(self.seznamsmeri[-1])
            while( polje.koordinateHrana in self.koordinate):
                hranay = random.randint(0, 24)
                hranax = random.randint(0, 9)
                polje.koordinateHrana = [hranax, hranay]




kacica = Kaca([[2,4], [2,5], [2,6]], "right", True)
mreza = np.zeros((10, 25))
koordinateHranee = [5,3]


polje = Polje(kacica, mreza, koordinateHranee)
#print(polje)

polje.game_loop()