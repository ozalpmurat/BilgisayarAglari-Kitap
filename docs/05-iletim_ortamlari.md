# İletim Ortamları

Temelde **atmosfer** ve **kablo** olmak üzere iki farklı iletim ortamı
mevcuttur. Atmosferde RF (radyo frekans) dalgalarını kullanarak iletişim
gerçekleşir. Kablolarda ise genellikle **fiberoptik** ve **bakır** kablo
kullanılmaktadır.

İnternet yaygınlaşmaya başladığında, dünyadaki her eve kablo çekmek mümkün olmadığından, mevcut altyapılardan nasıl yararlanılacağına çalışıldı. Her eve gidebilecek en kolay yöntem telefon hattı olduğundan ilk İnternet bağlantıları telefon hattı üzerinden sağlandı. Eskiden telefon hattı üzerinden internet hizmeti de kullanmaya çalışırken, şimdi internet altyapısı üzerinden -_ihtiyaç olursa_- telefon hizmeti de kullanabiliyoruz.

## İki Telli Bakır Telefon Hattı
Telefon iletişimini sağlamak için tasarlanmıştır. İnternet'te yaygın kullanılan ilk kablo türüdür. Temel bant ve geniş bant internet hizmeti verilmektedir. Analog modülasyon teknikleriyle en fazla 56 Kb/s’lik band genişliği sağlar. xDSL teknolojileriyle teorik olarak 400 Mb/s’lik bant genişliğine ulaşılmaktadır.

![Çevirmeli Ağ](images/B05-CevirmeliAg.png)  
*Görsel kaynağı: https://www.geeksforgeeks.org/types-of-internet-connection/*

## Koaksiyel (Coaxial) Kablo
Genellikle elektriksel gürültünün yoğun olduğu şartlarda kullanılırdı.Yalıtkan bir tüpün içerisinde giden bir tel ve tüpün dışına sarılmış kafes şeklinde teller vardır. Yerel ağlarda (LAN) 180m’de(max) 10M b/s bant genişliği sağlar. Bu kullanımı 10 Base 2 olarak bilinir. Daha sonra 500 m mesafede çalıştırılacak hale getirilir. 10 Base 2 ismiyle standartlaştırılmıştır. 50 ohm’luk direnç değeri vardır. BNC tarzında konnektörler kullanılır. Günümüzde LAN’da hiç
kullanılmamaktadır. Sebebi hem 10 Mb/s hızının çok düşük olması, hem de
UTP kablolar kadar ekonomik ve işlevsel olmamasıdır. Bilgisayar ağlarında doğrusal (bus) topolojilerde kullanılmıştır.

![Koaksiyel ](images/B05-Koaksiyel_Kablo.png)  
*Görsel kaynağı: https://www.wiremasters.com/newshub/news/the-ins-and-outs-of-coaxial-cable*

![BNC konnektörler](images/B05-BNC_Konnektorler.png)  
*BNC Konnektörler*

## Bükümlü Çift Kablo (Twisted Pair Cable)
İçerisinde bükülmüş çiftler halinde bakır tel bulunur. Kabloların birbirleri üzerindeki direnç elektromanyetik etkisini azaltmak için ikişerli olarak sarılı durumundadırlar. 
![Bükümlü Çift Kablo](images/B02-BukumluCiftKablo.png)  
*Bükümlü çift kablo*

![Bükümlü Çift Kablolar](images/B02-BukumluCiftKablolar.png)  
*Görsel kaynağı: https://www.linx-com.com/copper-construction/*

- U: Unshilded (Korumasız)
- F: Foiled (Folyolu)
- S: Shielded (Korumalı)

### Frekanslarına Göre xTP kablolar
![Bükümlü Çift Kablolar](images/B02-UTP-Kategoriler-1.png)  
*Görsel kaynağı: https://dc.mynetworkinsights.com/categories-of-copper-twisted-pair-cables/*

![Bükümlü Çift Kablolar](images/B02-UTP-Kategoriler-2.png){width="800"}  
*Görsel kaynağı: https://telecom.samm.com/history-of-ethernet-lan-cables-categories*

!!! warning "CAT-1, CAT-2, CAT-3"
    Telefon hatlarında kullanılır, ağlarda kullanılmaz.  

<figure markdown="span">
  ![RJ-45 konnektör](images/B02-RJ45-Konnektor.png){ width="800" }
  <figcaption>Görsel kaynağı: https://www.electricalvolt.com/how-to-crimp-rj45-connector/</figcaption>
</figure>

Bükümlü çift CAT5 VE CAT6 Kabloları sonlandırmak için RJ-45 adı verilen
konnektörler kullanılır. Bu kablolar iki farklı iki şekilde
sonlandırılabilir.**568-A,568-B**  
Kablonun iki ucunun aynı standartlarla sonlandırılmasına **düz (Straight
kablo)** denir. İki ucunda iki farklı standartta sonlandırılma yapılırsa
**çapraz(cross-over)kablo** adı verilir.

