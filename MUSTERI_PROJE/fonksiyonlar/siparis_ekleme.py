
def siparisEkle(cursor,db):
    MUSTERI_ID = int(input("MÜŞTERİ ID: "))
    URUN_ID = int(input("ÜRÜN ID: "))
    TARIH = input("TARİH (YYYY-MM-DD): ")
    cursor.execute("INSERT INTO SIPARISLER (MUSTERI_ID, URUN_ID, TARIH) VALUES (?, ?, ?)",(MUSTERI_ID, URUN_ID, TARIH))
    db.commit()
    print("Sipariş eklendi.")