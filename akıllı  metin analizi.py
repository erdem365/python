import re
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# AKILLI METİN ANALİZ SİSTEMİ
# ============================================

# ============================================
# TXT DOSYASINI OKUMA
# ============================================

dosya_adi = "metin.txt"

try:

    with open(dosya_adi, "r", encoding="utf-8") as file:
        metin = file.read()

except FileNotFoundError:

    print(f"{dosya_adi} bulunamadı!")
    exit()

# ============================================
# METNİ TEMİZLEME
# ============================================

kucuk_metin = metin.lower()

temiz_metin = re.sub(r"[^\w\s]", "", kucuk_metin)

kelimeler = temiz_metin.split()

# ============================================
# STOP WORDS
# ============================================

stop_words = [
    "ve",
    "ile",
    "bir",
    "bu",
    "şu",
    "de",
    "da",
    "için",
    "ama",
    "gibi",
    "çok",
    "daha",
    "en",
    "mi",
    "mı"
]

filtrelenmis_kelimeler = []

for kelime in kelimeler:

    if kelime not in stop_words:
        filtrelenmis_kelimeler.append(kelime)

# ============================================
# TEMEL İSTATİSTİKLER
# ============================================

toplam_kelime = len(filtrelenmis_kelimeler)

cumleler = re.split(r"[.!?]", metin)

toplam_cumle = len(cumleler) - 1

toplam_karakter = len(metin)

kelime_uzunluklari = []

for kelime in filtrelenmis_kelimeler:
    kelime_uzunluklari.append(len(kelime))

ortalama_kelime_uzunlugu = (
    sum(kelime_uzunluklari) / len(kelime_uzunluklari)
)

# ============================================
# EN ÇOK KULLANILAN KELİMELER
# ============================================

kelime_sayaci = Counter(filtrelenmis_kelimeler)

en_yaygin_10 = kelime_sayaci.most_common(10)

# ============================================
# SONUÇLARI YAZDIRMA
# ============================================

print("\n===== METİN ANALİZ RAPORU =====\n")

print(f"Toplam Karakter Sayısı: {toplam_karakter}")

print(f"Toplam Kelime Sayısı: {toplam_kelime}")

print(f"Toplam Cümle Sayısı: {toplam_cumle}")

print(
    f"Ortalama Kelime Uzunluğu: "
    f"{ortalama_kelime_uzunlugu:.2f}"
)

print("\n--- EN SIK KULLANILAN 10 KELİME ---\n")

for kelime, adet in en_yaygin_10:

    print(f"{kelime} -> {adet}")

# ============================================
# DATAFRAME OLUŞTURMA
# ============================================

df = pd.DataFrame(
    en_yaygin_10,
    columns=["Kelime", "Frekans"]
)

print("\n--- DATAFRAME ---\n")

print(df)

# ============================================
# CSV DOSYASINA AKTARMA
# ============================================

df.to_csv(
    "kelime_analizi.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nCSV dosyası oluşturuldu!")

# ============================================
# GRAFİK OLUŞTURMA
# ============================================

plt.figure(figsize=(10, 5))

plt.bar(df["Kelime"], df["Frekans"])

plt.title("En Çok Kullanılan Kelimeler")

plt.xlabel("Kelimeler")

plt.ylabel("Kullanım Sayısı")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()

# ============================================
# DUYGU ANALİZİ
# ============================================

pozitif_kelimeler = [
    "iyi",
    "güzel",
    "harika",
    "mükemmel",
    "başarılı",
    "mutlu",
    "süper",
    "sevgi"
]

negatif_kelimeler = [
    "kötü",
    "berbat",
    "üzücü",
    "sinirli",
    "başarısız",
    "nefret",
    "zor",
    "korku"
]

pozitif_sayi = 0

negatif_sayi = 0

for kelime in filtrelenmis_kelimeler:

    if kelime in pozitif_kelimeler:
        pozitif_sayi += 1

    if kelime in negatif_kelimeler:
        negatif_sayi += 1

print("\n--- DUYGU ANALİZİ ---\n")

print(f"Pozitif Kelime Sayısı: {pozitif_sayi}")

print(f"Negatif Kelime Sayısı: {negatif_sayi}")

if pozitif_sayi > negatif_sayi:

    print("Metin genel olarak POZİTİF.")

elif negatif_sayi > pozitif_sayi:

    print("Metin genel olarak NEGATİF.")

else:

    print("Metin NÖTR görünüyor.")

# ============================================
# EN UZUN VE EN KISA KELİME
# ============================================

en_uzun_kelime = max(filtrelenmis_kelimeler, key=len)

en_kisa_kelime = min(filtrelenmis_kelimeler, key=len)

print("\n--- KELİME ANALİZİ ---\n")

print(f"En Uzun Kelime: {en_uzun_kelime}")

print(f"En Kısa Kelime: {en_kisa_kelime}")

# ============================================
# BELİRLİ BİR KELİMEYİ ARAMA
# ============================================

aranan_kelime = input(
    "\nAramak istediğiniz kelimeyi girin: "
).lower()

adet = kelime_sayaci[aranan_kelime]

print(
    f"\n'{aranan_kelime}' kelimesi "
    f"{adet} kez kullanılmıştır."
)

# ============================================
# RAPOR DOSYASI OLUŞTURMA
# ============================================

with open(
    "rapor.txt",
    "w",
    encoding="utf-8"
) as rapor:

    rapor.write("===== METİN ANALİZ RAPORU =====\n\n")

    rapor.write(
        f"Toplam Karakter: {toplam_karakter}\n"
    )

    rapor.write(
        f"Toplam Kelime: {toplam_kelime}\n"
    )

    rapor.write(
        f"Toplam Cümle: {toplam_cumle}\n"
    )

    rapor.write(
        f"Ortalama Kelime Uzunluğu: "
        f"{ortalama_kelime_uzunlugu:.2f}\n"
    )

    rapor.write("\nEn Sık Kelimeler:\n")

    for kelime, adet in en_yaygin_10:

        rapor.write(f"{kelime} -> {adet}\n")

print("\nRapor dosyası oluşturuldu!")

# ============================================
# PROGRAM SONU
# ============================================

print("\nProgram başarıyla tamamlandı!")
