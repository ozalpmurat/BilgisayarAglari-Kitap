# Yerel Ağlarda Güvenlik

LAN ortamlarında karşılaşılabilecek başlıca tehditler şunlardır:

- Yetkisiz erişim
- Veri dinleme (sniffing)
- Adres sahteciliği (ARP/DHCP spoofing)
- Zararlı yazılımlar (malware)
- İç tehditler (içeriden erişim yapan kötü niyetli kullanıcılar)

## Fiziksel Güvenlik

Ağ güvenliğinin ilk adımı fiziksel güvenliktir. Anahtarlar (switch), yönlendiriciler (router) ve sunucular gibi aktif cihazlar kilitli dolaplarda veya sunucu odalarında saklanmalıdır. Ağ bağlantı noktalarına fiziksel erişim sadece yetkili personele verilmelidir.

## Erişim Kontrolü

- MAC adresi filtreleme: Belirli cihazlara ağ erişimi sağlanır.
- 802.1X: Port tabanlı kimlik doğrulama protokolüdür. Erişim öncesi kullanıcı doğrulaması yapılır.
- NAC (Network Access Control): Ağa bağlanan cihazların sağlık durumu ve politikalarla uyumluluğu kontrol edilir.

## Trafik Güvenliği

LAN'da veri trafiğinin güvenliğini sağlamak için aşağıdaki önlemler alınabilir:

- ARP spoofing: Saldırgan, sahte ARP mesajlarıyla ağdaki veri akışını üzerine çeker.
  - Çözüm: Dynamic ARP Inspection, statik ARP tabloları.
- DHCP spoofing: Saldırgan sahte DHCP sunucusu gibi davranarak kullanıcıları yönlendirir.
  - Çözüm: DHCP Snooping ile sadece yetkili portlardan DHCP yanıtı alınması sağlanır.

## VLAN Kullanımı ve Segmentasyon

Ağ segmentasyonu ile farklı kullanıcı gruplarının trafiği ayrılır. VLAN’lar, bu segmentasyonu mantıksal olarak sağlar. VLAN hopping saldırılarına karşı:

- Etiketli/etiketsiz port ayarları doğru yapılmalı,
- Native VLAN yapılandırmasına dikkat edilmelidir.

## Port Güvenliği

Switch portlarına yönelik güvenlik önlemleri şunlardır:

- Kullanılmayan portlar devre dışı bırakılmalı,
- Belirli MAC adreslerine izin verilerek sabitleme (Sticky MAC) yapılmalı,
- Port güvenliği ihlalinde port otomatik olarak kapanmalıdır (shutdown).

## Loglama ve Denetim

Ağ olaylarının izlenmesi ve kaydedilmesi güvenliğin sürekliliği açısından önemlidir.

- SNMP ve Syslog gibi protokollerle loglar merkezi sistemlere yönlendirilir.
- SIEM sistemleri, logları analiz ederek anormal aktiviteleri tespit eder.

## Yazılım ve Donanım Güncellemeleri

Ağ cihazlarında üretici güncellemeleri ve güvenlik yamaları zamanında uygulanmalıdır. Firmware güncellemeleri, yeni tehditlere karşı cihazları korur ve performansı artırır.