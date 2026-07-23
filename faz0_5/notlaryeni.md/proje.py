
    
def kisi_olustur(isim, yas, sehir):
    try:
        yas=int(yas)
    except ValueError:
        print("Sayı giriniz!")
        yas=None
    kisi = {"isim": isim, "yas": yas, "sehir": sehir}
    return kisi
kisi1=kisi_olustur("Aslı", "ondokuz", "İstanbul")
kisi2=kisi_olustur("mehmet",20,"Ankara")
kisi3=kisi_olustur("melike",7,"İstanbul")
kisiler=[kisi1,kisi2,kisi3]
for kisi1 in kisiler:
    print(f"{kisi1['isim']} {kisi1['yas']} yaşında {kisi1['sehir']}'da yaşıyor.")

