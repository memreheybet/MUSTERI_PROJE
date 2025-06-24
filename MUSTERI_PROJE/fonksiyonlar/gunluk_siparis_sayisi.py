

def gunluk_siparis_sayisi(cursor,db):
    cursor.execute("""
        SELECT 
            CAST(S.TARIH AS DATE) AS SIPARIS_TARIHI,
            COUNT(S.ID) AS SIPARIS_SAYISI
        FROM SIPARISLER S
        GROUP BY CAST(S.TARIH AS DATE)
        ORDER BY SIPARIS_TARIHI;
    """)
    veriler = cursor.fetchall()
    print("\nGünlük Sipariş Sayısı:")
    for v in veriler:
        print(f"{v[0]} : {v[1]} sipariş")
#gunluk_siparis_sayisi(cursor)
