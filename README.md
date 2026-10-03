🔧 Technical Services System

Python kullanarak geliştirdiğim terminal tabanlı bir teknik servis takip sistemidir.

Bu proje, bir teknik servise getirilen cihazların müşteri bilgilerinin, cihaz bilgilerinin, arıza durumlarının, yapılan işlemlerin ve servis ücretlerinin takip edilmesini amaçlamaktadır.

📌 Proje Özellikleri

Program üzerinden:

* Yeni servis kaydı oluşturma
* Tüm servis kayıtlarını listeleme
* Servis kaydı arama
* Servis kaydı güncelleme
* Servis kaydına yapılan işlem ekleme
* Servis kaydına ücret ekleme
* Duruma göre servis kayıtlarını listeleme
* Servis istatistiklerini görüntüleme

işlemleri yapılabilir.

🖥️ Menü

Program çalıştırıldığında aşağıdaki işlemler sunulur:

1. New Services Record
2. List All Service Records
3. Search Service Record
4. Update Service Record
5. Add Operation
6. Add Cost
7. List Records by Status
8. Service Statistics
9. Exit

📋 Servis Kaydı

Yeni bir servis kaydı oluşturulurken aşağıdaki bilgiler alınır:

* Müşteri adı
* Telefon numarası
* Cihaz türü
* Marka
* Model
* Garanti durumu
* Arıza açıklaması
* Öncelik

Her servis kaydına ayrıca benzersiz bir servis numarası atanır.

Örneğin:

SRV-1001

🔄 Servis Durumları

Servis kayıtlarının durumları takip edilebilir.

Örneğin:

Pending
Under Review
Waiting for Parts
Being Repaired
Completed
Delivered

💰 Ücret Takibi

Bir servis kaydına birden fazla işlem ve ücret eklenebilir.

Toplam servis ücreti, kayıt içerisinde bulunan maliyetlerin toplamı üzerinden hesaplanır.

📊 Servis İstatistikleri

Program servis kayıtları üzerinden çeşitli istatistikler oluşturabilir.

Örneğin:

* Bekleyen servis sayısı
* İncelenen servis sayısı
* Parça bekleyen servis sayısı
* Tamir edilen servis sayısı
* Tamamlanan servis sayısı
* Teslim edilen servis sayısı

🧠 Kullanılan Python Konuları

Bu projeyi geliştirirken aşağıdaki Python konularını kullandım:

* Object-Oriented Programming (OOP)
* Classes
* Objects
* Methods
* Lists
* Dictionaries
* Functions
* if / elif / else
* for döngüsü
* while döngüsü
* try / except
* String işlemleri
* Kullanıcıdan veri alma
* Modüller ve dosyalar arası import
* Veri yönetimi
* Koşullu işlemler

📁 Proje Yapısı

technical-services-system
│
├── main.py
├── models.py
├── assistant.py
└── README.md

main.py

Programın ana menüsünü ve kullanıcı ile etkileşimi yönetir.

models.py

Servis sistemiyle ilgili class yapılarını ve servis kayıtlarının yönetimini içerir.

assistant.py

Kullanıcıdan alınan bazı bilgilerin yönetilmesi, seçimlerin yapılması ve servis numarası oluşturulması gibi yardımcı işlemleri içerir.

▶️ Nasıl Çalıştırılır?

Terminal üzerinden proje klasörüne girip:

python3 main.py

komutunu çalıştırabilirsiniz.
