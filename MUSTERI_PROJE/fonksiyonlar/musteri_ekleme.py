

def musteriEkle(cursor,db):
    ISIM = input("İSİM: ")
    SOYISIM = input("SOYİSİM: ")
    EMAIL = input("EMAIL: ")
    SEHIR = input("ŞEHİR: ")
    cursor.execute("INSERT INTO MUSTERILER (ISIM, SOYISIM, EMAIL, SEHIR) VALUES (?, ?, ?, ?)",
                   (ISIM, SOYISIM, EMAIL, SEHIR))
    db.commit()
    print("Müşteri eklendi.")
