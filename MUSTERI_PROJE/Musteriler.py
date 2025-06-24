from selectors import SelectSelector

import pypyodbc
#from fonksiyonlar import musteri_ekleme
from fonksiyonlar.en_cok_satilan_urun import en_cok_satilan_urun
from fonksiyonlar.gunluk_siparis_sayisi import gunluk_siparis_sayisi
from fonksiyonlar.musteri_ekleme import musteriEkle
from fonksiyonlar.musteri_silme import musteriSil
from fonksiyonlar.raporlama import raporla
from fonksiyonlar.siparis_ekleme import siparisEkle
from fonksiyonlar.urun_ekleme import urunEkle
from fonksiyonlar.en_cok_siparisveren import en_cok_siparis_veren

# Bağlantı
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=.;'
    'Database=MUSTERI_TAKIP_SISTEMI;'
    'Trusted_Connection=True;'
)
cursor = db.cursor()


# === MENÜ ===
while True:
    print("\n--- MENÜ ---")
    print("1. Müşteri Ekle")
    print("2. Urun Ekle")
    print("3. Musteri Sil")
    print("4. Sipariş Ver")
    print("5. Raporla")
    print("6. En Cok Siparis Veren Bilgisi")
    print("7. En Cok Satilan Urun Bilgisi")
    print("8. Gunluk siparis sayisi")
    print("9. Cikis")



    secim = input("Seçiminizi girin: ")

    if secim == "1":
        musteriEkle(cursor,db)
    elif secim == "2":
        urunEkle(cursor,db)
    elif secim == "3":
        musteriSil(cursor,db)
    elif secim == "4":
        siparisEkle(cursor,db)
    elif secim == "5":
        raporla(cursor,db)
    elif secim == "6":
        en_cok_siparis_veren(cursor,db)
    elif secim == "7":
        en_cok_satilan_urun(cursor,db)
    elif secim == "8":
        gunluk_siparis_sayisi(cursor,db)
    elif secim == "9":
        print("Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim!")

# Kapat
db.close()
