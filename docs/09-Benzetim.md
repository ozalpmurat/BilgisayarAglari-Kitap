# Bilgisayar Ağları Modelleme

Bu başlıkta simülatör ve emülatör kavramları açıklanmaya çalışılıp örnek
uygulamalar verilecektir.

## Simülatör & Emülatör

Bilgisayar üzerinde bir ağı modellemek için; simülatör ve emülatör
şeklinde iki tür program kullanılmaktadır:

**Simülatör**: Gerçek ortamdaki sistemler ile (çok benzese de) birebir
aynı şekilde çalışmaz. Uçuş simülatörleri buna örnek gösterilebilir.
Gerçek sistemlerde kullanılan donanımların üzerindeki yazılımlar bunda
kullanılmaz, simülatörlerde kullanılan sanal cihazlarda özel
geliştirilmiş ve kısıtlı yazılımlar çalışır. Ayrık zamanda çalışır:
gerçek hayatta binlerce saat sürecek bir işlem 1 saniyede yapılabilir;
gerçek hayatta 1ms içerisinde biten bir eylem saniyelerce sürecek
şekilde yavaşlatılabilir.

**Emülatör**: Gerçek cihazlarda kullanılan yazılımlar doğrudan burada da
çalıştırılır. Virtualbox üzerinde Windows çalıştırmak için, gerçek
Windows kurulumu yaptığımızı hatırlayın. Donanımlar sanallaştırılır ama
donanımlar üzerinde gerçek yazılımlar (işletim sistemleri) kullanılır.
Gerçek zamanda çalışır.

Simülatör ve emülatör kavramlarını bilgisayar ağları konusu özelinde
özetlemeye çalışalım.

İnternet’in ortak dilinin IP olması gibi, bilgisayar ağlarında ortak
donanım da Cisco firmasının ürünleridir. Pazara erken girmiş olması,
ürünlerinin kaliteli olması, geniş ürün yelpazesi olması, bol miktarda
dokümanı olması, kullanıcı sayısının çok olması, vb. nedenlerle
bilgisayar ağları çalışan hemen herkes Cisco cihazlara hakim olmaktadır.
Bu nedenle, ağ modelleme programlarında öncelikle Cisco cihazlara
(yönlendirici, anahtar, vb.) destek sağlanmaktadır.

Emülatör uygulamalarında, *-simülatörlerden farklı olarak-* gerçek Cisco
işletim sistemi kullanılması gerekmektedir. Gerçek işletim sistemi
kullanıldığı için, gerçek cihazlarla yapılan fiziksel ağ uygulamalarına
çok yakın bir çalışma ortamı sağlamaktadır. Bunun en büyük dezavantajı
ise Cisco işletim sistemleri ücretli olduğu için ilave maliyet
çıkarmasıdır. Diğer taraftan; bu işletim sistemlerinin İnternet’in
yeraltı dünyasında yaygınlaşması gibi illegal durumlara da sebebiyet
vermektedir.

## Ağ Modelleme Platformları (Ücretsiz Olanlar)

### Cisco Packet Tracer

Cisco firması tarafından geliştirilmektedir. Cisco’nun Networking
Academy adı altında vermiş olduğu eğitimlerde katılımcılara
verilmektedir. Bunun haricinde satışı bulunmamaktadır. Simülatör
tarzında bir uygulamadır.

<figure>
<img src="images/SimulatorCiscoPT.png" id="fig:CiscoPT"
alt="Cisco Packet Tracer arayüzü. Sol tarafta &quot;mantıksal&quot;, sağ tarafta &quot;fiziksel&quot; görünüm" />
<figcaption aria-hidden="true">Cisco Packet Tracer arayüzü. Sol tarafta
"mantıksal", sağ tarafta "fiziksel" görünüm</figcaption>
</figure>

Kataloğunda Sadece Cisco firmasına ait ürünler bulunmaktadır.
Yönlendirici, anahtar, kablosuz erişim noktası, IP telefon sistemler,
vb. farklı türde ürünler kullanılabilmektedir. Linux ve Windows
sürümleri bulunmaktadır. Program kurulduğunda, ilave bir işlem yapmaya
gerek kalmadan tüm özellikleri ile aktif halde olmaktadır. Program
içerisinde oluşturulan sanal cihazların gerçek hayat ile bağlantısı
yapılamamaktadır. Sadece klasik bilgisayar ağları değil, üst katmanlarda
da uygulama gerçekleştirilebilmektedir. Sanal sunucu cihazı üzerinden
HTTP, DNS, e-posta sunucuları gibi servisler de simüle edilebilmektedir.

