# İletim Ortamları

Temelde atmosfer ve kablo olmak üzere iki farklı iletim ortamı
mevcuttur. Atmosferde RF (radyo frekans) dalgalarını kullanarak iletişim
gerçekleşir. Kablolarda ise genellikle fiberoptik ve bakır kablo
kullanılmaktadır.

## İKİ TELLİ BAKIR TELEFON HATTI 

Telefon iletişimini sağlamak için tasarlanmıştır. Temel bant ve geniş
bant internet hizmeti verilmektedir. Analog modülasyon teknikleriyle en
fazla 56 Kb/s’lik band genişliği sağlar. xDSL teknolojileriyle 25
Mb/s’lik bant genişliğine ulaşmaktadır.

<figure>
<img src="images/ikitellibakirkablo" id="fig:iki_telli_bakir_kablo"
style="width:8cm;height:6cm" alt="İki telli Bakir Kablo" />
<figcaption aria-hidden="true">İki telli Bakir Kablo</figcaption>
</figure>

## KOAKSİYEL (COAXIAL) KABLO

Genellikle elektriksel gürültünün yoğun olduğu şartlarda
kullanılırdı.Yalıtkan bir tüpün içerisinde giden bir tel ve tüpün dışına
sarılmış kafes şeklinde teller vardır. Yerel ağlarda (LAN) 180m’de(max)
10M b/s bant genişliği sağlar. Bu kullanımı 10 Base 2 olarak bilinir.
Daha sonra 500 m mesafede çalıştırılacak hale getirilir. 10 Base 2
ismiyle standartlaştırılmıştır. 50 ohm’luk direnç değeri vardır. BNC
tarzında konnektörler kullanılır. Günümüzde LAN’da hiç
kullanılmamaktadır. Sebebi hem 10 Mb/s hızının çok düşük olması, hem de
UTP kablolar kadar ekonomik ve işlevsel olmamasıdır. Bilgisayar
ağlarında doğrusal (bus) topolojilerde kullanılmıştır.

<figure>
<img src="images/400px-RG-59" id="fig:kooksiyel_kablo" style="width:8cm"
alt="Koaksiyel Kablo" />
<figcaption aria-hidden="true">Koaksiyel Kablo</figcaption>
</figure>

## BÜKÜMLÜ ÇİFT KABLO

İçerisinde 4 çift bakır kablo bulunur.Kabloların birbirleri üzerindeki
direnç elektromanyetik etkisini azaltmak için ikişerli olarak sarılı
durumundadırlar. Örneğin: UTP,CAT5,Ethernet Kablosu

<figure>
<img src="images/bukumlukablo" id="fig:Bukumlu_cift_kablo"
style="width:6cm" alt="Bükümlü çift kablodan bir kesit" />
<figcaption aria-hidden="true">Bükümlü çift kablodan bir
kesit</figcaption>
</figure>

### UTP (UNSHILDED TWISTED PAIR) Korumasız Bükümlü Çift

8 iletkenin her biri ince bir yalıtkan ile kaplanmıştır. En dışında
tamamını kaplayan bir yalıtkan vardır.

### STP(SHİLDED TWİSTED PAİR)

Her çiftin altında koruma (topraklama ) vardır.

### FTP(FOILED TWISTED PAİR )

4 çiftin tamamının etrafında folyo koruma vardır.

### S/FTP 

İkisinin de özelliğini taşımaktadır.

## FREKANSLARINA GÖRE BÜKÜMLÜ ÇİFT KABLO

<figure>
<img src="images/Bolum03_BukumluKablolar.png"
id="fig:Bolum03_BukumluKablolar" style="width:17cm"
alt="Bükümlü çift kablo kategorileri.https://telecom.samm.com/history-of-ethernet-lan-cables-categories" />
<figcaption aria-hidden="true">Bükümlü çift kablo
kategorileri.https://telecom.samm.com/history-of-ethernet-lan-cables-categories</figcaption>
</figure>

