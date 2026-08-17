# Güvenlik Politikası (Security Policy)

## 🔒 Gizlilik ve Veri Güvenliği
Bu proje tamamen **yerel (local)** çalışacak şekilde tasarlanmıştır.

- **Veri Toplama Yok:** Yazılım hiçbir kişisel veriyi, Wi-Fi şifresini veya ağ bilgisini harici sunuculara göndermez.
- **Yerel Çalışma:** Tüm işlemler Windows'un kendi yerel komut satırı araçları (`netsh`, `arp`, `ipconfig`) üzerinden bilgisayarınızda gerçekleşir.
- **İnternet Bağlantısı:** Kodun internete veri aktaran hiçbir bağımlılığı (HTTP/socket isteği) bulunmamaktadır.

## 🐛 Güvenlik Açığı Bildirimi
Eğer kod içerisinde herhangi bir güvenlik riski veya beklenmeyen bir durum tespit ederseniz, lütfen kamuya açık bir `Issue` açmak yerine doğrudan geliştirici ile iletişime geçin.

- **Desteklenen Sürümler:** `v3.1` ve üzeri
