# TEMEL KAVRAMLAR

## Band Genişliği (Bandwidth)

Haberleşme kanalının veya iletim ortamının kapasitesini ifade etmek için
kullanılır. Analog sinayallerde birini **<span
style="color: violet">hertz (hz)</span>** iken digital sistemlerde
**<span style="color: violet">bps (b/s)</span>**.  
bir haberleşme sistemi, gönderirici, alıcı ve iletim ortamından oluşur.
İletim kapasitesi en büyük olan bütün sistemin bant genişliği belirler.

<span style="color: red">Örnek</span>:

<figure>
<img src="images/bandwidth" id="fig:bandwidth_example"
style="width:17cm" alt="Bant Genişliği" />
<figcaption aria-hidden="true">Bant Genişliği</figcaption>
</figure>

**<span style="color: red">Soru</span>**

1.  240 mb büyüklüğündeki bir MP3 dosyası bir sistemde 4dk’da
    aktarılıyor. Bu sistemin aktarım kapasitesini (bant genişliğini)
    bulunuz.

2.  MP3 yerine MPG olsaydı ne olurdu?

**<span style="color: red">Çözüm</span>**

Bw=?

1.  4dk 240 mb =\> saniyede 1mb = <span style="color: red">8mb/s</span>

2.  Değişim olmaz...

## Temel Band (Base Band)

İletim ortamında tek bir frekans bandı kullanılır. Böylece teorik olarak
iletim ortamının tüm kapasitesi tek bir kanal için kullanılır.  
**Örneğin**: Ethernette bu band kullanır.

## Geniş Band (Brood Band)

İletim ortamında birden fazla frekans bandı kullanılır. bulunur. Basit
bir frekans band filtresi sayesinde kanallar ayrıştırılabilir. Telefon
hattından aynı anda ses verinin taşınması buna örnektir.

<img src="images/brood_band" style="width:17cm;height:7cm"
alt="image" />

## Paralel ve Seri İletişim

Paralel iletişimde byte düzenyinde iletişim sağlanır. İki uç arasında en
az 8 tane fiziksel iletim ortamı olmalıdır. Band genişliği teorik olarak
8 hat daha fazla olduğu düşünülebilir. Ancak hem maliyet hem protokol
tercihi hem de kullanılan topoloji gibi ektenler bu konuda etkilidir.

## Haberleşme Kanalı Modlari

1.  **<span style="color: blue"> Simplex Kanal</span>**: Televizyon ve
    radyo gibi yayının tek taraflı olarak yapıldığı kanallardır.

2.  **<span style="color: blue"> Half-dubleks Kanal</span>**: Çıft yönlu
    iletişim vardır. Ancak aynı anda sadece bir taraf veri gönderebilir.
    Örnek olarak **<span style="color: red">telsiz</span>**.

3.  **<span style="color: blue"> Full-dubleks Kanal</span>**: İki uc
    arasında iki tane simplex kanal vardır. Böylece aynı anda iki taraf
    veri gönderebilir ve alabilir. Örnek telefon görüşmeleri.

4.  Günümüzde tüm bilgisayar ağları **<span
    style="color: red">Full-dubleks</span>**’dir.