**KABLO KATEGORİLERİ**  
**CAT1-CAT3**  
Telefon hatlarında bulunur.  
**CAT5**  
En yaygın kullanılan ağ kablosudur. Azami 100m mesafe ve 10Mb/s
destekler.  
**CAT6**  
100 m mesafede 1G b/s destekler.  
*10 BASE T* Ethernet(Eth)  
*100 BASE T* Fast Ethernet(Fa,Fe)  
*1000 BASE T* Gigabit Ethernet(G,GE)  
Bükümlü çift CAT5 VE CAT6 Kabloları sonlandırmak için RJ-45 adı verilen
konnektörler kullanılır. Bu kablolar iki farklı iki şekilde
sonlandırılabilir.**568-A,568-B**  
Kablonun iki ucunun aynı standartlarla sonlandırılmasına **düz (Straight
kablo)** denir. İki ucunda iki farklı standartta sonlandırılma yapılırsa
**çapraz(cross-over)kablo** adı verilir.

## ÇAPRAZ VE DÜZ KABLO

Düz kablo, bir bilgisayarı yönlendirici gibi bir ağ hub’ına bağlamak
için yerel alan ağlarında kullanılan bir tür bükümlü çift kablodur. Bu
tür kablolara bazen yama kablosu da denir ve bir veya daha fazla
bilgisayarın kablosuz bir sinyal yoluyla bir yönlendiriciye eriştiği
kablosuz bağlantılara bir alternatiftir. Aynı türden iki cihazı bağlamak
için genellikle bir çapraz kablo kullanılır. Düz kablo ve çapraz kablo
tasarımları aynı standartların ve kuralların çoğunu kullanır.

<figure>
<img src="images/caprazduzz" id="fig:caprazduz_kablo" style="width:8cm"
alt="kablolar" />
<figcaption aria-hidden="true">kablolar</figcaption>
</figure>

Yeni ağ cihazlarının tamamı MDI/MDIX adı verilen teknoloji sayesinde
karşıdaki cihazın ne tarz bir cihaz olduğunu anlar ve hangi iletkenin ne
amaçla kullanılacağını buna göre düzenler. Diğerleri enerji göndermek
için kullanılır.

<figure>
<img src="images/ethcable" id="fig:caprazduz_kablo_ornek_gosterim"
style="width:10cm" alt="kablolar-örnek" />
<figcaption aria-hidden="true">kablolar-örnek</figcaption>
</figure>

# FİBER OPTİK KABLOLAR

Fiber optik kablolar, veri göndermek için ışık sinyallerini
kullanmaktadır.Bu kablolar elektrik kablolarına benzer. Ancak elektrik
kablolarından farklı olarak ışığı taşımak için kullanılan minimum bir
adet fiber optik içeren bir kablo çeşididir.  
Fiber optik kablolar çeşitli özelliklere ve avantajlara sahiptirler.
Fiber optik kablonun farklı alanlarda bu kadar sık tercih edilmesinin
nedenleri kabloların bulundurduğu özellikler ve sunduğu bu
avantajlardır.  

<figure>
<img src="images/fiberoptik" id="fig:fiberoptikkablo" style="width:8cm"
alt="fiberkablo" />
<figcaption aria-hidden="true">fiberkablo</figcaption>
</figure>

**Fiber Optik Avantajları**  

-   Elektrik parazitlerinden etkilenmez.

-   Sıcaklık değişimleri ve neme karşı dayanıklıdır.

-   Metalik kablolardan daha hafif ve daha küçüktürler.

-   Sinyal kaybı yok denecek kadar azdır ve sinyal güçlendirici
    ihtiyacını azaltır.

-   Sıcaklık değişimleri, su baskınları, şiddetli hava ve nem gibi
    çevresel parametrelere karşı dayanıklıdır.

Bu kablolarda iletim için ışığın yansımasını kullanılır. Böylelikle bu
kablolar çok daha uzun mesafelere veri iletimi yapılabilirler.
Elektromanyetik enerji sızması meydana gelmediği için bilgi güvenliği
sağlanmış olur. Bu kablolar ile bilginin ekonomik, verimli ve hızlı bir
şekilde ulaştırılması sağlanır.

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
