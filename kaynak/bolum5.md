# IP YÖNLENDİRME

IP’nin yönlendirilebilir olması protokolün en güçlü özelliğidir. Çok
sayıda iletişim protokolü mevcut olmasına rağmen IP’nin
yönlendirilebilir esnek yapısı internetin temel dili olmasını
sağlamıştır. Yönlendirme işlemini "Yönlendirici(Router)" yapar.

**Yönlendirme Tablosunda**

1.  Kaynak

2.  Hedef(Ip ve Maske)

3.  Ağ Geçidi

4.  Ara Birim(Interface)

5.  Ölçüt(Metrik)

<figure>
<img src="images/BurayaGorselGelecek.png" id="fig:YonlendirmeTablosu"
style="width:5cm" alt="Yönlendirme Tablosu" />
<figcaption aria-hidden="true">Yönlendirme Tablosu</figcaption>
</figure>

## STATİK YÖNLENDİRME

Ağ yöneticisi tarafından elle sabit olarak yazılır.Genellikle
yönlendiricisi ve yönlendirme işlemi çok fazla olmayan ağlarda
kullanılır.Yönlendirme tablolarının güncellemesi ağdaki fiziksel
değişikliklere göre yeniden elle yapılmalıdır.

<figure>
<img src="images/BurayaGorselGelecek.png" id="fig:StatikYonlendirme"
style="width:5cm" alt="Statik Yönlendirme" />
<figcaption aria-hidden="true">Statik Yönlendirme</figcaption>
</figure>

## DİNAMİK YÖNLENDİRME

Yönlendirme algoritmaları tarafından hesaplanarak bulunur. Ağ yöneticisi
tarafından önceden bazı filtreler ve tanımlamalar yapılmalıdır. Ağda
değişiklik olduğunda yollar otomatik olarak düzeltilir. En yaygın
yönlendirme algoritmadır.

<figure>
<img src="images/BurayaGorselGelecek.png" id="fig:DinamikYonlendirme1"
style="width:5cm" alt="Dinamik Yönlendirme1" />
<figcaption aria-hidden="true">Dinamik Yönlendirme1</figcaption>
</figure>

şekildeki ağın sağlıklı çalışabilmesi için ..... sağlanmalıdır

<figure>
<img src="images/BurayaGorselGelecek.png" id="fig:DinamikYonlendirme2"
style="width:5cm" alt="Dinamik Yönlendirme2" />
<figcaption aria-hidden="true">Dinamik Yönlendirme2</figcaption>
</figure>

1.  C’nin E1 bacağı ile A aynı ağda olmalıdır.

2.  C’nin E2 bacağı ile B aynı ağda olmalıdır.

3.  A’nin ağ geçidi C’nin E1 bacağındaki IP olmadır.

4.  B’nın ağ geçidi C’nin E2 bacağındaki IP olmalıdır.

5.  C’ye IP yönlendirme komutu verilmelidir.

Yönlendirme tablosunda birbirini kapsayan kurallar var ise bunlar
küçükten büyüğe sıra ie değerlendirilir.

<figure>
<img src="images/BurayaGorselGelecek.png" id="fig:DinamikYonlendirme3"
style="width:5cm" alt="Dinamik Yönlendirme3" />
<figcaption aria-hidden="true">Dinamik Yönlendirme3</figcaption>
</figure>

Örnek trafik 10.0.0.5 IP’yi google götürmek üzere /26 kullanır. Gerçi
hepsini kapsıyor ondan en küçüğün kabul eder. 10.0.0.199 google
göstermek için /24 kullanır.

<figure>
<img src="images/BurayaGorselGelecek.png" id="fig:DinamikYonlendirme4"
style="width:5cm" alt="Dinamik Yönlendirme4" />
<figcaption aria-hidden="true">Dinamik Yönlendirme4</figcaption>
</figure>

<div class="center">

<u>Yönlendirme Tablosu</u>

</div>

|         |             |             |     |
|:--------|:------------|:------------|:----|
| A → B   | 10.0.1.0/24 | 10.0.2.0/24 | E2  |
| B → A   | 10.0.2.0/24 | 10.0.1.0/24 | E1  |
| (A+B) → | 0.0.0.0/0   | 0.0.0.0/0   | E3  |

Tablo XXX

<span style="color: red">NOT: </span> Yönlendiriciler de kendisine
doğrudan bağlıdan (directly connected) ağlar için genellikle yönlendirme
çünkü doğrudan bağlı olan bütün ağlar tanırlar.

|                                                           |     |                                                             |
|:----------------------------------------------------------|:----|:------------------------------------------------------------|
| <span style="color: red"><u>Directly Connected</u></span> |     | <span style="color: red"><u>Eklenmesi Gerekenler</u></span> |
| A→ 1,2                                                    |     | A→ 3,5,b } 3 satır kural eklemesi gerekiyor                 |
| B→ 2,3,4                                                  |     | A→ 1,5,b } 3 satır                                          |
| c→ 1,2                                                    |     | A→ 1,3 } 2 satır                                            |

Tablo XXX
