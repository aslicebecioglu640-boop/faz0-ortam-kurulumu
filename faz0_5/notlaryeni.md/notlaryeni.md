+Python3 Notları
-Python'da veri tanımlamak için veri tipi belirtmeye gerek yoktur.
-True veya false döndüren değişkenler için:
değişken_adı = True/False
-type() ile tipleri öğrenilir.
-Bir sayıyı metne dönüştürmek için str() kullanılır.
Yani mesela: 25 sayısı → "25" e dönüşür.
Tam tersi (metni sayıya çevirmek) int() ile yapılır.
-Çoklu atama yapılabilir:
a, b, c = 1, 2, 3
-Python ile C++ Arasındaki Fark
C++ statik bir dil, o yüzden değişkenin tipini kendimiz belirtmeliyiz.
Python ise dinamik bir dil, girileni kendisi anlıyor.
C++'taki nullptr, Python'daki None ile aynı ama bir konuda farklı: C++'ta pointer'ın hiçbir şeyi göstermediğini söyler.
-Operatörler
-or, and operatörleri yazıyla yazılır.
/ → normal bölme
// → tam sayı bölme, küsüratı atar.
% → kalanı ekrana yazdırır (mod alma).
+= → x'e değer eklemek için kullanılır.
-elif: else if anlamına gelir.
-Boş bir liste ([]), boş bir string (""), 0, None gibi değerler otomatik olarak "yanlış" (falsy) sayılır.
-İçi dolu bir liste, dolu bir string, sıfır olmayan bir sayı ise "doğru" (truthy) sayılır.

- C++'ta süslü parantezler kod bloğunu belirler.süslü parantez kullanmaz isek kod bloğu karışabilir.
  Python'da ise blok sınırlarını girintiler belirler.
  -Truthy-- if içinde true davranan değerlere denir.(dolu liste,dolu string vb.)
  -Falsy-- if içinde false davranan değerler.(boş liste,boş string vb.)
  Range()for ile kullanılınca sayı dizisinde gezinmeyi sağlar.
  -forda tek tek harf yazdırmak için range gibi bir şey kullanmamız gerekmez kelimeyi tırnak içinde yazarak yapabiliriz.
  -break: Kodu beliri bir koşulda durdurmak için kullanılır.
  -continue:Bir noktada durup tekrar devam edebilmek için kullanılır.
  -enumerate({}):listenin elemanlarını hem elemanı hem indeksini yazdırır.
- For ve while karşılaştırması: for kaç kere döneceği bilindiğinde kullanılır.Belirli bir aralıkta sayı saymak gibi.
  while ise bir koşul sağlandığında devam etmesini istenildiğinde kullanılır.
  -Break ve continue karşılaştırması: break döngüyü tamamen dondurur.
  continue ise sadece o anki adımı durdurur.
  -Fonksiyon tanımamak için başına def kullanılır define anlamına gelir.
  -Print ile return karşılaştırma:Print sadece ekrana bir şey gösterir.
  Return ise fonksiyon sonucunu iletir.Ekrana bir şey yazdırmaz.
  -Local ve global değişken karşılaştırması:Local bir fonksiyonun içinde tanımlanan değişken.Dışarıdan erişilemez.
  Global fonksiyon dışında tanımlanır ve dışarıdan erişilebilir.
  -.append() ile listeye yeni bir eleman eklenir.
- len()etikeli ile listede kaç eleman içerdiği öğrenilir.
  -.remove() ile listeden belirli bir eleman silinir.
  -.pop() ile listenin son elemanı silinir.
  -.sort() ile küçükten büyüğe sıralanır.
  -C++ ta dizi oluşturulduğu anda boyut sabitlenir.python list ise dinamik boyutludur.
  -.get(): olmayan bir anahtara erişmeye çalıştığında programın çökmesini engellemek, yerine senin belirlediğin bir "yedek" değeri döndürmek.
  .keys():sözlükteki başlıkları söyler.
  .values(): değerleri yazar.
  .items():değeri ve başlıkları parantez içinde yazar.
- nested dictionary yapabilmek için; sözlüğün içinde anahtarın yanına süslü parantez açılır.
  -iç içe liste ve sözlük yapısı kullanılabilir.
  JSON :(JavaScript Object Notation):bir veri yazma şeklidir.Bilgiyi düzenli bi şekilde saklatır.Veriyi tutar.
  -get kullanmak programı çökmekten kurtarır o yüzden daha işe yarar bir araçtır.
  -Dictinory json'a benzer çünkü json'un yapı taşı ile benzer.
- İki string'i birleştirmek için f-string kullanılır.
-.upper:kelimeyi büyük harflerle yazdırır.
-.lower:kelimeyi küçük harflerle yazdırır.
-.split:cümledeki kelimeleri tek tek alıp kelimelerle liste oluşturur.
-.join: ise listedeki elemanları birleştirir.
- try except bloğu hatayı program çökmeden görmemize yardımcı olan bir araçtır.
-finally bloğu her durumda çalışan bir durumdur.except ile arasındaki fark except hata olursa çalışır , finally her durumda çalışır.
-Kodumda bir deneme yapmak istersem try/except kullanabilirm.
-Finally: Ne olursa olsun yapılması gereken şeylerde kullanılır.
-Raise:Koşul koymak istersem kullanabilirim.