### GNS3 (Graphical Network Simulator 3)

Cisco’nun kendi cihazları için tasarladığı IOS isimli işletim
sistemlerini kullanır. Bu IOS’lerden GNS3 içerisine en az 1 tane dahil
edilmelidir. Bu IOS’leri elde etmek için yasal bir yol malesef
bulunmamaktadır. Cisco müşterisi olanlar WEB üzerinden
indirebilmektedir. Bunun haricinde satışı bulunmamaktadır. VirtualBox
PC’leri bunun içine dahil edilebilmektedir. Gerçek yönlendirici imajları
ve gerçek sanal bilgisayarlar kullandığından oldukça gerçekçi bir
çalışma ortamı sağlamaktadır. Cisco sertifikasyon sınavlarına
hazırlananlar için de kullanışlıdır. Programın önemli bir özelliği de
sanal ağda kullanılan sanal makinaların Host-PC (fiziksel bilgisayar)
üzerinden internet’e çıkabilmesidir.

<figure>
<img src="images/SimulatorGNS3.png" id="fig:GNS3"
alt="GNS3 arayüzü içindeki yönlendiricinin konsolu" />
<figcaption aria-hidden="true">GNS3 arayüzü içindeki yönlendiricinin
konsolu</figcaption>
</figure>

### CORE (Common Open Resource Emulator) 

Linux ve BSD üzerinde çalışıyor. Windows üzerinde sanal bilgisayarda
çalıştırılabiliyor. Hatta kendi sitesinde, VmWare Player için hazır
imajları da var. CORE içindeki her bir sanal PC’de Linux çalışıyor.
Sanal ağ üzerinde lazım olan tüm işlevleri bu Linux’lar vasıtasıyla
gerçekleştirilebiliyor. DHCP sunucusu, yönlendirici hizmeti, WEB
sunucusu, vb. tüm işlevler Linux platformları üzerinden sağlanabiliyor.
Yönlendirici olarak Cisco kullanma alışkanlığı olanlar, bir sanal Linux
üzerine Quagga kurarak, onu sahte Cisco yönlendiriciye çevirebilirler.

Sanal ağı, gerçek ağa bağlayarak internet’e çıkarma özelliği
bulunmaktadır. Büyük projelerde kullanmak üzere dağıtık hesaplama
desteği de bulunmaktadır. Örneğin; elinizde 3 tane fiziksel PC varsa ve
200 tane node’dan oluşan sanal bir ağ kullanmak istiyorsanız, node’ları
iki fiziksel PC’ye paylaştırabilir, 1 PC’yi de GUI amacı ile
kullanabilirsiniz. Phyton ile script yazılabildiğini de belirtelim.

<figure>
<img src="images/SimulatorCORE.png" id="fig:CORE"
alt="CORE ekran görüntüsü" />
<figcaption aria-hidden="true">CORE ekran görüntüsü</figcaption>
</figure>

### Diğerleri

-   **NS2:** <http://www.isi.edu/nsnam/ns/>

-   **NS3:** <https://www.nsnam.org/> (NS2’nin devamı olarak yapılmasına
    rağmen geriye doğru uyumluluğu olmadığından ayrı bir yazılım olarak
    değerlendiriliyor)

<!-- -->

-   **Cloonix**: [http://clownix.net](http://clownix.net/) Açık
    kaynaklı. KVM sanal makine desteği var.

-   **IMUNES**: [http://www.imunes.net](http://www.imunes.net/) Açık
    kaynaklı. FreeBSD üzerinde çalışıyor. Sanal makinede
    çalıştırılabilir.

-   **OMNeT++**: <http://www.omnetpp.org/>

-   **Marionnet**: <http://www.marionnet.org/EN/>

-   **Mininet**: [http://www.mininet.org](http://www.mininet.org/)

-   **Netkit:** [http://wiki.netkit.org](http://wiki.netkit.org/)

-   **Psimulator2:** <http://code.google.com/p/psimulator/>

-   **Virtualsquare:**
    <http://wiki.virtualsquare.org/wiki/index.php/Main_Page>

-   **VNX and VNUML:** <http://www.dit.upm.es/vnx>

-   **OPNET (Ücretli):**
    <http://www.riverbed.com/products/performance-management-control/opnet.html>

# Kaynaklar

1.  <http://www.brianlinkletter.com/open-source-network-simulators/>

2.  <http://www.finmars.co.uk/blog/4-evaluating-network-simulation-tools>

3.  <http://nil.uniza.sk/network-simulation-and-modelling/network-simulators-list>