### Ethernet Kablosunda Pin Dizilimi

![Ethernet Pinout](images/B05-Ethernet_Pinout.png)  
*Görsel kaynağı: https://resources.altium.com/p/gigabit-ethernet-101-basics-implementation/*

### Çapraz ve Düz Kablo

Bilgisayar ile dağıtıcı cihazların (anahtar, hub) iletişim kurabilmesi için; Bilgisayarın TX (Transmit) hattına karşılık anahtarın RX (Receive) hattı denk gelmelidir. Dağıtıcı olan ve olmayan cihazların pinleri karşılıklı denk gelecek şekilde (TX <-> RX) tasarlanmıştır. Ancak aynı türde iki cihaz birbirine bağlanırsa o zaman TX-TX ve RX-RX portlar karşılıklı gelmiş olur. Bu durumda çapraz (Crossover) kablo kullanılır.

![Çapraz kablo ne zaman kullanılır?](images/B05-CaprazKabloNeZaman.png)  
*Çapraz kablo ne zaman kullanılır?*

![Çapraz kablo](images/B05-Capraz_Kablo.png)  
*FastEthernet çapraz kablosu. Görsel kaynağı: https://www.youtube.com/watch?v=WSIuPM4q5Tw/*

!!! note "Auto-MDI-X"
    Yeni ağ cihazlarının tamamı Auto-MDI-X adı verilen teknoloji sayesinde
    karşıdaki cihazın ne tarz bir cihaz olduğunu anlar ve hangi pin'in ne
    amaçla kullanılacağını buna göre düzenler.

#### Örnek
![Çapraz ve düz kablo kullanımı](images/B05-CaprazveDuz_Kablo_Kullanimi.png)  
*Çapraz kablo kullanım yerleri (örnek)*

## Fiberoptik Kablolar

Fiber optik kablolar, veri göndermek için ışık sinyallerini kullanmaktadır. Işığın cam br tüp içinde iletilmesi şeklinde çalışır. Uzak mesafelerde veri iletişimi konusunda en sağlam ve ucuz seçenek fiberoptik kablolardır. Diğer seçenekler, Wifi ve uydu iletişimi olabilir.

![Fİberoptik Kablo](images/B05-Fİberoptik_Kablo_Yapisi.jpg)  
*Görsel kaynağı: https://www.researchgate.net/publication/325386764_Optical_Fiber_Sensor_Review_and_Applications/*

### Fiberoptik Kablo Avantajları
1. **Yüksek hız ve bant genişliği**: Fiber optik kablolar, geleneksel metal iletişim hatlarına göre daha yüksek bant genişliği sağlar. Bu sayede hızlı ve verimli veri aktarımı mümkün olur.
1. **Daha az sinyal zayıflaması**: Optik fiberdeki sinyal kaybı bakır tellere göre daha azdır. Bu nedenle daha uzun mesafelerde veri iletimi sağlanabilir.
1. **Daha az elektromanyetik girişim (EMI)**: Fiber optik kablolar, elektromanyetik girişime karşı daha az duyarlıdır ve daha güvenilirdir.
1. **İnce ve hafif**: Fiber optik kablolar, bakır kablolar gibi kalın ve ağır değildir. Bu özellikleri sayesinde kurulum ve bakım işlemleri daha kolaydır.
1. **Dış ortam koşullarına dayanıklı**: Sıcaklık değişimleri, su baskınları, şiddetli hava ve nem gibi çevresel parametrelere karşı dayanıklıdır.
1. **Güvenli**: Elektromanyetik enerji sızması meydana gelmediği için bilgi güvenliği de sağlanmış olur. Kötü kişilerin araya girmesi, bakırdaki kadar kolay değildir.

<figure>
<img src="images/b03-fiberoptik_oyuncak.png"
id="fig:b03-fiberoptik-oyuncak.png" style="width:8cm"
alt="Fiber optik kablodan yapılan süs eşyası" />
<figcaption aria-hidden="true">Fiber optik kablodan yapılan süs
eşyası</figcaption>
</figure>

**Fiber Optik Dezavantajları**  
Sınırlı Uygulama — Fiber optik kablo sadece zeminde kullanılabilir ve
zemini terk edemez veya mobil iletişim ile çalışamaz.  
Düşük Güç — Işık yayan kaynaklar, düşük güçle sınırlıdır. Güç kaynağını
iyileştirmek için yüksek güç yayıcıları bulunmasına rağmen, ek maliyet
ekleyecektir.  
Kırılganlık - Fiber optik, bakır tellere kıyasla daha kırılgandır ve
hasara karşı daha hassastır. Fiber optik kabloları bükmemeli veya
bükmemelisiniz.  
Mesafe — Verici ve alıcı arasındaki mesafe kısa olmalı veya sinyali
arttırmak için tekrarlayıcılara ihtiyaç duyulmalıdır.  

