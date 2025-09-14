grenciler = {}  # öğrenci verilerini tutacak sözlük
ogrenci_id = 1   # öğrenci numarası

def ogretmen_girisi():
    global ogrenci_id
    sayi = int(input("Kaç öğrenci eklemek istiyorsunuz? "))
    for _ in range(sayi):
        isim = input("Öğrenci adı ve soyadı: ")
        vize = float(input("Vize notu: "))
        final = float(input("Final notu: "))
        ogrenciler[ogrenci_id] = {"isim": isim, "vize": vize, "final": final}
        ogrenci_id += 1
    print("Öğrenciler eklendi:")
    for id, bilgi in ogrenciler.items():
        print(f"{id}: {bilgi}")

def ogrenci_girisi():
    numara = int(input("Öğrenci numarası: "))
    isim = input("İsim: ")
    if numara in ogrenciler and ogrenciler[numara]["isim"].lower() == isim.lower():
        print("Giriş başarılı ✅")
        ogrenci = ogrenciler[numara]
        print(f"Adı Soyadı: {ogrenci['isim']}")
        print(f"Vize: {ogrenci['vize']}, Final: {ogrenci['final']}")
        ortalama = ogrenci['vize']*0.4 + ogrenci['final']*0.6
        print(f"Ortalama: {ortalama}")
        if ortalama < 50:
            print("Kaldı ❌")
        else:
            print("Geçti ✅")
    else:
        print("Hatalı giriş ❌")

def admin_girisi():
    while True:
        print("\n--- Admin Menüsü ---")
        print("1- Öğrenci Güncelle")
        print("2- Öğrenci Sil")
        print("3- Sınıf Ortalaması")
        print("4- Kalan Öğrenciler")
        print("0- Çıkış")
        secim = input("Seçim: ")
        
        if secim == "1":
            num = int(input("Güncellenecek öğrenci numarası: "))
            if num in ogrenciler:
                isim = input("Yeni isim: ")
                vize = float(input("Yeni vize notu: "))
                final = float(input("Yeni final notu: "))
                ogrenciler[num] = {"isim": isim, "vize": vize, "final": final}
                print("Öğrenci güncellendi ✅")
            else:
                print("Öğrenci bulunamadı ❌")
        elif secim == "2":
            num = int(input("Silinecek öğrenci numarası: "))
            if num in ogrenciler:
                del ogrenciler[num]
                print("Öğrenci silindi ✅")
            else:
                print("Öğrenci bulunamadı ❌")
        elif secim == "3":
            if ogrenciler:
                ort = sum([v["vize"]*0.4 + v["final"]*0.6 for v in ogrenciler.values()]) / len(ogrenciler)
                print(f"Sınıf Ortalaması: {ort}")
            else:
                print("Öğrenci yok ❌")
        elif secim == "4":
            print("Kalan Öğrenciler:")
            for id, v in ogrenciler.items():
                ortalama = v["vize"]*0.4 + v["final"]*0.6
                if ortalama < 50:
                    print(f"{id}: {v['isim']} - Ortalama: {ortalama}")
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim ❌")

# Ana Program Döngüsü
while True:
    print("\n--- Sınıf Not Yönetim Sistemi ---")
    print("1- Öğretmen Girişi")
    print("2- Öğrenci Girişi")
    print("3- Admin Girişi")
    print("0- Çıkış")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        ogretmen_girisi()
    elif secim == "2":
        ogrenci_girisi()
    elif secim == "3":
        admin_girisi()
    elif secim == "0":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim ❌")
