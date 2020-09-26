# -*- coding: utf-8 -*-

from numpy import random
import copy

class Raspored:
    
    def __init__(self, brojZaposlenika, brojSmjena, brojPoslova, brojLokacija , brojSmjenaPoUgovoru, listaBrojaObavljanjaPoslova):
        
        self._brojZaposlenika = brojZaposlenika
        
        self._brojSmjena = brojSmjena
        
        self._brojPoslova = brojPoslova
        
        self._brojLokacija = brojLokacija
        
        self._brojSmjenaPoUgovoru = brojSmjenaPoUgovoru
        
        self._listaSlova = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        self._listaBrojaObavljanjaPoslova = []
        
        self.setListaBrojaObavljanjaPoslova(listaBrojaObavljanjaPoslova)
        
        self._Zaposlenici = [] 
        self.setZaposlenici(self.getBrojZaposlenika())
        
        self._Smjene = [] 
        self.setSmjene(self.getBrojSmjena())
        
        self._Poslovi = [] 
        self.setPoslovi(self.getBrojPoslova())
        
        self._Lokacije = [] 
        self.setLokacije(self.getBrojLokacija())
        
        self._M = []
        self.setM(self.getBrojZaposlenika(), self.getBrojSmjena())
        
        self._preferenceZaposlenika = []
        self.setInicijalnePreference()
        
        self._kompetencijeZaposlenika = []
        self.setInicijalneKompetencije()
    
    def __eq__(self, drugi):
        
        if isinstance(drugi, self.__class__):
            
            M = self.getM()
            drugiM = drugi.getM()
            
            if self.getBrojZaposlenika() != drugi.getBrojZaposlenika() or self.getBrojSmjena() != drugi.getBrojSmjena():
                
                return False
            
            
            for i in range(self.getBrojZaposlenika()):
                for j in range(self.getBrojSmjena()):
                    
                    if M[i][j] != drugiM[i][j]:
                        
                        return False
            
            return True
                
        else:
            return False
    
    def postaviNaDrugi(self, drugi):
        
        self.postaviRaspored(drugi.getM())
        
      
    
    def __str__(self):
        
        
        ispis = ""
        ispis += "\t"
        
        
        for i in range(self.getBrojSmjena()):
            ispis += str(i+1) + "\t"
        
        ispis += "\n"
        
        
        for i in range(self.getBrojZaposlenika()):
            ispis += str(self.getZaposlenici()[i]) + "\t"
            for j in range(self.getBrojSmjena()):
                if self.getM()[i][j] == 0:
                    ispis += str(self.getM()[i][j])+ "\t"
                else:
                    ispis += str(self.getM()[i][j])+ ""
            
            ispis += "\n"
            
        
        ispis += "POSLOVI:" + str(self.getPoslovi()) +"\n"
        ispis += "BROJ SMJENA PO UGOVORU (SEDMIČNO):" + str(self.getBrojSmjenaPoUgovoru()) + "\n"
        
        ispis += "\t"
        
        
        for i in range(self.getBrojSmjena()):
            ispis += str(i+1) + "\t"
        
        ispis += "\n"
        
        
        for i in range(self.getBrojZaposlenika()):
            ispis += str(self.getZaposlenici()[i]) + "\t"
            for j in range(self.getBrojSmjena()):
                ispis += str(self.getPreferenceZaposlenika()[i][j])+ "\t"
                
            
            ispis += "\n"
        
        ispis += "KOMPETENCIJE ZAPOSLENIKA:" + "\n"
        
        ispis += "\t"
   
        for i in range(self.getBrojPoslova()):
            ispis += str(i+1) + "\t"
        
        ispis += "\n"
        
        for i in range(self.getBrojZaposlenika()):
            ispis += str(self.getZaposlenici()[i]) + "\t"
            for j in range(self.getBrojPoslova()):
                ispis += str(self.getKompetencijeZaposlenika()[i][j])+ "\t"
                
            
            ispis += "\n"
        
        
        c1 = 10
        c2 = 50
        c3 = 20
        F1, F2, F3, F4 = self.dajKvalitetRasporeda(c1, c2, c3)
        ispis += "KVALITET RASPOREDA: " + str(F1) + " " + str(F2) + " " + str(F3) + " " + str(F4) +"\n"
        
        return ispis
        
    def getBrojZaposlenika(self):
        return self._brojZaposlenika
        
    def getBrojSmjena(self):
        return self._brojSmjena
            
    def getBrojPoslova(self):
        return self._brojPoslova
        
    def getBrojLokacija(self):
        return self._brojLokacija
    
    def getListaBrojaObavljanjaPoslova(self):
        return self._listaBrojaObavljanjaPoslova
        
    def setBrojZaposlenika(self, brojZaposlenika):
        if type(brojZaposlenika) != int:
            raise TypeError("Broj zaposlenika mora biti cijeli broj!")
        if brojZaposlenika <= 0:
            raise ValueError("Broj zaposlenika mora biti pozitivan broj!")
        
        
        self._brojZaposlenika = brojZaposlenika
        
    def setBrojSmjena(self, brojSmjena):
        if type(brojSmjena) != int:
            raise TypeError("Broj smjena mora biti cijeli broj!")
        if brojSmjena <= 0:
            raise ValueError("Broj smjena mora biti pozitivan broj!")
                
        self._brojSmjena = brojSmjena
            
    def setBrojPoslova(self, brojPoslova):
        if type(brojPoslova) != int:
            raise TypeError("Broj poslova mora biti cijeli broj!")
        if brojPoslova <= 0:
            raise ValueError("Broj poslova mora biti pozitivan broj!")
                
        self._brojPoslova = brojPoslova
        
    def setBrojLokacija(self, brojLokacija):
        if type(brojLokacija) != int:
            raise TypeError("Broj lokacija mora biti cijeli broj!")
        if brojLokacija <= 0:
            raise ValueError("Broj lokacija mora biti pozitivan broj!")
                
        self._brojLokacija = brojLokacija
    
    def setBrojSmjenaPoUgovoru(self, brojSmjenaPoUgovoru):
        if type(brojSmjenaPoUgovoru) != int:
            raise TypeError("Broj lokacija mora biti cijeli broj!")
        if brojSmjenaPoUgovoru <= 0:
            raise ValueError("Broj lokacija mora biti pozitivan broj!")
                
        self._brojSmjenaPoUgovoru = brojSmjenaPoUgovoru
        
    def setListaBrojaObavljanjaPoslova(self, listaBrojaObavljanjaPoslova):
        self._listaBrojaObavljanjaPoslova = []
       
        if len(listaBrojaObavljanjaPoslova) != self.getBrojPoslova():
            raise ValueError("Duzina liste broja obavljanja poslova ne odgovara broju poslova!")
            
        for i in range(len(listaBrojaObavljanjaPoslova)):
            self._listaBrojaObavljanjaPoslova.append(listaBrojaObavljanjaPoslova[i]) 
    
    def getZaposlenici(self):
        return self._Zaposlenici
        
    def getSmjene(self):
        return self._Smjene
        
    def getPoslovi(self):
        return self._Poslovi
        
    def getPosao(self, nazivPosla):
        
        for i in range(len(self.getPoslovi())):
            if self.getPoslovi()[i][0] == nazivPosla:
                return self.getPoslovi()[i]
        
        return None
                
    def getLokacije(self):
        return self._Lokacije
    
    def getBrojSmjenaPoUgovoru(self):
        return self._brojSmjenaPoUgovoru
        
    def setZaposlenici(self, brojZaposlenika):
        self._Zaposlenici = []
        for i in range(brojZaposlenika):
            self._Zaposlenici.append(i+1)
        
    def setSmjene(self, brojSmjena):
        self._Smjene = []
        for i in range(brojSmjena):
            self._Smjene.append(i+1)
        
    def setPoslovi(self, brojPoslova):
        
        
        self._Poslovi = []
        
        
        for i in range(brojPoslova):
            self._Poslovi.append((self._listaSlova[i], self._listaBrojaObavljanjaPoslova[i], []))
                
    def setLokacije(self, brojLokacija):
        self._Lokacije = []
        for i in range(brojLokacija):
            self._Lokacije.append(i+1)
        
    def setM(self, brojZaposlenika, brojSmjena):
        self._M = []
        for i in range(brojZaposlenika):
            self._M.append([])
            for j in range(brojSmjena):
                self._M[i].append(0)
    
    def postaviRaspored(self, raspored):
        self._M = []
        for i in range(len(raspored)):
            self._M.append([])
            for j in range(len(raspored[0])):
                self._M[i].append(raspored[i][j])
    
    def getM(self):
        return self._M
    
    def setInicijalnePreference(self):
        
        self._preferenceZaposlenika = []
        
        for i in range(self.getBrojZaposlenika()):
            self._preferenceZaposlenika.append([])
            for j in range(self.getBrojSmjena()):
                self._preferenceZaposlenika[i].append(0)
                
    def setInicijalneKompetencije(self):
        
        self._kompetencijeZaposlenika = []
        
        for i in range(self.getBrojZaposlenika()):
            self._kompetencijeZaposlenika.append([])
            for j in range(self.getBrojPoslova()):
                self._kompetencijeZaposlenika[i].append(0)
        
    def getPreferenceZaposlenika(self):
        return self._preferenceZaposlenika
        
    def getKompetencijeZaposlenika(self):
        return self._kompetencijeZaposlenika
    
    def setPreferenceZaposlenika(self, zaposlenik, listaPreferenci):
        
        preferenceZaposlenika = self.getPreferenceZaposlenika()
        
        for j in range(self.getBrojSmjena()):
            if listaPreferenci[j] < 0 or listaPreferenci[j] > 10:
                raise ValueError("Preference trebaju biti cijeli brojevi u opsegu [0 (najvisa preferenca), 10 (najmanja preferenca)]")
            preferenceZaposlenika[zaposlenik-1][j] = listaPreferenci[j]
    
    def setKompetencijeZaposlenika(self, zaposlenik, listaKompetencija):
        
        kompetencijeZaposlenika = self.getKompetencijeZaposlenika()
        
        
        for j in range(self.getBrojPoslova()):
            if listaKompetencija[j] < 0 or listaKompetencija[j] > 10:
                raise ValueError("Preference trebaju biti cijeli brojevi u opsegu [0 (najvisa preferenca), 10 (najmanja preferenca)]")
            kompetencijeZaposlenika[zaposlenik-1][j] = listaKompetencija[j]

        
    def setDozvoljeneLokacijeZaPosao(self, posao, listaLokacija):
        
        posaoPostoji = False;
        indexPosla = 0
        for i in range(len(self.getPoslovi())):
            if self.getPoslovi()[i][0] == posao:
                posaoPostoji = True
                indexPosla = i
        
        if not posaoPostoji:
            raise ValueError("Specificirani posao ne postoji!")
        
        self.getPoslovi()[indexPosla] = (self.getPoslovi()[indexPosla][0], self.getPoslovi()[indexPosla][1],listaLokacija)
    
    def provjeriZadovoljenostUgovora(self, M):
        
        M = M
        
        
        for i in range(self.getBrojZaposlenika()):
            brojac = 0
            for j in range(self.getBrojSmjena()):
                
                if M[i][j] != 0:
                    brojac += 1
                    
            
            if brojac > 5:
                
                return False
        
        return True
    
    def provjeriOdmorZaposlenika(self, M):
        
        M = M
        
        for i in range(self.getBrojZaposlenika()):
            smjeneUKojimaRadi = []
            for j in range(self.getBrojSmjena()):
                
                if M[i][j] != 0:
                    smjeneUKojimaRadi.append(j)
            
            for j in range(len(smjeneUKojimaRadi) - 1):
                if smjeneUKojimaRadi[j+1] - smjeneUKojimaRadi[j] <= 2:
                    return False
        
        return True
    
    def provjeriDaLiJeIspravanParPosaoLokacija(self, M):
        
        M = M
        
        for i in range(self.getBrojZaposlenika()):
            for j in range(self.getBrojSmjena()):
                prihvatljiv = False
                if M[i][j] != 0:
                    posao = self.getPosao(M[i][j][0])
                    
                    lokacija = M[i][j][1]
                
                    
                    for k in range(len(posao[2])):
                        if lokacija == posao[2][k]:
                            prihvatljiv = True
                else:
                    prihvatljiv = True
                    
                
                if not prihvatljiv:
                    return False    
                        
        return True
    
    def provjeriPredvidjeniBrojObavljanjaPoslova(self, M):
        
         M = M
         
         
         listaPoslova = self.getPoslovi()
         
         pomocnaLista = []
         
         for i in range(len(listaPoslova)):
             pomocnaLista.append(0)
         
         for j in range(self.getBrojSmjena()):
             for i in range(self.getBrojZaposlenika()):
                 if M[i][j] != 0:
                     indeksPosla = 0
                     for k in range(len(listaPoslova)):
                         if M[i][j][0] == listaPoslova[k][0]:
                             
                            indeksPosla = k
                            pomocnaLista[indeksPosla] += 1
                     
             if (j+1)%3 == 0:
                if pomocnaLista != self.getListaBrojaObavljanjaPoslova():
                    return False
                pomocnaLista = []
         
                for i in range(len(listaPoslova)):
                    pomocnaLista.append(0)
                     
                 
                         
         return True
    
    def provjeriZauzetostLokacije(self, M):
        
        for j in range(self.getBrojSmjena()):
            listaBrojaca = []
            for k in range(len(self.getLokacije())):
                listaBrojaca.append(0)
            for i in range(self.getBrojZaposlenika()):
                if M[i][j] != 0:
                    listaBrojaca[M[i][j][1]-1] += 1
            
            
            for k in range(len(listaBrojaca)):
                if listaBrojaca[k] > 1:
                    return False
        
        return True
        
    
    def provjeriPrihvatljivostRasporeda(self, M):
        
        prihvatljiv = True
        
        prihvatljiv = self.provjeriZadovoljenostUgovora(M)
        
        
        if not prihvatljiv:
            return prihvatljiv
        
        prihvatljiv = self.provjeriOdmorZaposlenika(M)
        
        
        if not prihvatljiv:
            return prihvatljiv
        
        prihvatljiv = self.provjeriDaLiJeIspravanParPosaoLokacija(M)
        
        
        if not prihvatljiv:
            return prihvatljiv
        
        prihvatljiv = self.provjeriPredvidjeniBrojObavljanjaPoslova(M)
        
        if not prihvatljiv:
            return prihvatljiv
        
        prihvatljiv = self.provjeriZauzetostLokacije(M)
        
        if not prihvatljiv:
            return prihvatljiv        
        
        return prihvatljiv
    
    def kreirajSlucajniRaspored(self):
        
        poslovi = copy.copy(self.getPoslovi())
              
        M = copy.copy(self.getM())
        
        zaposlenici = copy.copy(self.getZaposlenici())  
        
        brojDana = int(self.getBrojSmjena() / 3)
        iteracija = 0        
            
        while True:
            
            
            for dan in range(brojDana):    
                
                random.shuffle(zaposlenici)
                
                while True:
                    indeksPosla = 0
                    indeksZaposlenika = 0
                    listaBrojaObavljanjaPoslova = copy.copy(self.getListaBrojaObavljanjaPoslova())
                    
                    #clear M
                
                    for i in range(self.getBrojZaposlenika()):
                        for j in range( 3*dan,3*dan + 3):
                            M[i][j] = 0
                        
                    while True:
                            if listaBrojaObavljanjaPoslova[indeksPosla] == 0:
                                if indeksPosla == len(listaBrojaObavljanjaPoslova) -1:
                                    break
                                else:
                                    indeksPosla += 1
                            
                            ## prvi dan (ostali identicni)
                            if dan == 0:
                                smjena = random.randint(3*dan, 3*dan + 3)
                            else:
                                prethodnaSmjena = None
                                for j in range(self.getBrojSmjena()):
                                    if M[zaposlenici[indeksZaposlenika] - 1][j] != 0:
                                        prethodnaSmjena = j
                                if prethodnaSmjena != None:
                                    smjena = prethodnaSmjena + 3
                                else:
                                    smjena = random.randint(3*dan, 3*dan + 3)
                            print(zaposlenici[indeksZaposlenika] - 1, smjena)
                            
                            if smjena > 17:
                                smjena = 17
                            
                            lokacija = random.randint(0, len(poslovi[indeksPosla][2]))
 
                            M[zaposlenici[indeksZaposlenika] - 1][smjena] = (poslovi[indeksPosla][0], poslovi[indeksPosla][2][lokacija])
                            
                            
                            listaBrojaObavljanjaPoslova[indeksPosla] -= 1
                            indeksZaposlenika += 1
                            
                            
                            
                    if True:
                        
                        break
                
            
            
            if self.provjeriZadovoljenostUgovora(M):
                break
                
        
        
        self._M = M
        return
        
    def setInicijalniRaspored(self):
        
        Mtemp = self.getM()
        M = []
        for i in range(len(Mtemp)):
            M.append([])
            for j in range(len(Mtemp[0])):
                M[i].append(Mtemp[i][j])
        
        
        M[0][4] = ('A', 2)
        M[0][8] = ('C', 3)
        M[0][11] = ('C', 6)
        M[0][14] = ('A', 1)
        
        M[1][0] = ('A', 1)
        M[1][5] = ('B', 4)
        M[1][8] = ('B', 4)
        M[1][13] = ('C', 7)
        M[1][16] = ('B', 5)
        
        M[2][0] = ('A', 2)
        M[2][3] = ('A', 2)
        M[2][9] = ('A', 1)
        M[2][12] = ('A', 2)
        M[2][17] = ('C', 6)
        
        M[3][1] = ('B', 2)
        M[3][4] = ('C', 7)
        M[3][7] = ('A', 2)
        M[3][10] = ('B', 2)
        M[3][15] = ('A', 1)
        
        M[4][2] = ('C', 3)
        M[4][6] = ('A', 1)
        M[4][9] = ('A', 2)
        M[4][13] = ('B', 5)
        M[4][16] = ('A', 1)
        
        
        
        if not self.provjeriPrihvatljivostRasporeda(M):
            
            return
        else:
            
            self._M = M
            
    def pomakZamjenaRadnika(self, trenutniRaspored):
        
        i = random.randint(0, self.getBrojZaposlenika()-1)
        j = random.randint(0, self.getBrojSmjena()-1)
        
        M = trenutniRaspored
        
        susjedniRaspored = []
        
        for k in range(len(M)):
            susjedniRaspored.append([])
            for l in range(len(M[0])):
                susjedniRaspored[k].append(M[k][l]) 
        
        while susjedniRaspored[i][j] == 0:
            i = random.randint(0, self.getBrojZaposlenika()-1)
            j = random.randint(0, self.getBrojSmjena()-1)
        
        jGornje = j
        jDonje = j
        
        while jGornje % 3 != 2:
            jGornje += 1
            
        while jDonje % 3 != 0:
            jDonje -= 1      
        
        
        listaNezaposlenih = []
        for k in range(self.getBrojZaposlenika()):
            daLiNeRadi = True
            for l in range(jDonje, jGornje + 1):
                if susjedniRaspored[k][l] != 0:
                    daLiNeRadi = False
            
            if daLiNeRadi:
                listaNezaposlenih.append(k)
       
        k = random.choice(listaNezaposlenih)     
        
        susjedniRaspored[k][j] = susjedniRaspored[i][j]
        susjedniRaspored[i][j] = 0
        
        return susjedniRaspored
        
    def pomakZamjenaLokacije(self, trenutniRaspored):
        
        i = random.randint(0, self.getBrojZaposlenika()-1)
        j = random.randint(0, self.getBrojSmjena()-1)
        
        M = trenutniRaspored
        
        susjedniRaspored = []
        
        for k in range(len(M)):
            susjedniRaspored.append([])
            for l in range(len(M[0])):
                susjedniRaspored[k].append(M[k][l]) 
        
        while susjedniRaspored[i][j] == 0:
            i = random.randint(0, self.getBrojZaposlenika()-1)
            j = random.randint(0, self.getBrojSmjena()-1)
        
        
        posao = self.getPosao(susjedniRaspored[i][j][0])
        
        novaLokacija = random.choice(posao[2]) #probati obje mogucnosti: kada moze ostati ista lokacija i kada se mora promjeniti u svakoj iteraciji
        
        susjedniRaspored[i][j] = (susjedniRaspored[i][j][0], novaLokacija)
        
        return susjedniRaspored
            
            
    def dajSusjedniRaspored(self):
        
        
        susjedniRaspored = self.pomakZamjenaRadnika(self.getM())
      
        susjedniRaspored = self.pomakZamjenaLokacije(susjedniRaspored)
       
        return susjedniRaspored
    
    def postaviPrihvatljivogSusjeda(self):
        
        M = self.dajSusjedniRaspored()
        
        while not self.provjeriPrihvatljivostRasporeda(M):
            M = self.dajSusjedniRaspored()
        
        self._M = M

    
    def dajPrihvatljivogSusjeda(self):
        
        M = self.dajSusjedniRaspored()
        
        while not self.provjeriPrihvatljivostRasporeda(M):
            M = self.dajSusjedniRaspored()
        
        return M
    
    def dajIndeksPosla(self, posao):
        
        poslovi = self.getPoslovi()
        
        
        for i in range(len(poslovi)):
            if poslovi[i][0] == posao:
                return i
                
        return None
    
    def uracunajStabilnostSmjene(self, c3):
        
        suma = 0
        prethodnaSmjena = None
        
        for i in range(self.getBrojZaposlenika()):
            prethodnaSmjena = None
            for j in range(self.getBrojSmjena()):
                if self.getM()[i][j] != 0:
                    if prethodnaSmjena != None:
                        if (j - prethodnaSmjena) % 3 != 0:
                            
                            suma += c3
                    prethodnaSmjena = j
        
        return suma
    
    def uracunajStabilnostLokacija(self, c3):
        
        suma = 0
        prethodnaLokacija = None
        
        for i in range(self.getBrojZaposlenika()):
            prethodnaLokacija = None
            for j in range(self.getBrojSmjena()):
                if self.getM()[i][j] != 0:
                    if prethodnaLokacija != None:
                        if self.getM()[i][j][1] != prethodnaLokacija:
                            
                            suma += c3
                    prethodnaLokacija = self.getM()[i][j][1]
        
        return suma
        
    def dajKvalitetRasporeda(self, c1, c2, c3):
        
        ## sume za razlicite grupe mekih ogranicenja
        F1 = 0
        F2 = 0
        F3 = 0
        F4 = 0
        
        preference = self.getPreferenceZaposlenika()
        kompetencije = self.getKompetencijeZaposlenika()
        M = self.getM()
        
        for i in range(self.getBrojZaposlenika()):
            for j in range(self.getBrojSmjena()):
                if M[i][j] != 0:
                    F1 += c1*preference[i][j]
                    indeksPosla = self.dajIndeksPosla(M[i][j][0])
                    
                    F2 += c2*kompetencije[i][indeksPosla]
                    
        F3 += self.uracunajStabilnostSmjene(c3)
        F4 += self.uracunajStabilnostLokacija(c3)
        
        return (F1, F2, F3, F4)
        
    def dajUkupniKvalitetRasporeda(self, c1, c2, c3):
        F1, F2, F3, F4 = self.dajKvalitetRasporeda(c1, c2, c3)
        
        return F1 + F2 + F3 + F4

