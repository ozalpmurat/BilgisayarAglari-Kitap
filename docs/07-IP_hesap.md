# İnternet'in Protokolü: IP

Bu bölümdeki içeriği anlattığım bir video var. Alt ağlara bölme konusuna kadar anlatmıştım. İsteyenler videodan da faydalanabilir: [https://www.youtube.com/embed/e9-lU0aXz1g](https://www.youtube.com/embed/e9-lU0aXz1g)
![type:video](https://www.youtube.com/embed/e9-lU0aXz1g)

## Genel Bilgiler

![a](images/B07-IP_Version.png){width="300"}

IPv4 adresleri tükendiği için, artık IPv6 adresleri dağıtılmaktadır. Uzunca bir süre daha ikisini birlikte kullanmak zorundayız.

IPv4 adresleme sisteminde $2^{32}$ IP adresi kullanılabilirken, IPv6 adreslemesinde $2^{128}$ adet IP adresi kullanılabilmektedir. Aşağıda bu iki sayı açık olarak yazılmıştır:

- **IPv4 adres sayısı**: $4.294.967.296$ (yaklaşık 4,3 milyar)
- **IPv6 adres sayısı**: $340.282.366.920.938.463.463.374.607.431.768.211.456$

**Bu ders içerisinde IP ifadesi her kullanıldığında, IPv4 anlaşılmalıdır.** Bu ders açısından ikisi arasındaki en önemli fark; birisinin 32, diğerinin ise 128 bit olmasıdır. IP hesaplamaları tamamen aynıdır. Hesap mantığını anlamak için v4 hesapları -*kısa olduğu için*- daha iyi olacaktır. Sonrasında aynı hesapları v6'da da yapabilirsiniz.

### IANA: IP Dağıtan Kuruluş

<https://www.iana.org/> web sitesinde faaliyetleri hakkında bilgi alınabilir.

![IANA](images/B07-IANA1.png)  
*IANA tarafından yetkilendirilen bölgesel internet kayıtçıları (RIR)*

IANA, IP adreslerini /8 şeklinde RIR'lara dağıttı.
![/8 IP adresleri](images/B07-IANA2.png)  
*Görsel kaynağı: <https://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xhtml>*

IANA elindeki tüm IPv4 adresleri 2011'de bitti.
![IPv4 bitmesi](images/B07-IPv4-bitmesi.png)  
*Görsel kaynağı: <https://en.wikipedia.org/wiki/IPv4_address_exhaustion>*

### IP Sınıfları

IP'nin ilk tasarlandığı sıralarda ortaya çıkmış bir kavramdır.
Kurumlarda IP adresleri tahsis edilirken ihtiyaca göre optimal sayıda
IP  adresi verebilmek için tasarlanmıştır. En büyük IP sınıfı A sınıfı olanlar, en küçük IP sınıfı da C sınıfı olanlardır.

!!! info "Güncel bilgi"
    Günümüzde IP sınıfları bu anlamın yanında, ağın büyüklüğünü ifade etmek için kullanılmaktadır.

![IP Sınıfları](images/B07-IP_Sinif1.png)  
*Görsel kaynağı: <https://medium.com/networks-security/tricks-to-remember-five-classes-of-ipv4-484c191678fb>*

![IP sınıfları](images/B07-IP_Sinif2.png){width="700"}  
*Görsel kaynağı: <https://www.routerfreak.com/definitive-guide-ip-address-classes/>*

**Örnekler:**

- **BŞEÜ**: `79.123.224.15` A sınıfı olduğu için, bu IP'nin dahil olduğu ağda $2^{24}$ (~16M) tane IP olabilir.
- **ODTÜ**: `144.122.145.153` IP adresi B sınıfıdır. Bu IP'nin dahil olduğu ağda, $2^{16}$ (~65K) tane IP olabilir.
- **SAÜ**: `193.140.253.240` IP adresi C sınıfıdır. Bu IP'nin dahil olduğu ağda $2^8$ (256) tane IP olabilir.

!!! warn "IP sınıflarının günümüzdeki anlamı"
    İlk başta IP adresleri dağıtılırken kolaylık olsun diye tasarlanmış olan IP sınıfları günümüzde bu anlamda kullanılmamaktadır. BŞEÜ'de 16M IP adresi yoktur. SAÜ'de de C sınıfından (256) daha fazla IP adresi vardır. Örneklerden sadece ODTÜ'nünki gerçekten B sınıfı olarak (~65K) tahsis edilmiştir.

## Rezerve IP Adresleri

IETF ve IANA tarafından, özel amaçlar için kullanılmak üzere farklı adres blokları ayrılmıştır. En temel olarak; ==özel== ve ==genel== IP adresleri şeklinde bir ayrım yapılmıştır. İç ağda özel IP adresine sahip olan bilgisayarlar, İnternet'e çıkarken genel IP adresi kullanırlar.

Bunların dışında da farklı amaçlarla ayrılmış adres aralıkları bulunmaktadır. Aşağıda ayrılmış olan bu adresler kısaca açıklanmıştır.

### Özel ve genel IP Adresleri (Private & public IP Blocks)

Özel (private) IP adresleri, İnternet'te kullanılmayan IP adresleridir. Bu nedenle *sanal IP adresi* de denir. İnternet üzerinde hiçbir yönlendirici tarafından iletilmezler. Bu adreslerin kullanım amacı, test uygulamaları ve NAT uygulamaları gibi durumlardır. Aşağıdaki tabloda özel IP adres aralıkları verilmiştir. Bunların dışındaki adresler, genel (public) IP adresidir.

| CIDR gösterimi | Adres aralığı                 | IP sayısı |
| -------------- | ----------------------------- | --------- |
| /8            | 10.0.0.0 - 10.255.255.255     | 16.777.216|
| /12            | 172.16.0.0 - 172.31.255.255   |  1.048.576|
| /16            | 192.168.0.0 - 192.168.255.255 |     65.536|

### Diğer ayrılmış IP adres aralıkları

| **Adres bloğu** | **Adres aralığı**             | **Adres sayısı** | **Açıklama**           |
| --------------- | ----------------------------- | ---------------- | ---------------------- |
| 0.0.0.0/8       | 0.0.0.0 - 0.255.255.255       | 16.777.216         | Ağın kendisi (“Bu” ağ) |
| 127.0.0.0/8     | 127.0.0.0 - 127.255.255.255   | 16.777.216         | Loopback (localhost)   |
| 169.254.0.0/16  | 169.254.0.0 - 169.254.255.255 | 65.536            | Link-local             |

**Loopback adresi**: Bilgisayarın kendisini temsil eder. Paketler bilgisayardan cihazdan asla ayrılmazlar. Bilgisayarın kendi üzerinde çalıştırılan uygulamalar için kullanılır. Test amacıyla da kullanılabilir.

IPv4 için, `127.0.0.0/8` A sınıfı adres bloğunun tamamı loopback için ayrılmıştır. IPv6'da ise bu amaçla sadece `::1` adresi kullanılır.

**Link-local adresler**: DHCP vasıtasıyla otomatik IP almak üzere yapılandırılmış ağlarda, bir IP adresi alamayan bilgisayarlar bu bloktan kendi kendine bir IP adresi verirler. Eğer bir bilgisayarda `169.254.X.X` şeklinde bir IP adresi görürseniz, "*bu bilgisayar IP alamamış*" denir. Eğer DHCP sisteminde bir sorun olursa, link-local adresler sayesinde aynı ağdaki (LAN) bilgisayarlar kendileri arasında haberleşebilirler.

### NAT (Network Address Translation)

![NAT](images/B07-NAT_Tablosu.png)  
*Görsel kaynağı: <https://onlinecomputertips.com/support-categories/networking/601-network-address-translation-nat/>*

Bir IP adresinin, diğer ağlara giderken farklı bir adrese dönüştürülmesi işlemidir. Genellikle, kurumlarda tahsis edilen az sayıda *-hatta tek-* public IP adresini, çok sayıda bilgisayarda kullanabilmek için uygulanır. IPv4'ün beklenenden erken bitmesine karşılık çözüm olarak kullanılmaktadır. IPv6'ya geçildiğinde bu işlemlere gerek kalmayacaktır.

**NAT Tablosu**: NAT işlemi yapılırken hangi IP adresini kimin ne zaman kullandığını tutar. Bu sayede ilgili IP'nin yaptığı isteklere gelen cevaplar doğru şekilde iletilebilir.

!!! note "Bahçe terliği benzetmesi"
    Yalnızca 1 public IP adresi olan bir kurumun ağında çok sayıda bilgisayar internet'e çıkıyor olsun. Bu örneği, evin arka bahçe kapısında tek terlik bulunmasına benzetebiliriz. Bahçede işi olan kişi terliği giyer, işini halledince terliği çıkarıp eve girer. Sonra başkası aynı terliği kullanır. Bahçeyi gören komşular hep aynı terlikleri görürler ama o terlikleri kullanan kişi değişmiş olur.

## IP Adresi ve Hesaplamaları

32 bit uzunluğa sahip olan IP adresi 2 temel bileşene sahiptir:

1. Ağ tanımlayıcı
2. Host tanımlayıcı

![IP bileşenleri](images/B07-IP2.png)  
*IP bileşenleri*

!!! note "Host"
    Bir ağ içerisinde IP atanabilen ve kendisinin ağa bağlanma ihtiyacı olan cihazların tümüne **host** denir. Örneğin; bilgisayar, yönlendirici, güvenlik duvarı, akıllı saat, cep telefonu, IoT cihazları, vb.

IP adresleri 32 bitin sekizerli olarak gruplandırılması ve onluk (decimal) olarak gösterilmesi şeklindedir. Bu 8 bitlik grupların her birine **oktet** denir. Her oktet birbirinden nokta ile ayrılır.

![IP adresi](images/B07-IP1.png){width="500"}  
*Görsel kaynağı: <https://www.cloudns.net/blog/what-is-ipv4-everything-you-need-to-know/>*

!!! note "Kaç bitle kaç adres?"
    $N$ tane bit kullanılarak yapılacak bir adresleme sisteminde, $2^N$ tane adres kullanılabilir.

![a](images/B07-4bit_ile_16_adres.png)  
*4 bit ile 2^4=16 tane farklı adres kullanılabilir*

### Host ve Network Kısımlarının Ayrıştırılması

Bir IP adresinde soldan itibaren ilk X tane bit ağ tanımlayıcısıdır. Geri kalan Y tane bit te host tanımlayıcısıdır. Bu durumda $X+Y=32$ olur.

![a](images/B07_IP_Adresi_Host_ve_Net_ID.png)  
*Görsel kaynağı: <https://sherihansliit.blogspot.com/2012/12/understanding-ip-address-configuration.html/>*

!!! question "Müteahhit problemi"
    Metin adında bir müteahhit, bir arazi üzerinde konut projesi yapacak. Metin'e şu şartlarla izin veriliyor:

    1. Toplam 16 tane adres numarası kullanabilir. Bu numaraları bina numarası veya daire numarası olarak kullanabilir.
    2. Her binada zemin kat ve çatı katında kimse oturamaz.

    Metin, kaç daireli kaç bina yapmalı ki; hem kârı çok azalmasın hem de müşteriler mutsuz olmasın?
    ![a](images/B07-Müteahhit.png)
    *Müteahhit problemi. 16 daireli tek bina mı, 8 daireli 2 bina mı, ya da?*

!!! note
    Ağlardaki bilgisayar sayıları (kullanılabilecek IP sayıları) belirlenirken maksimum kapasite 2'nin kuvveti $(2^n)$ alınarak belirlenir.

**ÖRNEK :** Bir şirketin iki farklı şubesinde 120 ve 280 adet bilgisayar
kullanılmaktadır. Bu şirketler için optimal ağ büyüklüklerini hesaplayınız.

![a](images/B07-2nin_Kuvvetleri.png)  

!!! note "IP sayısı ve host sayısı"
    Host tanımlayıcısı kısmındaki bit sayısı ile elde edilebilecek adres sayısı, o ağda kullanılabilecek IP adresi sayısıdır. Her ağın ilk IP adresi `ağ adresi` ve son IP adresi de `yayın adresi` olarak kullanıldığından, her ağda kullanılabilecek **host sayısı IP sayısından 2 eksiktir**.

- Host bitleri : $N$ tane
- Ağdaki IP adresi : $2^N$ tane
- Ağda kullanılabilecek host sayısı $2^N-2$

**ÖRNEK :** 10.9.8.0 IP adresinin 30. bitten sonra bölündüğünü varsayalım. Bu ağda kullanılabilecek bütün IP adreslerini, kullanım amacına göre yazalım.

![a](images/B07-Ornek-30bit.png)  

IP sayısı = $2^2=4$ tane  
Host sayısı = $2^2-2=2$ tane

1. IP adresi 10.9.8.0 : `Ağ adresi`
2. IP adresi 10.9.8.1 : `Hostlar için kullanılabilir`
3. IP adresi 10.9.8.2 : `Hostlar için kullanılabilir`
4. IP adresi 10.9.8.3 : `Yayın adresi`

![/30 network kullanım örneği](images/B07-Bolu30_network.png)  
*Örnek /30 ağ kullanım şekli: Dummy Network*  
*Görsel kaynağı: <https://www.computernetworkingnotes.com/ccna-study-guide/contiguous-and-discontiguous-networks-explained.html>*

### Ağ hesapları neden yapılıyor?

![Ag hesapları amacı iş akışı](images/B07-AgHesaplariAmaci.png)  

### Ağ Maskesi (Netmask)

"Alt ağ maskesi" de denir Ağın kaçıncı bitten bölündüğü belirtir. IP adresi gibi 32 bitten oluşur. İkilik sistemde soldan itibaren `1`'lerle başlar, sonra `0`'larla devam eder. 1'den 0'a geçilen nokta, ağın bölündüğü kısımdır. Gündelik hayatta kolay olması için, onluk sistemde kullanılır.

Ağ maskesinin temel görevleri:

1. IP adresinde, `network ID` ile `host ID` kısımlarının hangi bitlerden ayrıldığını belirlemek.
1. Ağın büyüklüğünü belirtmek
1. Ağın nerede başladığı (ağ adresi) hesabında kullanmak

**Örnek bazı maskeler:**
![Örnek maskeler](images/B07-Ornek_Maskeler.png){width="600"}  

![Maskeleme](images/B07-maskeleme.png){width="400"}  
*Görsel kaynağı: <https://www.bestpickreports.com/blog/post/6-painting-hacks-with-tape/>*

!!! note
    IP adresi ile beraber, ağ maskesinin kullanılması zorunludur.

![Ağ büyüklüğü](images/B07-maske_ag_boyutu.png)

![Windows IP yapılandırması](images/B07-IP_config.png)  
*Windows'ta iki farklı yerden IP yapılandırması yapılabiliyor. Görsel kaynağı: <https://pureinfotech.com/set-static-ip-address-windows-10/>*

![Farklı alt ağ maskelerinin etkisi](images/B07-maske-tablo.png)  
*Görsel kaynağı: <https://www.trance-cat.com/electrical-circuit-calculators/en/subnet-mask-calculator.php>*

### CIDR Notasyonu

Ağ maskesine alternatif olarak CIDR Notasyonu kullanılmaktadır. Bu gösterim şeklinde, IP adresinin sağına `/` işareti konulup kaçıncı bitten sonra bölündüğü bilgisi yazılır.

**Örnekler:**

- `192.168.1.75` IP adresli ve `255.255.255.0` ağ maskesine sahip bir cihazın CIDR notasyonu `192.168.1.75/24` şeklindedir.
- `10.1.0.0` ve `255.0.0.0` ise `10.1.0.0/8` olarak gösterilir.
- `10.9.8.0` ve `255.255.255.128` ise `10.9.8.0/25` şeklinde gösterilir. (`128` ikilik tabanda `10000000` şeklinde gösterildiğinden soldan itibaren 25 tane `1`, 7 tane de `0` vardır.)

### Ağ adresi

Ağ maskesi herhangi bir IP adresi ile ikilik sistemde çarpılırsa (mantıksal `VE` işlemi) çıkan sonuç **ağın adresi**ni verir. Bu sayede, ağın nerede başladığı bulunmuş olur.

![Maskeleme](images/B07-maskeleme2.png)  
*Görsel kaynağı: <https://en.wikipedia.org/wiki/Mask_%28computing%29>*

**Örnek:**  IP adresi `192.168.1.75` olsun. Alt ağ maskesi de `255.255.255.0` olsun. Bu ağın ağ adresini bulalım.

![Ağ adresi bulma](images/B07-Ornek-Ag_Adresi_Bulma.png){width="500"}  

### Ağ adresi ve yayın adresinin pratik hesabı

IP adresinin nereden bölündüğünü biliyorsak; **IP adresinde** bu bitten sonrası `1` yapılırsa, `yayın adresi`ni buluruz. Aynı bitleri `0` yaptığımızda ise `ağ adresi`ni buluruz.

![Kolay hesap](images/B07-Ornek-Kolay_Hesap.png){width="500"}  

### IP hesaplarında formüller ve özet

1. **IP (v4) adresleri $32$ bitten oluşur**. Bu bitler sekizer gruplu (oktet) olarak yazılır ve okunur. Örnek: `10.170.265.44`. IP adresinin her oktetinde 8 bit bulunduğundan, hiç bir oktet 255'ten büyük olamaz. Yani az önce verdiğim IP adresi, bozuk bir IP adresidir.
1. IP adresindeki $32$ bitin soldan itibaren $M$ tanesi ağı tanımlar. geri kalan $N$ tanesi de ($N=32-M$) hostları tanımlar. Bu iki bileşeni birbirinden ayırmanın iki yolu vardır:
    - **CIDR** gösteriminde bölü işareti ( "/" ) kullanılır. örnek: `10.5.0.100/16`
    - **Maske** ile gösteriminde M tane 1, N tane 0 olacak şekilde bitler ifade edilir. Sonra 10'luk sisteme çevrilerek IP adresinin yanına yazılır. Örnek: `10.5.0.100 - 255.255.0.0`
1. Bir **ağda kaç IP** olduğunu bulmak için, bölü işaretinden sonraki bitlerin sayısına bakılır. $N$ tane bit varsa, $2^N$ formülü ile ağdaki IP sayısı hesaplanır.
1. Ağları alt ağlara bölmeye başlamadan önce mutlaka mevcut ağı tanımla. Nerede başlar? Nerede biter? Maskesi nedir? CIDR gösterimi nedir? Bu ağda kaç IP vardır?
1. Bir ağın **alt ağ maskesi**ni bulmak için;
    - IP adresinde, bölü'den önceki bitlerin tamamı `1` yapılır.
    - IP adresinde, bölü'den sonraki bitlerin tamamı `0` yapılır.
    - Sonra 10'luk sisteme çevrilir.
1. Bir ağın **ağ adresi**ni bulmak için;
    - IP adresinde bölü'den sonraki bitlerin tamamı 0 yapılır. Sonra 10'luk sisteme çevrilir.
1. Bir ağın **yayın adresi**ni bulmak için;
    - IP adresinde bölü'den sonraki bitlerin tamamı 1 yapılır. Sonra 10'luk sisteme çevrilir.
1. $/N$ şeklinde verilen bir ağı 2 alt ağa bölersek, yeni ağlar $/(N-1)$ olmuş olur. Yani bölü işareti 1 bit sağa kaymış olur. Örneğin, `/20` şeklinde bir ağı ikiye bölersek iki tane `/21` ağ oluşur. Benzer şekilde, $/N$ şeklindeki bir ağı dörde bölersek, 2 bit kaydırmalıyız. Yani `/20` şeklindeki ağ dörde bölünürse elimizde 4 tane `/22` ağ oluşur.

## Alt Ağlara Bölme

IP adresi ve ağı temsil eden bit sayısı belirli olan bir ağ, birden fazla
küçük ağlara bölünebilir. Alt ağa bölme işlemi alt ağ maskesinde bit
kaydırılarak yapılır. /N şeklindeki bir ağ için; /(N+1) şeklinde 1 bitlik kaydırma yapılırsa, önceki ağ ikiye bölünmüş olur. 2 bit kaydırılırsa, 4'e bölünmüş olur. Bu şekilde $2^n$ tane alt ağ bölme işlemi
yapılabilir.

!!! note "Not:"
    Çözüme geçmeden önce mutlaka bölünmemiş ağın analiz edilmesi gerekir. Başlangıç-bitiş adreslerini ve kaç IP adresi olduğunu belirlemeliyiz.

---

### Örnek-1: İkiye bölme

!!! question "İkiye bölme"
    10.0.0.0/24 ağını iki ayrı ağa bölünüz.  

**ANALİZ**

- Verilen ağ `/24` şeklindedir. Bunu ağ maskesi cinsinden yazmak istersek; 24 tane `1`, 8 tane `0` olur. Yani alt ağ maskesi `255.255.255.0` şeklindedir.
- Bu ağda hostları tanımlamak için 8 bit kullanılmıştır. Demek ki ağda $2^8$=`256` tane IP adresi vardır. İkiye böldüğümüzde `128` IP'lik iki ayrı ağ oluşacaktır.
- Ana ağın başlangıç noktasını belirlemek için ağ adresini bulmalıyız. Bu ağda ağ adresi `10.0.0.0` IP adresidir.
- Ana ağın son IP adresi ise yayın adresidir. Bunu hesaplarsak, `10.0.0.255` buluruz.

![IP adres aralığı](images/B07-IP_adresi_cetveli-24.png)  
*Görsel: IP adres aralığı. Bölünmeden önceki hali*

**ÇÖZÜM**

> - Ana ağın maskesini ikilik sistemde `11111111.11111111.11111111.00000000` şeklinde yazabiliriz.  
> - `24.` bitten bölünmüş olan ağda 1 bit kaydırma yaparsak; `25 tane 1`, `7 tane 0` olacaktır. Bu durumda ana ağı ikiye bölmüş oluruz. Her bir alt ağda $2^7$=`128` tane IP adresi olur.  
> - Ağ bölündükten sonra 1. alt ağın başlangıç adresi (ağ adresi), ana ağın ağ adresi ile aynı olacaktır. Buna göre tabloyu oluşturabiliriz.
>
> |       | Ağ adresi     | Yayın adresi | Ağ maskesi      | IP sayısı | Host sayısı |
> |-------|---------------|--------------|-----------------|-----------|---|
> | 1. ağ | 10.0.0.0/25   | 10.0.0.127   | 255.255.255.128 | 128       | 126 |
> | 2. ağ | 10.0.0.128/25 | 10.0.0.255   | 255.255.255.128 | 128       | 126 |
>
> ![IP adres aralığı](images/B07-IP_adresi_cetveli-25.png)  
> *Görsel: IP adres aralığı. İkiye bölünmüş hali*

---

### Örnek-2: Dörde bölme

!!! question "Dörde bölme"
    10.9.6.200/25 şeklinde verilen bir IP adresi var. Bu IP adresinin bulunduğu ağı, 4 ayrı alt ağa bölünüz.

**ANALİZ**

- **Alt ağ maskesi:** Verilen ağ `/25` şeklindedir. Bunu ağ maskesi cinsinden yazmak istersek; 25 tane `1`, 7 tane `0` olur. Yani alt ağ maskesi `255.255.255.128` şeklindedir. Bunu dörde böldüğümüzde, `/27` şeklinde 4 tane alt ağ oluşacaktır.
- **Ağdaki IP sayısı:** Bu ağda hostları tanımlamak için 7 bit kullanılmıştır. Demek ki ağda $2^7$=`128` tane IP adresi vardır. Dörde böldüğümüzde `32` IP'lik dört ayrı ağ oluşacaktır.
- **Ağ adresi:** Ana ağın başlangıç noktasını belirlemek için, IP adresindeki 25. bitten sonrasını 0 yaparsak "10.9.6.(1<font color='blue'>0000000</font>)~2~" olur. Bunu onluk olarak yazarsak, ağ adresini `10.9.6.128` şeklinde buluruz.
- **Yayın adresi:** Ana ağın son IP adresini hesaplamak için 25. bitten sonrasını 1 yaparsak "10.9.6.(1<font color='blue'>1111111</font>)~2~" olur. Bunu onluk olarak yazarsak, `10.9.6.255` buluruz.

![IP adres aralığı](images/B07-IP_adresi_cetveli-soru2-25.png)  
*Görsel: IP adres aralığı. Bölünmeden önceki hali*

**ÇÖZÜM**

> - `25`. bitten bölünmüş olan ağda `2` bit kaydırma yaparsak; ağı dörde bölmüş oluruz (2^2^=4). Alt ağların maskesinde; 27 tane 1, 5 tane 0 olacaktır. Bu durumda ana ağı dörde bölmüş oluruz. Her bir alt ağda 32 tane IP adresi olur.
> - Ağ bölündükten sonra 1. alt ağın başlangıç adresi (ağ adresi), ana ağın ağ adresi ile aynı olacaktır. Buna göre tabloyu oluşturabiliriz.
> - İlk ağın ilk IP adresinden itibaren, `32` ekleyerek devam edersek, bütün alt ağların ağ adreslerini bulabiliriz.

> |       | Ağ adresi     | Yayın adresi | Ağ maskesi      | IP sayısı | Host sayısı |
> |-------|---------------|--------------|-----------------|-----------|---|
> | 1. ağ | 10.9.6.128/27 | 10.9.6.159   | 255.255.255.224 | 32       | 30 |
> | 2. ağ | 10.9.6.160/27 | 10.9.6.191   | 255.255.255.224 | 32       | 30 |
> | 3. ağ | 10.9.6.192/27 | 10.9.6.223   | 255.255.255.224 | 32       | 30 |
> | 4. ağ | 10.9.6.224/27 | 10.9.6.255   | 255.255.255.224 | 32       | 30 |
>
> ![IP adres aralığı](images/B07-IP_adresi_cetveli-soru2-27.png)  
> *Görsel: IP adres aralığı. Bölündükten sonra*

---

### Örnek-3: Büyük ağları bölme

!!! question "Büyük ağları bölme"
    192.168.1.100/16 ağını 8 alt ağa bölün. İlk ve son alt ağlar için şunları hesaplayın:  
    - Ağ adresi  
    - Yayın adresi
    - Alt ağ maskesi

**ANALİZ**

- **Alt ağ maskesi:** Verilen ağ `/16` şeklindedir. Bunu ağ maskesi cinsinden yazmak istersek; 16 tane `1`, 16 tane `0` olur. Yani alt ağ maskesi `255.255.0.0` şeklindedir. Bunu sekize böldüğümüzde, `/19` şeklinde 8 tane alt ağ oluşacaktır.
- **Ağdaki IP sayısı:** Bu ağda hostları tanımlamak için 16 bit kullanılmıştır. Demek ki ağda $2^16$=`65536` tane IP adresi vardır. Sekize böldüğümüzde `8192` IP'lik sekiz ayrı ağ oluşacaktır.
- **Ağ adresi:** Ana ağın başlangıç noktasını belirlemek için, IP adresindeki 16. bitten sonrasını 0 yaparsak `192.168.0.0` olur.
- **Yayın adresi:** Ana ağın son IP adresini hesaplamak için 16. bitten sonrasını 1 yaparsak `192.168.255.255` olur.

![IP adres aralığı](images/B07-IP_adresi_cetveli-soru3-16.png)  
*Görsel: IP adres aralığı. Bölünmeden önceki hali*

!!! note "Not:"
    Küçük ağlarda alt ağları hesaplamak için, örneğin 32'şer ilerleyerek kolayca hesaplayabiliyoruz. Ancak büyük ağlarda 8192 ekleyerek gitmek çok kolay olmayacak. Bu örneğin öncekilerden farklı yanı budur. Aşağıdaki çözüme dikkat ediniz.

**ÇÖZÜM**

> - `16`. bitten bölünmüş olan ağda `3` bit kaydırma yaparsak; ağı sekize bölmüş oluruz (2^3^=8). Alt ağların maskesinde; 19 tane 1, 13 tane 0 olacaktır. Bu durumda ana ağı sekize bölmüş oluruz. Her bir alt ağda 8192 tane (2^13^) IP adresi olur.
> - Ağ bölündükten sonra **1. alt ağın başlangıç adresi** (ağ adresi), ana ağın ağ adresi ile aynı olacaktır: `192.168.0.0`
> - **Son alt ağın yayın adresi** de ana ağın yayın adresi ile aynı olacaktır: `192.168.255.255`
> - Birinci alt ağın yayın adresini bulmak için, bu alt ağ içindeki herhangi bir IP adresini örnek olarak alıp, 19. bitten sonrasını 1 yapabiliriz. Elimizde zaten bu alt ağdan bir IP adresi var. 192.168.0.0 IP adresi hem bölünmemiş ana ağın, hem de bölündükten sonraki ilk alt ağın bir parçasıdır. Eğer /16 olarak düşünülürse, ana ağın bir parçası olarak hesaplanabilir. /19 olarak düşündüğümüzde ise 8192 IP adresine sahip olan 1. alt ağa ait bir IP adresidir.  192.168.0.0 IP adresinin 19. bitten sonrasını 1 yaparsak **birinci alt ağın yayın adresi**ni buluruz:  
192.168.(000<font color="blue">11111.11111111</font>)~2~ = `192.168.31.255`
> - Üstteki maddeye benzer şekilde; son alt ağdan  1 IP adresini alıp bunun ağ adresini (/19 olarak) hesaplarsak, son alt ağın ağ adresini bulmuş oluruz. Bu nedenle son alt ağa ait olan 192.168.255.255 IP adresinin 19. bitten sonrasını 0 yaparsak **son alt ağın ağ adresi**ni buluruz:  
192.168.(111<font color="blue">00000.00000000</font>)~2~ = `192.168.224.0`
> - Yeni oluşan küçük ağların alt ağ maskesini hesaplamak için /19 olan ifadeyi ikilik sistemde yazmalıyız:
(11111111.11111111.111<font color="blue">00000.00000000</font>)~2~ = `255.255.224.0`

> ![IP adres aralığı](images/B07-IP_adresi_cetveli-soru3-19.png)  
> *Görsel: IP adres aralığı. Bölündükten sonra*

> Görsel üzerinde siyah ile işaretlenen IP adresleri zaten ilk analizde bulunmuştu. Mavi ile işaretlenenler, soruda istenen ve çözümde bulduğumuz IP adresleri. Yeşil ile işaretlenenler soruda istenmiyordu ama birkaç tanesini göstermek istedim şekil üzerinde de. Soruda istenen verileri yeniden tablo halinde yazalım:

> |       | Ağ adresi        | Yayın adresi    | Ağ maskesi    |
> |-------|------------------|-----------------|---------------|
> | 1. ağ | 192.168.0.0/19   | 192.168.31.255  | 255.255.224.0 |
> | 8. ağ | 192.168.224.0/19 | 192.168.255.255 | 255.255.224.0 |

---

### Örnek-4: Farklı büyüklüklerde alt ağlar

!!! question "Farklı büyüklüklerde alt ağlar"
    Bir şirkete 192.168.100.0/24 şeklinde IP aralığı tahsis edilmiştir. Şekilde sistem yöneticisi ağdaki aşırı yayın trafiğinin sorun çıkardığını düşünerek ağı alt ağlara bölmek istiyor. Birimlerin PC sayısı aşağıdaki gibidir.

    Teknik birim=70, Pazarlama=40, Muhasebe=20, İdari birim=25

**ANALİZ**

- **Alt ağ maskesi:** Verilen ağ `/14` şeklindedir. Bunu ağ maskesi cinsinden yazmak istersek; `255.255.0.0` şeklindedir.
- **Ağdaki IP sayısı:** Ağda $2^8$=`256` tane IP adresi vardır.
- **Ağ adresi:** IP adresindeki 24. bitten sonrasını 0 yaparsak `192.168.100.0/24` olur.
- **Yayın adresi:** Ana ağın son IP adresini hesaplamak için 16. bitten sonrasını 1 yaparsak `192.168.100.255` olur.
- Her birim için 2^n^ formülüne göre optimum ağ büyüklüklerini yazalım:  
    Teknik: 2^7^ = 128  
    Pazarlama : 2^6^ = 64  
    Muhasebe: 2^5^ = 32  
    İdari: 2^5^ = 32
- Ağları alt ağlara bölerken iki eşit parçaya bölündüğünü biliyoruz. Burada ise farklı boyutlarda ağ ihtiyacı var. Normalde bu tarz bir uygulama pek olmamaktadır. Ancak verilen soru özellikle hazırlanmıştır. Önce ağı ikiye bölerek 2x128 ağ yapılabilir. Sonra bu alt ağlardan birisi yeniden ikiye bölünerek 128+64+64 şeklinde 3 ağ yapılabilir. BU 64'lerden birisi bir daha ikiye bölünürse 128+64+32+32 şeklinde 4 tane alt ağ elde edebiliriz. Bu da tam örneğe uygun hale gelmektedir.

![Bölündükten sonraki durum](images/B07-IP_adresi_cetveli-soru4.png)  
*Görsel: bölünme sonrası durum*

**ÇÖZÜM**
> Çözümü size bırakıyorum[.](https://gist.github.com/ozalpmurat/866b27e515129c098757d9fb0954f5f7)
---

### Çalışma soruları

1. /17 şeklinde gösterilen ağın maskesi nedir?
1. IP adresi 10.10.0.0 ve alt ağ maskesi 255.255.0.0 olan bir bilgisayarın bulunduğu ağda kaç IP olabilir?
1. 255.255.255.224 şeklindeki alt ağ maskesi olan bir ağda kaç host olabilir?
1. 192.168.1.0/8 ağını ikiye bölün.
1. 172.16.172.220/26 ağını ikiye bölün.
1. 10.0.0.0/8 ağını 16'ya bölün. Sadece ilk alt ağ için ağ adresi, yayın adresi, alt ağ maskesi değerlerini hesaplayın.
1. 10.0.0.0/29 ağını ikiye bölün.
1. 10.50.100.200/25 şeklinde IP adresi tahsis edilmiş bir bilgisayarın ağ adresi ve yayın adresi nedir?

## Ağ Geçidi IP Adresleri

![Ağ geçidi](images/B07-Ag_gecidi_01.png)  
*Görsel: Windows bilgisayarda ağ geçidi IP adresi*

Aynı ağdaki bilgisayarlar, kendi aralarında 2. katmanda MAC adresleri ile haberleşirler. Farklı bir ağdaki IP adresi ile iletişim kurmak istediklerinde, ilk gitmeleri gereken yer, kendi ağ geçidi olarak bildikleri IP adresidir. Ağ geçidi, bir ağdaki bilgisayarların diğer ağlara gidebilmesi için geçmeleri gereken kapıya denir.

Genellikle her ağda yalnızca 1 tane ağ geçidi olur. Bu da IP adresleri ile beraber bilgisayarlara otomatik olarak gönderilir. Özel durumlarda ağlarda birden fazla ağ geçidi olabilir. Bu tarz durumlarda hangi hedeflere giderken hangi ağ geçidinden geçmesi gerektiğini belirten "yönlendirme tablosu" kullanılır.

Her ağ için; ilk IP adresinin ağ adresi, son IP adresinin yayın adresi olduğunu
biliyoruz. Kural olmamakla birlikte, genel teamüllere göre, ağ adresinden
sonraki ilk IP adresi (kullanılabilecek ilk host adresi) ağ geçidi olarak
belirlenir.

!!! note "Ağ geçidi IP adresi"
    Ağ geçidi IP adresi, her bir ağın doğrudan bağlı olduğu yönlendirici arayüzünde (interface, ağ arabirimi, port, ethernet kartı, NIC[*Network Interface Card*]) tanımlı olan IP adresi olmak zorundadır.

Yukarıdaki örnek için ağ geçidi bilgileri aşağıdaki görselde verilmiştir. Her ağın kullanılabilir ilk host adresi "ağ geçidi" IP adresi olarak yönlendiricinin ilgili bacağına (NIC) verilmiştir. Yönlendiricinin WAN bacağı ise internet bağlantısı olarak kullanılmaktadır. Bu bacakta 256 IP adresi tanımlıdır.
![Ağ geçidi örneği](images/B07-Ag_gecidi_03.png)  
*Görsel: Önceki örneğin ağ bilgileri*

Aşağıdaki görselde, Cisco yönlendiricilerde bir bacağa (NIC, Ethernet kartı, port) IP adresinin nasıl verildiği görülmektedir.  Görselde verilen yönlendiricide iki NIC vardır: `FastEthernet 0/1` ve `FastEthernet 1/1` şeklinde. Bu iki interface'e IP adresi verilebilmesi için yapılması gereken konfig te aynı görselin üst kısmındaki metinlerde verilmiştir.  
![Ağ geçidi örneği](images/B07-Ag_gecidi_04.png)  
*Görsel kaynağı: <https://www.flackbox.com/cisco-basic-router-switch-configuration>*

Aşağıdaki görselde kurumlarda güncel durumda kullanılan standart bir topoloji verilmiştir. Artık bulut tabanlı çözümlere geçilmeye başladığı için birçok kurumda fiziksel sunucu bile bulunmamaktadır. Ancak kendi veri merkezi olan ve sunucusu olan kurumlar bu tarz bir yapı kullanmaktadır. Bu görsele ilaveten istenirse; IPS, WAF, traffic shaper, NAC, vb. birçok sistem eklenebilir. Ancak sade olması için minimal çizim yapılmıştır. Görselde birkaç noktayı vurgulayabiliriz:

1. Güvenlik duvarının 3 bacağı (*interface, NIC, port, Ethernet kartı. Hepsi aynı anlamda.*) var: LAN, WAN ve DMZ. İstenirse bu bölgelerin sayısı arttırılabilir.
1. Hem LAN'lar hem de VLAN'lar kullanılıyor.
1. VLAN'lar omurga anahtarında oluşturulmuş. Her VLAN'ın bir interface'i (sanal NIC) var. Bu interface'lere IP adresi verilmiş. Her VLAN'daki her bilgisayarın da ağ geçidi bu IP adresleri olarak kullanılıyor.
1. Herhangi bir VLAN veya LAN'da bir PC IP almak istediğinde, "Ortamda DHCP sunucusu var mı?" (`discovery`) diye bir broadcast mesajı gönderiyor. Bu mesaj sadece kendi ağındaki IP'lere gidiyor. Bu IP'lere kendi ağ geçidi de dahil. Ağ geçidi olan cihaz da (*bu topoloji için omurga anahtarı*) bu mesajı alıp DHCP sunucuya aktarıyor. Gelen cevabı (`offer`) ilgili PC'ye geri gönderiyor. Bir IP alma isteğinin, başka bir ağdaki sunucuya iletilmesi işlemine ==DHCP relay== denir. DHCP relay işlemini; anahtar, yönlendirici ya da ağdaki herhangi bir PC yapabilir.
1. Sunucu bölgesinde otomatik IP kullanılmayabilir. Elle yönetmek çok zor olmaz, hatta "elle IP vermek" hataları da azaltabilir. Ancak kullanıcı bilgisayarlarında her zaman otomatik IP kullanırız.
1. DHCP sunucusuna bir "IP isteği" mesajı geldiğinde, sunucu bu mesaja 4 temel veri içeren bir cevap döndürür: IP adresi, alt ağ maskesi, ağ geçidi, DNS sunucu IP adresi. İstenirse bunlara ilave başka veriler de gönderilebilir: NTP server, TFTP server, vb.
1. Evlerde kullandığımız xDSL modemler buradaki bir çok işi tek başına yapıyor: Protokol çevirme, yönlendirme, NAT, güvenlik duvarı, switching, Wifi Access point, traffic shaping, vb.

![Güncel ağ topolojisi](images/B07-Ag_gecidi_ve_GenelTopoloji.png)  
*Kurumlarda kullanılan güncel topoloji*

Aşağıdaki görselde Cisco cihazlarda yapılan bir DHCP-relay işlemi gösterilmiştir. Görseldeki 50.0.0.10 IP adresi, o network'ün DHCP server IP adresidir.

![Cisco DHCP relay](images/B07-Ag_gecidi_DHCP_relay.png)  
*Görsel: Cisco DHCP relay işlemi*

## İki Bilgisayar Aynı Ağda Mı?

!!! note "İki bilgisayar aynı ağda mı?"
    A bilgisayarı; iletişim kurmak istediği B bilgisayarı ile aynı ağda olup olmadığını anlamak için, B nin IP adresiyle kendi ağ maskesini çarpar. Çıkan sonucu kendi ağ adresiyle karşılaştırır.

### Örnek-5

!!! question "Örnek-5"
    10.0.0.127/24 ve 10.0.0.128/24 IP adreslerinin, birbirleri ile haberleşebilmek için ağ geçidine ihtiyaçları var mıdır?

A'nın B ile haberleşmesi :
  ------------------ --- ------------ -- --
  B'nin IP adresi        10.0.0.128
  A'nın ağ maskesi   x   10.0.0.128
                         10.0.0.0
  ------------------ --- ------------ -- --

Çıkan sonuç A'nın ağ adresiyle aynı olduğundan haberleşirler.

A'nın C ile haberleşmesi :

  ------------------ --- ------------ -- --
  C'nin IP adresi        10.0.0.254
  A'nın ağ maskesi   x   10.0.0.128
                         10.0.0.128
  ------------------ --- ------------ -- --

Çıkan sonuç A'nın ağ adresiyle aynı olmadığından haberleşemezler.
