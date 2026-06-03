import pandas as pd
import numpy as np

# 1. DataFrame oluştur
data = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
    "matematik": [80, 95, 60, 100],
    "fizik": [70, 88, 75, 92],
    "kimya": [90, 91, 70, 98]
}
df = pd.DataFrame(data)

# 2. Ortalama not sütunu oluştur
df["ortalama"] = df[["matematik", "fizik", "kimya"]].mean(axis=1)

print("=== DataFrame ===")
print(df)
print("\n")

# 3. En yüksek ortalamaya sahip öğrenciyi bul
en_yuksek_ogrenci = df.loc[df["ortalama"].idxmax(), "isim"]
en_yuksek_ortalama = df["ortalama"].max()
print(f"En yüksek ortalamaya sahip öğrenci: {en_yuksek_ogrenci} (Ortalama: {en_yuksek_ortalama})")
print("\n")

# 4. Tüm derslerin ortalamasını hesapla
ders_ortalamalari = df[["matematik", "fizik", "kimya"]].mean()
print("Her dersin ortalaması:")
print(ders_ortalamalari)
print("\n")

# 5. 85 üstü ortalamaya sahip öğrencileri filtrele
ust_85 = df[df["ortalama"] > 85]
print("85 üstü ortalamaya sahip öğrenciler:")
print(ust_85[["isim", "ortalama"]])
print("\n")

# 6. Notları büyükten küçüğe sırala (ortalama sütununa göre)
sirali_df = df.sort_values(by="ortalama", ascending=False)
print("Öğrencilerin ortalamaya göre büyükten küçüğe sıralanmış hali:")
print(sirali_df[["isim", "ortalama"]])
print("\n")

# ========== NUMPY KISMI ==========
# 7. Notları NumPy array’e çevir (sadece ders notları, isim ve ortalama hariç)
notlar_array = df[["matematik", "fizik", "kimya"]].to_numpy()
print("Notların NumPy array hali:\n", notlar_array)
print("\n")

# 8. Tüm sınıfın genel ortalamasını numpy.mean() ile hesapla
genel_ortalama = np.mean(notlar_array)
print(f"Tüm sınıfın genel ortalaması (tüm dersler ve öğrenciler): {genel_ortalama:.2f}")
print("\n")

# 9. Standart sapmayı bul
standart_sapma = np.std(notlar_array)
print(f"Tüm notların standart sapması: {standart_sapma:.2f}")
