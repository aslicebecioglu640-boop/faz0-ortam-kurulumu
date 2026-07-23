yas=19
boy=1.70
isim="Aslı"
ogrenci_mi=True
sehir="İstanbul"
print("Yaş:", yas)
print("Boy:", boy)
print("İsim:", isim)
print("Öğrenci mi:", ogrenci_mi)
print("Yaş tipi:", type(yas))
print("Boy tipi:", type(boy))
print("İsim tipi:", type(isim))
print("Öğrenci mi tipi:", type(ogrenci_mi))

metin=str(yas)
print(type(metin))

sayı=int(yas)
print(type(sayı))
a,b,c=1,2,3
print(a,b,c)
isimi=input("Bir isim giriniz: ")
print("merhaba", isimi)
deger=None
print(type(deger))
v,y=9,6
print(v+y)
print(v-y)
print(v*y)
print(v/y)
print(v%y)
print(v//y)
print(v**y)
print("v y den büyük mü?", v>y)
print("v y den küçük mü?", v<y)
print("v y ye eşit mi?", v==y)
u=True
p=False
print("u ve p:", u and p)
print("u veya p:", u or p)
print("u değil mi?", not u)
x=5
x+=1
print(x)
x-=1
print(x)
x*=2
print(x)
print(1<x<10)
meyve=[1,2,3,4,5]
print("2" in meyve)
if yas>18:
    print("yetişkin")
else:
    print("çocuk")

if yas>18:
    print("yetişkin")
elif 13<= yas <= 18:
    print("genç")
elif 0<= yas <=12:
    print("çocuk")

if yas>18 and boy>1.60:
    print("yetişkin ve boyu uzun")

    if yas>18:
        if sehir=="İstanbul":
            print("İstanbul'da yaşayan yetişkin")

print("yetişkin" if yas<18 else "çocuk")
liste=[]
if liste==[]:
    print("liste boş")
else:
    print("liste dolu")
string=""
if string=="":
    print("string boş")
else:
    print("string dolu")
for sayı in range(1,11):
    print(sayı)
for sayı in range(1,11):
    if sayı%2==0:
        print(sayı)
sayac=0
while sayac<=5:
    print(sayac)
    sayac+=1 
for harf in "aslı":
    print(harf)
for sayı in range(1,101):
    if sayı==7:
        break
    print(sayı)
for sayı in range(1,11):
    if sayı%2==1:
        continue
    print(sayı)
print("enumerate ile film listesi:")
for i, film in enumerate(["rp1", "rp2", "rp3"]):
    print(f"{i}: {film}")
for a in range(1,4):
    for b in range(1,4):
        print(a*b)
def fon1():
    print("merhaba")
fon1()
def selam_ver(isim):
    print(f"merhaba {isim}")
selam_ver("Aslı")  
def topla(a,b): 
    return a+b
sonuc=topla(3,5)
print(sonuc)
def selam_ver(isim="misafir"):
    print(f"merhaba {isim}")
selam_ver()
def ortal(a, b):
    return topla(a, b) / 2
def fon3(a,b):
    return a*2 + b*2
"""Bu fonksiyon iki sayının iki katlarının toplamını döndürür."""
def fon4(t,e):
  t=2
  e=3       
  return t*2 + e*2
filmler=["rp1", "rp2", "rp3"]
print(filmler[0],filmler[2])
filmler.append("rp4")
for film in filmler:
    print(film)

print(len(filmler))

print(filmler[0:2])
filmler.remove("rp2")
print(filmler)
filmler.pop()
print(filmler)
sayılistesi=[5,6,3,4,0,1,2]
sayılistesi.sort()
print(sayılistesi)
liste1=[1,2,3]
liste2=[4,5,6]
liste3=liste1+liste2
print(liste3)
print("matrix" in filmler)
kisi={"isim":"Aslı", "yas":19, "sehir":"İstanbul"}
print(kisi["isim"])
print(kisi["sehir"])
print(kisi["yas"])
kisi["meslek"]="öğrenci"
for key in kisi:
    print(key, kisi[key])
kisi2={"isim":"Ahmet", "yas":25, "sehir":"Ankara"}   
kisiler=[kisi, kisi2]
print(kisiler)
print(kisi.get("telefon", "telefon bulunamadı"))
print(kisi.keys())
print(kisi.values())
print(kisi.items())
print("isim" in kisi)
kisi.pop("meslek")
print(kisi)
kisi={"isim":"mehmet", "yas":30, "sehir":"izmir", "adres"
:{"ilce":"konak", "mahalle":"gazi"}}
print(kisi["adres"]["ilce"])
soyisim="Cebecioğlu"
concatenation=isim+" "+soyisim
print(concatenation),
f_string=f"{isim} {soyisim}"
print(f_string)
isim.upper()
print(isim.upper())
isim.lower()
print(isim.lower())
okul=str(" kaan ")
okul.strip()
print(okul.strip())
no="0 535 780 72 23"
print(no)
no=no.replace(" ", "")
print(no)
cümle="faz0 ortam kurulumu"
cümle.split()
print(cümle.split())
kelimeler=cümle.split()
" ".join(kelimeler)
print(" ".join(kelimeler))
print(isim[0:3])
print(no.startswith("0"))
print(no.endswith("2"))
print(len(no))
try:
    int("abc")
except ValueError:
    print("Geçersiz değer hatası!")
try:
    5/0
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")

try:
    int("abc")
except ValueError:
    print("Geçersiz değer hatası!")
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")

finally:
    print("Hata yönetimi tamamlandı.")
if yas<0:
    raise ValueError("Yaş negatif olamaz!")

