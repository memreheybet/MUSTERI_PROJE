

def en_cok_siparis_veren(cursor,db):
    cursor.execute("""
                   SELECT top 1
            M.ID, M.ISIM + ' ' + M.SOYISIM AS MUSTERI_ADI,
                          COUNT(S.ID) AS SIPARIS_SAYISI
                   FROM SIPARISLER S
                            JOIN MUSTERILER M ON S.MUSTERI_ID = M.ID
                   GROUP BY M.ID, M.ISIM, M.SOYISIM
                   ORDER BY SIPARIS_SAYISI DESC
                   """)

    sonuc = cursor.fetchone()

    if sonuc:
        print(f"En çok sipariş veren: {sonuc[1]} - Sipariş Sayısı: {sonuc[2]}")
    else:
        print("Hiç veri gelmedi.")
        en_cok_siparis_veren(cursor)