def azurirajTabuListu(x, tabuLista, duzinaTabuliste):
    
    tabuLista.append(x)
            
    while len(tabuLista) > duzinaTabuliste:
            
        del tabuLista[0]   
                
    return tabuLista

def TabuPretrazivanjeRaspored(duzinaTabuListe, pocetniRaspored, maxBrojIteracija, maxBrojSusjeda, c1, c2, c3):
    
    ## incijalizacija
    x0 = copy.copy(pocetniRaspored)
    v0 = x0.dajUkupniKvalitetRasporeda(c1, c2, c3)
    xNajbolje = copy.copy(x0)
    vNajbolje = v0
    
    ## inicijalizacija taboo liste
    tabuLista = []
    
    
    brojacIteracija = 0
    
    ##trenutnoX
    x = copy.copy(x0)
    
    ## dodajemo pocetno rjesenje u taboo listu
    tabuLista = azurirajTabuListu(copy.copy(x), tabuLista, duzinaTabuListe)
    brojIteracijaBezPoboljsanjaNajboljegRasporeda = 0
    
    while True:
        
        brojacIteracija += 1
        if brojacIteracija > maxBrojIteracija:
            break
            
        brojSusjedaBrojac = 0
        listaPosjecenihSusjeda = []
        
        brojIteracijaZaSusjeda = 0
        
        while True:
            
            brojIteracijaZaSusjeda += 1
            brojSusjedaBrojac += 1
            if brojSusjedaBrojac > maxBrojSusjeda or brojIteracijaZaSusjeda > maxBrojSusjeda * 3:
                break
            
            x = copy.copy(x)
            
            ## eksperiment, ako se previse udaljavamo od optimuma
            if brojIteracijaBezPoboljsanjaNajboljegRasporeda > 50:
                x = copy.copy(xNajbolje)
                
            ## provjeravamo okolinu trenutnog x
            x.postaviRaspored(x.dajPrihvatljivogSusjeda())
            
            vecPosjecen = False
            for i in range(len(listaPosjecenihSusjeda)):
                if listaPosjecenihSusjeda[i] == x:
                    vecPosjecen = True
                    brojSusjedaBrojac -= 1
                    
            for i in range(len(tabuLista)):
                if tabuLista[i] == x:
                    vecPosjecen = True
                    brojSusjedaBrojac -= 1
                    
            if not vecPosjecen:
                listaPosjecenihSusjeda.append(x)
            
        
        ##print("LISTA POSJECENIH SUSJEDA")
        ##for l in range(len(listaPosjecenihSusjeda)):
            ##print(listaPosjecenihSusjeda[l])
        
        ## nije pronadjed nijedan validan susjed koji vec nije u taboo listi
        if len(listaPosjecenihSusjeda) == 0:
            print("EXHAUSTED NEIGHBORHOOD")
            return (xNajbolje, vNajbolje)
                
        ## odredjivanje naboljeg susjeda
        najboljiSusjed = copy.copy(listaPosjecenihSusjeda[0])
        vrijednostNajboljegSusjeda = najboljiSusjed.dajUkupniKvalitetRasporeda(c1, c2, c3)
        for i in range(len(listaPosjecenihSusjeda)):
            kvalitetItogRasporeda = listaPosjecenihSusjeda[i].dajUkupniKvalitetRasporeda(c1, c2, c3)
            if kvalitetItogRasporeda < vrijednostNajboljegSusjeda:
                vrijednostNajboljegSusjeda = kvalitetItogRasporeda
                najboljiSusjed = copy.copy(listaPosjecenihSusjeda[i])
                
                    
        ## odredjivanje naboljeg susjeda
        
        x = copy.copy(najboljiSusjed)
        
        ##po potrebi azuriramo najbolje rjesenje
        
        brojIteracijaBezPoboljsanjaNajboljegRasporeda += 1
        
        if x.dajUkupniKvalitetRasporeda(c1, c2, c3) < vNajbolje:
            vNajbolje = x.dajUkupniKvalitetRasporeda(c1, c2, c3)
            xNajbolje = copy.copy(x)
            brojIteracijaBezPoboljsanjaNajboljegRasporeda = 0
        ## dodajemo trenutno rjesenje u taboo listu
        tabuLista = azurirajTabuListu(copy.copy(x), tabuLista, duzinaTabuListe)
        
        ##print("ITERACIJA ")
        ##print(brojacIteracija)    
        
        ##print("TABU LISTA")
        ##for l in range(len(tabuLista)):
            ##print(tabuLista[l])
    
    return (xNajbolje, vNajbolje)
        