<figure>
<img src="images/b03-kirik-fiberoptik.png"
id="fig:b03-kirik-fiberoptik.png" style="width:8cm"
alt="Kırık fiber optik kablo" />
<figcaption aria-hidden="true">Kırık fiber optik kablo</figcaption>
</figure>

Veri optik dalgalar arıcılığı ile ışığın yansıma kurallarına göre elde
edilir. Elektriksel sinyallerine göre mesafeye bağı zayıflama sinyalleri
çok azdır. Bakır kablolarda olduğu gibi gerilim farkından kaynaklanan
topraklama ihtiyacı yoktur. Fiberoptik kabloların yerel ağa
bağlanmasında elektriksel sinyal ile optik dalgalar arasında çevrilmesi
gerekir.Verici tarafından ışık kaynağı olarak lazer diyod(led),alıcı
tarafında ise fotodiyod ya da foto transistör kullanılır.

## FİBER OPTİK KABLO TÜRLERİ

Single mod(SM) ve Multi mod(MM) olmak üzere ikiye ayrılır  
**Multi-Mode**  
Bina ya da kampüs içi kısa mesafelerde tercih edilir.Optik dalga üretmek
için Led kullanılır.Verici ve alıcı maliyetleri single moduna göre yarı
yarıya azdır. **Single-Mode** Hem daha uzun mesafelerde hem de daha
yüksek band genişliğine imkan sağlar. Optik dalga üretmek için
LazerDiyod kullanılır.Bu nedenle verici ve alıcı donanım maliyetleri
daha fazladır.

<figure>
<img src="images/single-multimode" id="fig:single_multi_mode"
style="width:10cm" alt="single-multimode" />
<figcaption aria-hidden="true">single-multimode</figcaption>
</figure>

## FİBER OPTİK ÇEVİRİCİLER

\*F/O CONVERTOR  
\*F/O TRANSREİVER (ALICI/VERİCİ)  
\*GBIC (Switch modülü halindedir)  
\*STP (Switch modülü halindedir)  

## YEREL AĞLAR (LAN)

Kablo çekebileceğimiz (bize ait olan ) yerler yerel ağlardır. Ağlarda
band genişliği ,protokol,topoloji gibi altarnetifler isteğe göre
özelleştirilebilir. Günümüz yerel ağlarında ethernet harici protokol
kullanılmamamktadır.

## ETHERNET PROTOKOLÜ

İlk kez "INTEL VE XEROX" tarafından geliştirilmiştir.Daha sonra
IEEE(Institue of Electrical and Electronical Enginner) tarafından 809.3
ismi ile standartlaştırılmıştır.

## 10 M b/s Ethernet Portları

**10 Base 2 :** 10 sayısı 10 m b/s’yi ifade eder.Base sözcüğü temel
bandı ifade eder.En sondaki kablo türüdür.2 olduğunda ince (thin)
kooksiyel kablodur.  
**10 Base 5 :** Sondaki 5 Kalın(thick) kooksiyel kablo olduğunu
belirtir.  
**10 Base T :**Bükümlü çift kablo olduğunu ifade eder.  

## 100 M b/s ETHERNET PORTLARI

**100 Base Tx :**Fast Ethernet Cat-5 kablo kullanılır.  
**100 Base Fx :**F harfi Fiberoptik Kablo kullanıldığını belirtir.  

## 1000 M b/s ETHERNET PORTLARI

**1000 Base-T :** Cat5 ve Cat6 kablolar kullanılır.Ancak Cat6 tercih
edilir.  
**1000 Base-Lx :** L long kısaltmasıdır.SM,MM,FO kblolar kullanılır.Uzak
mesafelerde tercih edilir.En önemli dezavantajı maliyetlerin SX’e göre
fazla olmasıdır.  
**1000 Base-SX :**Yalnızca mm FO kablolar kullanılır.Kısa mesafeleri
destekler.Ekipmanları daha ucuzdur.  

## FİBEROPTİK SONLANDIRMA ŞEKİLLERİ

LC,SC,ST,FC sonlandırma mevcuttur.Günümüzde en yagın olan "LC" tipi
sonlandırma şeklidir.  

<figure>
<img src="images/Fiber-Optik-Ek-ve-Sonlandirma" id="fig:fosonlandirma"
style="width:10cm" alt="fibersonlandırma" />
<figcaption aria-hidden="true">fibersonlandırma</figcaption>
</figure>

  
\*F/O eki füzyon cihazı ile yapılır.2 tane cam tüpleri kaynatarak
birbirine ekler.  
İşlemler mikron seviyesinde yapıldığından kendi mikroskopu olan ve
hassasiyeti yüksek olan cihazlar kullanılır.  
F/O kablo testleri "OTDR" isimli cihaz ile yapılır.
