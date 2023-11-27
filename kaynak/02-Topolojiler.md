# AĞ TOPOLOJİLERİ 

<figure>
<img src="images/62_ağ_topolojisi" id="fig:topolojiler"
style="width:14cm" alt="Topolojiler" />
<figcaption aria-hidden="true">Topolojiler</figcaption>
</figure>

Ağ topolojileri nedir sorusunun en net cevabı, "bir ağı oluşturan
cihazların fiziksel ve mantıksal yerleşimidir". Network Topology (Ağ
Topolojisi) Yerel Ağ Alanı (LAN) içerisinde bulunan bilgisayarların
fiziksel ve mantıksal yerleşimini ifade eder. Fiziksel Topoloji ağ
içerisinde bulunan tüm cihazların birbirlerine nasıl bağlanacağını ve
bağlantı için ne tür kablo kullanacağını belirtirken Mantıksal Topoloji
bu cihazların nasıl haberleşeceğini belirtir ve bu cihazları ortak bir
protokol altında birleştirir. Kullanılmak istenen Ağ Teknolojisine göre
farklı ağ topolojileri kullanılmaktadır. Fiziksel Topolojinin 6 farklı
çeşidi vardır. Bunlar Bus(Yol), Ring(Halka), Yıldız(Star), Ext
Star(Gelişmiş Yıldız), Mesh(Örgü) ve Tree(Ağaç) topolojileridir.
Broadcast(Yayın) ve Token Passing(İz) mantıksal topolojilere birer
örnektir.

## DOĞRUSAL (BUS) TOPOLOJİ

Doğrusal bir hat üzerinde bilgisayarların T konnektörlerle bağlanması
şeklinde kurulur. Hattın her iki ucunda sonlandırıcı kullanmak
zorunludur. Koaksiyel kablo kullanılır. Ağın herhangi bir noktasında
arıza olması durumunda ağın tamamı çöker. Ağdaki veri trafiği tüm uçlara
gider. Herkes herkesin trafiğini görebilir. Bu yüzden çok fazla
**çakışma (collision)** olur.

<figure>
<img src="images/bus-topolojisi" id="fig:bustopolojisi"
style="width:8cm" alt="Bus Topolojisi" />
<figcaption aria-hidden="true">Bus Topolojisi</figcaption>
</figure>

## HALKA (RING) TOPOLOJİ

Doğrusal topolojiye benzer. Sonlandırıcı kullanılmaz. Hattın iki ucu
birleşiktir. Hatta sanal bir jeton dolaşır(token).Jeton sırası gelen
bilgisayar, jeton boş ise göndereceği veriyi hatta yerleştirir.
Bilgisayarlar sırayla veri gönderdiklerinden çakışma daha
azdır.Günümüzde hiç kullanılmamaktadır. Herkes herkesin verisini
kullanabilmektedir.

<figure>
<img src="images/ring-topology-removebg-preview"
id="fig:halka_topolojisi" style="width:8cm"
alt="Halka-Ring Topolojisi" />
<figcaption aria-hidden="true">Halka-Ring Topolojisi</figcaption>
</figure>

## YILDIZ (STAR) TOPOLOJİ

Merkezde dağıtıcı bir cihaz olur. Buradan tüm bilgisayarlara birer kablo
gider. Ağın bir noktasındaki arıza sadece ilgili bilgisayarın ağ
bağlantısına zarar verir. Genellikle **(**bükümlü çift (twisted
pair,xtp)) kullanılır. Trafiğin herkese mi gönderileceği ya da sadece
ilgili uca mı gideceği dağıtıcıya bağlıdır. Dağıtıcının performansı ve
kabiliyeti ağı doğrudan etkiler. Günümüzde en yaygın topolojidir.

<figure>
<img src="images/star-Topology-1024x512-removebg-preview"
id="fig:yildiz_topolojisi" style="width:8cm"
alt="Yıldız-StarTopolojisi" />
<figcaption aria-hidden="true">Yıldız-StarTopolojisi</figcaption>
</figure>

## ÖRGÜ (MESH)TOPOLOJİ

<figure>
<img src="images/mesh-topology-1-1024x512-removebg-preview"
id="fig:Orgu_mesh_topolojisi" style="width:12cm"
alt="Örgü-Mesh Topolojisi" />
<figcaption aria-hidden="true">Örgü-Mesh Topolojisi</figcaption>
</figure>

Uçları arasında birden fazla rota üzerinde haberleşme imkanı olan
yapılardır. Günümüzde genellikle farklı yıldız ağlar arasında yedekleme
amacı olarak kullanılır.

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