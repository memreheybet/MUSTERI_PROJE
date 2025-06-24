

def musteriSil(cursor,db):
    musteri_id = int(input("Silinecek MÜŞTERİ ID'sini girin: "))

    cursor.execute("DELETE FROM SIPARISLER WHERE MUSTERI_ID = ?", (musteri_id,))
    cursor.execute("DELETE FROM MUSTERILER WHERE ID = ?", (musteri_id,))
    db.commit()

    print("Silme Islemi Basarili")
