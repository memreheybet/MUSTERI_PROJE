

def en_cok_satilan_urun(cursor,db):
    cursor.execute("""
        SELECT TOP 1
            U.URUN_ID,
            COUNT(S.ID) AS SATIS_SAYISI
        FROM SIPARISLER S
        JOIN URUNLER U ON S.URUN_ID = U.ID
        GROUP BY U.URUN_ID
        ORDER BY SATIS_SAYISI DESC;
    """)
    sonuc = cursor.fetchone()
    if sonuc:
        print(f"En çok satılan ürünün ID'si: {sonuc[0]}, Satış sayısı: {sonuc[1]}")
    else:
        print("Veri bulunamadı.")
        en_cok_satilan_urun(cursor)