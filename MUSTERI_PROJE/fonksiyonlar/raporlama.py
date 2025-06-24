
def raporla(cursor,db):
    try:
        cursor.execute("""
            SELECT 
                S.ID,
                M.ISIM + ' ' + M.SOYISIM AS MUSTERI_ADI,
                U.URUN_ID,
                S.TARIH
            FROM SIPARISLER S
            JOIN MUSTERILER M ON S.MUSTERI_ID = M.ID
            JOIN URUNLER U ON S.URUN_ID = U.ID
            ORDER BY S.TARIH DESC
        """)
        veriler = cursor.fetchall()
        print("\n--- Sipariş Raporu ---")
        for v in veriler:
            print(f"#{v[0]} | {v[1]} | {v[2]} | {v[3]}")
    except Exception as e:
        print("Raporlama sırasında hata oluştu:", e)
