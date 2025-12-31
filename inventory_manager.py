envanter={}
def esya_ekle(isim,adet):
    if isim in envanter:
        envanter[isim]+=adet
        print(f"{isim} güncellendi. Yeni miktar {envanter[isim]}")
    else:
        envanter[isim]=adet
        print(f"{isim} envantere eklendi.")
def esya_sil(isim):
    if isim in envanter:
        envanter.pop(isim)
        print(f"{isim} silindi.")
    else:
        print(f"Hata: {isim} bulunamadı.")
def envanter_goster():
    if not envanter:
        print("Envanter boş.")
    else:
        for urun,miktar in envanter.items():
            print(f"- {urun}:{miktar} adet")
def main():
    while True:
        print(f"\n1- Ekle | 2- Sil | 3- Listele | Q- Çıkış")
        secim=input("Lütfen seçiminizi yapiniz.").lower()

        if secim=="1":
            ad=input("Eşya adını giriniz: ")
            sayi=int(input("Adet: "))
            esya_ekle(ad,sayi)
        elif secim=="2":
            ad=input("Silinecek eşya adi: ")
            esya_sil(ad)    
        elif secim=="3":
            envanter_goster()
        elif secim=="q":
            print("Sistemden çıkılıyor. İyi yolculuklar.")
            break
        else:
            print("Geçersiz seçim")
if __name__ == "__main__":
    main()