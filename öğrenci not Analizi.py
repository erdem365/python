import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ÖĞRENCİ NOT ANALİZ SİSTEMİ


# Örnek veri oluşturma
data = {
    "Ad": [
        "Ali", "Ayşe", "Mehmet", "Zeynep", "Can",
        "Ece", "Murat", "Elif", "Ahmet", "Sude"
    ],
    "Matematik": [80, 55, 90, 40, 75, 88, 60, 95, 45, 70],
    "Fizik": [70, 60, 85, 35, 80, 92, 58, 90, 50, 72],
    "İngilizce": [90, 58, 88, 45, 70, 95, 65, 98, 55, 75]
}

df = pd.DataFrame(data)


# VERİLERİ GÖSTER


def verileri_goster():
    print("\n--- ÖĞRENCİ VERİLERİ ---")
    print(df)


# ORTALAMA HESAPLAMA


def ortalama_hesapla():
    df["Ortalama"] = df[
        ["Matematik", "Fizik", "İngilizce"]
    ].mean(axis=1)

    print("\n--- ORTALAMALAR ---")
    print(df[["Ad", "Ortalama"]])


# HARF NOTU HESAPLAMA


def harf_notu_hesapla():

    if "Ortalama" not in df.columns:
        ortalama_hesapla()

    harfler = []

    for ortalama in df["Ortalama"]:

        if ortalama >= 85:
            harfler.append("AA")

        elif ortalama >= 70:
            harfler.append("BB")

        elif ortalama >= 50:
            harfler.append("CC")

        else:
            harfler.append("FF")

    df["Harf Notu"] = harfler

    print("\n--- HARF NOTLARI ---")
    print(df[["Ad", "Ortalama", "Harf Notu"]])


# SINIF İSTATİSTİKLERİ


def sinif_istatistikleri():

    if "Ortalama" not in df.columns:
        ortalama_hesapla()

    print("\n--- SINIF İSTATİSTİKLERİ ---")

    sinif_ortalamasi = df["Ortalama"].mean()

    en_basarili = df.loc[df["Ortalama"].idxmax()]

    en_dusuk = df.loc[df["Ortalama"].idxmin()]

    kalan_sayi = len(df[df["Ortalama"] < 50])

    print(f"Sınıf Ortalaması: {sinif_ortalamasi:.2f}")

    print(
        f"En Başarılı Öğrenci: "
        f"{en_basarili['Ad']} "
        f"({en_basarili['Ortalama']:.2f})"
    )

    print(
        f"En Düşük Ortalama: "
        f"{en_dusuk['Ad']} "
        f"({en_dusuk['Ortalama']:.2f})"
    )

    print(f"Kalan Öğrenci Sayısı: {kalan_sayi}")


# DERS ORTALAMALARI


def ders_ortalamalari():

    matematik_ort = df["Matematik"].mean()
    fizik_ort = df["Fizik"].mean()
    ingilizce_ort = df["İngilizce"].mean()

    print("\n--- DERS ORTALAMALARI ---")
    print(f"Matematik: {matematik_ort:.2f}")
    print(f"Fizik: {fizik_ort:.2f}")
    print(f"İngilizce: {ingilizce_ort:.2f}")


# GRAFİK OLUŞTURMA


def grafik_olustur():

    dersler = ["Matematik", "Fizik", "İngilizce"]

    ortalamalar = [
        df["Matematik"].mean(),
        df["Fizik"].mean(),
        df["İngilizce"].mean()
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(dersler, ortalamalar)

    plt.title("Ders Ortalamaları")

    plt.xlabel("Dersler")

    plt.ylabel("Ortalama")

    plt.show()


# BAŞARI DAĞILIM GRAFİĞİ


def basari_dagilimi():

    if "Ortalama" not in df.columns:
        ortalama_hesapla()

    plt.figure(figsize=(8, 5))

    plt.hist(df["Ortalama"], bins=5)

    plt.title("Başarı Dağılımı")

    plt.xlabel("Ortalama")

    plt.ylabel("Öğrenci Sayısı")

    plt.show()


# VERİ KONTROLÜ


def veri_kontrolu():

    print("\n--- VERİ KONTROLÜ ---")

    eksik_veri = df.isnull().sum()

    print("\nEksik Veriler:")
    print(eksik_veri)

    for ders in ["Matematik", "Fizik", "İngilizce"]:

        hatali = df[
            (df[ders] < 0) | (df[ders] > 100)
        ]

        if len(hatali) > 0:
            print(f"\nHatalı veri bulundu -> {ders}")
            print(hatali)

        else:
            print(f"{ders} verileri doğru.")


# EXCEL'E AKTARMA


    dosya_adi = "ogrenci_analiz.xlsx"

    df.to_excel(dosya_adi, index=False)

    print(f"\nVeriler Excel'e aktarıldı: {dosya_adi}")

===
# EN ZOR DERSİ BULMA


def en_zor_ders():

    ortalamalar = {
        "Matematik": df["Matematik"].mean(),
        "Fizik": df["Fizik"].mean(),
        "İngilizce": df["İngilizce"].mean()
    }

    en_dusuk = min(ortalamalar, key=ortalamalar.get)

    print("\n--- EN ZOR DERS ---")

    print(
        f"En zor ders: {en_dusuk} "
        f"({ortalamalar[en_dusuk]:.2f})"
    )


# MENÜ


def menu():

    while True:

        print("\n")
        print("===== ÖĞRENCİ NOT SİSTEMİ =====")
        print("1 - Verileri Göster")
        print("2 - Ortalama Hesapla")
        print("3 - Harf Notlarını Hesapla")
        print("4 - Sınıf İstatistikleri")
        print("5 - Ders Ortalamaları")
        print("6 - Grafik Oluştur")
        print("7 - Başarı Dağılımı")
        print("8 - Veri Kontrolü")
        print("9 - Excel'e Aktar")
        print("10 - En Zor Dersi Bul")
        print("0 - Çıkış")

        secim = input("\nSeçiminizi girin: ")

        if secim == "1":
            verileri_goster()

        elif secim == "2":
            ortalama_hesapla()

        elif secim == "3":
            harf_notu_hesapla()

        elif secim == "4":
            sinif_istatistikleri()

        elif secim == "5":
            ders_ortalamalari()

        elif secim == "6":
            grafik_olustur()

        elif secim == "7":
            basari_dagilimi()

        elif secim == "8":
            veri_kontrolu()

        elif secim == "9":
            excel_aktar()

        elif secim == "10":
            en_zor_ders()

        elif secim == "0":
            print("\nProgram kapatılıyor...")
            break

        else:
            print("\nHatalı seçim yaptınız!")


# PROGRAMI BAŞLAT


menu()