raspored1 = Raspored(5, 18, 3, 7, 5, [2, 1, 1])

raspored1.setDozvoljeneLokacijeZaPosao('A', [1, 2])

raspored1.setDozvoljeneLokacijeZaPosao('B', [2, 4, 5])

raspored1.setDozvoljeneLokacijeZaPosao('C', [3, 6, 7])

raspored1.setInicijalniRaspored()


raspored1.setPreferenceZaposlenika(1, [0, 5, 10, 10, 0, 6, 7, 10, 0, 0, 8, 0, 2, 1, 0, 5, 10, 6])
raspored1.setPreferenceZaposlenika(2, [9, 0, 9, 10, 7, 0, 4, 5, 0, 10, 2, 0, 9, 0, 3, 5, 0, 6])
raspored1.setPreferenceZaposlenika(3, [10, 5, 1, 0, 10, 4, 6, 0, 9, 0, 10, 8, 0, 9, 4, 10, 9, 0])
raspored1.setPreferenceZaposlenika(4, [0, 4, 8, 2, 0, 10, 5, 0, 3, 10, 0, 10, 9, 1, 10, 0, 10, 3])
raspored1.setPreferenceZaposlenika(5, [2, 4, 0, 0, 9, 7, 0, 1, 10, 0, 5, 0, 2, 0, 6, 0, 0, 10])


