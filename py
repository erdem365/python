class Not_hesap(object):
    def __init__(self):
        self.adet=int(input("Kaç adet not gireceksiniz: "))

        for i in range(self.adet):
            self.vize=int(input(f"{i+1}. öğrenvinin vize notunu giriniz: "))
            self.final=int(input(f"{i+1}. öğrenvinin final notunu giriniz: "))
            ortalama=self.vize*0.4+self.final*0.6
            print(f"{i+1}. öğrenvinin not ortalaması: ",ortalama)
            if ortalama>=90:
                print("AA aldınız")
            elif ortalama>=85:
                print("BA aldınız")
            elif ortalama>=80:
                print("BB aldınız")
            elif ortalama>=75:
                print("CB aldınız")
            elif ortalama>=70:
                print("CC aldınız")
            elif ortalama>=65:
                print("DC aldınız")     
            elif ortalama>=60:
                print("DD aldınız")
            elif ortalama>=50:
                print("FD aldınız")
            else:
                print("FF aldınız")


            while True:
               devam=input("Devam etmek istiyor musunuz? (E/H): ")
               if devam in ['E','e']:
                   break
               elif devam in ['H','h']:
                   print("Program sonlandırıldı.")
                   exit()
               else:
                   print("Geçersiz giriş, lütfen tekrar deneyin.")

                   while True:
                       try:
                           self.adet=int(input("Kaç adet not gireceksiniz: "))
                           if self.adet <= 0:
                               print("Lütfen pozitif bir sayı giriniz.")
                               continue
                           break
                       except ValueError:
                           print("Geçersiz giriş, lütfen bir sayı giriniz.")


                   while True:
                                try:
                                    self.vize=int(input(f"{i+1}. öğrenvinin vize notunu giriniz: "))
                                    if not (0 <= self.vize <= 100):
                                        print("Lütfen 0 ile 100 arasında bir not giriniz.")
                                        continue
                                    break
                                except ValueError:
                                    print("Geçersiz giriş, lütfen bir sayı giriniz.")

                   while True:
                                try:
                                    self.final=int(input(f"{i+1}. öğrenvinin final notunu giriniz: "))
                                    if not (0 <= self.final <= 100):
                                        print("Lütfen 0 ile 100 arasında bir not giriniz.")
                                        continue
                                    break
                                except ValueError:
                                    print("Geçersiz giriş, lütfen bir sayı giriniz.")
                   print("Tüm notlar girildi.")
