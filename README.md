# ♿ BarrierFree-Architect: Engelsiz Yaşam Teknolojileri Rehberi

![TEKNOFEST 2025](https://img.shields.io/badge/TEKNOFEST-2025-blue.svg?style=for-the-badge)
![Category](https://img.shields.io/badge/Kategori-Engelsiz_Yaşam-green.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Elite_Architect-gold.svg?style=for-the-badge)

**BarrierFree-Architect**, engelli bireylerin sosyal hayata, eğitime ve istihdama katılımını kolaylaştıran teknolojik çözümler için tasarlanmış bir "Master Architecture" ve uygulama rehberidir. Bu repo, erişilebilirliği bir lütuf değil, bir mühendislik standardı olarak konumlandırır.

---

## 🎯 Vizyon ve Misyon
> *"Mükemmel bir sistem, herkesin hiçbir yardım almadan kullanabildiği sistemdir."*

Bu çalışma, TEKNOFEST 2025 Engelsiz Yaşam Teknolojileri kategorisinde, karmaşık bilişim mimarilerinin engelli bireylerin hayatını nasıl dönüştürebileceğine dair bir yol haritası sunar. Hedefimiz, "Herkes İçin Tasarım" (Design for All) prensiplerini en uç teknolojik sınırlarla birleştirmektir.

---

## 👨‍💻 Hazırlayan Hakkında
### **Bahattin Yunus Çetin**
**IT Architect Candidate | Technology Enthusiast**

Trabzon/Of'ta akademik yolculuğuna devam eden, yazılım mimarilerini insani değerlerle dokumayı amaçlayan bir vizyoner. "Engelsiz bir dünya" hayali, kod satırlarının ötesinde, yaşayan bir sistem tasarımıdır.

*   **📍 Location:** Trabzon, Türkiye
*   **🔗 LinkedIn:** [linkedin.com/in/bahattinyunus](https://www.linkedin.com/in/bahattinyunus/)
*   **📂 GitHub:** [github.com/bahattinyunus](https://github.com/bahattinyunus)

---

## 🏗️ Sistem Mimarisi (Accessibility Architecture)

Aşağıdaki diyagram, engelsiz yaşam teknolojilerinin katmanlı yapısını ve veri akışını temsil eder:

```mermaid
graph TD
    subgraph "Girdi Katmanı (Sensory Input)"
        A1[Kamera / Görüntü] --> B[Yapay Zeka Motoru]
        A2[Mikrofon / Ses] --> B
        A3[Hareket / IoT Sensörleri] --> B
    end

    subgraph "İşleme Katmanı (Core Brain)"
        B{AI Logic Processor}
        B -->|Nesne Tanıma| C1[Sesli Betimleme]
        B -->|NLP / STT| C2[Metin/İşaret Dili]
        B -->|Navigasyon| C3[Engelden Sakınma]
    end

    subgraph "Çıktı Katmanı (Accessibility Interface)"
        C1 --> D1((Ekran Okuyucu / Sesli Asistan))
        C2 --> D2((Görsel Arayüz / Haptic Geri Bildirim))
        C3 --> D3((Akıllı Baston / Giyilebilir Cihaz))
    end

    style B fill:#f96,stroke:#333,stroke-width:4px
```

---

## 🚀 Teknolojik Derinlik

### 1. Algılama Katmanı (Perception Layer)
*   **Görüntü İşleme (Computer Vision):** YOLOv8 ve TensorFlow tabanlı modellerle gerçek zamanlı nesne tanıma (Object Detection). Görme engelliler için çevre analizi.
*   **Ses Tanıma & Dönüştürme:** Whisper AI gibi yüksek doğluklu modellerle fısıltı seviyesindeki konuşmaları dahi anlık metne dönüştürme.
*   **Sensör Füzyonu:** LiDAR ve ultrasonik sensörlerin verilerini birleştirerek milimetrik doğrulukta mesafe ölçümü.

### 2. İletişim ve Veri İşleme (Processing Layer)
*   **Edge Computing:** Verinin buluta gitmeden cihaz üzerinde (on-device) işlenmesi sayesinde sıfır gecikme (zero latency).
*   **Cloud Integration:** Büyük veri analitiği ve model güncellemeleri için AWS/Azure hibrit bulut yapıları.
*   **Güvenlik:** Kişisel verilerin korunması için uçtan uca şifreleme ve anonimleştirme protokolleri.

### 3. Kullanıcı Arayüzü (Interface Layer)
*   **WCAG 2.2 Standartları:** AAA seviyesinde erişilebilirlik uyumluluğu.
*   **Haptic Interface:** Görme engelliler için titreşim tabanlı (mors kodu/ritmik) geri bildirim sistemleri.
*   **BCI (Brain-Computer Interface):** İleri derece fiziksel engelliler için zihin kontrolü arayüzleri tasarımı.

---

## 🛠️ Araç Seti (The Tech Stack)
| Alan | Teknoloji |
| :--- | :--- |
| **Dil** | Python, C++, TypeScript |
| **AI/ML** | PyTorch, MediaPipe, OpenCV |
| **IoT** | ESP32, Raspberry Pi, LoRaWAN |
| **Mobil** | Flutter (Erişilebilir Widget Seti) |
| **Veritabanı**| PostgreSQL, Cassandra |

---

## 📜 Lisans & Telif
Bu proje, "Engelsiz Bir Dünya" mottosuyla geliştirilmiştir.
© 2025 Bahattin Yunus Çetin. Tüm hakları saklıdır.

---
![Footer Image](https://img.shields.io/badge/Made_with-Love_and_Code-red?style=flat-square)
*“En büyük engel, tasarlanmamış teknolojidir.”*
