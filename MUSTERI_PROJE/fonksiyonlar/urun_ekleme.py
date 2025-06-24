

def urunEkle(cursor,db):
    URUN_ID = input("ÜRÜN ADI: ")
    FIYAT = int(input("FİYAT: "))
    cursor.execute("INSERT INTO URUNLER (URUN_ID, FIYAT) VALUES (?, ?)",
                   (URUN_ID, FIYAT))
    db.commit()
    print("Ürün eklendi.")
