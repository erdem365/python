import pandas as pd
import numpy as np

# 1. Create DataFrame
data = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep"],
    "matematik": [80, 95, 60, 100],
    "fizik": [70, 88, 75, 92],
    "kimya": [90, 91, 70, 98]
}
df = pd.DataFrame(data)

# 2. Create average grade column
df["ortalama"] = df[["matematik", "fizik", "kimya"]].mean(axis=1)

print("=== DataFrame ===")
print(df)
print("\n")

# 3. Find the student with the highest average
en_yuksek_ogrenci = df.loc[df["ortalama"].idxmax(), "isim"]
en_yuksek_ortalama = df["ortalama"].max()
print(f"Student with highest average: {en_yuksek_ogrenci} (Average: {en_yuksek_ortalama})")
print("\n")

# 4. Calculate the average of each subject
ders_ortalamalari = df[["matematik", "fizik", "kimya"]].mean()
print("Average per subject:")
print(ders_ortalamalari)
print("\n")

# 5. Filter students with average above 85
ust_85 = df[df["ortalama"] > 85]
print("Students with average above 85:")
print(ust_85[["isim", "ortalama"]])
print("\n")

# 6. Sort grades from highest to lowest (by average)
sirali_df = df.sort_values(by="ortalama", ascending=False)
print("Students sorted by average (highest to lowest):")
print(sirali_df[["isim", "ortalama"]])
print("\n")

# ========== NUMPY PART ==========
# 7. Convert grades to NumPy array (only subject grades, exclude name and average)
notlar_array = df[["matematik", "fizik", "kimya"]].to_numpy()
print("Grades as NumPy array:\n", notlar_array)
print("\n")

# 8. Calculate overall class average using numpy.mean()
genel_ortalama = np.mean(notlar_array)
print(f"Overall class average (all subjects and students): {genel_ortalama:.2f}")
print("\n")

# 9. Find standard deviation
standart_sapma = np.std(notlar_array)
print(f"Standard deviation of all grades: {standart_sapma:.2f}")