raspored1.setKompetencijeZaposlenika(1, [0, 10, 10])
raspored1.setKompetencijeZaposlenika(2, [10, 10, 0])
raspored1.setKompetencijeZaposlenika(3, [0, 10, 10])
raspored1.setKompetencijeZaposlenika(4, [10, 0, 10])
raspored1.setKompetencijeZaposlenika(5, [0, 10, 10])


print("POCETNI RASPORED")
print(raspored1)

(xNajbolje, vNajbolje) = TabuPretrazivanjeRaspored(35, raspored1, 100, 8, 10, 50, 20)

print(xNajbolje)

print("---------------------------------------------------------------------------------------------------")


raspored2 = Raspored(5, 18, 3, 7, 5, [2, 1, 1])

raspored2.setDozvoljeneLokacijeZaPosao('A', [1, 2])

raspored2.setDozvoljeneLokacijeZaPosao('B', [2, 4, 5])

raspored2.setDozvoljeneLokacijeZaPosao('C', [3, 6, 7])

raspored2.setPreferenceZaposlenika(1, [0, 5, 10, 10, 0, 6, 7, 10, 0, 0, 8, 0, 2, 1, 0, 5, 10, 6])
raspored2.setPreferenceZaposlenika(2, [9, 0, 9, 10, 7, 0, 4, 5, 0, 10, 2, 0, 9, 0, 3, 5, 0, 6])
raspored2.setPreferenceZaposlenika(3, [10, 5, 1, 0, 10, 4, 6, 0, 9, 0, 10, 8, 0, 9, 4, 10, 9, 0])
raspored2.setPreferenceZaposlenika(4, [0, 4, 8, 2, 0, 10, 5, 0, 3, 10, 0, 10, 9, 1, 10, 0, 10, 3])
raspored2.setPreferenceZaposlenika(5, [2, 4, 0, 0, 9, 7, 0, 1, 10, 0, 5, 0, 2, 0, 6, 0, 0, 10])


raspored2.setKompetencijeZaposlenika(1, [0, 10, 10])
raspored2.setKompetencijeZaposlenika(2, [10, 10, 0])
raspored2.setKompetencijeZaposlenika(3, [0, 10, 10])
raspored2.setKompetencijeZaposlenika(4, [10, 0, 10])
raspored2.setKompetencijeZaposlenika(5, [0, 10, 10])

print("---------------------------------------------------------------------------------------------------")

raspored2.kreirajSlucajniRaspored()

print(raspored2)





print("---------------------------------------------------------------------------------------------------")


        