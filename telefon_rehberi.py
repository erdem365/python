import os

class PhoneBook:
    FILE_NAME = "Files/phonebook.txt"

    def __init__(self):
        # Klasör yoksa oluştur
        os.makedirs("Files", exist_ok=True)
        # Dosya yoksa oluştur
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w", encoding="utf-8"):
                pass

    #  Kişi ekleme
    def add_contact(self, firstname, lastname, phone):
        with open(self.FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"{firstname},{lastname},{phone}\n")
        print(f"✅ {firstname} {lastname} rehbere eklendi.")

    #  Rehber listeleme
    def list_contacts(self):
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            print(" Rehber boş.")
        else:
            print("\n Telefon Rehberi:")
            for line in lines:
                firstname, lastname, phone = line.strip().split(",")
                print(f"- {firstname} {lastname}: {phone}")

    #  Kişi silme
    def delete_contact(self, name):
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        contact_found = False
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            for line in lines:
                firstname, lastname, phone = line.strip().split(",")
                if firstname.lower() != name.lower() and lastname.lower() != name.lower():
                    file.write(line)
                else:
                    contact_found = True

        if contact_found:
            print(f" {name} rehberden silindi.")
        else:
            print(f" {name} adlı kişi bulunamadı.")

    #  Kişi arama
    def search_contact(self, keyword):
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        found = False
        print(f"\n '{keyword}' için arama sonuçları:")
        for line in lines:
            firstname, lastname, phone = line.strip().split(",")
            if (keyword.lower() in firstname.lower() or
                keyword.lower() in lastname.lower() or
                keyword in phone):
                print(f"- {firstname} {lastname}: {phone}")
                found = True

        if not found:
            print(" Eşleşen kayıt bulunamadı.")

    #  Kişi güncelleme
    def update_contact(self, name):
        with open(self.FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        contact_found = False
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            for line in lines:
                firstname, lastname, phone = line.strip().split(",")
                if firstname.lower() == name.lower() or lastname.lower() == name.lower():
                    print(f" {firstname} {lastname} güncelleniyor...")
                    new_first = input("Yeni ad (boş bırakmak için Enter): ") or firstname
                    new_last = input("Yeni soyad (boş bırakmak için Enter): ") or lastname
                    new_phone = input("Yeni telefon (boş bırakmak için Enter): ") or phone
                    file.write(f"{new_first},{new_last},{new_phone}\n")
                    contact_found = True
                else:
                    file.write(line)

        if contact_found:
            print(f" {name} başarıyla güncellendi.")
        else:
            print(f" {name} adlı kişi bulunamadı.")


# ==========================================================
# ANA PROGRAM (MENÜ)
# ==========================================================

def main():
    pb = PhoneBook()

    while True:
        print("\n=====  TELEFON REHBERİ =====")
        print("1 - Kişi Ekle")
        print("2 - Kişileri Listele")
        print("3 - Kişi Sil")
        print("4 - Kişi Ara")
        print("5 - Kişi Güncelle")
        print("6 - Çıkış")

        choice = input("Seçiminizi yapın (1-6): ")

        if choice == "1":
            firstname = input("Ad: ")
            lastname = input("Soyad: ")
            phone = input("Telefon: ")
            pb.add_contact(firstname, lastname, phone)

        elif choice == "2":
            pb.list_contacts()

        elif choice == "3":
            name = input("Silmek istediğiniz kişinin adını veya soyadını girin: ")
            pb.delete_contact(name)

        elif choice == "4":
            keyword = input("Aramak istediğiniz ad, soyad veya numara: ")
            pb.search_contact(keyword)

        elif choice == "5":
            name = input("Güncellemek istediğiniz kişinin adını veya soyadını girin: ")
            pb.update_contact(name)

        elif choice == "6":
            print(" Programdan çıkılıyor...")
            break

        else:
            print(" Geçersiz seçim. Lütfen 1-6 arasında bir değer girin.")


if __name__ == "__main__":
    main()
