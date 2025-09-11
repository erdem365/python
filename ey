class  BankaHesabi:
    def __init__(self,hesapsahibi,hesapNo,bakiye=0) :
        self.hesapsahibi=hesapsahibi
        self.hesapNO=hesapNo
        self.bakiye=bakiye
        self.işlemGeçmişi=[]

        def parayatir(self,miktar):
            if miktar>0:
                self.bakiye+=miktar
                self.işlemGeçmişi.append(f"{miktar} TL yatırıldı.")
                print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
            else:
                 print("Geçersiz miktar. Lütfen pozitif bir değer giriniz.") 
        def paracek(self,miktar):
            if 0<miktar<=self.bakiye:
                self.bakiye-=miktar
                self.işlemGeçmişi.append(f"{miktar} TL çekildi.")
                print(f"{miktar} TL çekildi. Yeni bakiye: {self.bakiye} TL")
            else:
                 print("Yetersiz bakiye veya geçersiz miktar.")
                 def bakiye_sorgula(self):
                     print(f"Hesap sahibi: {self.hesapsahibi}\nHesap No: {self.hesapNO}\nBakiye: {self.bakiye} TL")
                 def hesap_bilgileri(self):
                     print(f"Hesap sahibi: {self.hesapsahibi}\nHesap No: {self.hesapNO}")
                 def işlemleri_göster(self):
                    if self.işlemGeçmişi:
                        print("İşlem Geçmişi:")
                        for işlem in self.işlemGeçmişi:
                            print(işlem)
                    else:
                        print("Henüz işlem yapılmadı.")



hesap1=BankaHesabi("Erdem","123456789",1000)
hesap2=BankaHesabi("Ali","987654321",000)

print(hesap1.hesap_bilgileri())
print(hesap1.parayatir(600))
print(hesap1.paracek(100))
print(hesap1.paracek(3000))
print(hesap1.bakiyesorgula())
print(hesap1.işşlemleri_göster())

print(hesap2.hesap_bilgileri())
print(hesap2.parayatir(800))
print(hesap2.paracek(200))
print(hesap2.bakiyesorgula())
print(hesap2.işlemleri_göster())


