---
marp: true
theme: uncover
paginate: true
style: |
  section {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
    color: #f8fafc;
    font-family: 'Inter', 'Segoe UI', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 60px;
  }
  h1 {
    font-size: 2.5em;
    font-weight: 800;
    line-height: 1.3;
    text-shadow: 0px 4px 15px rgba(0, 0, 0, 0.5);
    letter-spacing: -1px;
  }
  h1 strong {
    color: #22d3ee;
    text-shadow: 0px 0px 20px rgba(34, 211, 238, 0.3);
  }
  footer {
    color: #94a3b8;
    font-size: 0.8em;
  }
  header {
    color: #22d3ee;
    font-weight: bold;
  }
  img {
    max-width: 48%;
    width: auto;
    height: auto;
    object-fit: contain;
    display: inline-block;
    margin: 0 8px;
  }
  p > img:only-child {
    max-width: 100%;
  }
---

# Python ile **GTK3** Uygulama Geliştirme Eğitimi

GaziSiber Özgür Yazılım Ve Pardus Takımı
22/04/2026 - Edip Hazuri


---
### Temel Kavramlar: Kütüphane

Kendinizi 20 tane büyük projesi olan bir yazılımcı olarak hayal edin. Bir gün bütün uygulamalarınıza tıklandığında bilgisayarı yok eden bir buton eklemek istediniz. Nasıl yaparsınız?


**A)** Kodu bir uygulama için yaz sonra diğerlerine tek tek kopyala
**B)** Kodu bir kere yazıp, bütün uygulamalar için ortak bir yere koyup gerektiğinde oradan çağırmak <!--cevap-->

---
### Temel Kavramlar: Arayüz Kütüphanesi
Bir uygulama tasarlamak istiyorsunuz. Bu uygulamanın ilk aşaması olarak ekrana sadece bir buton koymak istediniz. Nasıl yaparsınız?

**A)** Ekranın piksellerini tek tek boya, butonun gölgesi için ışık açılarını hesapla, farenin koordinatlarını anlık takip etmek için binlerce satır kod yaz. 
**B)** Bir Arayüz Kütüphanesine (GTK3 gibi) sadece "Bana buraya 'Giriş' yazan bir buton koy" de. Geri kalan matematiksel hesaplamaları, görsel efektleri o halletsin.

---

# Peki GTK nasıl Doğdu?

1996 yılında Peter Mattis ve Spencer Kimball, GIMPi yazmaya karar verdiler. Ancak o dönemde kullandıkları "Motif" isimli arayüz kütüphanesi hem hantaldı hem de lisans kısıtlamalarıyla doluydu.
Peter ve Spencer, GIMP'i tamamlayabilmek için önce kendi araç kutularını yazmak zorunda kaldılar: GTK (GIMP Tool Kit) böylece bir yan proje olarak doğdu.

---
# Peki GTK nasıl Büyüdü?
Peter Mattis ve Spencer Kimball'ın yazdığı bu arayüz kütüphanesi o kadar iyi ve kadar o esnek oldu ki. 1997 yılında başlayan GNOME masaüstü ortamı, tüm masaüstü ortamını GTK üzerine inşa etmeye karar verdi.
Bundan sonra GTK, GNOME'un projesi haline geldi ve ismi Gnome ToolKit oldu 

---
![alt text](image.png)![alt text](image-1.png)
![alt text](image-3.png)![alt text](image-4.png)

---

### Gtk3 için ortamı hazırlayalım.
- git clone https://github.com/vilez0/gtk3-examples
- sudo apt install glade build-essential pkg-config libgtk-3-dev python3-gi python3-gi-cairo gir1.2-gtk-3.0
