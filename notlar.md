# Terminal, Git ve Python Notları

## Terminal Komutları

- **pwd**: Şu an nerede olduğunu gösterir.
- **ls**: Dosyaları listeler.
- **cd Desktop**: Desktop klasörüne girer.
- **cd ..**: Klasör hiyerarşisinde bir üst klasöre çıkarır.
- **cd ~**: En baş / ana sayfaya döndürür. (`~`'den sonra boşluk var)
- **py**: Python çalıştırır.

## Python - print()

`print()` ile birden fazla bilgiyi farklı satırlarda göstermenin iki temel yolu var:

- Her bilgi için ayrı bir `print` açmak
- Tek bir `print` içinde `\n` kullanmak

### Tarih Eklemek İçin

```python
import datetime
print(datetime.datetime.now())
```

> Girinti (indent), üstteki komutun altında olduğunu gösterir.

---

## Git Komutları

### git status
Çalışılan klasörde git deposunun şu anki durumunu gösterir. Neyin değişip değişmediğini gösterir.

- **Modified**: Git'in önceden tanıdığı bir dosyada değişiklik var ama kaydedilmemiş.
- **Untracked**: Git'e eklenmemiş, o yüzden değişiklikleri bilmiyor.

### Temel Komutlar

- **git add**: Yeni dosyayı bir sonraki commit için hazırlar.
- **git commit**: Hazırlanan değişiklikleri bir açıklama mesajıyla git geçmişine kalıcı olarak kaydeder.
- **git push**: Bilgisayarında yaptığın commit'leri GitHub'daki repoya gönderir.

> Commit sadece bilgisayarında kalır. Push olmadan GitHub'da görünmez.

### Akış

```
add → commit → push
```

### Dosyayı Git'e Atmak İçin

```bash
git add (dosya adı)
git commit -m (mesaj)
git push
```

> `-m` mesaj eklenmesi / açılmaması için kullanılır.

### Mesaj Ekranı Açılırsa (yani `git commit` mesajsız yazılırsa)

Mesaj nasıl yazılır:

1. `i` → mesajı yaz
2. `Esc`'e bas
3. `:wq` → kaydet ve çık
