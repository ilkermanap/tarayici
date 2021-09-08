import nmap


"""
bir ag tarayicisi yapacagimiz icin, agi ve icindeki istemcileri tanimlamamiz gerek. 
ag icindeki sistemler dict degiskeni ile, Istemci tipinde degiskenler olusturacagiz.
Istemci icin komut calistirma ya da baska seyler de tanimlayabiliriz.
"""

#TODO: farkli erisim yontemlerini de dusunmeli. kerberos gibi
class Istemci:
    def __init__(self, ipaddr, kullanici=None, parola=None, durum=False):
        self.adres = ipaddr
        self.durum = durum
        self.kullanici = kullanici
        self.parola = parola

    def rapor(self):
        print(f"{self.adres}\t{self.durum}")

        
class Tarama:
    def __init__(self):
        self.tarayici = nmap.PortScanner()

    def tara(self, adres, port):
        # adres ve port string olmali
        liste = self.tarayici.scan(adres, port)
        durum = [(x, self.tarayici[x]['status']['state']== "up") for x in self.tarayici.all_hosts()]
        return durum
        
class Ag:
    def __init__(self, adres):
        self.adres = adres
        self.sistemler = {}        

    def tara(self, port):
        t = Tarama()
        liste = t.tara(self.adres, port)
        for adres, durum in liste:
            if adres not in self.sistemler.keys():
                self.sistemler[adres] = Istemci(adres, durum=durum)

    def rapor(self):
        for k,v in self.sistemler.items():
            v.rapor()
