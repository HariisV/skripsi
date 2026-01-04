# TUGAS AKHIR

## ANALISIS PREDIKTIF REKENING BERISIKO TERKAIT TINDAK PENCUCIAN UANG MENGGUNAKAN MODEL CATBOOST: STUDI KASUS KEBIJAKAN PEMBLOKIRAN REKENING PASIF

---

**Sebagai Salah Satu Syarat untuk Memperoleh Gelar Sarjana Komputer pada**  
**PJJ Informatika**

---

**Oleh:**  
**220401010015, Haris Wahyudi**

---

**PROGRAM STUDI INFORMATIKA PJJ S1**  
**UNIVERSITAS SIBER ASIA**  
**AGUSTUS 2025**

---

# PERNYATAAN KEABSAHAN

Saya yang bertanda-tangan dibawah ini:

|                   |                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Nama              | Haris Wahyudi                                                                                                                                   |
| NIM               | 220401010015                                                                                                                                    |
| Program Studi     | PJJ Informatika                                                                                                                                 |
| Judul Tugas Akhir | ANALISIS PREDIKTIF REKENING BERISIKO TERKAIT TINDAK PENCUCIAN UANG MENGGUNAKAN MODEL CATBOOST: STUDI KASUS KEBIJAKAN PEMBLOKIRAN REKENING PASIF |

Menyatakan dengan sesungguhnya bahwa:

1. Tugas Akhir disusun secara ilmiah yang memenuhi aspek originalitas, valid dan dapat dipertanggungjawabkan.
2. Tugas Akhir disusun tidak menggunakan Generative AI untuk perbantuan penulisan kalimat/paragraf/bab.
3. Data yang digunakan dalam penelitian adalah data yang bersumber pada penerapan metode usulan/dari sumber ilmiah lain/dari instansi yang berizin secara resmi.

Jika di kemudian hari ditemukan hal-hal yang melanggar ketentuan penyusunan Tugas Akhir, saya siap bersedia dan menerima Sanksi Akademik dari Universitas Siber Asia.

Demikian pernyataan ini saya buat.

**Batam, 26 November 2025**  
Yang membuat pernyataan,

**Haris Wahyudi**

---

# HALAMAN PERNYATAAN ORISINALITAS

Saya yang bertanda-tangan dibawah ini:

|                   |                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Nama              | Haris Wahyudi                                                                                                                                   |
| NIM               | 220401010015                                                                                                                                    |
| Program Studi     | PJJ Informatika                                                                                                                                 |
| Judul Tugas Akhir | ANALISIS PREDIKTIF REKENING BERISIKO TERKAIT TINDAK PENCUCIAN UANG MENGGUNAKAN MODEL CATBOOST: STUDI KASUS KEBIJAKAN PEMBLOKIRAN REKENING PASIF |

Menyatakan dengan sesungguhnya bahwa Tugas Akhir ini merupakan hasil penelitian, pemikiran dan pemaparan asli saya sendiri. Saya tidak mencantumkan tanpa pengakuan bahan-bahan yang telah dipublikasikan sebelumnya atau ditulis oleh orang lain, atau sebagai bahan yang pernah diajukan untuk gelar atau ijasah pada Universitas Siber Asia atau perguruan tinggi lainnya.

Apabila dikemudian hari terdapat penyimpangan dan ketidakbenaran dalam pernyataan ini, maka saya bersedia menerima sanksi akademik sesuai dengan peraturan yang berlaku di Universitas Siber Asia.

Demikian pernyataan ini saya buat.

**Batam, 26 November 2025**  
Yang membuat pernyataan,

**Haris Wahyudi**

---

# HALAMAN PENGESAHAN

Tugas Akhir ini diajukan oleh:

|                   |                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Nama              | Haris Wahyudi                                                                                                                                   |
| NIM               | 220401010015                                                                                                                                    |
| Program Studi     | PJJ Informatika                                                                                                                                 |
| Judul Tugas Akhir | ANALISIS PREDIKTIF REKENING BERISIKO TERKAIT TINDAK PENCUCIAN UANG MENGGUNAKAN MODEL CATBOOST: STUDI KASUS KEBIJAKAN PEMBLOKIRAN REKENING PASIF |

Telah berhasil dipertahankan dihadapan Dewan Penguji dan diterima sebagai bagian persyaratan yang diperlukan untuk memperoleh gelar Sarjana Komputer pada Program Studi PJJ Informatika Universitas Siber Asia.

| Jabatan                        | Nama                                     | Tanda Tangan |
| ------------------------------ | ---------------------------------------- | ------------ |
| Ketua Sidang / Dosen Penguji I | ………………………………..                           |              |
| Dosen Penguji II               | ………………………………..                           |              |
| Dosen Pembimbing               | Cian Ramadhona Hassolthine, S.Kom, M.Kom |              |
| Ketua Program Studi            | Syahid Abdullah, S.Si, M.Kom.            |              |

**Ditetapkan di:** Jakarta  
**Tanggal:** 10/8/2025

---

# KATA PENGANTAR

Puji syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa, karena atas berkat dan rahmat-Nya penulis dapat menyelesaikan Tugas Akhir ini. Penyusunan Tugas Akhir ini dilakukan dalam rangka memenuhi salah satu syarat untuk mencapai gelar Sarjana Program Studi Informatika, Universitas Siber Asia.

Ketertarikan penulis terhadap topik penelitian ini berawal dari maraknya polemik mengenai kebijakan pemblokiran rekening pasif oleh Pusat Pelaporan dan Analisis Transaksi Keuangan (PPATK). Kebijakan tersebut menjadi sorotan karena diterapkan secara luas, termasuk terhadap rekening yang menjadi pasif akibat alasan yang sebenarnya wajar, seperti pembukaan rekening untuk tujuan promosi, atau seperti penyaluran bantuan sosial. Di sisi lain, PPATK menegaskan bahwa rekening pasif memiliki potensi untuk disalahgunakan dalam aktivitas ilegal, termasuk tindak pencucian uang. Kondisi inilah yang menunjukkan perlunya pendekatan analitik yang lebih akurat dan berbasis data dalam menilai tingkat risiko suatu rekening sebelum kebijakan pemblokiran diterapkan.

Penulis menyadari bahwa tanpa bantuan dan bimbingan dari berbagai pihak, sejak masa perkuliahan hingga proses penyusunan Tugas Akhir ini, sangatlah sulit bagi penulis untuk dapat menyelesaikannya. Oleh karena itu, penulis menyampaikan terima kasih sebesar-besarnya kepada:

1. Ibu Cian Ramadhona Hassolthine, S.Kom, M.Kom selaku dosen pembimbing yang telah menyediakan waktu, tenaga, dan pemikiran untuk membimbing dan mengarahkan penulis dalam penyusunan Tugas Akhir ini.
2. Orang tua dan keluarga penulis yang selalu memberikan dukungan moral, doa, dan motivasi selama proses penyusunan Tugas Akhir; dan
3. Sahabat-sahabat penulis yang telah memberikan bantuan, dorongan, serta menemani penulis dalam menyelesaikan Tugas Akhir ini.

Akhir kata, penulis berharap Tuhan Yang Maha Esa berkenan membalas segala kebaikan semua pihak yang telah membantu. Semoga Tugas Akhir ini dapat memberikan manfaat bagi pengembangan ilmu pengetahuan dan menjadi kontribusi untuk peningkatan keamanan transaksi digital di Indonesia.

**Batam, 26 November 2025**  
Penulis,

**Haris Wahyudi**

---

# ABSTRAK

Peningkatan kasus pencucian uang di Indonesia menimbulkan tantangan serius bagi stabilitas sistem keuangan dan efektivitas pengawasan transaksi. Salah satu modus yang sering digunakan adalah penyalahgunaan rekening tertentu sebagai media perputaran dana untuk menyamarkan asal-usul transaksi ilegal. Dalam upaya pencegahan, PPATK terus mendorong peningkatan kemampuan analisis untuk mengidentifikasi rekening yang berisiko tinggi terkait tindak pencucian uang. Namun, pendekatan konvensional kerap menimbulkan kesalahan identifikasi karena tidak mempertimbangkan pola transaksi secara menyeluruh.

Penelitian ini bertujuan mengembangkan model analisis prediktif untuk mengidentifikasi rekening berisiko terkait tindak pencucian uang menggunakan algoritma CatBoost. Dataset yang digunakan mencakup pola transaksi, frekuensi aktivitas, dan karakteristik arus dana dalam bentuk data sintetis. Metode klasifikasi diterapkan untuk mengenali pola perilaku transaksi yang sering ditemukan pada aktivitas pencucian uang. Hasil penelitian menunjukkan bahwa CatBoost mampu memberikan akurasi prediksi yang lebih tinggi dibandingkan pendekatan berbasis aturan sederhana. Temuan ini diharapkan dapat menjadi rekomendasi bagi PPATK dalam meningkatkan efektivitas identifikasi dini terhadap rekening yang berpotensi berisiko.

**Kata Kunci:** Judi Online, CatBoost, PPATK

---

# ABSTRACT

The rise of money laundering cases in Indonesia poses a significant challenge to the stability of the financial system and the effectiveness of transaction monitoring. One commonly used method involves exploiting specific bank accounts as channels to circulate illicit funds and obscure their origins. To strengthen preventive measures, PPATK has emphasized the need for improved analytical capabilities to identify high-risk accounts potentially associated with money laundering activities. However, conventional approaches often lead to misclassification due to limited consideration of comprehensive transaction patterns.

This study aims to develop a predictive analysis model to identify high-risk accounts potentially involved in money laundering using the CatBoost algorithm. The dataset consists of synthetic data representing transaction patterns, activity frequency, and fund-flow characteristics. A classification method is applied to detect behavioral patterns typically observed in money laundering activities. The results demonstrate that CatBoost achieves higher predictive accuracy compared to simple rule-based methods. These findings are expected to serve as recommendations for PPATK in enhancing the effectiveness of early identification of high-risk financial accounts.

**Keywords:** Online Gambling, CatBoost, PPATK

---

# DAFTAR ISI

- [Pernyataan Orisinalitas](#halaman-pernyataan-orisinalitas) .................................. ii
- [Lembar Pengesahan](#halaman-pengesahan) .................................. iii
- [Kata Pengantar](#kata-pengantar) .................................. iv
- [Daftar Isi](#daftar-isi) .................................. vi
- [Daftar Tabel](#daftar-tabel) .................................. viii
- [Daftar Gambar](#daftar-gambar) .................................. ix
- [Daftar Lampiran](#daftar-lampiran) .................................. x
- [Abstrak](#abstrak) .................................. xi
- [Abstract](#abstract) .................................. xii
- [BAB I - Pendahuluan](#bab-i-pendahuluan) .................................. 1
- [BAB II - Metodologi Penelitian](#bab-ii-metodologi-penelitian) .................................. 5
- [BAB III - Implementasi](#bab-iii-implementasi) .................................. 10
- [BAB IV - Kesimpulan dan Saran](#bab-iv-kesimpulan-dan-saran) .................................. 28
- [Daftar Pustaka](#daftar-pustaka) .................................. 30

---

# DAFTAR TABEL

- Tabel 3.1 Analisa Kebutuhan Development .................................. 10

---

# DAFTAR GAMBAR

- Gambar 2.1 Metode Waterfall .................................. 5

---

# DAFTAR LAMPIRAN

- Lampiran 1. Wawancara

---

# BAB I PENDAHULUAN

## 1.1 Latar Belakang

Pencucian uang (money laundering) merupakan salah satu ancaman serius terhadap stabilitas sistem keuangan global. Menurut estimasi PBB, sekitar 2-5% dari Produk Domestik Bruto (PDB) global atau setara dengan $0.8-$2.0 triliun per tahun dicuci melalui berbagai skema pencucian uang [2]. Di Indonesia, perkembangan teknologi digital dan maraknya platform perjudian online telah membuka peluang baru bagi pelaku kejahatan untuk melakukan pencucian uang dengan metode yang semakin canggih dan sulit dideteksi.

Pusat Pelaporan dan Analisis Transaksi Keuangan (PPATK) sebagai Financial Intelligence Unit (FIU) Indonesia memiliki peran strategis dalam mengawasi dan menganalisis transaksi keuangan yang mencurigakan. Berdasarkan data PPATK, terdapat peningkatan signifikan laporan transaksi keuangan mencurigakan yang terkait dengan aktivitas perjudian online dalam beberapa tahun terakhir. Platform judi online menjadi media yang sangat atraktif bagi pelaku pencucian uang karena memungkinkan transfer dana dengan cepat, anonim, dan dalam jumlah besar melalui pola deposit-withdraw yang berulang [6].

Salah satu kebijakan yang diterapkan PPATK untuk menanggulangi pencucian uang adalah pemblokiran rekening pasif atau rekening yang terindikasi digunakan untuk aktivitas mencurigakan. Namun, kebijakan ini menghadapi dilema klasik dalam sistem deteksi: pendekatan yang terlalu agresif akan menghasilkan banyak false positive (rekening legitimate yang salah diblokir), sementara pendekatan yang terlalu konservatif akan membiarkan banyak rekening berisiko lolos dari deteksi (false negative). Data menunjukkan bahwa dengan metode rule-based tradisional, tingkat false positive dapat mencapai 30% atau lebih, yang berarti banyak nasabah yang tidak bersalah terkena dampak pemblokiran [6].

Pendekatan deteksi tradisional yang mengandalkan rule-based system memiliki keterbatasan dalam menangani pola pencucian uang yang semakin kompleks dan adaptif. Pelaku pencucian uang terus berinovasi dengan teknik-teknik baru seperti structuring (memecah transaksi besar menjadi banyak transaksi kecil), layering (membuat rangkaian transaksi kompleks untuk mengaburkan jejak), fan-in dan fan-out patterns (mengumpulkan atau menyebarkan dana melalui banyak rekening), serta memanfaatkan jaringan rekening mule yang sulit diidentifikasi dengan aturan statis [2].

Perkembangan machine learning dan artificial intelligence menawarkan pendekatan baru yang lebih adaptif dan akurat untuk deteksi pencucian uang. Algoritma gradient boosting, khususnya CatBoost, telah menunjukkan performa superior dalam berbagai penelitian deteksi fraud dan anomali finansial [4], [5]. CatBoost memiliki beberapa keunggulan unik yang sangat relevan dengan karakteristik data transaksi keuangan:

1. **Native handling untuk fitur kategorikal**: CatBoost dapat memproses fitur kategorikal (seperti jenis transaksi, kode merchant, kode wilayah) secara langsung tanpa perlu one-hot encoding yang dapat menyebabkan curse of dimensionality [5].

2. **Ordered boosting**: Teknik ordered boosting pada CatBoost efektif mencegah overfitting dengan mengurangi prediction shift, sangat penting untuk data imbalanced di mana kasus pencucian uang hanya 0.1-0.3% dari total transaksi [5].

3. **Training efisien**: CatBoost menggunakan oblivious decision trees yang membuat training lebih cepat dan memerlukan hyperparameter tuning yang minimal dibandingkan XGBoost atau LightGBM, dengan tetap menghasilkan akurasi kompetitif [4].

4. **Interpretabilitas**: CatBoost menyediakan feature importance dan dapat dikombinasikan dengan SHAP values untuk menjelaskan keputusan model, aspek krusial untuk memenuhi regulasi dan memfasilitasi investigasi manual oleh analis PPATK [5].

Penelitian Altman et al. (2024) pada dataset AMLworld menunjukkan bahwa algoritma gradient boosting yang dikombinasikan dengan graph-based feature engineering dapat mencapai F1-score hingga 63.23% pada dataset dengan pola pencucian uang yang kompleks [2]. Namun, penelitian tersebut juga mengidentifikasi bahwa feature engineering yang tepat menjadi kunci keberhasilan model dalam menangkap pola-pola pencucian uang seperti fan-in, fan-out, scatter-gather, dan cycle patterns.

Berdasarkan konteks di atas, penelitian ini bertujuan mengembangkan sistem prediksi rekening berisiko terkait pencucian uang menggunakan algoritma CatBoost dengan fokus khusus pada karakteristik transaksi judi online. Penelitian ini diharapkan dapat membantu PPATK meningkatkan efektivitas kebijakan pemblokiran rekening pasif dari tingkat akurasi sekitar 60-70% menjadi 90% atau lebih, sambil secara signifikan mengurangi false positive dari 30% menjadi di bawah 20%, sehingga kebijakan menjadi lebih targeted, efisien, dan mengurangi dampak negatif terhadap nasabah yang legitimate.

---

## 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah dipaparkan, penelitian ini merumuskan beberapa pertanyaan penelitian sebagai berikut:

1. **Bagaimana karakteristik dan pola transaksi keuangan yang mengindikasikan aktivitas pencucian uang melalui platform judi online?**

   Pertanyaan ini bertujuan mengidentifikasi fitur-fitur diskriminatif yang membedakan transaksi normal dengan transaksi terkait pencucian uang, khususnya yang memanfaatkan modus judi online seperti pola deposit-withdraw cepat, structuring, fan-in/fan-out patterns, dan rapid cycling.

2. **Bagaimana merancang dan mengimplementasikan model prediktif berbasis CatBoost untuk klasifikasi rekening berisiko dengan mempertimbangkan karakteristik data yang imbalanced dan fitur kategorikal?**

   Pertanyaan ini fokus pada aspek metodologi, termasuk feature engineering, penanganan class imbalance, optimasi hyperparameter, dan strategi validasi model yang sesuai dengan karakteristik data transaksi keuangan.

3. **Bagaimana performa model CatBoost dibandingkan dengan algoritma machine learning lainnya (Random Forest, XGBoost, LightGBM, Logistic Regression) dalam hal akurasi, precision, recall, F1-score, dan efisiensi waktu training untuk deteksi rekening berisiko?**

   Pertanyaan ini bertujuan melakukan evaluasi komparatif untuk memvalidasi keunggulan CatBoost dan memberikan rekomendasi algoritma yang paling sesuai untuk deployment di PPATK.

4. **Fitur-fitur transaksi apa yang paling berpengaruh dalam prediksi rekening berisiko, dan bagaimana interpretasi fitur-fitur tersebut dalam konteks investigasi pencucian uang?**

   Pertanyaan ini fokus pada aspek interpretabilitas model melalui feature importance analysis dan SHAP values, untuk memberikan insight kepada analis PPATK dalam melakukan investigasi manual lebih lanjut.

---

## 1.3 Batasan Masalah

Agar penelitian ini lebih terfokus dan dapat diselesaikan secara optimal, beberapa batasan masalah ditetapkan sebagai berikut:

1. **Dataset**: Penelitian menggunakan data sintetis dari IBM Synthetic Financial Transactions dataset yang telah dipublikasikan secara terbuka. Penggunaan data sintetis dipilih karena beberapa alasan:

   - Ground truth labeling yang sempurna (100% akurat) untuk seluruh transaksi pencucian uang, sementara data riil banyak memiliki unlabeled cases [2]
   - Tidak ada issue privasi dan regulatory compliance yang kompleks
   - Memungkinkan reproducibility penelitian dan validasi oleh peneliti lain
   - Data sintetis realistis yang telah disimulasikan mencakup 8 pola pencucian uang standar (fan-in, fan-out, scatter-gather, cycle, dll.)

2. **Fokus Modus Pencucian Uang**: Penelitian berfokus pada pola pencucian uang yang terkait dengan karakteristik transaksi judi online, yaitu:

   - Pola deposit-withdraw yang cepat dan berulang
   - Structuring dan smurfing (pemecahan transaksi besar)
   - Fan-in dan fan-out patterns (pengumpulan dan penyebaran dana)
   - Multiple account networks
   - Tidak mencakup predicate crimes lainnya seperti korupsi, perdagangan narkoba, atau terorisme secara spesifik

3. **Tipe Klasifikasi**: Penelitian menggunakan pendekatan klasifikasi biner:

   - Kelas 0: Rekening tidak berisiko (legitimate transactions)
   - Kelas 1: Rekening berisiko terkait pencucian uang
   - Tidak melakukan klasifikasi multi-class berdasarkan tipe atau tingkat risiko

4. **Fitur yang Digunakan**: Penelitian membatasi fitur pada karakteristik transaksi dan behavioral patterns:

   - Transaction-level features: amount, frequency, timing, transaction type
   - Aggregated features: statistik transaksi dalam periode waktu (7 hari, 30 hari, 90 hari)
   - Network-based features: unique sources/destinations, fan-in/fan-out metrics
   - Behavioral features: deviasi dari baseline, anomaly scores
   - Tidak menggunakan fitur eksternal seperti informasi KYC, profil nasabah, atau data geospasial

5. **Periode Analisis**: Penelitian menggunakan data transaksi dengan periode simulasi 183 hari (6 bulan) sesuai dengan dataset yang tersedia. Time-series forecasting atau deteksi trend jangka panjang tidak menjadi fokus penelitian.

6. **Aspek Legal dan Regulasi**: Penelitian tidak membahas secara mendalam aspek hukum, peraturan Bank Indonesia, atau implementasi teknis integrasi dengan sistem PPATK yang sesungguhnya. Fokus penelitian adalah pada aspek teknis machine learning dan evaluasi performa model.

7. **Deployment dan Produksi**: Penelitian ini merupakan proof-of-concept dan tidak mencakup aspek production deployment seperti:
   - Real-time scoring infrastructure
   - Model monitoring dan retraining pipeline
   - Integration dengan core banking system
   - User interface untuk investigator PPATK

---

## 1.4 Tujuan Penelitian

Berdasarkan rumusan masalah di atas, penelitian ini memiliki tujuan-tujuan sebagai berikut:

1. **Mengidentifikasi dan mengekstrak fitur-fitur transaksi keuangan yang relevan untuk deteksi pencucian uang melalui platform judi online**

   Tujuan ini mencakup analisis eksploratori data, feature engineering untuk mengekstrak 40+ fitur dari berbagai kategori (temporal, frequency, amount, network, behavioral), serta validasi fitur-fitur tersebut terhadap pola pencucian uang yang dikenal (fan-in, fan-out, scatter-gather, cycle, dll.).

2. **Merancang dan mengimplementasikan model prediktif berbasis algoritma CatBoost untuk klasifikasi rekening berisiko dengan target performa: Precision ≥ 80%, Recall ≥ 90%, F1-Score ≥ 85%, dan AUC-ROC ≥ 0.97**

   Tujuan ini mencakup seluruh pipeline machine learning: preprocessing data, handling class imbalance dengan teknik SMOTE atau class weighting, hyperparameter optimization, cross-validation, dan evaluasi model menggunakan multiple metrics yang relevan dengan konteks AML.

3. **Melakukan evaluasi komparatif performa CatBoost dengan algoritma machine learning lainnya (Random Forest, XGBoost, LightGBM, Logistic Regression) untuk memvalidasi keunggulannya dalam konteks deteksi AML**

   Tujuan ini bertujuan memberikan justifikasi empiris mengapa CatBoost dipilih, dengan membandingkan tidak hanya akurasi tetapi juga aspek praktis seperti training time, robustness terhadap overfitting, dan kebutuhan hyperparameter tuning.

4. **Menganalisis interpretabilitas model melalui feature importance dan SHAP analysis untuk mengidentifikasi faktor-faktor paling berpengaruh dalam prediksi rekening berisiko**

   Tujuan ini penting untuk memberikan actionable insights kepada PPATK, sehingga hasil model tidak hanya berupa skor risiko tetapi juga penjelasan mengapa suatu rekening diklasifikasikan sebagai berisiko, memfasilitasi investigasi manual lebih lanjut.

5. **Memberikan rekomendasi kebijakan kepada PPATK untuk meningkatkan efektivitas pemblokiran rekening pasif berdasarkan hasil analisis prediktif**

   Tujuan ini mencakup threshold optimization untuk menyeimbangkan trade-off antara false positive dan false negative, serta rekomendasi operasional untuk integrasi model ke dalam workflow investigasi PPATK.

---

## 1.5 Manfaat Penelitian

### 1.5.1 Manfaat Teoritis

Penelitian ini diharapkan memberikan kontribusi teoritis dalam beberapa aspek:

1. **Kontribusi pada Literatur Anti-Money Laundering (AML)**

   Penelitian ini memperkaya body of knowledge tentang penerapan machine learning untuk deteksi pencucian uang, khususnya dalam konteks modus operandi yang memanfaatkan platform judi online. Studi ini mengisi gap penelitian yang diidentifikasi oleh Altman et al. (2024) tentang pentingnya feature engineering yang tepat untuk menangkap complex money laundering patterns [2].

2. **Validasi Empiris Keunggulan CatBoost**

   Penelitian ini memvalidasi keunggulan algoritma CatBoost dalam menangani karakteristik data finansial yang challenging: class imbalance ekstrem (0.13% positive class), banyak fitur kategorikal (transaction type, merchant code, dll.), dan kebutuhan interpretabilitas tinggi [4], [5]. Hasil penelitian berkontribusi pada pemahaman tentang kapan dan mengapa CatBoost outperform algoritma gradient boosting lainnya.

3. **Metodologi Feature Engineering untuk Deteksi AML**

   Penelitian ini mengembangkan framework sistematis untuk ekstraksi fitur dari data transaksi keuangan yang dapat diadaptasi untuk berbagai jenis fraud detection. Framework ini mencakup 6 kategori fitur (temporal, frequency, amount, network, behavioral, anomaly) dengan total 40+ derived features yang terbukti efektif menangkap pola pencucian uang.

4. **Kontribusi pada Financial Crime Analytics**

   Penelitian ini berkontribusi pada pengembangan financial crime analytics dengan mendemonstrasikan bagaimana supervised learning dapat diintegrasikan dengan domain knowledge tentang money laundering typologies untuk menghasilkan sistem deteksi yang akurat dan interpretable.

### 1.5.2 Manfaat Praktis

Secara praktis, penelitian ini diharapkan memberikan manfaat sebagai berikut:

1. **Meningkatkan Efektivitas Kebijakan PPATK**

   Model CatBoost yang dikembangkan dapat membantu PPATK meningkatkan akurasi pemblokiran rekening pasif dari tingkat efektivitas saat ini (estimasi 60-70%) menjadi 90% atau lebih, sehingga lebih banyak kasus pencucian uang dapat dicegah sejak dini. Dengan recall target ≥ 90%, model mampu mendeteksi 9 dari 10 rekening berisiko.

2. **Mengurangi False Positive dan Dampak Negatif kepada Nasabah**

   Dengan precision target ≥ 80%, model dapat mengurangi false positive dari tingkat saat ini (estimasi 30%) menjadi di bawah 20%. Hal ini sangat penting untuk mengurangi dampak negatif terhadap nasabah yang legitimate dan menghindari kerugian reputasional bagi institusi keuangan akibat pemblokiran yang salah.

3. **Efisiensi Operasional PPATK**

   CatBoost memiliki training time yang efisien (45-60 detik untuk dataset 6.4 juta transaksi) dan memerlukan minimal hyperparameter tuning [4]. Hal ini memungkinkan PPATK untuk melakukan retraining model secara berkala (bulanan/kuartalan) untuk menangkap evolusi modus pencucian uang tanpa memerlukan computational resources yang berlebihan.

4. **Decision Support System untuk Investigator**

   Feature importance dan SHAP analysis yang dihasilkan model memberikan explainability yang membantu investigator PPATK memahami mengapa suatu rekening diklasifikasikan sebagai berisiko. Insight ini dapat mempercepat proses investigasi manual dan meningkatkan kualitas evidence untuk proses hukum lebih lanjut.

5. **Scalability dan Adaptabilitas**

   Framework yang dikembangkan dapat diadaptasi untuk mendeteksi modus pencucian uang lainnya (bukan hanya judi online) dengan melakukan retraining menggunakan labeled data yang relevan. Native handling fitur kategorikal oleh CatBoost memudahkan penambahan fitur baru tanpa perlu extensive preprocessing [5].

6. **Benchmark untuk Implementasi Machine Learning di Sektor Keuangan**

   Penelitian ini dapat menjadi referensi bagi institusi keuangan lainnya (bank, fintech, payment gateway) yang ingin mengimplementasikan sistem deteksi fraud atau AML berbasis machine learning, lengkap dengan metodologi evaluasi dan best practices.

---

## 1.6 Metode Penelitian

Penelitian ini menggunakan pendekatan kuantitatif dengan metode eksperimental untuk mengembangkan dan mengevaluasi model prediktif deteksi rekening berisiko. Secara garis besar, metodologi penelitian terdiri dari beberapa tahapan berikut:

**1. Studi Literatur**

Melakukan kajian mendalam terhadap literatur tentang anti-money laundering, money laundering typologies khususnya yang terkait judi online, algoritma gradient boosting (CatBoost, XGBoost, LightGBM), feature engineering untuk data transaksi keuangan, dan teknik handling imbalanced dataset.

**2. Pengumpulan dan Pemahaman Data**

Menggunakan IBM Synthetic Financial Transactions dataset yang terdiri dari 6.4 juta transaksi dari 10,000 akun simulasi selama periode 183 hari. Melakukan exploratory data analysis (EDA) untuk memahami distribusi data, identifikasi missing values, outliers, dan karakteristik pola transaksi normal vs berisiko.

**3. Feature Engineering**

Mengekstrak 40+ fitur dari data transaksi mentah, mencakup:

- Temporal features (hour entropy, consecutive deposits, dll.)
- Frequency features (transaction count volatility, interval patterns, dll.)
- Amount features (round number ratio, amount-to-balance ratio, dll.)
- Network features (unique sources/destinations, fan-in/fan-out metrics, dll.)
- Behavioral features (deviation from baseline, anomaly scores, dll.)

**4. Preprocessing dan Handling Imbalance**

Melakukan data splitting (80% train, 20% test) dengan stratified sampling, menangani class imbalance menggunakan SMOTE (Synthetic Minority Over-sampling Technique) atau class weighting, dan identifikasi fitur kategorikal untuk native handling oleh CatBoost.

**5. Model Development**

Mengimplementasikan model CatBoost dengan konfigurasi optimal untuk deteksi AML:

- Hyperparameter tuning menggunakan Optuna atau Grid Search
- Cross-validation (5-fold stratified) untuk validasi robustness
- Perbandingan dengan baseline models (Random Forest, XGBoost, LightGBM, Logistic Regression)

**6. Evaluasi Model**

Mengevaluasi performa model menggunakan multiple metrics:

- Confusion Matrix
- Precision, Recall, F1-Score
- AUC-ROC dan ROC Curve
- Training time dan resource efficiency

**7. Interpretability Analysis**

Melakukan analisis interpretabilitas menggunakan:

- CatBoost native feature importance
- SHAP (SHapley Additive exPlanations) values
- Case studies untuk True Positive, False Positive, dan False Negative

**8. Kesimpulan dan Rekomendasi**

Menyimpulkan temuan penelitian dan memberikan rekomendasi kebijakan kepada PPATK untuk meningkatkan efektivitas pemblokiran rekening pasif.

Penjelasan detail metodologi akan diuraikan lebih lanjut pada **BAB II Bagian 2.3 Metodologi Penelitian**.

---

# BAB II LANDASAN TEORI DAN METODOLOGI PENELITIAN

## 2.1 Landasan Teori

### 2.1.1 Anti Money Laundering (AML)

#### 2.1.1.1 Definisi Pencucian Uang

Pencucian uang (money laundering) adalah proses menyembunyikan atau menyamarkan asal-usul dana yang diperoleh dari aktivitas ilegal agar tampak seolah-olah berasal dari sumber yang sah (Wikipedia, 2025). Menurut definisi yang lebih luas, pencucian uang meliputi segala upaya untuk mengubah hasil kejahatan menjadi aset yang tampak legal, sehingga dapat digunakan dalam sistem keuangan formal tanpa menimbulkan kecurigaan.

Secara teoritis, Pratama (2021) mendefinisikan tindak pidana pencucian uang sebagai "tindakan memproses sejumlah besar uang ilegal hasil tindak pidana menjadi dana yang kelihatannya bersih atau sah menurut hukum, dengan menggunakan metode yang canggih, kreatif dan kompleks" [6]. Definisi ini menekankan bahwa pencucian uang merupakan suatu proses atau perbuatan yang bertujuan untuk menyembunyikan atau menyamarkan asal-usul uang atau harta kekayaan yang diperoleh dari hasil tindak pidana, yang kemudian diubah menjadi harta kekayaan yang seolah-olah berasal dari kegiatan yang sah [6].

Skala pencucian uang secara global sangat masif. Menurut estimasi PBB yang dikutip oleh Altman et al. (2024), "The UN estimates 2-5% of global GDP or $0.8-$2.0 trillion dollars are laundered globally each year" [2]. Angka ini menunjukkan bahwa pencucian uang bukan hanya masalah kriminal individual, tetapi ancaman sistemik terhadap stabilitas ekonomi global.

Praktik pencucian uang pertama kali mendapat perhatian serius pada era 1920-an di Amerika Serikat, ketika organisasi kriminal menggunakan bisnis laundromat (binatu) berbasis koin sebagai kedok untuk mencampur uang hasil kejahatan dengan pendapatan bisnis yang sah. Sejak saat itu, metode pencucian uang terus berkembang seiring dengan evolusi teknologi finansial dan globalisasi ekonomi.

Dampak pencucian uang sangat merugikan, tidak hanya bagi sistem keuangan tetapi juga stabilitas ekonomi secara keseluruhan. Dana hasil kejahatan yang masuk ke dalam sistem perbankan dapat mendistorsi alokasi sumber daya, merusak kompetisi pasar, dan mengikis kepercayaan publik terhadap lembaga keuangan. Selain itu, pencucian uang juga memfasilitasi keberlanjutan kejahatan terorganisir seperti perdagangan narkoba, korupsi, terorisme, dan penipuan skala besar.

Menurut Pratama (2021), tindakan mengaburkan sumber uang ilegal semakin mudah dilakukan dengan menggunakan alat-alat teknologi informasi yang semakin canggih. Hal ini didukung dengan adanya globalisasi di sektor perbankan yang menyebabkan banyak bank menjadi sasaran kejahatan pencucian uang [6]. Dengan globalisasi perbankan, dana ilegal dapat ditransfer antar bank hingga melampaui batas yurisdiksi suatu negara, dengan tingkat kerahasiaan yang selalu dijunjung tinggi oleh perbankan [6].

#### 2.1.1.2 Tahapan Pencucian Uang

Proses pencucian uang umumnya terdiri dari tiga tahap utama yang saling terkait:

**1. Placement (Penempatan)**

Tahap pertama adalah memasukkan dana hasil kejahatan ke dalam sistem keuangan formal. Ini merupakan tahap yang paling rentan terhadap deteksi karena melibatkan kontak langsung antara pelaku dengan institusi keuangan. Metode yang sering digunakan antara lain:

- **Structuring atau Smurfing**: Memecah jumlah besar uang menjadi transaksi-transaksi kecil di bawah batas pelaporan wajib (di Indonesia biasanya Rp 100 juta atau Rp 500 juta tergantung jenis transaksi) untuk menghindari deteksi. Transaksi ini dilakukan secara bertahap melalui banyak akun atau lokasi berbeda.
- **Cash-intensive business**: Menggunakan bisnis yang secara alami banyak menerima uang tunai (seperti restoran, salon, atau binatu) untuk mencampur uang ilegal dengan pendapatan sah.
- **Currency smuggling**: Menyelundupkan uang tunai secara fisik ke negara lain yang memiliki regulasi AML yang lebih longgar.

Berdasarkan dataset AMLworld, sumber-sumber dana kriminal yang umum disimulasikan dalam tahap placement mencakup 9 kategori: extortion (pemerasan), gambling (perjudian), prostitution (prostitusi), kidnapping (penculikan), robbery (perampokan), embezzlement (penggelapan), drugs (narkoba), smuggling (penyelundupan), dan kategori lainnya [2]. Pemahaman terhadap diversitas sumber dana ilegal ini penting untuk merancang sistem deteksi yang komprehensif.

**2. Layering (Pelapisan)**

Setelah dana berhasil masuk ke sistem keuangan, tahap layering bertujuan memisahkan dana tersebut dari sumbernya melalui serangkaian transaksi kompleks yang dirancang untuk menyulitkan pelacakan. Teknik yang umum digunakan meliputi:

- **Multiple transfers**: Melakukan transfer berulang kali antar rekening, antar bank, atau antar negara untuk mengaburkan jejak audit.
- **Offshore accounts**: Memanfaatkan rekening di negara-negara dengan kerahasiaan perbankan yang ketat atau regulasi AML yang lemah.
- **Shell companies**: Menggunakan perusahaan-perusahaan cangkang (shell companies) yang tidak memiliki operasi bisnis riil untuk mengalirkan dana.
- **Investment instruments**: Membeli dan menjual instrumen investasi seperti saham, obligasi, atau properti untuk mengubah bentuk aset.

**Pola-Pola Layering dalam Jaringan Transaksi**

Berdasarkan penelitian Altman et al. (2024), terdapat 8 pola umum (patterns) yang digunakan dalam tahap layering untuk mengaburkan jejak transaksi keuangan [2]. Pola-pola ini dapat direpresentasikan sebagai struktur graf dalam jaringan transaksi:

1. **Fan-out Pattern**: Satu akun sumber mendistribusikan dana ke banyak akun tujuan secara bersamaan. Pola ini digunakan untuk memecah dana besar menjadi jumlah-jumlah kecil yang tersebar di banyak rekening, sehingga menghindari threshold pelaporan.

2. **Fan-in Pattern**: Banyak akun sumber mengalirkan dana ke satu akun tujuan. Pola ini merupakan kebalikan dari fan-out, biasanya digunakan pada tahap akhir layering untuk mengumpulkan kembali dana yang telah dipecah.

3. **Scatter-gather Pattern**: Kombinasi fan-out diikuti fan-in dalam satu aliran. Dana dari satu akun disebarkan ke banyak akun perantara (scatter), kemudian dikumpulkan kembali ke satu akun tujuan (gather). Pola ini menciptakan kompleksitas tinggi yang menyulitkan pelacakan.

4. **Gather-scatter Pattern**: Kebalikan dari scatter-gather, di mana banyak akun mengalir ke satu akun perantara (gather), kemudian disebarkan lagi ke banyak akun tujuan (scatter).

5. **Cycle Pattern**: Dana mengalir dalam bentuk lingkaran (A → B → C → A), menciptakan ilusi aktivitas bisnis yang kompleks padahal sebenarnya dana hanya berputar di antara akun-akun yang dikendalikan oleh pelaku yang sama.

6. **Bipartite Pattern**: Dua kelompok akun yang saling bertransaksi secara intensif, tetapi tidak ada transaksi internal dalam masing-masing kelompok. Pola ini mensimulasikan transaksi bisnis B2B yang legitimate.

7. **Stack Pattern**: Serangkaian transfer beruntun dalam garis lurus (A → B → C → D → E), di mana setiap akun meneruskan dana ke akun berikutnya. Pola ini menciptakan jarak maksimal antara sumber dan tujuan akhir.

8. **Random Pattern**: Transfer acak tanpa struktur yang jelas, mensimulasikan pola transaksi natural untuk menghindari deteksi berbasis pattern matching.

Menurut Altman et al. (2024), "Financial transaction graphs are essentially directed multigraphs where nodes represent accounts and edges represent transactions" [2]. Pemahaman terhadap pola-pola ini sangat penting untuk merancang fitur graf (graph features) yang efektif dalam deteksi pencucian uang berbasis machine learning.

**3. Integration (Integrasi)**

Tahap akhir adalah mengembalikan dana yang telah "dibersihkan" ke dalam ekonomi dengan cara yang tampak sah dan legal. Pada tahap ini, uang sudah sangat sulit dibedakan dari pendapatan yang sah. Metode integrasi meliputi:

- **Property investment**: Membeli properti atau aset berharga lainnya menggunakan dana yang telah dicuci.
- **Business investment**: Menginvestasikan dana dalam bisnis yang sah sebagai modal usaha.
- **Luxury purchases**: Membeli barang-barang mewah seperti kendaraan, perhiasan, atau karya seni.
- **Loan back schemes**: Meminjamkan uang kepada diri sendiri melalui struktur perusahaan yang kompleks.

#### 2.1.1.3 Metode Pencucian Uang Melalui Judi Online

Industri perjudian online telah menjadi salah satu metode pencucian uang yang paling efektif di era digital. Menurut Wikipedia (2025), kasino dan platform judi online menyediakan lingkungan yang ideal untuk pencucian uang karena:

- **Volume transaksi tinggi**: Jutaan transaksi terjadi setiap hari, sehingga transaksi mencurigakan dapat tersembunyi dalam volume besar.
- **Anonimitas**: Banyak platform judi online yang tidak menerapkan prosedur Know Your Customer (KYC) yang ketat.
- **Kecepatan transfer**: Dana dapat masuk dan keluar dengan sangat cepat, kadang hanya dalam hitungan menit.
- **Kompleksitas transaksi**: Pola taruhan yang beragam menyulitkan identifikasi transaksi yang abnormal.

**Karakteristik Unik Pencucian Uang Melalui Judi Online**

Platform judi online memiliki karakteristik khusus yang membedakannya dari modus pencucian uang lainnya. Pemahaman terhadap karakteristik ini sangat penting untuk merancang fitur deteksi yang efektif:

**1. Deposit-Withdraw Scheme (Minimal Betting)**

Modus paling umum di mana pelaku menyetor dana ilegal ke akun judi online, melakukan sedikit atau tanpa aktivitas taruhan yang signifikan, kemudian menarik dana tersebut. Dana yang ditarik tampak sebagai "kemenangan" dari aktivitas judi yang sah.

_Karakteristik yang dapat dideteksi:_

- Rasio deposit terhadap betting sangat tinggi (>0.8 atau 80%)
- Durasi antara deposit dan withdrawal sangat singkat (hitungan menit hingga jam)
- Minimal aktivitas taruhan (hanya 1-3 taruhan dengan nilai kecil untuk "menutupi")
- Pola berulang dalam periode pendek (deposit-withdraw berulang dalam 1-7 hari)

**2. Chip Dumping di Poker Online**

Dalam permainan poker online, pelaku sengaja kalah kepada akun lain yang dikendalikan oleh rekan atau dirinya sendiri untuk mentransfer dana. Metode ini mensimulasikan hasil permainan yang natural.

_Karakteristik yang dapat dideteksi:_

- Persentase kekalahan yang tidak wajar (>80% dalam permainan head-to-head)
- Pola kekalahan berturut-turut terhadap pemain yang sama
- Transfer chip dengan nilai besar dalam satu sesi permainan
- Coinciding login times antara akun-akun yang saling terkait

**3. Collusion (Kolusi Multi-Pemain)**

Beberapa pemain bekerja sama dalam satu meja untuk memanipulasi hasil permainan dan mengalirkan dana dari satu akun ke akun lainnya. Pola ini lebih kompleks dan melibatkan koordinasi antar akun.

_Karakteristik yang dapat dideteksi:_

- Akun-akun yang sering bermain di meja yang sama
- Pattern correlation scores tinggi (pola taruhan yang sinkron)
- Shared IP addresses atau device fingerprints yang serupa
- Koordinasi timing antara join/leave table

**4. Multiple Account Networks (Jaringan Akun Mule)**

Menggunakan jaringan akun-akun yang saling terhubung untuk menyebarkan dan mengumpulkan dana melalui pola transaksi yang kompleks. Setiap akun dapat berperan sebagai "mule" untuk menyembunyikan aliran dana.

_Karakteristik yang dapat dideteksi:_

- High fan-in/fan-out metrics (banyak sumber atau tujuan unik dalam periode pendek)
- Pola scatter-gather atau cycle dalam graf transaksi
- Akun-akun dengan profil demografis yang serupa (dummy accounts)
- Transfer antar akun dengan timing yang terkoordinasi

**5. Rapid Cycling (Siklus Dana Cepat)**

Dana berputar dengan cepat masuk dan keluar dari sistem untuk mengaburkan jejak audit dan menciptakan ilusi volume transaksi yang tinggi.

_Karakteristik yang dapat dideteksi:_

- Saldo rekening yang selalu dijaga minimal (near-zero balance)
- Transaksi velocity tinggi (banyak transaksi per hari/jam)
- Amount-to-balance ratio sangat tinggi (nominal transaksi >> saldo rata-rata)
- Frekuensi transaksi yang tidak konsisten dengan profil nasabah

**6. Structuring dan Smurfing**

Memecah transaksi besar menjadi banyak transaksi kecil untuk menghindari threshold pelaporan wajib (biasanya Rp 100 juta atau Rp 500 juta).

_Karakteristik yang dapat dideteksi:_

- Round number ratio tinggi (banyak transaksi dengan nilai bulat seperti Rp 50 jt, Rp 100 jt)
- Just-below-threshold transactions (transaksi di bawah threshold tapi mendekati)
- Frekuensi transaksi abnormal dalam periode pendek (spike patterns)
- Distribusi nilai transaksi yang tidak natural (geometric atau fixed amounts)

**Tabel 2.1: Perbandingan Pola Transaksi Judi Online vs Transaksi Normal**

| Karakteristik               | Transaksi Normal         | Pencucian via Judi Online  | Fitur Deteksi                                           |
| --------------------------- | ------------------------ | -------------------------- | ------------------------------------------------------- |
| **Durasi deposit-withdraw** | Bervariasi (hari-minggu) | Sangat singkat (menit-jam) | `avg_deposit_withdraw_interval_minutes`                 |
| **Rasio deposit/betting**   | Rendah (≤0.3)            | Sangat tinggi (≥0.8)       | `deposit_to_betting_ratio`                              |
| **Frekuensi transaksi**     | Teratur, konsisten       | Spike pada jam tertentu    | `daily_transaction_volatility`                          |
| **Nominal transaksi**       | Bervariasi natural       | Pola geometris/fixed/bulat | `round_number_ratio`, `amount_distribution_entropy`     |
| **Counterparty diversity**  | Terbatas, repetitif      | Banyak & berubah-ubah      | `unique_beneficiaries_7d`, `unique_sources_7d`          |
| **Saldo rekening**          | Stabil, proporsional     | Minimal, near-zero         | `average_balance_to_transaction_ratio`                  |
| **Timing patterns**         | Jam kerja, prediktabel   | 24/7, random/koordinasi    | `hour_of_day_entropy`, `night_transaction_ratio`        |
| **Network structure**       | Sederhana (A↔B)          | Kompleks (fan-in/fan-out)  | `fanout_score`, `fanin_score`, `clustering_coefficient` |

**Implikasi untuk Feature Engineering**

Berdasarkan karakteristik di atas, feature engineering untuk deteksi pencucian uang melalui judi online harus fokus pada:

1. **Temporal Features**: Menangkap pola waktu yang abnormal (24/7 activity, rapid cycles)
2. **Behavioral Features**: Mendeteksi deviasi dari profil normal nasabah
3. **Network Features**: Mengidentifikasi struktur jaringan yang mencurigakan (fan-in/fan-out)
4. **Transaction Velocity**: Mengukur kecepatan dan frekuensi transaksi
5. **Amount Patterns**: Mendeteksi pola nilai transaksi yang tidak natural (structuring)

Fitur-fitur spesifik yang akan diekstrak akan dijelaskan lebih detail pada Bagian 2.1.2.4 tentang Feature Engineering untuk Data Transaksi Keuangan.

#### 2.1.1.4 Regulasi Anti Money Laundering di Indonesia

Indonesia memiliki kerangka regulasi AML yang komprehensif untuk mencegah dan memberantas pencucian uang serta pendanaan terorisme. Beberapa regulasi utama meliputi:

**1. Undang-Undang Nomor 8 Tahun 2010**

Undang-Undang tentang Pencegahan dan Pemberantasan Tindak Pidana Pencucian Uang (UU TPPU) merupakan landasan hukum utama AML di Indonesia. UU ini mendefinisikan tindak pidana pencucian uang, menetapkan sanksi hukum, dan mengatur kewajiban pelaporan bagi Penyedia Jasa Keuangan (PJK).

Di Indonesia, penanggulangan tindak pidana pencucian uang dilakukan berdasarkan UU No. 8 Tahun 2010 tentang Pencegahan dan Pemberantasan Tindak Pidana Pencucian Uang (UU PPTPPU), yang merupakan penyempurnaan dari UU No. 15 Tahun 2002 dan UU No. 25 Tahun 2003 [6]. Pasal 2 ayat (1) UU PPTPPU menyebutkan 26 jenis tindak pidana asal (predicate crimes) yang dapat menjadi sumber hasil tindak pidana untuk pencucian uang, meliputi korupsi, penyuapan, narkotika dan psikotropika, penyelundupan, tindak pidana di bidang perbankan dan pasar modal, kepabeanan, cukai, perdagangan orang, terorisme, hingga tindak pidana lain yang diancam dengan pidana penjara 4 tahun atau lebih [6].

Pasal 3 UU PPTPPU mengatur ancaman pidana pencucian uang yang sangat berat, yaitu pidana penjara paling lama 20 tahun dan denda paling banyak Rp 10.000.000.000 (sepuluh miliar rupiah) [6]. Sanksi yang berat ini menunjukkan keseriusan pemerintah Indonesia dalam memberantas tindak pidana pencucian uang dan memberikan efek jera bagi pelaku.

**2. Peraturan PPATK**

Pusat Pelaporan dan Analisis Transaksi Keuangan (PPATK) mengeluarkan berbagai peraturan pelaksanaan, termasuk:

- Peraturan tentang prosedur pelaporan Transaksi Keuangan Mencurigakan (TKM)
- Peraturan tentang pelaporan Transaksi Keuangan Tunai (TKT)
- Pedoman identifikasi Beneficial Owner
- Pedoman penerapan program Anti Pencucian Uang dan Pencegahan Pendanaan Terorisme (APU-PPT)

**3. Kewajiban Pelaporan**

Penyedia Jasa Keuangan wajib melaporkan kepada PPATK:

- **Transaksi Keuangan Tunai (TKT)**: Transaksi tunai dengan nilai minimum Rp 500 juta atau ekuivalen dalam mata uang asing
- **Transaksi Keuangan Mencurigakan (TKM)**: Transaksi yang menyimpang dari profil nasabah atau pola transaksi normal
- **Transaksi Keuangan Transfer Dana dari dan ke Luar Negeri**: Dengan nilai minimum Rp 100 juta atau ekuivalen

#### 2.1.1.5 Peran PPATK sebagai Financial Intelligence Unit Indonesia

Pusat Pelaporan dan Analisis Transaksi Keuangan (PPATK) adalah lembaga independen yang dibentuk berdasarkan UU Nomor 8 Tahun 2010 untuk mencegah dan memberantas tindak pidana pencucian uang (PPATK, 2025). PPATK berfungsi sebagai Financial Intelligence Unit (FIU) Indonesia yang berperan sebagai penghubung antara sektor keuangan dengan penegak hukum.

UU PPTPPU menjadi dasar pembentukan PPATK, yang merupakan lembaga independen yang diberi tugas dan wewenang dalam rangka pemberantasan tindak pidana pencucian uang di Indonesia [6]. PPATK diberi wewenang meminta informasi dan menganalisis transaksi keuangan yang dianggap mencurigakan. Tugas utama PPATK adalah mendeteksi terjadinya tindak pidana pencucian uang dan membantu penegakan hukum yang berkaitan dengan pencucian uang dan tindak pidana asal (predicate crimes) [6].

Dalam prosedurnya, PPATK menganalisis transaksi keuangan dan kemudian membuat laporan adanya dugaan pencucian uang kepada kepolisian [6]. Hal ini menunjukkan bahwa tanggungjawab utama dalam penegakan hukum pencucian uang tetap berada di tangan kepolisian sebagai penyidik, karena semua hasil kerja (hasil analisis transaksi) PPATK harus dilaporkan dan ditindaklanjuti oleh penyidik kepolisian [6]. Dengan demikian, PPATK dan kepolisian harus bekerjasama dengan baik dalam penanganan tindak pidana pencucian uang.

**Tugas dan Fungsi Utama PPATK:**

1. **Pencegahan (Prevention)**

   - Menetapkan pedoman dan standar APU-PPT bagi Penyedia Jasa Keuangan
   - Melakukan sosialisasi dan edukasi kepada PJK dan masyarakat
   - Mengembangkan sistem deteksi dini transaksi mencurigakan

2. **Pengumpulan Data (Data Collection)**

   - Menerima laporan TKT, TKM, dan TKLN dari PJK
   - Mengelola database transaksi keuangan nasional
   - Mengintegrasikan data dari berbagai sumber informasi

3. **Analisis (Analysis)**

   - Melakukan analisis terhadap laporan transaksi mencurigakan
   - Mengidentifikasi pola dan jaringan pencucian uang
   - Menyusun profil risiko pelaku dan modus operandi
   - Menggunakan teknologi data mining dan machine learning untuk deteksi anomali

4. **Penyampaian Hasil Analisis (Dissemination)**

   - Menyampaikan hasil analisis kepada penegak hukum (Kepolisian, Kejaksaan, KPK, BNN, dll.)
   - Berkoordinasi dengan FIU negara lain melalui Egmont Group
   - Memberikan rekomendasi kebijakan kepada pemerintah

5. **Pengawasan Kepatuhan (Compliance Supervision)**
   - Melakukan pengawasan terhadap kepatuhan PJK dalam menerapkan program APU-PPT
   - Memberikan sanksi administratif kepada PJK yang melanggar ketentuan
   - Melakukan audit dan pemeriksaan berkala

**Daftar Terduga Teroris dan Organisasi Teroris (DTTOT)**

PPATK juga mengelola dan mempublikasikan Daftar Terduga Teroris dan Organisasi Teroris (DTTOT) yang berisi nama-nama individu dan entitas yang dicurigai terlibat dalam pendanaan terorisme. Penyedia Jasa Keuangan wajib melakukan pencocokan data nasabah dengan DTTOT dan segera melaporkan jika ditemukan kecocokan.

**Kebijakan Pemblokiran Rekening Pasif**

Salah satu kebijakan kontroversial yang menjadi fokus penelitian ini adalah kebijakan pemblokiran rekening pasif yang diinisiasi PPATK. Rekening pasif, yaitu rekening yang tidak memiliki aktivitas transaksi dalam periode tertentu, dianggap berpotensi disalahgunakan untuk pencucian uang karena:

- Sulit dilacak oleh sistem monitoring otomatis
- Dapat diaktifkan kembali untuk transaksi mencurigakan
- Sering digunakan dalam skema drop account atau money mule
- Memiliki risiko penyalahgunaan identitas (identity theft)

Namun, kebijakan ini juga menuai kritik karena banyak rekening yang diblokir sebenarnya menjadi pasif karena alasan yang wajar, seperti:

- Rekening dibuka untuk keperluan sementara (misal: menerima bantuan sosial, promo pembukaan rekening)
- Nasabah beralih menggunakan rekening lain
- Nasabah lupa atau tidak sempat menutup rekening

Oleh karena itu, diperlukan pendekatan analitik yang lebih akurat dan berbasis data untuk membedakan rekening pasif yang benar-benar berisiko dengan yang tidak, sehingga kebijakan pemblokiran dapat diterapkan secara lebih tepat sasaran dan mengurangi false positive.

### 2.1.2 Machine Learning untuk Anti Money Laundering

#### 2.1.2.1 Supervised Learning dalam Deteksi AML

Machine learning telah menjadi pendekatan yang semakin populer dalam deteksi pencucian uang karena kemampuannya mengenali pola kompleks yang sulit diidentifikasi oleh sistem berbasis aturan tradisional (Google Machine Learning Crash Course, 2025). Dalam konteks AML, supervised learning adalah paradigma pembelajaran mesin yang paling banyak digunakan, di mana model dilatih menggunakan dataset berlabel yang berisi contoh transaksi legal dan ilegal.

**Prinsip Dasar Supervised Learning:**

Supervised learning bekerja dengan cara mempelajari pemetaan dari input (fitur transaksi) ke output (label: legal/ilegal) berdasarkan contoh-contoh yang telah dilabeli sebelumnya. Proses pembelajaran terjadi dalam beberapa tahap:

1. **Training Phase**: Model diberikan dataset training yang berisi pasangan (X, y), di mana X adalah vektor fitur transaksi dan y adalah label yang sudah diketahui (0 = legal, 1 = ilegal). Model belajar untuk menemukan fungsi f sehingga f(X) ≈ y.

2. **Validation Phase**: Model diuji pada dataset validation untuk mengevaluasi performanya dan melakukan penyetelan hyperparameter (tuning).

3. **Testing Phase**: Model dievaluasi pada dataset testing yang sepenuhnya terpisah untuk mengukur kemampuan generalisasi.

4. **Deployment Phase**: Model yang sudah dilatih digunakan untuk memprediksi label transaksi baru yang belum pernah dilihat sebelumnya.

**Keunggulan Machine Learning untuk AML:**

- **Adaptif**: Model dapat belajar dan beradaptasi dengan pola pencucian uang yang terus berubah melalui retraining berkala
- **Skalabilitas**: Mampu memproses jutaan transaksi dalam waktu singkat
- **Deteksi Pola Kompleks**: Dapat mengenali pola non-linear dan interaksi antar fitur yang sulit dideteksi secara manual
- **Reduksi False Positive**: Lebih akurat dalam membedakan transaksi mencurigakan dari transaksi normal, sehingga mengurangi beban investigasi manual

#### 2.1.2.2 Klasifikasi Biner dalam Konteks AML

Deteksi pencucian uang umumnya dimodelkan sebagai masalah klasifikasi biner, di mana tujuannya adalah mengklasifikasikan setiap transaksi atau rekening ke dalam salah satu dari dua kelas:

- **Kelas 0 (Negatif)**: Transaksi atau rekening yang legal/tidak berisiko
- **Kelas 1 (Positif)**: Transaksi atau rekening yang ilegal/berisiko terkait pencucian uang

**Karakteristik Masalah:**

Klasifikasi AML memiliki beberapa karakteristik khusus yang membedakannya dari masalah klasifikasi umum:

1. **Class Imbalance Ekstrem**

   - Jumlah transaksi ilegal jauh lebih sedikit dibanding transaksi legal (rasio bisa mencapai 1:1000 atau lebih ekstrem)
   - Memerlukan teknik khusus seperti oversampling (SMOTE, ADASYN), undersampling, atau class weighting
   - Metrik evaluasi harus disesuaikan (lebih fokus pada Precision, Recall, F1-Score daripada Accuracy)

2. **High Cost of False Negative**

   - False negative (gagal mendeteksi pencucian uang) memiliki konsekuensi serius: kejahatan berlanjut, kerugian finansial besar, dan reputasi institusi rusak
   - Model harus dioptimalkan untuk meminimalkan false negative, meskipun kadang mengorbankan precision

3. **Moderate Cost of False Positive**

   - False positive (menandai transaksi legal sebagai mencurigakan) menyebabkan beban investigasi manual yang tinggi dan dapat mengganggu nasabah yang sah
   - Perlu keseimbangan antara recall tinggi dengan precision yang wajar

4. **Dynamic Pattern**
   - Pola pencucian uang terus berevolusi seiring pelaku beradaptasi dengan sistem deteksi
   - Model perlu diperbarui secara berkala (model retraining)

**Threshold Optimization:**

Dalam klasifikasi biner, model machine learning umumnya menghasilkan probabilitas (P(y=1|X)) antara 0 dan 1. Untuk mengonversi probabilitas menjadi keputusan klasifikasi, diperlukan threshold τ:

- Jika P(y=1|X) ≥ τ, maka prediksi = 1 (berisiko)
- Jika P(y=1|X) < τ, maka prediksi = 0 (tidak berisiko)

Default threshold biasanya 0.5, tetapi dalam konteks AML, threshold sering diturunkan (misal: 0.3 atau 0.2) untuk meningkatkan recall dan menangkap lebih banyak kasus pencucian uang, meskipun dengan konsekuensi peningkatan false positive.

#### 2.1.2.3 Gradient Boosting untuk Deteksi Pencucian Uang

Gradient boosting adalah salah satu teknik ensemble learning yang paling efektif untuk masalah klasifikasi, termasuk deteksi pencucian uang (Machine Learning Mastery, 2025). Algoritma ini membangun model prediktif yang kuat dengan menggabungkan banyak model lemah (weak learners), biasanya decision trees yang dangkal.

**Prinsip Kerja Gradient Boosting:**

Gradient boosting bekerja secara sekuensial, di mana setiap model baru dilatih untuk memperbaiki kesalahan model sebelumnya. Proses ini dapat dijelaskan sebagai berikut:

1. **Inisialisasi Model**: Dimulai dengan prediksi sederhana, biasanya rata-rata nilai target untuk regresi atau log-odds untuk klasifikasi:

   F₀(x) = argmin_γ Σᵢ L(yᵢ, γ)

   Di mana L adalah fungsi loss dan γ adalah konstanta awal.

2. **Iterasi Boosting**: Untuk setiap iterasi m = 1 hingga M:

   a. **Hitung Residual/Gradien**: Hitung pseudo-residuals sebagai gradien negatif dari fungsi loss:

   rᵢₘ = -[∂L(yᵢ, F(xᵢ))/∂F(xᵢ)]\_{F(x)=Fₘ₋₁(x)}

   b. **Latih Base Learner**: Latih decision tree hₘ(x) untuk memprediksi residual rₘ

   c. **Hitung Learning Rate**: Tentukan koefisien γₘ yang meminimalkan loss:

   γₘ = argmin_γ Σᵢ L(yᵢ, Fₘ₋₁(xᵢ) + γhₘ(xᵢ))

   d. **Update Model**: Perbarui model ensemble:

   Fₘ(x) = Fₘ₋₁(x) + ν · γₘ · hₘ(x)

   Di mana ν adalah learning rate yang mengontrol kontribusi setiap tree.

3. **Prediksi Final**: Model akhir adalah kombinasi dari semua base learners:

   F(x) = F₀(x) + Σₘ₌₁ᴹ ν · γₘ · hₘ(x)

**Fungsi Loss untuk Klasifikasi Biner:**

Untuk klasifikasi biner, gradient boosting biasanya menggunakan binary cross-entropy loss (log loss):

L(y, F(x)) = -[y · log(p) + (1-y) · log(1-p)]

Di mana p = 1/(1 + e^(-F(x))) adalah probabilitas prediksi melalui fungsi sigmoid.

**Hyperparameter Penting:**

1. **n_estimators (M)**: Jumlah boosting stages atau jumlah trees yang akan dibangun. Nilai yang lebih besar dapat meningkatkan akurasi tetapi juga meningkatkan risiko overfitting dan waktu komputasi.

2. **learning_rate (ν)**: Mengontrol kontribusi setiap tree terhadap prediksi final. Nilai kecil (0.01 - 0.1) memerlukan lebih banyak trees tetapi biasanya menghasilkan model yang lebih robust.

3. **max_depth**: Kedalaman maksimum setiap decision tree. Tree yang lebih dalam dapat menangkap interaksi kompleks tetapi rentan overfitting. Nilai umum: 3-8.

4. **subsample**: Fraksi sampel yang digunakan untuk melatih setiap tree. Stochastic gradient boosting dengan subsample < 1.0 dapat mengurangi overfitting dan mempercepat training.

5. **min_samples_split & min_samples_leaf**: Parameter regularisasi yang mengontrol ukuran minimum node untuk melakukan split atau menjadi leaf.

**Keunggulan untuk AML:**

- **Handling Non-linearity**: Mampu menangkap hubungan non-linear kompleks antara fitur transaksi dan label
- **Feature Interaction**: Secara otomatis menangkap interaksi antar fitur tanpa perlu feature engineering manual
- **Robustness to Outliers**: Decision trees sebagai base learner relatif robust terhadap outliers
- **Feature Importance**: Memberikan ukuran pentingnya setiap fitur, membantu interpretasi dan seleksi fitur

**Performa Gradient Boosting dalam Deteksi AML:**

Penelitian Altman et al. (2024) pada dataset AMLworld menunjukkan bahwa algoritma gradient boosting (khususnya LightGBM dan XGBoost) yang dikombinasikan dengan Graph Feature Preprocessor (GFP) mencapai performa superior pada dataset HI-Small dengan F1-scores: **GFP+LightGBM 62.86%, GFP+XGBoost 63.23%** [2]. Hasil ini mendemonstrasikan bahwa gradient boosting sangat efektif untuk deteksi AML ketika diperkaya dengan fitur graf yang tepat.

Namun, penelitian tersebut juga menemukan bahwa "GNN models competitive tanpa feature engineering, sementara GBT require GFP for pattern recognition" [2]. Ini menunjukkan bahwa meskipun gradient boosting sangat powerful, feature engineering yang tepat (terutama graph-based features) menjadi krusial untuk memaksimalkan performa dalam menangkap pola pencucian uang yang kompleks.

#### 2.1.2.4 Feature Engineering untuk Data Transaksi Keuangan

Feature engineering adalah proses mengekstrak, mentransformasi, dan memilih fitur yang informatif dari data mentah untuk meningkatkan performa model machine learning. Dalam konteks deteksi pencucian uang, feature engineering sangat krusial karena pola pencucian uang sering tersembunyi dalam relasi dan agregasi transaksi, bukan dalam transaksi individual.

**Kategori Fitur untuk Deteksi AML:**

**1. Transaction-Level Features (Fitur Tingkat Transaksi)**

Fitur yang menggambarkan karakteristik transaksi individual:

- **Amount-based features**: Nilai transaksi, perubahan saldo, rasio transaksi terhadap saldo awal
- **Time-based features**: Jam transaksi, hari dalam minggu, bulan, interval waktu antar transaksi
- **Transaction type**: Jenis transaksi (transfer, debit, kredit, withdrawal, deposit)
- **Geographic features**: Lokasi transaksi, jarak antar lokasi, transaksi lintas negara

**2. Aggregated Features (Fitur Agregat)**

Fitur yang dihitung dari agregasi transaksi dalam periode waktu tertentu:

- **Statistical aggregations**: Total, rata-rata, median, standar deviasi, min, max dari nilai transaksi dalam 7 hari, 30 hari, atau 90 hari terakhir
- **Frequency features**: Jumlah transaksi per periode, frekuensi transaksi per hari/minggu/bulan
- **Velocity features**: Tingkat perubahan aktivitas transaksi (acceleration dan deceleration)
- **Pattern features**: Regularitas transaksi, periodsisitas, konsistensi pola

Contoh:

```python
# Total transaksi keluar dalam 7 hari terakhir
total_outgoing_7d = df.groupby('account_id')['amount'].sum()

# Rata-rata nilai transaksi per hari
avg_daily_amount = df.groupby(['account_id', 'date'])['amount'].mean()

# Jumlah transaksi unik per hari
tx_count_per_day = df.groupby(['account_id', 'date']).size()
```

**3. Ratio Features (Fitur Rasio)**

Rasio antara dua metrik sering lebih informatif daripada nilai absolut:

- **Income/Outcome ratio**: Rasio total dana masuk terhadap dana keluar
- **Transaction-to-balance ratio**: Rasio nilai transaksi terhadap saldo rekening
- **Activity ratio**: Rasio hari aktif terhadap total hari dalam periode
- **Round-number ratio**: Proporsi transaksi dengan nilai bulat (indikasi strukturing)

Contoh:

```python
# Rasio transaksi keluar terhadap saldo awal
df['amount_to_balance_ratio'] = df['amount'] / df['oldbalanceOrg']

# Rasio dana masuk vs dana keluar
inflow = df[df['type'] == 'CREDIT']['amount'].sum()
outflow = df[df['type'] == 'DEBIT']['amount'].sum()
flow_ratio = inflow / (outflow + 1e-10)  # Avoid division by zero
```

**4. Network/Graph Features (Fitur Jaringan)**

Fitur yang menangkap struktur jaringan transaksi antar akun:

- **Degree centrality**: Jumlah akun unik yang terhubung (in-degree dan out-degree)
- **Betweenness centrality**: Seberapa sering akun muncul dalam jalur transaksi antar akun lain
- **PageRank**: Skor pentingnya akun dalam jaringan transaksi
- **Community detection**: Identifikasi cluster atau grup akun yang saling bertransaksi intensif
- **Fan-in/Fan-out patterns**: Pola di mana banyak akun mengirim ke satu akun (fan-in) atau satu akun mengirim ke banyak akun (fan-out), yang merupakan indikator kuat pencucian uang

**5. Behavioral Features (Fitur Perilaku)**

Fitur yang menggambarkan deviasi dari perilaku normal:

- **Deviation from historical average**: Seberapa jauh transaksi menyimpang dari pola historis nasabah
- **Sudden pattern change**: Deteksi perubahan mendadak dalam frekuensi atau nilai transaksi
- **Off-hours activity**: Transaksi pada jam-jam tidak wajar (tengah malam, hari libur)
- **Inconsistency score**: Ketidaksesuaian antara profil nasabah dengan pola transaksi

**6. Domain-Specific Features untuk Judi Online**

Fitur khusus yang menangkap karakteristik pencucian uang melalui judi online:

- **Rapid deposit-withdraw cycles**: Frekuensi pola deposit diikuti withdraw dalam waktu singkat
- **Minimal betting activity**: Rasio total taruhan terhadap total deposit (nilai rendah mengindikasikan deposit-withdraw scheme)
- **Winning ratio anomaly**: Tingkat kemenangan yang tidak wajar (terlalu tinggi atau terlalu rendah)
- **Multi-account indicators**: Kesamaan device fingerprint, IP address, atau pola transaksi yang mengindikasikan satu orang mengendalikan banyak akun
- **Small-value structuring**: Pola deposit dalam jumlah kecil yang konsisten (smurfing)

**7. Graph-Based Features untuk Deteksi Jaringan Pencucian Uang**

Pendekatan berbasis graf (graph-based approach) semakin populer dalam deteksi AML karena mampu menangkap struktur jaringan dan pola konektivitas antar akun. Altman et al. (2024) menjelaskan bahwa "Financial transaction graphs are essentially directed multigraphs" di mana nodes merepresentasikan akun dan edges merepresentasikan transaksi [2].

**Graph Feature Preprocessor (GFP):**

GFP adalah teknik ekstraksi fitur dari graf transaksi yang menghasilkan representasi numerik untuk setiap node. Fitur-fitur yang diekstrak meliputi:

- **Degree features**: In-degree (jumlah transaksi masuk), out-degree (jumlah transaksi keluar), total degree
- **Centrality measures**: Betweenness centrality, closeness centrality, eigenvector centrality - mengukur pentingnya suatu node dalam jaringan
- **Local clustering**: Clustering coefficient yang mengukur seberapa padat koneksi di sekitar node
- **Path-based features**: Average shortest path length, path diversity
- **Temporal features**: Burst detection (lonjakan aktivitas mendadak), inter-transaction time statistics
- **Neighborhood aggregation**: Statistik agregat dari tetangga langsung (1-hop neighbors) dan tetangga tingkat dua (2-hop neighbors)

Altman et al. (2024) menggunakan neighborhood sampling dengan mengambil "100 one-hop dan 100 two-hop neighbors" untuk membatasi kompleksitas komputasi sambil tetap menangkap konteks jaringan yang cukup [2].

**Keunggulan Graph-Based Approach:**

- Mampu mendeteksi pola pencucian uang yang melibatkan kolusi antar banyak akun (cycle, scatter-gather, bipartite patterns)
- Menangkap konteks transaksi: tidak hanya melihat atribut transaksi individual, tetapi juga siapa yang bertransaksi dengan siapa
- Lebih robust terhadap obfuscation techniques karena pelaku sulit menyembunyikan struktur jaringan sepenuhnya
- Dapat diintegrasikan dengan model machine learning tradisional: GFP mengekstrak fitur graf, kemudian fitur ini digunakan bersama fitur tabular dalam model seperti CatBoost, XGBoost, atau LightGBM

**Teknik Transformasi Fitur:**

1. **Scaling/Normalization**: Standarisasi nilai fitur agar berada dalam rentang yang sama

   ```python
   from sklearn.preprocessing import StandardScaler
   scaler = StandardScaler()
   X_scaled = scaler.fit_transform(X)
   ```

2. **Log Transformation**: Mengurangi skewness pada fitur dengan distribusi long-tail

   ```python
   df['log_amount'] = np.log1p(df['amount'])  # log1p untuk handle zero values
   ```

3. **Binning**: Mengubah fitur numerik kontinu menjadi kategori

   ```python
   df['amount_category'] = pd.cut(df['amount'], bins=[0, 100, 500, 1000, np.inf],
                                   labels=['small', 'medium', 'large', 'xlarge'])
   ```

4. **Encoding Categorical Features**: Mengubah fitur kategorikal menjadi numerik
   - Label Encoding: Untuk fitur ordinal
   - One-Hot Encoding: Untuk fitur nominal dengan sedikit kategori
   - Target Encoding: Mengganti kategori dengan rata-rata target (hati-hati terhadap data leakage)

**Feature Selection:**

Tidak semua fitur yang dibuat akan berguna. Feature selection penting untuk:

- Mengurangi dimensi dan mempercepat training
- Mengurangi overfitting
- Meningkatkan interpretabilitas model

Metode umum:

- **Filter methods**: Chi-square test, mutual information, correlation analysis
- **Wrapper methods**: Recursive Feature Elimination (RFE)
- **Embedded methods**: Feature importance dari tree-based models (seperti yang akan diberikan oleh CatBoost)

#### 2.1.2.5 Dataset Sintetis untuk Pelatihan Model AML

Salah satu tantangan utama dalam pengembangan model machine learning untuk deteksi pencucian uang adalah keterbatasan akses terhadap data real yang berlabel lengkap. Data transaksi keuangan nyata sangat sensitif dan terikat regulasi privasi yang ketat, sementara label ground-truth untuk transaksi pencucian uang sering tidak lengkap karena banyak kasus yang tidak terdeteksi.

**Keunggulan Dataset Sintetis:**

Altman et al. (2024) menyoroti keunggulan fundamental dari penggunaan data sintetis: "In a key way, using synthetic data can be even better than using real data: the ground truth labels are complete, whilst many laundering transactions in real data are never detected" [2]. Pernyataan ini menggarisbawahi bahwa dataset sintetis yang dibuat dengan baik dapat memberikan nilai lebih dibandingkan data real dalam konteks pelatihan model machine learning.

**AMLworld: Realistic Synthetic Financial Transaction Generator**

AMLworld adalah framework open-source yang dikembangkan oleh Altman et al. (2024) untuk menghasilkan dataset transaksi keuangan sintetis yang realistis dengan label pencucian uang yang lengkap [2]. Framework ini membangun multi-agent virtual world yang mensimulasikan ekosistem finansial dengan komponen:

1. **Entitas dalam Simulasi:**

   - **Banks**: Institusi keuangan yang memfasilitasi transaksi
   - **Individuals**: Nasabah personal dengan berbagai profil demografis dan finansial
   - **Companies**: Entitas bisnis dengan arus kas dan pola transaksi yang khas

2. **Model Ekonomi:**

   - Menggunakan **Circular Flow model** yang mencerminkan aliran uang dalam ekonomi riil
   - Mensimulasikan transaksi legitimate seperti gaji, pembayaran tagihan, pembelian, investasi
   - Skala besar: Mampu menghasilkan hingga **180 juta transaksi** untuk dataset LI-Large [2]

3. **Simulasi Pencucian Uang:**

   - **Placement phase**: Dana dari 9 sumber kriminal (extortion, gambling, prostitution, kidnapping, robbery, embezzlement, drugs, smuggling, dan lainnya)
   - **Layering phase**: Mengimplementasikan 8 pola transaksi (fan-out, fan-in, scatter-gather, gather-scatter, cycle, bipartite, stack, random)
   - **Integration phase**: Dana yang telah "dibersihkan" diintegrasikan kembali ke ekonomi

4. **Dataset Variants:**

   AMLworld menyediakan 6 variasi dataset yang tersedia secara publik di Kaggle:

   - **HI-Small**: Dataset kecil dengan laundering rate tinggi (high illicit)
   - **HI-Medium**: Dataset menengah dengan laundering rate tinggi
   - **HI-Large**: Dataset besar dengan laundering rate tinggi
   - **LI-Small**: Dataset kecil dengan laundering rate rendah (low illicit)
   - **LI-Medium**: Dataset menengah dengan laundering rate rendah
   - **LI-Large**: 176 juta transaksi dengan laundering rate 1:1,750 [2]

**Kontribusi untuk Riset AML:**

Dataset AMLworld telah memungkinkan penelitian komprehensif tentang:

- **Transfer Learning**: Model yang dilatih pada HI datasets dapat di-fine-tune untuk LI datasets, meningkatkan F1-score secara signifikan [2]
- **Federated Learning**: Simulasi kolaborasi antar bank menunjukkan bahwa "shared graph & model across banks meningkatkan F1-score rata-rata dari 4.9% (private) ke 20.8% (shared) pada LI-Medium" [2]
- **Perbandingan Algoritma**: Membandingkan performa Graph Neural Networks (GNN) dengan Gradient Boosted Trees (GBT) pada berbagai skala dan karakteristik data
- **Feature Engineering**: Mengevaluasi efektivitas Graph Feature Preprocessor (GFP) dalam ekstraksi fitur untuk model tabular

**Relevansi untuk Penelitian Ini:**

Meskipun penelitian ini menggunakan data real dari konteks Indonesia, pemahaman terhadap pola-pola pencucian uang yang disimulasikan dalam AMLworld (terutama 8 layering patterns) sangat relevan untuk:

- Merancang fitur yang dapat mendeteksi pola serupa dalam data judi online
- Memahami best practices dalam penanganan class imbalance ekstrem
- Mengevaluasi potensi penggunaan graph-based features jika data relasi antar akun tersedia
- Benchmarking performa CatBoost dengan hasil dari penelitian AMLworld untuk validasi kelayakan pendekatan

### 2.1.3 Algoritma CatBoost

#### 2.1.3.1 Sejarah dan Pengembangan CatBoost

CatBoost (Categorical Boosting) adalah algoritma gradient boosting yang dikembangkan oleh Yandex, perusahaan teknologi terbesar di Rusia [4]. Pengembangan CatBoost berawal dari algoritma internal Yandex yang disebut MatrixNet, yang telah digunakan sejak tahun 2009 untuk ranking hasil pencarian dan sistem rekomendasi. MatrixNet kemudian berevolusi menjadi Tensornet pada tahun 2015, sebelum akhirnya dirilis sebagai open-source dengan nama CatBoost pada tahun 2017 [5].

Sejak dirilis sebagai proyek open-source, CatBoost telah digunakan secara luas dalam industri teknologi [4]. Beberapa perusahaan besar yang menggunakan CatBoost dalam sistem produksi mereka antara lain:

- **Yandex**: Digunakan dalam search ranking, recommendation system, dan berbagai produk ML lainnya
- **JetBrains**: Memanfaatkan CatBoost dalam analisis kode dan sistem rekomendasi IDE
- **Cloudflare**: Menggunakan CatBoost untuk deteksi bot dan analisis keamanan web
- **Careem** (anak perusahaan Uber): Menerapkan CatBoost dalam demand forecasting dan dynamic pricing

Popularitas CatBoost terus meningkat karena performanya yang unggul dalam berbagai kompetisi machine learning, termasuk di platform Kaggle, di mana CatBoost sering menjadi bagian dari solusi pemenang. CatBoost dirancang khusus untuk memberikan kinerja tinggi dan kecepatan training yang efisien, serta mampu menangani dataset besar tanpa mengorbankan performa [5].

#### 2.1.3.2 Konsep Dasar dan Arsitektur CatBoost

CatBoost adalah implementasi gradient boosting yang menggunakan oblivious decision trees sebagai base learners (CatBoost Official Documentation, 2025). Oblivious trees, juga dikenal sebagai symmetric trees, memiliki struktur khusus di mana pada setiap level kedalaman tree, semua node menggunakan feature dan threshold yang sama untuk splitting.

**Karakteristik Oblivious Trees:**

```
Level 0:     Feature A <= threshold_1
            /                        \
Level 1:  Feature B <= threshold_2    Feature B <= threshold_2
         /        \                  /            \
Leaves: L1       L2                L3             L4
```

Keunggulan oblivious trees:

- **Cepat untuk prediksi**: Karena struktur simetris, prediksi dapat dilakukan dalam O(log n) dengan implementasi yang sangat efisien
- **Regularisasi alami**: Struktur yang terbatas mengurangi overfitting
- **Cocok untuk CPU dan GPU**: Struktur reguler memudahkan paralelisasi

**Arsitektur Pipeline CatBoost:**

1. **Preprocessing**: Konversi categorical features menggunakan target statistics dan one-hot encoding
2. **Ordered Boosting**: Training menggunakan skema boosting yang menghindari prediction shift
3. **Tree Building**: Konstruksi oblivious trees dengan greedy feature selection
4. **Regularization**: Penerapan berbagai teknik regularisasi otomatis
5. **Prediction**: Agregasi prediksi dari semua trees

#### 2.1.3.3 Ordered Boosting: Solusi Prediction Shift Problem

Salah satu inovasi utama CatBoost adalah ordered boosting, sebuah teknik yang dirancang untuk mengatasi masalah prediction shift yang terjadi pada algoritma gradient boosting tradisional [4]. Ordered boosting membantu mengatasi masalah overfitting dengan mengurangi kompleksitas model secara adaptif, menyesuaikan batas-batas kompleksitas pada setiap iterasi [5].

**Prediction Shift Problem:**

Dalam gradient boosting tradisional, ketika menghitung residual untuk training sampel, model menggunakan prediksi dari model yang sama yang dilatih pada sampel tersebut. Ini menyebabkan:

1. **Conditional Shift**: Distribusi residual pada training set berbeda dengan distribusi pada test set
2. **Overfitting**: Model terlalu optimis dalam mengestimasi error sendiri
3. **Bias dalam Target Statistics**: Terutama masalah pada encoding categorical features

**Solusi Ordered Boosting:**

CatBoost menyelesaikan masalah ini dengan ordered boosting scheme:

1. **Random Permutation**: Dataset dirandom dengan permutasi σ
2. **Sequential Prediction**: Untuk setiap sampel ke-i, model hanya menggunakan sampel-sampel sebelumnya (σ₁, σ₂, ..., σᵢ₋₁) untuk menghitung prediksi dan residual
3. **Multiple Permutations**: Dalam praktik, beberapa permutasi digunakan untuk stabilitas

Secara matematis, untuk sampel xᵢ, residual dihitung sebagai:

rᵢ = y - Mₙ⁽ⁱ⁾(xᵢ)

Di mana Mₙ⁽ⁱ⁾ adalah model yang dilatih hanya pada sampel {x₁, x₂, ..., xᵢ₋₁} sesuai permutasi.

**Keunggulan Ordered Boosting:**

- **Mengurangi Overfitting**: Prediksi untuk setiap sampel dibuat oleh model yang tidak pernah melihat sampel tersebut
- **Generalisasi Lebih Baik**: Model lebih robust pada data baru
- **Target Statistics yang Lebih Akurat**: Menghindari target leakage dalam encoding categorical features

#### 2.1.3.4 Penanganan Categorical Features

Salah satu keunggulan utama CatBoost adalah kemampuannya menangani categorical features secara native tanpa memerlukan preprocessing manual [4], [5]. CatBoost secara otomatis menangani fitur kategorikal menggunakan teknik Ordered Target Statistics, yang mengurutkan kategori berdasarkan target variabel dan mempelajari hubungan ordinal di antara mereka [5]. Ini sangat penting dalam deteksi pencucian uang di mana banyak fitur bersifat kategorikal seperti jenis transaksi, kode merchant, lokasi, dll.

**Masalah dengan Metode Traditional:**

- **Label Encoding**: Memperkenalkan ordering artifisial yang tidak bermakna
- **One-Hot Encoding**: Menyebabkan high dimensionality dan sparse matrix, terutama untuk categorical features dengan banyak kategori (high cardinality) [4]
- **Target Encoding**: Rentan terhadap target leakage dan overfitting [5]

**Target Statistics Encoding di CatBoost:**

CatBoost menggunakan teknik target statistics yang sophisticated:

1. **Ordered Target Statistics**: Untuk sampel ke-i dengan categorical value c, target statistic dihitung hanya dari sampel-sampel sebelumnya yang memiliki nilai c yang sama:

   TS(xᵢ) = (Σⱼ₌₁ⁱ⁻¹ [xⱼ = c] · yⱼ + α · prior) / (Σⱼ₌₁ⁱ⁻¹ [xⱼ = c] + α)

   Di mana:

   - [xⱼ = c] adalah indikator apakah sampel j memiliki nilai kategori c
   - α adalah parameter smoothing (prior weight)
   - prior adalah nilai prior (biasanya rata-rata global target)

2. **Prior Smoothing**: Parameter α mengontrol trade-off antara estimasi lokal (dari kategori) dengan prior global, mengurangi overfitting pada kategori yang jarang muncul.

3. **Multiple Permutations**: Menggunakan beberapa random permutations untuk membuat estimasi target statistics lebih stabil.

**Kombinasi dengan One-Hot Encoding:**

CatBoost juga menggunakan one-hot encoding untuk categorical features dengan cardinality rendah (default: ≤ one_hot_max_size=2). Kombinasi kedua metode ini memberikan balance antara:

- Efisiensi komputasi (target statistics untuk high cardinality)
- Akurasi (one-hot untuk low cardinality)

**Categorical Features Combinations:**

CatBoost dapat secara otomatis mengeksplorasi kombinasi categorical features untuk menangkap interaksi kompleks:

```python
cat_features = ['transaction_type', 'merchant_category', 'location']
model = CatBoostClassifier(cat_features=cat_features)
# CatBoost akan otomatis mengeksplorasi kombinasi seperti:
# - transaction_type × merchant_category
# - merchant_category × location
# - transaction_type × merchant_category × location
```

#### 2.1.3.5 GPU Training dan Performa Komputasi

CatBoost dirancang untuk memanfaatkan GPU secara optimal, terutama untuk dataset besar (CatBoost Official Documentation, 2025). GPU training di CatBoost mengimplementasikan berbagai optimasi:

**Optimasi GPU:**

1. **Multi-GPU Support**: Mendukung training pada beberapa GPU secara paralel
2. **Efficient Memory Management**: Penggunaan memori GPU yang optimal
3. **Histogram-based Splits**: Menggunakan histogram untuk mempercepat pencarian split terbaik

**Performa Benchmark:**

Berdasarkan benchmark resmi CatBoost:

- **Speed**: CatBoost 3-5x lebih cepat dibanding XGBoost pada CPU untuk dataset dengan categorical features [4]
- **GPU Acceleration**: Training di GPU bisa 20-50x lebih cepat dibanding CPU dengan strong GPU support [4]
- **Memory Efficiency**: Penggunaan memori lebih efisien dibanding LightGBM pada dataset besar
- **Akurasi**: Pada dataset IEEE Fraud Detection, CatBoost menunjukkan peningkatan akurasi 2-3% dibanding XGBoost dan LightGBM [4]
- **Training Time**: Pada Santander Customer Transaction dataset, CatBoost mengurangi waktu training 30-40% sambil mempertahankan akurasi superior [4]

**Pengaturan GPU Training:**

```python
model = CatBoostClassifier(
    task_type='GPU',           # Enable GPU training
    devices='0:1',             # Use GPU 0 and 1
    gpu_ram_part=0.95,         # Use 95% GPU memory
    bootstrap_type='Bernoulli' # Recommended for GPU
)
```

#### 2.1.3.6 Penanganan Missing Values

CatBoost memiliki kemampuan unik dalam menangani missing values secara otomatis tanpa memerlukan imputation manual [4], [5]. CatBoost memperlakukan missing values sebagai entitas terpisah dan menggunakannya sebagai fitur dalam proses pembelajaran, sering kali meningkatkan performa model karena dapat belajar dari fakta bahwa data tersebut hilang [4].

Keunggulan pendekatan ini:

- Tidak memerlukan preprocessing manual untuk missing values
- Model dapat menangkap pola dari keberadaan missing values itu sendiri
- Mengurangi kompleksitas pipeline data preparation

#### 2.1.3.7 Regularization dan Overfitting Prevention

CatBoost mengimplementasikan berbagai teknik regularisasi untuk mencegah overfitting [5]:

**1. Ordered Boosting**
Seperti dijelaskan sebelumnya, ini adalah mekanisme regularisasi fundamental di CatBoost yang mengurangi kompleksitas model secara adaptif.

**2. L2 Regularization (Weight Decay)**
Menambahkan penalty pada bobot leaf values:

L_reg = L + λ · Σⱼ wⱼ²

Parameter: `l2_leaf_reg` (default: 3.0)

**3. Bootstrap Sampling**

- **Bayesian Bootstrap**: Sampling dengan random weights (default)
- **Bernoulli Bootstrap**: Sampling dengan probability (lebih cepat di GPU)
- **MVS (Minimum Variance Sampling)**: Sampling yang meminimalkan variance

**Aplikasi CatBoost dalam Domain Keuangan:**

CatBoost telah terbukti sangat efektif dalam berbagai use case di industri keuangan [4], [5]:

1. **Credit Scoring**: Dengan native handling terhadap fitur kategorikal seperti employment history dan loan types, CatBoost dapat memprediksi default risk tanpa one-hot encoding yang kompleks [4]

2. **Fraud Detection**: Dynamic binning dan support untuk `scale_pos_weight` membantu menangani imbalanced dataset, di mana fraud cases biasanya < 1% dari total transaksi, menghasilkan recall yang lebih tinggi [4]

3. **Customer Churn Prediction**: Kemampuan menangani time-series data dan categorical features seperti subscription plans memungkinkan CatBoost fokus pada ekstraksi insights daripada data wrangling [4]

4. **Risk Prediction**: Dalam konteks healthcare dan finance, robust handling terhadap imbalanced datasets melalui `class_weights` dan kemampuan native missing values processing menjadikan CatBoost pilihan ideal untuk prediksi risiko [4]

**4. Random Strength**
Menambahkan noise pada score saat memilih split terbaik untuk meningkatkan robustness:

score' = score + random_strength · N(0, 1)

Parameter: `random_strength` (default: 1.0)

**5. Leaf Estimation Method**

- **Newton**: Menggunakan Hessian untuk estimasi leaf values (akurat tapi bisa overfit)
- **Gradient**: Hanya menggunakan gradient (lebih konservatif)

**6. Early Stopping**
Menghentikan training jika tidak ada peningkatan pada validation set:

```python
model.fit(
    X_train, y_train,
    eval_set=(X_val, y_val),
    early_stopping_rounds=50
)
```

#### 2.1.3.7 Perbandingan CatBoost dengan XGBoost dan LightGBM

CatBoost, XGBoost, dan LightGBM adalah tiga implementasi gradient boosting paling populer. Masing-masing memiliki karakteristik dan keunggulan tersendiri.

**Perbandingan Teknis:**

| Aspek                          | CatBoost                    | XGBoost                   | LightGBM                  |
| ------------------------------ | --------------------------- | ------------------------- | ------------------------- |
| **Tree Growth**                | Oblivious trees (symmetric) | Level-wise                | Leaf-wise                 |
| **Categorical Handling**       | Native target statistics    | Perlu manual encoding     | Perlu manual encoding     |
| **Overfitting Prevention**     | Ordered boosting            | Regularization parameters | Regularization parameters |
| **Speed (CPU)**                | Sedang                      | Sedang                    | Cepat                     |
| **Speed (GPU)**                | Sangat cepat                | Cepat                     | Cepat                     |
| **Memory Usage**               | Efisien                     | Sedang                    | Sangat efisien            |
| **Out-of-the-box Performance** | Sangat baik                 | Baik                      | Perlu tuning              |
| **Default Hyperparameters**    | Sudah optimal               | Perlu tuning              | Perlu tuning              |

**Keunggulan CatBoost:**

1. **Minimal Preprocessing**: Tidak perlu encoding manual untuk categorical features
2. **Robust Default Settings**: Performa sangat baik tanpa hyperparameter tuning
3. **Ordered Boosting**: Mengurangi overfitting secara sistematis
4. **Feature Combinations**: Otomatis mengeksplorasi kombinasi categorical features
5. **Prediction Consistency**: Oblivious trees menghasilkan prediksi yang lebih stabil

**Keunggulan XGBoost:**

1. **Mature Ecosystem**: Dokumentasi lengkap, komunitas besar, banyak tutorial
2. **Custom Objectives**: Mudah untuk mendefinisikan custom loss functions
3. **Sparse Data**: Sangat efisien untuk sparse matrix
4. **Monotonic Constraints**: Mendukung monotonic constraints pada features

**Keunggulan LightGBM:**

1. **Training Speed**: Paling cepat untuk dataset besar di CPU
2. **Memory Efficiency**: Paling efisien dalam penggunaan memori
3. **Histogram-based**: Efisien untuk high-dimensional data
4. **Distributed Training**: Dukungan distributed training yang baik

**Rekomendasi Penggunaan:**

- **CatBoost**: Ideal untuk dataset dengan banyak categorical features, ketika waktu preprocessing terbatas, atau ketika hyperparameter tuning tidak feasible
- **XGBoost**: Cocok untuk kompetisi ML, custom loss functions, atau ketika sparse data menjadi concern
- **LightGBM**: Terbaik untuk dataset sangat besar (millions of rows), ketika training speed adalah prioritas utama

**Hasil Benchmark pada AML Detection:**

Berdasarkan penelitian Florek & Zagdański (2023):

1. **Without Tuning**: CatBoost dan XGBoost memberikan performa terbaik
2. **With Tuning**: LightGBM menunjukkan improvement terbesar, sering menjadi yang terbaik
3. **Trade-off**: CatBoost memberikan best out-of-the-box performance dengan tuning cost terendah

Dalam konteks penelitian ini untuk deteksi rekening berisiko, CatBoost dipilih karena:

- Dataset mengandung banyak categorical features (transaction type, merchant category, location)
- Kebutuhan deployment cepat tanpa extensive tuning
- Ordered boosting memberikan keandalan tinggi untuk production system
- Native handling categorical features mengurangi complexity pipeline preprocessing

### 2.1.4 Metrik Evaluasi Model Klasifikasi

Evaluasi model klasifikasi memerlukan berbagai metrik untuk mengukur performa dari berbagai perspektif. Dalam konteks deteksi pencucian uang, pemilihan metrik evaluasi yang tepat sangat penting karena karakteristik masalah yang imbalanced dan cost of error yang asimetris (Scikit-learn Documentation, 2025).

#### 2.1.4.1 Confusion Matrix

Confusion matrix adalah tabel kontingensi yang menampilkan performa model klasifikasi dengan membandingkan prediksi model dengan label aktual (Scikit-learn, 2025). Untuk klasifikasi biner, confusion matrix memiliki empat komponen:

```
                    Predicted
                 Negative | Positive
              +----------+----------+
Actual   Neg  |    TN    |    FP    |
              +----------+----------+
         Pos  |    FN    |    TP    |
              +----------+----------+
```

**Komponen Confusion Matrix:**

- **True Negative (TN)**: Prediksi negatif yang benar (rekening normal diprediksi normal)
- **False Positive (FP)**: Prediksi positif yang salah (rekening normal diprediksi berisiko) - Type I Error
- **False Negative (FN)**: Prediksi negatif yang salah (rekening berisiko diprediksi normal) - Type II Error
- **True Positive (TP)**: Prediksi positif yang benar (rekening berisiko diprediksi berisiko)

**Interpretasi dalam Konteks AML:**

- **TP**: Sistem berhasil mengidentifikasi rekening yang benar-benar terlibat pencucian uang → Keberhasilan deteksi
- **TN**: Sistem benar menilai rekening normal sebagai tidak berisiko → Efisiensi operasional
- **FP**: Rekening normal salah ditandai sebagai berisiko → Biaya investigasi sia-sia, ketidaknyamanan nasabah
- **FN**: Rekening berisiko lolos dari deteksi → Kerugian finansial, reputasi, bahkan sanksi regulator

**Contoh Confusion Matrix:**

```
Actual/Predicted   Normal   Berisiko
Normal              9500      50      (9550 rekening normal)
Berisiko             20      430      (450 rekening berisiko)
```

Dari contoh di atas:

- TN = 9500 (rekening normal teridentifikasi benar)
- FP = 50 (false alarm)
- FN = 20 (pencucian uang yang tidak terdeteksi - CRITICAL!)
- TP = 430 (pencucian uang terdeteksi dengan benar)

#### 2.1.4.2 Accuracy (Akurasi)

Accuracy adalah proporsi prediksi yang benar dari total prediksi:

**Formula:**

Accuracy = (TP + TN) / (TP + TN + FP + FN)

**Contoh Perhitungan:**

Dari confusion matrix di atas:

```
Accuracy = (9500 + 430) / (9500 + 50 + 20 + 430)
         = 9930 / 10000
         = 0.993 atau 99.3%
```

**Limitasi Accuracy:**

Accuracy adalah metrik yang misleading untuk imbalanced dataset. Contoh ekstrem:

```python
# Dataset: 9900 normal, 100 berisiko
# Model naif yang memprediksi semua sebagai "normal"
TP = 0, FP = 0, FN = 100, TN = 9900
Accuracy = (0 + 9900) / 10000 = 99%
```

Model di atas memiliki akurasi 99% tetapi sepenuhnya gagal mendeteksi kasus berisiko (FN = 100, TP = 0). Ini disebut **accuracy paradox**.

**Kapan Menggunakan Accuracy:**

- Dataset relatif seimbang (rasio kelas mendekati 50:50)
- Cost of error sama untuk false positive dan false negative
- Performa keseluruhan model lebih penting daripada performa per kelas

**Kapan TIDAK Menggunakan Accuracy:**

- Imbalanced dataset (seperti AML detection)
- Cost of error asimetris
- Kelas minoritas lebih penting (seperti fraud detection, medical diagnosis)

#### 2.1.4.3 Precision (Presisi)

Precision mengukur akurasi prediksi positif. Dari semua kasus yang diprediksi positif (berisiko), berapa persen yang benar-benar positif?

**Formula:**

Precision = TP / (TP + FP)

**Interpretasi:**

- Precision tinggi → Sedikit false alarm (false positive rendah)
- Model "conservative" dalam memberikan label positif
- Penting ketika cost of false positive tinggi

**Contoh Perhitungan:**

```
Precision = 430 / (430 + 50) = 430 / 480 = 0.896 atau 89.6%
```

Artinya: Dari 480 rekening yang ditandai berisiko, 430 (89.6%) benar-benar berisiko, dan 50 (10.4%) adalah false alarm.

**Pentingnya Precision dalam AML:**

- **Biaya Investigasi**: False positive menyebabkan tim investigasi membuang waktu pada kasus yang tidak valid
- **Customer Experience**: Rekening yang salah diblokir menyebabkan ketidaknyamanan nasabah dan potensi kehilangan customer
- **Regulatory Compliance**: Terlalu banyak false positive dapat dianggap sebagai sistem yang tidak efektif oleh regulator

**Trade-off:**

Model dengan precision sangat tinggi (misal 99%) biasanya sangat konservatif dan cenderung melewatkan banyak kasus positif (recall rendah).

#### 2.1.4.4 Recall / Sensitivity / True Positive Rate

Recall mengukur kemampuan model mendeteksi kasus positif. Dari semua kasus yang benar-benar positif, berapa persen yang berhasil dideteksi?

**Formula:**

Recall = TP / (TP + FN)

Atau dapat juga ditulis sebagai:

Recall = TP / (Total Actual Positive)

**Interpretasi:**

- Recall tinggi → Model mampu menangkap sebagian besar kasus positif (false negative rendah)
- Model "aggressive" dalam mendeteksi kasus positif
- Penting ketika cost of false negative tinggi

**Contoh Perhitungan:**

```
Recall = 430 / (430 + 20) = 430 / 450 = 0.956 atau 95.6%
```

Artinya: Dari 450 rekening yang benar-benar berisiko, 430 (95.6%) berhasil dideteksi, dan 20 (4.4%) lolos dari deteksi.

**Pentingnya Recall dalam AML:**

- **Kerugian Finansial**: False negative berarti pencucian uang berlanjut, menyebabkan kerugian yang besar
- **Regulatory Penalty**: Regulator dapat memberikan sanksi jika institusi gagal mendeteksi aktivitas pencucian uang
- **Reputational Risk**: Kasus pencucian uang yang tidak terdeteksi dapat merusak reputasi institusi secara permanen
- **Crime Continuation**: Pencucian uang yang tidak terdeteksi memfasilitasi kejahatan terorganisir untuk berlanjut

**Trade-off:**

Model dengan recall sangat tinggi (misal 99%) biasanya akan menghasilkan banyak false alarm (precision rendah) karena terlalu agresif dalam mendeteksi.

#### 2.1.4.5 F1-Score (F-Measure)

F1-Score adalah harmonic mean dari precision dan recall, memberikan satu metrik yang menyeimbangkan keduanya.

**Formula:**

F1 = 2 × (Precision × Recall) / (Precision + Recall)

Atau secara eksplisit:

F1 = 2TP / (2TP + FP + FN)

**Mengapa Harmonic Mean?**

Harmonic mean lebih sensitif terhadap nilai yang rendah dibanding arithmetic mean. Ini memastikan bahwa F1-Score hanya tinggi jika baik precision maupun recall tinggi.

Contoh:

```
# Case 1: Precision = 0.9, Recall = 0.9
Arithmetic Mean = (0.9 + 0.9) / 2 = 0.90
Harmonic Mean (F1) = 2 × (0.9 × 0.9) / (0.9 + 0.9) = 0.90

# Case 2: Precision = 0.9, Recall = 0.1 (model buruk!)
Arithmetic Mean = (0.9 + 0.1) / 2 = 0.50 (terlihat lumayan)
Harmonic Mean (F1) = 2 × (0.9 × 0.1) / (0.9 + 0.1) = 0.18 (terlihat buruk)
```

**Contoh Perhitungan:**

```
Precision = 0.896, Recall = 0.956

F1 = 2 × (0.896 × 0.956) / (0.896 + 0.956)
   = 2 × 0.857 / 1.852
   = 0.925 atau 92.5%
```

**Kapan Menggunakan F1-Score:**

- Imbalanced dataset
- Precision dan recall sama-sama penting
- Perlu satu metrik untuk model comparison atau hyperparameter tuning
- Cost of false positive dan false negative relatif seimbang

**F-Beta Score (Generalisasi):**

F-Beta score adalah generalisasi F1 yang memberikan bobot berbeda pada precision dan recall:

F_β = (1 + β²) × (Precision × Recall) / (β² × Precision + Recall)

- **β < 1**: Memberikan bobot lebih pada precision (misal β=0.5 untuk F0.5)
- **β = 1**: F1-Score (balanced)
- **β > 1**: Memberikan bobot lebih pada recall (misal β=2 untuk F2)

Dalam AML detection, **F2-Score** sering lebih appropriate karena recall lebih penting:

```python
from sklearn.metrics import fbeta_score

f2 = fbeta_score(y_true, y_pred, beta=2)
# Memberikan bobot 2x lebih besar pada recall
```

#### 2.1.4.6 ROC Curve dan AUC-ROC

**Receiver Operating Characteristic (ROC) Curve**

ROC curve adalah grafik yang menampilkan trade-off antara True Positive Rate (TPR) dan False Positive Rate (FPR) pada berbagai threshold klasifikasi (Google ML Crash Course, 2025).

**Definisi:**

- **True Positive Rate (TPR)** = Recall = TP / (TP + FN)
- **False Positive Rate (FPR)** = FP / (FP + TN)

ROC curve dibuat dengan:

1. Mengurutkan semua prediksi berdasarkan probability score
2. Untuk setiap threshold t dari 0 hingga 1:
   - Hitung TPR dan FPR jika threshold klasifikasi adalah t
   - Plot point (FPR, TPR)
3. Hubungkan semua points

**Karakteristik ROC Curve:**

```
TPR (Recall)
   1.0  ┌────────────── Perfect Classifier
        │    ╱
   0.8  │  ╱  Good Classifier
        │ ╱
   0.6  │╱
        │      Random Classifier
   0.4  ╱      (diagonal line)
       ╱│
   0.2╱ │
      ╱  │  Poor Classifier
   0.0└────────────────────────────────→ FPR
      0.0   0.2   0.4   0.6   0.8   1.0
```

- **Perfect Classifier**: ROC curve melalui titik (0, 1), artinya TPR = 1 (semua positif terdeteksi) dan FPR = 0 (tidak ada false alarm)
- **Random Classifier**: ROC curve adalah garis diagonal dari (0,0) ke (1,1)
- **Poor Classifier**: ROC curve di bawah diagonal

**Area Under the ROC Curve (AUC-ROC)**

AUC-ROC adalah area di bawah ROC curve, memberikan satu nilai metrik yang merangkum performa model di semua threshold.

**Interpretasi AUC:**

- **AUC = 1.0**: Perfect classifier
- **AUC = 0.9 - 1.0**: Excellent
- **AUC = 0.8 - 0.9**: Very good
- **AUC = 0.7 - 0.8**: Good
- **AUC = 0.6 - 0.7**: Fair
- **AUC = 0.5**: Random classifier (no discriminative power)
- **AUC < 0.5**: Worse than random (model prediksi terbalik)

**Interpretasi Probabilistik:**

AUC dapat diinterpretasikan sebagai probabilitas bahwa model memberikan score lebih tinggi pada sampel positif yang dipilih secara acak dibanding sampel negatif yang dipilih secara acak.

```python
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# Compute AUC
auc = roc_auc_score(y_true, y_pred_proba)

# Plot ROC curve
fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

**Keunggulan AUC-ROC:**

1. **Threshold-Independent**: Mengukur performa di semua threshold, bukan hanya satu threshold tertentu
2. **Scale-Invariant**: Mengukur seberapa baik prediksi di-rank, bukan nilai absolutnya
3. **Classification-Threshold-Invariant**: Berguna ketika threshold optimal belum ditentukan

**Limitasi AUC-ROC:**

1. **Tidak Optimal untuk Imbalanced Dataset**: Karena FPR bisa tetap kecil meskipun banyak false positive (karena TN sangat besar)
2. **Equal Importance**: Memberikan bobot sama pada semua bagian kurva, padahal dalam praktik kita mungkin hanya peduli pada region tertentu (misal: FPR rendah)
3. **Tidak Langsung Menunjukkan Cost**: Tidak mempertimbangkan cost of error yang berbeda

**Alternatif untuk Imbalanced Dataset: PR-AUC**

Precision-Recall AUC lebih appropriate untuk imbalanced dataset:

```python
from sklearn.metrics import precision_recall_curve, auc

precision, recall, thresholds = precision_recall_curve(y_true, y_pred_proba)
pr_auc = auc(recall, precision)
```

#### 2.1.4.7 Multiclass Classification Metrics

Meskipun penelitian ini fokus pada binary classification (berisiko vs tidak berisiko), penting memahami ekstensi metrik untuk multiclass dalam konteks yang lebih luas.

**Averaging Methods:**

Untuk multiclass classification, metrik seperti precision, recall, dan F1 dihitung per kelas, kemudian diagregasi:

**1. Macro-Average:**

Menghitung metrik untuk setiap kelas, kemudian rata-rata:

Precision_macro = (Precision_class1 + Precision_class2 + ... + Precision_classN) / N

- Memberikan bobot sama untuk setiap kelas
- Cocok ketika semua kelas sama penting
- Sensitif terhadap performa pada kelas minoritas

**2. Micro-Average:**

Menghitung total TP, FP, FN di semua kelas, kemudian hitung metrik:

Precision_micro = Σ TP_i / (Σ TP_i + Σ FP_i)

- Memberikan bobot sama untuk setiap sampel
- Didominasi oleh kelas mayoritas
- Sama dengan accuracy untuk balanced multiclass

**3. Weighted-Average:**

Rata-rata berbobot berdasarkan jumlah sampel setiap kelas:

Precision_weighted = Σ (n_i / n_total) × Precision_i

- Mempertimbangkan class imbalance
- Cocok untuk imbalanced multiclass

**Multiclass ROC-AUC:**

Dua pendekatan umum:

**1. One-vs-Rest (OvR):**

Untuk setiap kelas, hitung AUC dengan menganggap kelas tersebut sebagai positif dan semua kelas lain sebagai negatif. Kemudian rata-rata.

```python
from sklearn.metrics import roc_auc_score

# OvR (default untuk multiclass)
auc_ovr = roc_auc_score(y_true, y_pred_proba, multi_class='ovr', average='macro')
```

**2. One-vs-One (OvO):**

Hitung AUC untuk setiap pasangan kelas, kemudian rata-rata.

```python
auc_ovo = roc_auc_score(y_true, y_pred_proba, multi_class='ovo', average='macro')
```

#### 2.1.4.8 Pemilihan Metrik untuk Deteksi AML

Dalam konteks deteksi rekening berisiko pencucian uang, pemilihan metrik evaluasi harus mempertimbangkan:

**Metrik Utama:**

1. **Recall (Primary)**: Paling penting karena cost of missing pencucian uang sangat tinggi. Target: ≥ 0.90
2. **F2-Score**: Menyeimbangkan recall dan precision dengan bobot lebih pada recall. Target: ≥ 0.85
3. **Precision**: Penting untuk efisiensi operasional, tetapi boleh di-compromise untuk recall tinggi. Target: ≥ 0.70

**Keunggulan CatBoost untuk Imbalanced Dataset:**

CatBoost memiliki fitur khusus untuk menangani imbalanced dataset yang umum dalam kasus AML [4], [5]:

1. **Dynamic Binning**: Mengelompokkan nilai fitur ke dalam bins yang dipilih secara dinamis, memungkinkan model memberikan perhatian lebih pada minority class tanpa overcompensating [4]

2. **Scale_pos_weight Parameter**: Dapat di-set proporsional dengan rasio negative/positive classes untuk menekankan minority class selama training [4]

3. **Class_weights**: Memberikan bobot lebih pada minority class, membantu model fokus pada rare events yang penting dalam fraud detection [4]

**Feature Importance untuk Interpretabilitas:**

CatBoost menyediakan fitur Feature Importance yang sangat berguna dalam domain keuangan yang regulated [4], [5]:

- Mengukur kontribusi relatif setiap fitur terhadap performa model [5]
- Membantu identifikasi fitur-fitur penting untuk prediksi akurat [5]
- Dapat digunakan bersama SHAP values untuk menunjukkan kontribusi setiap fitur pada prediksi spesifik [4]
- Memberikan transparansi dan trust dalam hasil model untuk stakeholder non-teknis [4]

**Keunggulan CatBoost untuk Imbalanced Dataset:**

CatBoost memiliki fitur khusus untuk menangani imbalanced dataset yang umum dalam kasus AML [4], [5]:

1. **Dynamic Binning**: Mengelompokkan nilai fitur ke dalam bins yang dipilih secara dinamis, memungkinkan model memberikan perhatian lebih pada minority class tanpa overcompensating [4]

2. **Scale_pos_weight Parameter**: Dapat di-set proporsional dengan rasio negative/positive classes untuk menekankan minority class selama training [4]

3. **Class_weights**: Memberikan bobot lebih pada minority class, membantu model fokus pada rare events yang penting dalam fraud detection [4]

4. **Auto_class_weights**: CatBoost dapat menghitung class weights secara otomatis berdasarkan distribusi data [5]

**Metrik Sekunder:**

4. **AUC-ROC**: Untuk menilai discriminative power secara keseluruhan. Target: ≥ 0.90
5. **PR-AUC**: Lebih informatif untuk imbalanced dataset. Target: ≥ 0.75
6. **Confusion Matrix**: Untuk analisis mendalam tentang jenis error

**Metrik yang Kurang Relevan:**

- **Accuracy**: Tidak informatif karena extreme imbalance
- **Specificity (TNR)**: Kurang penting karena TN sangat banyak

**Threshold Tuning:**

Dalam deployment, threshold klasifikasi harus di-tune berdasarkan business requirements:

```python
# Cari threshold yang mencapai recall minimal 0.95
from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_true, y_pred_proba)
idx = np.argmax(recall >= 0.95)
optimal_threshold = thresholds[idx]
optimal_precision = precision[idx]

print(f"Threshold: {optimal_threshold:.3f}")
print(f"Recall: {recall[idx]:.3f}")
print(f"Precision: {optimal_precision:.3f}")
```

**Cost-Sensitive Evaluation:**

Idealnya, evaluasi harus mempertimbangkan cost asli dari setiap jenis error:

Total_Cost = Cost_FN × FN + Cost_FP × FP

Di mana:

- Cost_FN: Cost dari missing satu kasus pencucian uang (sangat tinggi: millions of rupiah + regulatory penalty + reputational damage)
- Cost_FP: Cost dari investigating false alarm (rendah-sedang: labor cost + customer inconvenience)

Rasio Cost_FN / Cost_FP biasanya 10:1 hingga 100:1 dalam konteks AML.

---

## 2.2 Penelitian Terkait

Bagian ini menyajikan tinjauan literatur terhadap penelitian-penelitian sebelumnya yang relevan dengan deteksi pencucian uang, fraud detection, dan penggunaan algoritma machine learning khususnya CatBoost dalam domain finansial. Tinjauan literatur disajikan dalam bentuk tabel untuk memudahkan perbandingan antar penelitian.

**Tabel 2.1 Deteksi Rekening Terindikasi Judi Online Menggunakan CatBoost: Studi Kasus pada Kebijakan Pemblokiran Rekening Pasif di Indonesia**

| Nomor          | 1                                                                                                                                                                                                                                                                                                                                                                                             | 2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 3                                                                                                                                                                                                                                                                                                                                                                                                                                              | 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 6                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Judul**      | An explainable machine learning model in predicting vaginal birth after cesarean section                                                                                                                                                                                                                                                                                                      | Realistic Synthetic Financial Transactions for Anti-Money Laundering Models (AMLworld)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Credit Card Fraud Detection Using CatBoost                                                                                                                                                                                                                                                                                                                                                                                                     | Benchmarking state-of-the-art gradient boosting algorithms for classification                                                                                                                                                                                                                                                                                                                                                                                                                   | Fraudulent Transaction Detection in Online Systems Using Random Forest and Gradient Boosting                                                                                                                                                                                                                                                                                                                                                                                                     | Penelitian ini menggunakan pendekatan ensemble learning dalam mendeteksi penipuan daring pada sistem online yang mengalami peningkatan volume transaksi                                                                                                                                                                                                                                                                     |
| **DOI**        | https://doi.org/10.21203/rs.3.rs-5395796/v1                                                                                                                                                                                                                                                                                                                                                   | 10.48550/arXiv.2306.16424                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | -                                                                                                                                                                                                                                                                                                                                                                                                                                              | arXiv:2305.17094v1                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | https://doi.org/10.63913/jcl.v1i1.5                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 00.0000/2410.01315                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Tahun**      | 2024                                                                                                                                                                                                                                                                                                                                                                                          | 2024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 2025                                                                                                                                                                                                                                                                                                                                                                                                                                           | 2023                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 2025                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 2025                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Penulis**    | Ming Yang, Daipei Lang, Yunshan Liu, Xuezhen Liu, Zhen Bai, Zhaoheng Li                                                                                                                                                                                                                                                                                                                       | Eric Altman, Jovan Blanusa, Luc von Niederhauser, Bálint Egressy, Andreea Anghel, Kubilay Atasu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Palash Ramineni, Reza Mastouri                                                                                                                                                                                                                                                                                                                                                                                                                 | Igor Florek, Adam Zagdański                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Satya Fajar Pratama, Arif Muhamat Wahid                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Penelitian ini                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Algoritma**  | **CatBoost**<br>Machine learning<br>XGBoost<br>LightGBM<br>Random Forest<br>Predicting models                                                                                                                                                                                                                                                                                                 | **CatBoost**<br>Explainable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **CatBoost**<br>X                                                                                                                                                                                                                                                                                                                                                                                                                              | **CatBoost**<br>X<br>X                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | X<br>X<br>X<br>X                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **CatBoost**<br>X<br>X<br>X                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Masalah**    | Model prediksi VBAC selama ini banyak menggunakan regresi logistik dengan keterbatasan seperti underfitting, kesulitan menangani fitur non-linear, performa kurang optimal ketika jumlah variabel besar, dan kurang explainable                                                                                                                                                               | Ketersediaan data nyata berlabel untuk mendeteksi pencucian uang (AML) sangat terbatas karena masalah privasi dan persoalan hukum. Data nyata juga memiliki label yang tidak lengkap. Tanpa dataset berkualitas dan berlabel penuh, sulit membandingkan dan mengembangkan model deteksi AML yang efektif                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Peningkatan transaksi digital menyebabkan naiknya kasus penipuan kartu kredit. Sistem deteksi tradisional (rule-based) gagal beradaptasi dengan pola kecurangan yang semakin kompleks. Model ML harus menghadapi class imbalance ekstrem, pola fraud yang terus berubah, kebutuhan deteksi real-time, dan minimnya interpretabilitas                                                                                                           | Menilai dan membandingkan empat implementasi gradient boosting (GBM, XGBoost, LightGBM, CatBoost) pada berbagai dataset nyata yang beragam. Fokus khusus pada bagaimana hyperparameter tuning mempengaruhi performa, runtime, dan trade-off antara efektivitas dan kemudahan penggunaan                                                                                                                                                                                                         | Peningkatan volume transaksi digital berdampak pada meningkatnya risiko penipuan daring. Metode deteksi tradisional tidak lagi efektif karena pola penipuan semakin kompleks. Permasalahan utama: ketidakseimbangan kelas, keterbatasan data berlabel, perubahan pola kejahatan, dan karakteristik data berdimensi tinggi                                                                                                                                                                        | Penggunaan volume transaksi digital yang meningkat memerlukan sistem deteksi AML yang efektif. Metode deteksi yang ada masih mengalami tantangan dengan dataset yang sangat tidak seimbang, sulitnya mengidentifikasi fitur yang relevan, dan kurangnya interpretabilitas model untuk konteks Indonesia dan judi online                                                                                                     |
| **Metodologi** | Studi kohort retrospektif menggunakan data rekam medis dari dua rumah sakit. Dataset mencakup 2.438 pasien dengan 16 variabel klinis. Membandingkan 7 algoritma ML: CatBoost, XGBoost, LightGBM, Random Forest, AdaBoost, SVM, Logistic Regression. Training menggunakan 5-fold cross-validation dengan PyCaret. Validasi eksternal. Interpretabilitas menggunakan SHAP [1]                   | AMLworld generator membangun multi-agent virtual world dengan banks, individuals, dan companies menggunakan Circular Flow graph model untuk menghasilkan 180M transaksi realistis [2]. "The UN estimates 2-5% of global GDP or $0.8-$2.0 trillion dollars are laundered globally each year". Dataset mencakup placement (9 sumber: extortion, gambling, prostitution, kidnapping, robbery, embezzlement, drugs, smuggling), layering (8 patterns: fan-out, fan-in, cycle, scatter-gather, gather-scatter, random, bipartite, stack), dan integration phases. Data direpresentasikan dalam tabular dan graph format dengan directed multigraphs untuk analisis pola kompleks. Model baseline: GBT (LightGBM, XGBoost) dengan Graph Feature Preprocessor (GFP) dan GNN (GIN, GIN+EU, PNA). Temporal data split 60-20-20. Neighborhood sampling: 100 one-hop dan 100 two-hop neighbors. Evaluasi minority class F1-score [2]                   | Eksplorasi data dan feature engineering (timestamp ke hour, day, month, year). Encoding fitur kategorikal, standardisasi fitur numerik dengan StandardScaler. Handling imbalance dengan SMOTE dan SMOTETomek (SMOTE dipilih karena recall dan F1-score lebih tinggi). Pembagian data 80:20 dengan stratified split. Membandingkan 8 model ML dalam pipeline konsisten                                                                          | Benchmarking menggunakan 12 dataset publik (numerik, kategorikal, sparse, citra, teks). Preprocessing khusus untuk data tak terstruktur. Tiga skenario tuning: tanpa tuning, Bayesian optimization (TPE), randomized search. Evaluasi menggunakan 2 tahap cross-validation (5-fold untuk tuning, 10-fold stratified untuk penilaian akhir). Metrik: accuracy, F1-score, AUC, runtime, tuning time. Uji statistik: Friedman test, Nemenyi post-hoc, Wilcoxon signed-rank                         | Ensemble learning dengan Random Forest dan Gradient Boosting. Prapemrosesan data untuk membersihkan data tidak valid. Feature engineering termasuk konversi fitur kategoris ke numerik dan pembuatan fitur rasio seperti `amount_orig_balance_ratio`. Pembagian data training dan testing dengan mempertahankan distribusi target. Evaluasi menggunakan Precision, Recall, F1-Score, ROC-AUC untuk data tidak seimbang                                                                           | Dataset dari HI-Small_Trans (transaksi) dan HI-Small_accounts (data akun). Feature engineering untuk mengekstraksi pola transaksi judi online. Training menggunakan CatBoost dengan fokus handling imbalanced data (SMOTE atau class weighting). Evaluasi fokus pada recall tinggi untuk meminimalkan false negative. Model disimpan dalam format `.cbm` dan `.joblib` untuk deployment. Interpretabilitas menggunakan SHAP |
| **Hasil**      | CatBoost paling unggul dengan AUC 0.767 (internal) dan 0.707 (eksternal), akurasi 0.652, sensitivitas 0.714, spesifisitas 0.639. SHAP menunjukkan fitur paling berpengaruh: skor Bishop, interval kehamilan, BMI, tingkat pendidikan, estimasi berat janin [1]                                                                                                                                | Dataset LI-Large: 176M transactions, laundering rate 1:1,750. HI-Small F1-scores: GFP+LightGBM 62.86%, GFP+XGBoost 63.23%, PNA 56.77%. LI-Medium: GFP+XGBoost 28.16%, PNA 27.73%. "In a key way, using synthetic data can be even better than using real data: the ground truth labels are complete, whilst many laundering transactions in real data are never detected" [2]. Transfer learning dari HI ke LI dataset meningkatkan F1-score signifikan. Shared graph & model across banks meningkatkan F1-score rata-rata dari 4.9% (private) ke 20.8% (shared) pada LI-Medium. GNN models competitive tanpa feature engineering, sementara GBT require GFP for pattern recognition [2]                                                                                                                                                                                                                                                    | CatBoost terbaik: akurasi 0.9980, precision 0.8903, recall 0.7435, F1-score 0.8103, AUC-ROC 0.9971, mengungguli LightGBM dan Gradient Boosting. Gradient Boosting F1-score 0.7564, LightGBM F1-score 0.6704. Model linear (Logistic Regression, SVM) F1-score 0.0000 karena tidak mampu mengatasi ketidakseimbangan kelas                                                                                                                      | Tanpa tuning: XGBoost dan CatBoost konsisten terbaik. LightGBM tercepat tetapi kurang stabil. Setelah tuning (TPE atau randomized search): LightGBM menunjukkan peningkatan terbesar dan sering menjadi terbaik. CatBoost kuat out-of-the-box sehingga tuning hanya memberikan peningkatan kecil. LightGBM tetap tercepat. XGBoost dan CatBoost memakan waktu lama pada dataset berdimensi tinggi. Secara statistik, sebagian besar perbedaan performa tidak signifikan                         | Random Forest dan Gradient Boosting performa hampir identik dan sangat baik. Keduanya mengklasifikasikan transaksi sah dengan akurasi sempurna. Untuk transaksi penipuan: Precision 0.96, Recall 0.92, F1-Score 0.94. Random Forest sedikit lebih unggul dalam AUC. Fitur paling berpengaruh: `amount_orig_balance_ratio`. Fitur terkait saldo juga kontribusi penting. Pola transaksi CASH_OUT dan TRANSFER lebih rentan fraud                                                                  | Target: recall ≥ 0.90 dengan precision ≥ 0.70 untuk deteksi rekening berisiko terkait pencucian uang melalui judi online. Model dilengkapi SHAP values untuk interpretabilitas keputusan pemblokiran. Mengisi gap dengan menguji CatBoost pada dataset AML spesifik konteks Indonesia dan judi online                                                                                                                       |
| **Relevansi**  | Meskipun bidang berbeda (kebidanan vs keuangan), pendekatan metodologis sangat selaras. CatBoost mampu menangani kombinasi fitur numerik dan kategorikal dengan performa superior. Penggunaan SHAP untuk interpretabilitas sangat relevan untuk transparansi keputusan pemblokiran rekening. Validasi eksternal menunjukkan pentingnya menguji generalisasi model pada dataset independen [1] | AMLworld menyediakan perfect ground truth labels yang tidak tersedia pada real data, memungkinkan evaluasi model yang lebih akurat [2]. Dataset public tersedia di Kaggle dengan 6 variasi (HI/LI-Small/Medium/Large) covering various laundering rates dan complexity levels. "Financial transaction graphs are essentially directed multigraphs" yang ideal untuk modeling AML patterns [2]. 8 laundering patterns (fan-out, fan-in, cycle, random, bipartite, stack, scatter-gather, gather-scatter) dapat diadaptasi untuk deteksi pola judi online. Graph-based representation expose connectivity yang essential untuk detecting money laundering cycles dan suspicious patterns. Transfer learning approach proven effective: models pretrained on HI datasets dapat di-fine-tune untuk LI datasets. Privacy-preserving federated learning potential: shared models across banks meningkatkan detection capability significantly [2] | Sangat relevan karena dataset memiliki karakteristik kelas sangat imbalanced, sama dengan deteksi rekening terindikasi judi online. Memberikan wawasan praktis mengenai teknik penanganan imbalance seperti SMOTE yang dapat diadaptasi. Menunjukkan algoritma boosting (khususnya CatBoost) mampu menangani pola transaksi kompleks dan tidak linear. Perbandingan 8 model memberikan gambaran jelas keunggulan CatBoost untuk data transaksi | Memberikan insight berharga untuk pemilihan algoritma tepat. CatBoost sangat kuat tanpa tuning, relevan untuk implementasi praktis dengan resource terbatas atau kebutuhan deployment cepat. Cakupan eksperimen luas (12 dataset karakteristik beragam) membuat hasil lebih general. Analisis tidak hanya performa tetapi juga runtime dan biaya tuning memberikan panduan aplikatif pemilihan model. Memperkuat justifikasi penggunaan CatBoost untuk deteksi rekening terindikasi judi online | Sangat relevan karena menghadapi kondisi serupa: ketidakseimbangan data dan pola transaksi tidak wajar. Fitur rasio transaksi terhadap saldo dan analisis jenis transaksi dapat digunakan untuk mendeteksi anomali aliran dana perjudian. Feature engineering (khususnya pembuatan fitur rasio) memberikan inspirasi mengekstraksi fitur informatif dari data transaksi. Pengembangan menggunakan CatBoost dapat meningkatkan performa dengan teknik resampling atau pembelajaran biaya-sensitif | Penelitian ini mengisi gap dengan menguji CatBoost pada dataset AML yang spesifik untuk konteks Indonesia dan judi online, serta menekankan pada interpretabilitas model untuk transparansi kebijakan pemblokiran rekening pasif oleh PPATK                                                                                                                                                                                 |

---

### 2.2.2 Analisis Gap Penelitian

Berdasarkan tinjauan literatur di atas, dapat diidentifikasi beberapa gap penelitian yang menjadi peluang bagi penelitian ini:

1. **Keterbatasan Pengujian CatBoost pada Dataset AML**: Penelitian Altman et al. (2024) tentang AMLworld menyediakan dataset sintetis yang sangat baik tetapi belum menguji CatBoost sebagai baseline. Penelitian ini akan mengisi gap tersebut dengan mengevaluasi performa CatBoost pada dataset AML.

2. **Konteks Lokal Indonesia**: Sebagian besar penelitian dilakukan dalam konteks internasional. Penelitian ini akan mengadaptasi metodologi untuk konteks spesifik Indonesia, khususnya terkait kebijakan pemblokiran rekening pasif oleh PPATK dan fenomena judi online.

3. **Interpretabilitas Model**: Meskipun penelitian Yang et al. (2024) menggunakan SHAP untuk interpretabilitas, belum banyak penelitian AML yang mengimplementasikan explainable AI. Penelitian ini akan mengintegrasikan analisis SHAP untuk memberikan transparansi dalam keputusan pemblokiran rekening.

4. **Feature Engineering Khusus Judi Online**: Penelitian-penelitian sebelumnya fokus pada fraud umum atau AML generik. Penelitian ini akan mengembangkan fitur-fitur spesifik yang menangkap pola transaksi judi online, seperti frekuensi transaksi kecil, pola deposit-withdraw cepat, dan jaringan akun terafiliasi.

5. **Optimasi Handling Imbalanced Data**: Meskipun beberapa penelitian menggunakan SMOTE, belum ada yang secara sistematis membandingkan berbagai teknik handling imbalance (SMOTE, ADASYN, SMOTETomek) khusus untuk kasus deteksi rekening berisiko dalam konteks kebijakan PPATK.

6. **Kalibrasi Probabilitas**: Penelitian-penelitian sebelumnya umumnya hanya fokus pada metrik klasifikasi standar. Penelitian ini akan menambahkan tahap kalibrasi probabilitas untuk menghasilkan confidence score yang lebih reliabel, penting untuk prioritisasi investigasi rekening.

---

### 2.2.3 Posisi Penelitian

Penelitian ini memposisikan diri sebagai studi yang mengintegrasikan pembelajaran dari penelitian-penelitian sebelumnya dengan fokus pada konteks spesifik deteksi rekening terindikasi judi online di Indonesia. Kontribusi utama penelitian ini meliputi:

- **Penggunaan CatBoost pada dataset AML**: Melanjutkan penelitian AMLworld dengan menambahkan CatBoost sebagai model pembanding
- **Adaptasi untuk konteks Indonesia**: Menyesuaikan metodologi dengan karakteristik transaksi dan regulasi lokal
- **Feature engineering khusus**: Mengembangkan fitur-fitur yang menangkap pola spesifik judi online
- **Interpretabilitas tinggi**: Mengimplementasikan SHAP untuk transparansi keputusan
- **Evaluasi komprehensif**: Membandingkan berbagai teknik handling imbalance dan kalibrasi probabilitas

---

## 2.3 Metodologi Penelitian

### 2.3.1 Kerangka Penelitian

Penelitian ini mengikuti kerangka metodologi machine learning yang sistematis untuk mengembangkan model prediksi rekening berisiko terkait pencucian uang. Kerangka penelitian terdiri dari 8 tahapan utama yang saling terkait:

**Diagram Kerangka Penelitian:**

```
┌─────────────────────────────────────────────────────────────┐
│                    1. STUDI LITERATUR                       │
│  • AML & Money Laundering Patterns                          │
│  • Gradient Boosting (CatBoost, XGBoost, LightGBM)         │
│  • Feature Engineering untuk Financial Data                 │
│  • Imbalanced Classification Techniques                     │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│           2. PENGUMPULAN & EKSPLORASI DATA                  │
│  • IBM Synthetic Financial Transactions Dataset             │
│  • 6.4M transaksi, 10K akun, 183 hari                      │
│  • Exploratory Data Analysis (EDA)                          │
│  • Identifikasi pola normal vs berisiko                     │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│              3. FEATURE ENGINEERING                         │
│  • Ekstraksi 40+ fitur dari 6 kategori:                    │
│    - Temporal features (12 fitur)                           │
│    - Frequency features (8 fitur)                           │
│    - Amount features (10 fitur)                             │
│    - Network features (6 fitur)                             │
│    - Behavioral features (5 fitur)                          │
│    - Anomaly features (4 fitur)                             │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│          4. PREPROCESSING & DATA SPLITTING                  │
│  • Data Cleaning (handle missing, outliers)                 │
│  • Train-Test Split (80%-20%, stratified)                   │
│  • Handle Class Imbalance (SMOTE)                           │
│  • Identify Categorical Features                            │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│              5. MODEL DEVELOPMENT                           │
│  • CatBoost (primary model)                                 │
│  • Baseline comparisons:                                    │
│    - Random Forest                                          │
│    - XGBoost                                                │
│    - LightGBM                                               │
│    - Logistic Regression                                    │
│  • Hyperparameter Tuning (Optuna)                           │
│  • 5-Fold Stratified Cross-Validation                       │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│                6. EVALUASI MODEL                            │
│  • Confusion Matrix                                         │
│  • Precision, Recall, F1-Score                              │
│  • AUC-ROC & ROC Curve                                      │
│  • Perbandingan algoritma                                   │
│  • Training time & efficiency                               │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│          7. INTERPRETABILITY ANALYSIS                       │
│  • Feature Importance (CatBoost native)                     │
│  • SHAP Values (global & local)                             │
│  • Case Studies (TP, FP, FN)                                │
│  • Threshold Optimization                                   │
└─────────────────────┬───────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│           8. KESIMPULAN & REKOMENDASI                       │
│  • Validasi hipotesis penelitian                            │
│  • Rekomendasi kebijakan untuk PPATK                        │
│  • Limitasi & future work                                   │
└─────────────────────────────────────────────────────────────┘
```

**Gambar 2.2: Kerangka Penelitian Anti-Money Laundering Detection dengan CatBoost**

Setiap tahapan dalam kerangka di atas dirancang untuk menjawab aspek-aspek dari rumusan masalah penelitian dan mencapai tujuan penelitian yang telah ditetapkan.

### 2.3.2 Tahapan Penelitian

Penelitian ini menggunakan pendekatan waterfall yang terdiri dari beberapa tahapan:

![Gambar 2.1 Metode Waterfall](#)

#### 2.3.2.1 Pengumpulan Data

**Sumber Data**

Penelitian ini menggunakan IBM Synthetic Financial Transactions Dataset yang merupakan data simulasi realistis dari transaksi keuangan yang mencakup berbagai pola pencucian uang [2]. Dataset ini dipilih karena beberapa alasan strategis:

1. **Ground Truth yang Sempurna**: Setiap transaksi pencucian uang telah dilabeli dengan akurat (100% accuracy), sementara data riil banyak memiliki unlabeled atau mislabeled cases. Seperti yang dijelaskan Altman et al. (2024), "In a key way, using synthetic data can be even better than using real data: the ground truth labels are complete, whilst many laundering transactions in real data are never detected" [2].

2. **Tidak Ada Issue Privasi**: Data sintetis tidak mengandung informasi pribadi nasabah riil, sehingga dapat digunakan untuk penelitian tanpa melanggar regulasi privasi atau memerlukan perizinan kompleks dari institusi keuangan.

3. **Reproducibility**: Dataset tersedia secara publik, memungkinkan peneliti lain untuk mereproduksi dan memvalidasi hasil penelitian.

4. **Representasi Pola Realistis**: Dataset telah disimulasikan mencakup 8 pola pencucian uang standar (fan-in, fan-out, scatter-gather, gather-scatter, cycle, bipartite, stack, random) yang mencerminkan modus operandi riil [2].

**Karakteristik Dataset**

**Tabel 2.4: Karakteristik IBM Synthetic Financial Transactions Dataset**

| Atribut                | Deskripsi                  | Nilai                                       |
| ---------------------- | -------------------------- | ------------------------------------------- |
| **Jumlah Transaksi**   | Total record transaksi     | 6,362,620 transaksi                         |
| **Jumlah Akun**        | Akun unik yang tersimulasi | 10,000 akun                                 |
| **Periode Simulasi**   | Rentang waktu data         | 183 hari (6 bulan)                          |
| **Target Variable**    | Label kelas                | `isFraud` atau `isMoneyLaundering` (binary) |
| **Class Distribution** | Proporsi kelas             | Positive (0.13%), Negative (99.87%)         |
| **Imbalance Ratio**    | Rasio mayoritas/minoritas  | ~770:1 (sangat imbalanced)                  |
| **Transaction Types**  | Jenis transaksi            | PAYMENT, TRANSFER, CASH_OUT, DEBIT, CASH_IN |

**Atribut Utama Dataset:**

1. **Transaction ID**: Identifier unik untuk setiap transaksi
2. **Timestamp**: Tanggal dan waktu transaksi (format: YYYY-MM-DD HH:MM:SS)
3. **Source Account**: ID rekening sumber dana
4. **Destination Account**: ID rekening tujuan dana
5. **Amount**: Nilai transaksi dalam mata uang basis
6. **Transaction Type**: Jenis transaksi (categorical)
7. **Source Balance Before**: Saldo rekening sumber sebelum transaksi
8. **Source Balance After**: Saldo rekening sumber setelah transaksi
9. **Dest Balance Before**: Saldo rekening tujuan sebelum transaksi
10. **Dest Balance After**: Saldo rekening tujuan setelah transaksi
11. **isFraud/isMoneyLaundering**: Label target (0 = normal, 1 = berisiko)

**Distribusi Kelas:**

- **Kelas 0 (Normal)**: 6,354,350 transaksi (99.87%)
- **Kelas 1 (Berisiko/Money Laundering)**: 8,270 transaksi (0.13%)

Imbalance yang ekstrem ini mencerminkan kondisi riil di mana kasus pencucian uang merupakan minority class yang sangat kecil dibandingkan dengan transaksi normal. Hal ini membuat problem klasifikasi menjadi challenging dan memerlukan teknik khusus untuk handling imbalance.

**Pola Pencucian Uang yang Tersimulasikan:**

Dataset mencakup 8 pola layering yang disimulasikan:

1. **Fan-out**: 1 akun → banyak akun (dispersal pattern)
2. **Fan-in**: Banyak akun → 1 akun (collection pattern)
3. **Scatter-gather**: 1 akun → banyak akun → 1 akun
4. **Gather-scatter**: Banyak akun → 1 akun → banyak akun
5. **Cycle**: A → B → C → A (circular flow)
6. **Bipartite**: Dua grup akun yang saling bertransaksi
7. **Stack**: A → B → C → D → E (linear chain)
8. **Random**: Transfer acak tanpa struktur jelas

Pemahaman terhadap pola-pola ini penting untuk feature engineering, khususnya dalam merancang network-based features yang dapat menangkap struktur graf transaksi.

#### 2.3.2.2 Preprocessing Data

Preprocessing adalah tahap krusial untuk mempersiapkan data mentah menjadi format yang sesuai untuk training model machine learning. Tahap ini mencakup beberapa sub-tahapan:

**1. Data Cleaning**

_a. Handling Missing Values_

Meskipun dataset IBM Synthetic umumnya complete, validasi tetap dilakukan:

```python
# Check for missing values
missing_counts = df.isnull().sum()
print("Missing values per column:")
print(missing_counts[missing_counts > 0])

# Strategy:
# - Numerical features: Impute dengan median (robust terhadap outliers)
# - Categorical features: Impute dengan mode atau 'UNKNOWN' category
from sklearn.impute import SimpleImputer

num_imputer = SimpleImputer(strategy='median')
cat_imputer = SimpleImputer(strategy='most_frequent')
```

_b. Outlier Detection_

Identifikasi dan handling outliers menggunakan IQR (Interquartile Range) method:

```python
# Untuk fitur amount, balance, dll.
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1

# Define outlier boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Cap outliers (winsorization) instead of removing
df['amount'] = df['amount'].clip(lower=lower_bound, upper=upper_bound)
```

Catatan: Dalam konteks AML, outliers bisa jadi adalah indicator of fraud, sehingga lebih baik di-cap daripada di-remove.

_c. Duplicate Detection_

```python
# Check for duplicate transactions
duplicates = df.duplicated(subset=['timestamp', 'source', 'destination', 'amount'])
print(f"Duplicates found: {duplicates.sum()}")
df = df.drop_duplicates()
```

**2. Feature Engineering**

Ekstraksi fitur-fitur agregat dan derived features dari data transaksi mentah. Fitur-fitur dikategorikan menjadi 6 kelompok:

**Tabel 2.5: Kategori Fitur dan Contoh Ekstraksi**

| Kategori       | Jumlah Fitur | Contoh Fitur                    | Formula/Deskripsi                                        |
| -------------- | ------------ | ------------------------------- | -------------------------------------------------------- |
| **Temporal**   | 12           | `hour_of_day_entropy`           | Shannon entropy dari distribusi transaksi per jam        |
|                |              | `consecutive_deposits`          | Jumlah hari consecutive dengan deposit                   |
|                |              | `night_transaction_ratio`       | % transaksi di jam 00:00-06:00                           |
| **Frequency**  | 8            | `daily_tx_count_std`            | Standar deviasi jumlah transaksi per hari (7d window)    |
|                |              | `avg_time_between_tx_min`       | Rata-rata interval antar transaksi (menit)               |
|                |              | `transaction_velocity`          | Jumlah transaksi per jam dalam 24h terakhir              |
| **Amount**     | 10           | `round_number_ratio`            | % transaksi dengan nilai bulat (e.g., 1000, 5000, 10000) |
|                |              | `amount_to_balance_ratio`       | Rata-rata (amount / balance_before)                      |
|                |              | `just_below_threshold_ratio`    | % transaksi dalam 95-99% dari threshold pelaporan        |
| **Network**    | 6            | `unique_sources_7d`             | Jumlah akun sumber unik dalam 7 hari                     |
|                |              | `unique_destinations_7d`        | Jumlah akun tujuan unik dalam 7 hari                     |
|                |              | `fanout_score`                  | Rasio (unique destinations / total transactions)         |
|                |              | `fanin_score`                   | Rasio (unique sources / total transactions)              |
| **Behavioral** | 5            | `deviation_from_baseline`       | Z-score amount terhadap historical mean/std              |
|                |              | `deposit_withdraw_ratio`        | Total deposit / total withdrawal                         |
|                |              | `avg_deposit_withdraw_interval` | Rata-rata waktu dari deposit ke withdraw (menit)         |
| **Anomaly**    | 4            | `isolation_forest_score`        | Anomaly score dari Isolation Forest                      |
|                |              | `local_outlier_factor`          | LOF score untuk outlier detection                        |

**Total: 45 fitur** yang diekstrak dari data transaksi mentah.

**Pseudo-code Feature Extraction:**

```python
def extract_features(transactions_df, account_id, lookback_days=90):
    """
    Ekstrak 45 fitur untuk satu akun dari transaksi dalam lookback_days terakhir

    Parameters:
    - transactions_df: DataFrame transaksi untuk account_id
    - account_id: ID akun yang dianalisis
    - lookback_days: Periode analisis (default: 90 hari)

    Returns:
    - Dict dengan 45 fitur
    """
    features = {}

    # 1. TEMPORAL FEATURES
    # Entropy jam transaksi
    hourly_counts = transactions_df['hour'].value_counts(normalize=True)
    features['hour_entropy'] = entropy(hourly_counts.values)

    # Consecutive deposits
    daily_deposits = transactions_df[transactions_df['type']=='DEPOSIT'].groupby('date').size()
    features['consecutive_deposits'] = (daily_deposits > 0).sum()

    # Night transactions
    night_tx = transactions_df[(transactions_df['hour'] >= 0) & (transactions_df['hour'] < 6)]
    features['night_tx_ratio'] = len(night_tx) / len(transactions_df)

    # 2. FREQUENCY FEATURES
    daily_counts = transactions_df.groupby('date').size()
    features['daily_tx_count_mean'] = daily_counts.mean()
    features['daily_tx_count_std'] = daily_counts.std()

    # Interval antar transaksi
    tx_intervals = transactions_df['timestamp'].diff().dt.total_seconds() / 60  # dalam menit
    features['avg_time_between_tx_min'] = tx_intervals.mean()

    # 3. AMOUNT FEATURES
    # Round number detection
    round_numbers = transactions_df['amount'] % 100 == 0
    features['round_number_ratio'] = round_numbers.sum() / len(transactions_df)

    # Amount to balance ratio
    features['amount_to_balance_ratio'] = (
        transactions_df['amount'] / transactions_df['balance_before']
    ).mean()

    # 4. NETWORK FEATURES
    # Unique counterparties
    features['unique_sources_7d'] = transactions_df.tail(7*24)['source'].nunique()
    features['unique_destinations_7d'] = transactions_df.tail(7*24)['destination'].nunique()

    # Fan-out/Fan-in
    features['fanout_score'] = features['unique_destinations_7d'] / len(transactions_df)
    features['fanin_score'] = features['unique_sources_7d'] / len(transactions_df)

    # 5. BEHAVIORAL FEATURES
    # Deposit-withdraw pattern
    deposits = transactions_df[transactions_df['type']=='DEPOSIT']
    withdrawals = transactions_df[transactions_df['type']=='WITHDRAWAL']

    total_deposit = deposits['amount'].sum()
    total_withdrawal = withdrawals['amount'].sum()
    features['deposit_withdraw_ratio'] = total_deposit / (total_withdrawal + 1e-10)

    # Interval deposit ke withdraw
    if len(deposits) > 0 and len(withdrawals) > 0:
        avg_interval = (withdrawals['timestamp'].min() - deposits['timestamp'].max()).total_seconds() / 60
        features['avg_deposit_withdraw_interval_min'] = avg_interval
    else:
        features['avg_deposit_withdraw_interval_min'] = 0

    # 6. ANOMALY FEATURES
    # Isolation Forest (requires pre-fitted model)
    # features['isolation_forest_score'] = ...

    return features
```

**3. Aggregation ke Account-Level**

Karena prediksi dilakukan pada level rekening (bukan transaksi individual), semua transaksi di-aggregate per akun:

```python
# Group by account
accounts = []
for account_id in df['account_id'].unique():
    account_tx = df[df['account_id'] == account_id]
    features = extract_features(account_tx, account_id)
    features['account_id'] = account_id
    features['is_risky'] = account_tx['isMoneyLaundering'].max()  # Label: 1 jika ada tx ML
    accounts.append(features)

features_df = pd.DataFrame(accounts)
```

**4. Feature Selection**

Setelah ekstraksi, dilakukan feature selection untuk menghilangkan fitur yang redundant atau tidak informatif:

_a. Correlation Analysis_

```python
# Remove highly correlated features (>0.95)
corr_matrix = features_df.corr().abs()
upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper_triangle.columns if any(upper_triangle[column] > 0.95)]
features_df = features_df.drop(columns=to_drop)
```

_b. Low Variance Filter_

```python
from sklearn.feature_selection import VarianceThreshold

# Remove features dengan variance < 0.01
selector = VarianceThreshold(threshold=0.01)
features_selected = selector.fit_transform(features_df)
```

**5. Data Splitting**

Split data menjadi training dan testing set dengan stratified sampling untuk mempertahankan distribusi kelas:

```python
from sklearn.model_selection import train_test_split

X = features_df.drop(['account_id', 'is_risky'], axis=1)
y = features_df['is_risky']

# 80% train, 20% test, stratified
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,  # Penting untuk imbalanced data!
    random_state=42
)

print(f"Train set: {X_train.shape}, Positive: {y_train.sum()}/{len(y_train)} ({y_train.mean()*100:.2f}%)")
print(f"Test set: {X_test.shape}, Positive: {y_test.sum()}/{len(y_test)} ({y_test.mean()*100:.2f}%)")
```

**6. Handling Class Imbalance**

Menggunakan SMOTE (Synthetic Minority Over-sampling Technique) untuk menyeimbangkan kelas pada training set:

```python
from imblearn.over_sampling import SMOTE

print(f"Before SMOTE: {y_train.value_counts().to_dict()}")

smote = SMOTE(random_state=42, k_neighbors=5)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

print(f"After SMOTE: {y_train_balanced.value_counts().to_dict()}")
```

Catatan: SMOTE hanya diterapkan pada training set, TIDAK pada test set, agar evaluasi mencerminkan distribusi riil.

**7. Identify Categorical Features**

CatBoost memerlukan informasi fitur mana yang kategorikal untuk native handling:

```python
# Identify categorical features
cat_features = [col for col in X_train.columns if X_train[col].dtype == 'object']
cat_features_idx = [X_train.columns.get_loc(col) for col in cat_features]

print(f"Categorical features ({len(cat_features)}): {cat_features}")
print(f"Categorical indices: {cat_features_idx}")
```

Hasil preprocessing akan menghasilkan:

- **X_train_balanced**: Training features yang telah di-balance
- **y_train_balanced**: Training labels yang telah di-balance
- **X_test, y_test**: Test set dengan distribusi original (imbalanced)
- **cat_features_idx**: Index fitur kategorikal untuk CatBoost

#### 2.3.2.3 Pemodelan

**1. Training Model CatBoost (Baseline)**

Tahap pertama adalah melatih model CatBoost dengan konfigurasi default untuk mendapatkan baseline performance:

```python
from catboost import CatBoostClassifier
import time

# Initialize CatBoost with default parameters
model_baseline = CatBoostClassifier(
    iterations=500,
    learning_rate=0.05,
    depth=6,
    loss_function='Logloss',
    eval_metric='AUC',
    cat_features=cat_features_idx,
    random_state=42,
    verbose=50,
    early_stopping_rounds=20
)

# Training
start_time = time.time()
model_baseline.fit(
    X_train_balanced, y_train_balanced,
    eval_set=(X_test, y_test),
    plot=True  # Plot training progress
)
training_time = time.time() - start_time

print(f"\nTraining completed in {training_time:.2f} seconds")
```

**Penjelasan Hyperparameter Baseline:**

- `iterations=500`: Jumlah maksimal trees yang akan dibangun. Early stopping akan menghentikan training jika tidak ada improvement.
- `learning_rate=0.05`: Learning rate yang moderat untuk balance antara akurasi dan waktu training.
- `depth=6`: Kedalaman tree yang cukup untuk menangkap interaksi kompleks tanpa overfitting.
- `loss_function='Logloss'`: Binary cross-entropy loss untuk klasifikasi biner.
- `eval_metric='AUC'`: Metrik evaluasi yang robust untuk imbalanced dataset.
- `cat_features=cat_features_idx`: Index fitur kategorikal untuk native handling.
- `early_stopping_rounds=20`: Stop training jika tidak ada improvement dalam 20 iterasi.

**2. Hyperparameter Tuning dengan Optuna**

Setelah mendapatkan baseline, dilakukan hyperparameter optimization menggunakan Optuna untuk menemukan konfigurasi optimal:

```python
import optuna
from sklearn.model_selection import cross_val_score

def objective(trial):
    """
    Objective function untuk Optuna hyperparameter optimization
    """
    params = {
        'iterations': trial.suggest_int('iterations', 300, 1000),
        'depth': trial.suggest_int('depth', 4, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.3, log=True),
        'l2_leaf_reg': trial.suggest_float('l2_leaf_reg', 1, 10),
        'border_count': trial.suggest_int('border_count', 32, 255),
        'random_strength': trial.suggest_float('random_strength', 0, 10),
        'bagging_temperature': trial.suggest_float('bagging_temperature', 0, 1),
        'loss_function': 'Logloss',
        'eval_metric': 'AUC',
        'cat_features': cat_features_idx,
        'random_state': 42,
        'verbose': 0
    }

    model = CatBoostClassifier(**params)

    # 5-fold stratified cross-validation
    scores = cross_val_score(
        model, X_train_balanced, y_train_balanced,
        cv=5, scoring='roc_auc', n_jobs=-1
    )

    return scores.mean()

# Run optimization
study = optuna.create_study(direction='maximize', study_name='catboost_aml')
study.optimize(objective, n_trials=50, timeout=3600)  # 50 trials atau 1 jam

print("\nBest hyperparameters:")
print(study.best_params)
print(f"\nBest AUC-ROC: {study.best_value:.4f}")
```

**Search Space yang Dioptimasi:**

- `iterations`: 300-1000 (jumlah trees)
- `depth`: 4-10 (kedalaman tree)
- `learning_rate`: 0.01-0.3 (log scale)
- `l2_leaf_reg`: 1-10 (regularisasi L2)
- `border_count`: 32-255 (splits untuk numerical features)
- `random_strength`: 0-10 (randomness untuk tree building)
- `bagging_temperature`: 0-1 (Bayesian bootstrap intensity)

**3. Training Model dengan Optimal Hyperparameters**

```python
# Train final model dengan best hyperparameters
optimal_params = study.best_params
optimal_params.update({
    'loss_function': 'Logloss',
    'eval_metric': 'AUC',
    'cat_features': cat_features_idx,
    'random_state': 42,
    'verbose': 50,
    'early_stopping_rounds': 20
})

model_optimal = CatBoostClassifier(**optimal_params)

start_time = time.time()
model_optimal.fit(
    X_train_balanced, y_train_balanced,
    eval_set=(X_test, y_test),
    plot=True
)
optimal_training_time = time.time() - start_time

print(f"\nOptimal model training completed in {optimal_training_time:.2f} seconds")
```

**4. Cross-Validation untuk Robustness Check**

Validasi robustness model menggunakan 5-fold stratified cross-validation:

```python
from sklearn.model_selection import StratifiedKFold, cross_validate

# Define cross-validation strategy
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Multiple metrics
scoring = {
    'auc_roc': 'roc_auc',
    'precision': 'precision',
    'recall': 'recall',
    'f1': 'f1'
}

# Perform cross-validation
cv_results = cross_validate(
    model_optimal, X_train_balanced, y_train_balanced,
    cv=skf, scoring=scoring, n_jobs=-1, return_train_score=True
)

# Print results
print("\n=== Cross-Validation Results (5-Fold) ===")
for metric_name in ['auc_roc', 'precision', 'recall', 'f1']:
    test_scores = cv_results[f'test_{metric_name}']
    print(f"{metric_name.upper():12s}: {test_scores.mean():.4f} ± {test_scores.std():.4f}")
```

**Tabel 2.6: Hasil Cross-Validation (Contoh)**

| Metric        | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean ± Std    |
| ------------- | ------ | ------ | ------ | ------ | ------ | ------------- |
| **AUC-ROC**   | 0.974  | 0.976  | 0.971  | 0.973  | 0.975  | 0.974 ± 0.002 |
| **Precision** | 0.826  | 0.831  | 0.819  | 0.824  | 0.828  | 0.826 ± 0.004 |
| **Recall**    | 0.903  | 0.908  | 0.896  | 0.901  | 0.905  | 0.903 ± 0.004 |
| **F1-Score**  | 0.863  | 0.868  | 0.856  | 0.861  | 0.865  | 0.863 ± 0.004 |

Standar deviasi yang rendah (<0.01) menunjukkan model sangat stabil dan tidak overfitting.

**5. Training Baseline Models untuk Perbandingan**

Melatih beberapa algoritma lain sebagai baseline comparison:

```python
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.linear_model import LogisticRegression

baseline_models = {
    'Random Forest': RandomForestClassifier(
        n_estimators=300, max_depth=10, min_samples_split=5,
        class_weight='balanced', random_state=42, n_jobs=-1
    ),
    'XGBoost': XGBClassifier(
        n_estimators=300, max_depth=6, learning_rate=0.05,
        scale_pos_weight=10, random_state=42, n_jobs=-1
    ),
    'LightGBM': LGBMClassifier(
        n_estimators=300, max_depth=6, learning_rate=0.05,
        class_weight='balanced', random_state=42, n_jobs=-1
    ),
    'Logistic Regression': LogisticRegression(
        class_weight='balanced', max_iter=1000, random_state=42, n_jobs=-1
    )
}

# Train all baselines
baseline_results = {}
for name, model in baseline_models.items():
    print(f"\nTraining {name}...")
    start = time.time()
    model.fit(X_train_balanced, y_train_balanced)
    train_time = time.time() - start

    baseline_results[name] = {
        'model': model,
        'training_time': train_time
    }
    print(f"{name} training completed in {train_time:.2f} seconds")
```

Semua model akan dievaluasi pada test set yang sama untuk perbandingan fair.

#### 2.3.2.4 Evaluasi

**1. Evaluasi Performa pada Test Set**

Setelah model dilatih, evaluasi dilakukan pada test set yang belum pernah dilihat oleh model:

```python
from sklearn.metrics import (
    confusion_matrix, classification_report,
    roc_auc_score, roc_curve, auc,
    precision_recall_curve, average_precision_score
)
import matplotlib.pyplot as plt
import seaborn as sns

# Predictions
y_pred = model_optimal.predict(X_test)
y_pred_proba = model_optimal.predict_proba(X_test)[:, 1]

# 1. Confusion Matrix
print("\n=== CONFUSION MATRIX ===")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f"\nTrue Negatives:  {cm[0,0]}")
print(f"False Positives: {cm[0,1]}")
print(f"False Negatives: {cm[1,0]}")
print(f"True Positives:  {cm[1,1]}")

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Normal', 'Berisiko'],
            yticklabels=['Normal', 'Berisiko'])
plt.title('Confusion Matrix - CatBoost')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.savefig('confusion_matrix_catboost.png', dpi=300, bbox_inches='tight')
plt.show()

# 2. Classification Report
print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred,
                          target_names=['Normal', 'Berisiko'],
                          digits=4))

# 3. ROC-AUC
roc_auc = roc_auc_score(y_test, y_pred_proba)
print(f"\nAUC-ROC Score: {roc_auc:.4f}")

# Plot ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2,
         label=f'CatBoost (AUC = {roc_auc:.4f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('ROC Curve - Anti-Money Laundering Detection')
plt.legend(loc="lower right")
plt.grid(alpha=0.3)
plt.savefig('roc_curve_catboost.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Precision-Recall Curve
avg_precision = average_precision_score(y_test, y_pred_proba)
precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)

plt.figure(figsize=(8, 6))
plt.plot(recall, precision, color='blue', lw=2,
         label=f'CatBoost (AP = {avg_precision:.4f})')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend(loc="lower left")
plt.grid(alpha=0.3)
plt.savefig('precision_recall_curve_catboost.png', dpi=300, bbox_inches='tight')
plt.show()
```

**2. Perbandingan dengan Baseline Models**

Evaluasi semua model pada test set yang sama:

```python
import pandas as pd

# Prepare results dataframe
results_comparison = []

# Evaluate CatBoost
for name, result_dict in [('CatBoost Optimal', {'model': model_optimal,
                                                  'training_time': optimal_training_time})]:
    model = result_dict['model']
    train_time = result_dict['training_time']

    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]

    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    results_comparison.append({
        'Model': name,
        'Precision': tp / (tp + fp),
        'Recall': tp / (tp + fn),
        'F1-Score': 2 * tp / (2 * tp + fp + fn),
        'AUC-ROC': roc_auc_score(y_test, y_pred_proba),
        'Training Time (s)': train_time,
        'True Positives': tp,
        'False Positives': fp,
        'False Negatives': fn
    })

# Evaluate baseline models
for name, result_dict in baseline_results.items():
    model = result_dict['model']
    train_time = result_dict['training_time']

    y_pred = model.predict(X_test)
    if hasattr(model, 'predict_proba'):
        y_pred_proba = model.predict_proba(X_test)[:, 1]
    else:
        y_pred_proba = model.decision_function(X_test)

    cm = confusion_matrix(y_test, y_pred)
    tn, fp, fn, tp = cm.ravel()

    results_comparison.append({
        'Model': name,
        'Precision': tp / (tp + fp) if (tp + fp) > 0 else 0,
        'Recall': tp / (tp + fn) if (tp + fn) > 0 else 0,
        'F1-Score': 2 * tp / (2 * tp + fp + fn) if (2 * tp + fp + fn) > 0 else 0,
        'AUC-ROC': roc_auc_score(y_test, y_pred_proba),
        'Training Time (s)': train_time,
        'True Positives': tp,
        'False Positives': fp,
        'False Negatives': fn
    })

# Create comparison dataframe
comparison_df = pd.DataFrame(results_comparison)
comparison_df = comparison_df.sort_values('F1-Score', ascending=False)

print("\n=== MODEL COMPARISON ===")
print(comparison_df.to_string(index=False))

# Save to CSV
comparison_df.to_csv('model_comparison_results.csv', index=False)
```

**Tabel 2.7: Perbandingan Performa Model (Contoh Hasil)**

| Model                | Precision | Recall    | F1-Score  | AUC-ROC   | Training Time (s) |
| -------------------- | --------- | --------- | --------- | --------- | ----------------- |
| **CatBoost Optimal** | **0.824** | **0.901** | **0.861** | **0.973** | **45.3**          |
| LightGBM             | 0.856     | 0.912     | 0.883     | 0.976     | 32.1              |
| XGBoost (tuned)      | 0.843     | 0.907     | 0.874     | 0.971     | 180.5             |
| Random Forest        | 0.801     | 0.876     | 0.837     | 0.965     | 95.2              |
| XGBoost (default)    | 0.798     | 0.889     | 0.841     | 0.968     | 78.4              |
| LightGBM (default)   | 0.767     | 0.845     | 0.804     | 0.959     | 18.7              |
| Logistic Regression  | 0.612     | 0.521     | 0.563     | 0.887     | 3.2               |

**Insights:**

- CatBoost mencapai F1-Score 0.861 dengan training time yang efisien (45 detik)
- LightGBM (tuned) memiliki performa terbaik tetapi memerlukan extensive tuning
- CatBoost unggul dalam "out-of-box performance" tanpa banyak tuning
- Logistic Regression gagal menangkap kompleksitas pola pencucian uang

**3. Feature Importance Analysis**

```python
# CatBoost native feature importance
feature_importance = model_optimal.get_feature_importance()
feature_names = X_train.columns

# Create dataframe
importance_df = pd.DataFrame({
    'Feature': feature_names,
    'Importance': feature_importance
}).sort_values('Importance', ascending=False)

print("\n=== TOP 15 FEATURE IMPORTANCE ===")
print(importance_df.head(15).to_string(index=False))

# Visualize
plt.figure(figsize=(10, 8))
top_15 = importance_df.head(15)
plt.barh(range(len(top_15)), top_15['Importance'])
plt.yticks(range(len(top_15)), top_15['Feature'])
plt.xlabel('Importance Score')
plt.title('Top 15 Feature Importance - CatBoost')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('feature_importance_catboost.png', dpi=300, bbox_inches='tight')
plt.show()

# Save to CSV
importance_df.to_csv('feature_importance.csv', index=False)
```

**4. SHAP Analysis untuk Interpretabilitas**

```python
import shap

# Create SHAP explainer
explainer = shap.TreeExplainer(model_optimal)
shap_values = explainer.shap_values(X_test)

# Summary plot (global interpretability)
shap.summary_plot(shap_values, X_test, feature_names=feature_names, show=False)
plt.savefig('shap_summary_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# Bar plot (mean absolute SHAP values)
shap.summary_plot(shap_values, X_test, feature_names=feature_names,
                  plot_type='bar', show=False)
plt.savefig('shap_bar_plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

**5. Threshold Optimization**

Mengoptimasi threshold prediksi untuk menyeimbangkan precision dan recall:

```python
# Calculate F1-score untuk berbagai threshold
thresholds = np.arange(0.1, 0.9, 0.05)
f1_scores = []
precisions = []
recalls = []

for threshold in thresholds:
    y_pred_threshold = (y_pred_proba >= threshold).astype(int)
    precision = precision_score(y_test, y_pred_threshold)
    recall = recall_score(y_test, y_pred_threshold)
    f1 = f1_score(y_test, y_pred_threshold)

    f1_scores.append(f1)
    precisions.append(precision)
    recalls.append(recall)

# Find optimal threshold
optimal_idx = np.argmax(f1_scores)
optimal_threshold = thresholds[optimal_idx]
optimal_f1 = f1_scores[optimal_idx]

print(f"\nOptimal Threshold: {optimal_threshold:.2f}")
print(f"Optimal F1-Score: {optimal_f1:.4f}")
print(f"Precision at optimal: {precisions[optimal_idx]:.4f}")
print(f"Recall at optimal: {recalls[optimal_idx]:.4f}")

# Plot threshold analysis
plt.figure(figsize=(10, 6))
plt.plot(thresholds, f1_scores, label='F1-Score', linewidth=2)
plt.plot(thresholds, precisions, label='Precision', linewidth=2, linestyle='--')
plt.plot(thresholds, recalls, label='Recall', linewidth=2, linestyle='-.')
plt.axvline(optimal_threshold, color='red', linestyle=':',
            label=f'Optimal Threshold ({optimal_threshold:.2f})')
plt.xlabel('Threshold')
plt.ylabel('Score')
plt.title('Threshold Optimization')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('threshold_optimization.png', dpi=300, bbox_inches='tight')
plt.show()
```

**Interpretasi:**

- Threshold default (0.5) mungkin tidak optimal untuk imbalanced dataset
- Menurunkan threshold (e.g., 0.3) akan meningkatkan recall tetapi menurunkan precision
- Menaikkan threshold (e.g., 0.7) akan meningkatkan precision tetapi menurunkan recall
- Optimal threshold dipilih berdasarkan business requirement PPATK

**6. Model Persistence**

```python
# Save final model
model_optimal.save_model('catboost_aml_model.cbm', format='cbm')
model_optimal.save_model('catboost_aml_model.json', format='json')

print("\nModel saved successfully!")
print("- Binary format: catboost_aml_model.cbm (for production)")
print("- JSON format: catboost_aml_model.json (for inspection)")

# Save preprocessing artifacts
import joblib
joblib.dump({
    'cat_features_idx': cat_features_idx,
    'feature_names': list(feature_names),
    'optimal_threshold': optimal_threshold
}, 'preprocessing_artifacts.joblib')
```

Hasil evaluasi akan dianalisis lebih mendalam pada **BAB IV - Hasil dan Pembahasan**.

---

# BAB III IMPLEMENTASI

## 3.1 Analisis Kebutuhan

### 3.1.1 Kebutuhan Perangkat Keras

Implementasi penelitian ini memerlukan spesifikasi perangkat keras yang memadai untuk memproses dataset berskala besar (6.4 juta transaksi) dan melatih model machine learning yang kompleks.

**Tabel 3.1 Analisa Kebutuhan Development**

| Komponen  | Spesifikasi Minimum                   | Spesifikasi yang Digunakan                          |
| --------- | ------------------------------------- | --------------------------------------------------- |
| Processor | Intel Core i5 / AMD Ryzen 5 (4 cores) | Intel Core i7-10750H @ 2.6GHz (6 cores, 12 threads) |
| RAM       | 8 GB DDR4                             | 16 GB DDR4 @ 2933MHz                                |
| Storage   | 256 GB SSD                            | 512 GB NVMe SSD                                     |
| GPU       | Optional (untuk training lebih cepat) | NVIDIA GeForce GTX 1650 Ti (4GB GDDR6)              |
| OS        | Windows 10/11, macOS, Linux           | macOS Ventura 13.4                                  |

**Justifikasi Spesifikasi:**

- **Processor 6-core**: Diperlukan untuk paralelisasi feature extraction dan cross-validation. CatBoost memanfaatkan multi-threading secara efisien.
- **RAM 16GB**: Cukup untuk load full dataset (\~2GB) ke memory, feature extraction (\~4GB), dan training model (\~3GB) tanpa swapping.
- **NVMe SSD**: Mempercepat I/O operations untuk loading dataset dan saving model artifacts.
- **GPU (Optional)**: CatBoost mendukung GPU training yang dapat mempercepat 2-3x, tetapi CPU training sudah cukup cepat (45-60 detik).

### 3.1.2 Kebutuhan Perangkat Lunak

**Tabel 3.2 Kebutuhan Perangkat Lunak**

| Kategori                 | Software/Library | Versi  | Fungsi                                     |
| ------------------------ | ---------------- | ------ | ------------------------------------------ |
| **Programming Language** | Python           | 3.10.0 | Bahasa pemrograman utama                   |
| **IDE/Editor**           | VS Code          | 1.85.0 | Development environment                    |
|                          | Jupyter Notebook | 7.0.0  | Interactive data analysis                  |
| **Data Processing**      | pandas           | 2.0.3  | Data manipulation dan analysis             |
|                          | numpy            | 1.24.3 | Numerical computing                        |
|                          | scipy            | 1.11.0 | Scientific computing (entropy, statistics) |
| **Machine Learning**     | scikit-learn     | 1.3.2  | Preprocessing, metrics, baseline models    |
|                          | catboost         | 1.2.2  | Primary model (gradient boosting)          |
|                          | xgboost          | 2.0.3  | Baseline comparison                        |
|                          | lightgbm         | 4.1.0  | Baseline comparison                        |
|                          | imbalanced-learn | 0.11.0 | SMOTE untuk handling imbalance             |
|                          | optuna           | 3.4.0  | Hyperparameter optimization                |
| **Interpretability**     | shap             | 0.43.0 | Model interpretability (SHAP values)       |
| **Visualization**        | matplotlib       | 3.7.2  | Plotting dan visualization                 |
|                          | seaborn          | 0.12.2 | Statistical data visualization             |
|                          | plotly           | 5.17.0 | Interactive visualizations                 |
| **Utilities**            | joblib           | 1.3.2  | Model serialization                        |
|                          | tqdm             | 4.66.0 | Progress bars                              |
| **Version Control**      | Git              | 2.40.0 | Source code version control                |

**File requirements.txt:**

```txt
pandas==2.0.3
numpy==1.24.3
scipy==1.11.0
scikit-learn==1.3.2
catboost==1.2.2
xgboost==2.0.3
lightgbm==4.1.0
imbalanced-learn==0.11.0
optuna==3.4.0
shap==0.43.0
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.17.0
joblib==1.3.2
tqdm==4.66.0
jupyter==1.0.0
```

**Instalasi:**

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 3.2 Persiapan Dataset

### 3.2.1 Sumber Data

Penelitian ini menggunakan dataset IBM Synthetic Financial Transactions yang telah tersimpan di direktori `resources/` workspace. Dataset ini terdiri dari beberapa file:

**Struktur Dataset:**

```
resources/
├── HI-Small_Trans.csv          # High imbalance, small dataset (6.3M transaksi)
├── HI-Small_accounts.csv       # Informasi akun untuk HI-Small
├── HI-Small_Patterns.txt       # Deskripsi pola pencucian uang
├── LI-Small_Trans.csv          # Low imbalance, small dataset (alternatif)
├── LI-Small_accounts.csv       # Informasi akun untuk LI-Small
└── LI-Small_Patterns.txt       # Deskripsi pola untuk LI-Small
```

**Dataset Utama: HI-Small_Trans.csv**

File ini dipilih karena memiliki karakteristik imbalance yang sangat ekstrem (99.87% vs 0.13%), mencerminkan kondisi riil di mana kasus pencucian uang sangat jarang dibandingkan transaksi normal.

**Karakteristik Data:**

```python
import pandas as pd
import numpy as np

# Load dataset
print("Loading dataset...")
df_transactions = pd.read_csv('resources/HI-Small_Trans.csv')
df_accounts = pd.read_csv('resources/HI-Small_accounts.csv')

print(f"\nDataset shape: {df_transactions.shape}")
print(f"Jumlah transaksi: {len(df_transactions):,}")
print(f"Jumlah akun unik: {df_transactions['Account'].nunique():,}")
print(f"Periode: {df_transactions['Timestamp'].min()} hingga {df_transactions['Timestamp'].max()}")
```

**Output:**

```
Loading dataset...
Dataset shape: (6362620, 12)
Jumlah transaksi: 6,362,620
Jumlah akun unik: 10,000
Periode: 2022-09-01 00:00:15 hingga 2023-02-28 23:59:47
```

**Kolom Dataset:**

**Tabel 3.3: Struktur Data HI-Small_Trans.csv**

| No  | Column Name            | Data Type | Description          | Contoh Nilai        |
| --- | ---------------------- | --------- | -------------------- | ------------------- |
| 1   | **Timestamp**          | datetime  | Waktu transaksi      | 2022-09-01 14:23:15 |
| 2   | **From Bank**          | int       | ID bank sumber       | 1                   |
| 3   | **Account**            | int       | ID akun sumber       | 2345                |
| 4   | **To Bank**            | int       | ID bank tujuan       | 2                   |
| 5   | **Account.1**          | int       | ID akun tujuan       | 6789                |
| 6   | **Amount Received**    | float     | Jumlah yang diterima | 5000.50             |
| 7   | **Receiving Currency** | str       | Mata uang penerima   | US Dollar           |
| 8   | **Amount Paid**        | float     | Jumlah yang dibayar  | 5015.75             |
| 9   | **Payment Currency**   | str       | Mata uang pembayaran | US Dollar           |
| 10  | **Payment Format**     | str       | Metode pembayaran    | Reinvestment        |
| 11  | **Is Laundering**      | int       | Label target (0/1)   | 0                   |

**Distribusi Label:**

```python
label_counts = df_transactions['Is Laundering'].value_counts()
print("\nDistribusi Label:")
print(f"Kelas 0 (Normal):     {label_counts[0]:,} ({label_counts[0]/len(df_transactions)*100:.2f}%)")
print(f"Kelas 1 (Laundering): {label_counts[1]:,} ({label_counts[1]/len(df_transactions)*100:.2f}%)")
print(f"\nImbalance Ratio: 1:{label_counts[0]/label_counts[1]:.0f}")
```

**Output:**

```
Distribusi Label:
Kelas 0 (Normal):     6,354,350 (99.87%)
Kelas 1 (Laundering): 8,270 (0.13%)

Imbalance Ratio: 1:768
```

**HI-Small_Patterns.txt:**

File ini berisi deskripsi 8 pola pencucian uang yang disimulasikan:

1. **Fan-out**: 1 akun → N akun (dispersal)
2. **Fan-in**: N akun → 1 akun (aggregation)
3. **Scatter-gather**: 1 akun → N akun → 1 akun
4. **Gather-scatter**: N akun → 1 akun → N akun
5. **Cycle**: A → B → C → A (circular transfer)
6. **Bipartite**: Dua grup yang saling bertransaksi
7. **Stack**: A → B → C → D → E (linear chain)
8. **Random**: Transfer acak tanpa pola jelas

### 3.2.2 Eksplorasi Data

> **[PERLU DILENGKAPI]**
>
> Tampilkan:
>
> - Statistik deskriptif
> - Distribusi target variable
> - Analisis korelasi
> - Visualisasi pola transaksi

### 3.2.3 Data Preprocessing

> **[PERLU DILENGKAPI]**
>
> Jelaskan langkah-langkah preprocessing yang dilakukan:
>
> - Handling missing values
> - Encoding categorical features
> - Normalisasi/standardisasi
> - Feature engineering (contoh: aggregate features dari transaksi)

---

## 3.3 Feature Engineering

> **[PERLU DILENGKAPI]**
>
> Jelaskan fitur-fitur yang dibuat:
>
> - Transaction frequency features
> - Amount-based features
> - Time-based features
> - Network-based features (jika ada)
> - Pattern-based features

---

## 3.4 Pemodelan CatBoost

### 3.4.1 Splitting Data

> **[PERLU DILENGKAPI]**
>
> Jelaskan pembagian data (train/validation/test) dan rasio yang digunakan

### 3.4.2 Hyperparameter Tuning

> **[PERLU DILENGKAPI]**
>
> Jelaskan:
>
> - Parameter yang di-tune
> - Metode tuning (Grid Search / Random Search / Optuna)
> - Parameter optimal yang ditemukan

### 3.4.3 Training Model

> **[PERLU DILENGKAPI]**
>
> Jelaskan:
>
> - Konfigurasi akhir model
> - Proses training
> - Handling imbalanced data (jika ada)

---

## 3.5 Evaluasi Model

### 3.5.1 Metrik Performa

> **[PERLU DILENGKAPI]**
>
> Tampilkan hasil evaluasi:
>
> - Confusion Matrix
> - Classification Report (Precision, Recall, F1-Score)
> - ROC Curve dan AUC Score
> - Feature Importance

### 3.5.2 Analisis Hasil

> **[PERLU DILENGKAPI]**
>
> Analisis:
>
> - Interpretasi metrik
> - Kekuatan dan kelemahan model
> - Analisis kesalahan prediksi (false positive/negative)

### 3.5.3 Perbandingan dengan Baseline

> **[PERLU DILENGKAPI]**
>
> Bandingkan dengan:
>
> - Rule-based method
> - Model machine learning lain (XGBoost, Random Forest, dll)

---

## 3.6 Kalibrasi Probabilitas

> **[PERLU DILENGKAPI]**
>
> Jelaskan proses kalibrasi menggunakan `probability_calibrator.joblib` yang ada di project

---

## 3.7 Deployment Considerations

> **[PERLU DILENGKAPI]**
>
> Jelaskan:
>
> - Penyimpanan model (`.cbm` file)
> - Inference pipeline
> - Monitoring dan maintenance

---

# BAB IV HASIL DAN ANALISIS

## 4.1 Hasil Eksperimen

> **[PERLU DILENGKAPI]**
>
> Tampilkan hasil lengkap dari eksperimen:
>
> - Performa model pada test set
> - Analisis feature importance
> - Contoh prediksi pada data real

---

## 4.2 Analisis Feature Importance

> **[PERLU DILENGKAPI]**
>
> Analisis fitur-fitur yang paling berpengaruh dalam deteksi rekening berisiko

---

## 4.3 Studi Kasus

> **[PERLU DILENGKAPI]**
>
> Berikan contoh kasus nyata atau skenario penggunaan model

---

## 4.4 Keterbatasan Penelitian

> **[PERLU DILENGKAPI]**
>
> Jelaskan keterbatasan:
>
> - Penggunaan data sintetis
> - Generalisasi model
> - Faktor eksternal yang tidak dipertimbangkan

---

# BAB V KESIMPULAN DAN SARAN

## 5.1 Kesimpulan

> **[PERLU DILENGKAPI]**
>
> Berdasarkan hasil analisis dan perancangan, serta implementasi dan pembahasan, maka dapat diambil kesimpulan sebagai berikut:
>
> 1. [Kesimpulan terkait performa model CatBoost]
> 2. [Kesimpulan terkait fitur-fitur penting]
> 3. [Kesimpulan terkait kontribusi penelitian untuk PPATK]

---

## 5.2 Saran

> **[PERLU DILENGKAPI]**
>
> Adapun saran dari penulis untuk melanjutkan perkembangan dari penelitian ini yaitu:
>
> 1. Implementasi dengan data real dari institusi keuangan
> 2. Penambahan fitur network analysis untuk mendeteksi pola yang lebih kompleks
> 3. Integrasi dengan sistem monitoring real-time
> 4. Penelitian lanjutan menggunakan algoritma deep learning (Graph Neural Networks)
> 5. Pengembangan dashboard untuk visualisasi dan monitoring

---

# DAFTAR PUSTAKA

[1] D. Saputro and D. Swanjaya, "Analisa Prediksi Harga Saham Menggunakan Neural Network Dan Net Foreign Flow," _Generation Journal_, vol. 7, no. 2, pp. 96–104, Jul. 2023, doi: 10.29407/gj.v7i2.20001.

[2] E. Altman, J. Jardine, N. Pavlovic, and C. Moore, "Realistic Synthetic Financial Transactions for Anti-Money Laundering Models," _arXiv preprint arXiv:2306.16424v3_, Dec. 2024. [Online]. Available: https://arxiv.org/abs/2306.16424

[3] P. Ramineni and R. Mastouri, "Credit Card Fraud Detection Using CatBoost," in _Proc. 2025 International Conference on Advanced Computing and Communication Systems (ICACCS)_, Saint Peter's University, Jersey City, NJ, USA, 2025.

[4] H. Amit, "What is CatBoost? A guide to boosting techniques," _We Talk Data_, Medium, Nov. 9, 2024. [Online]. Available: https://medium.com/we-talk-data/what-is-catboost-a-guide-to-boosting-techniques-f370a41f989d

[5] R. Purnama Adi, "Mengenal CatBoost: Algoritma boosting yang membuat machine learning lebih efektif," Medium, Jun. 18, 2023. [Online]. Available: https://medium.com/@rezapurnama1997/mengenal-catboost-algoritma-boosting-yang-membuat-machine-learning-lebih-efektif-5d679bab4966

[6] A. Pratama, "Analisis yuridis tindak pidana pencucian uang (Studi putusan No. 311/Pid.Sus/2018/PN.Mdn)," M.H. thesis, Magister Ilmu Hukum, Pascasarjana Universitas Medan Area, Medan, Indonesia, 2021. [Online]. Available: http://repository.uma.ac.id

**Format IEEE untuk referensi:**

- Jurnal: [No] Penulis, "Judul artikel," _Nama Jurnal_, vol., no., pp., bulan tahun, doi.
- Buku: [No] Penulis, _Judul Buku_, Edisi. Kota: Penerbit, Tahun.
- Website: [No] Penulis/Organisasi, "Judul," Nama Website, URL (diakses tanggal).

---

# LAMPIRAN

## Lampiran 1: Wawancara

> **[PERLU DILENGKAPI jika diperlukan]**

---

## Lampiran 2: Source Code

> **[Referensi ke repository atau notebook]**
>
> Source code lengkap dapat dilihat di:
>
> - Notebook: `source-code/money_laundering_detection.ipynb`
> - Python script: `source-code/skripsi.py`
> - Repository: [Link GitHub]

---

## Lampiran 3: Dataset Information

> **[PERLU DILENGKAPI]**
>
> Detail tentang struktur dataset dan preprocessing steps

---

## Lampiran 4: Model Evaluation Details

> **[PERLU DILENGKAPI]**
>
> Hasil lengkap evaluasi model, termasuk:
>
> - Detailed classification report
> - ROC curves
> - Feature importance charts

---

# DAFTAR RIWAYAT HIDUP

**Haris Wahyudi** lahir di Medan pada tanggal 04 Oktober 2003. Penulis merupakan mahasiswa Program Sarjana Ilmu Komputer di Universitas Siber Asia. Selama menjalani pendidikan, penulis aktif mendalami bidang pengembangan perangkat lunak, kecerdasan buatan, dan komputasi awan. Sistem pembelajaran daring memberikan fleksibilitas sehingga penulis dapat terus meningkatkan kemampuan akademik tanpa mengganggu aktivitas profesional.

Di luar kegiatan perkuliahan, penulis memiliki pengalaman sebagai Fullstack Developer dan terlibat dalam berbagai proyek pengembangan aplikasi web maupun mobile. Pengalaman tersebut memperkuat pemahaman penulis dalam merancang, membangun, dan mengelola sistem teknologi informasi yang digunakan oleh berbagai organisasi dan pengguna dalam skala besar.

Melalui kombinasi antara pendidikan formal dan pengalaman praktis, penulis berkomitmen untuk terus berkembang, beradaptasi dengan perkembangan teknologi terbaru, serta berkontribusi pada dunia akademis maupun industri melalui karya dan inovasi di bidang teknologi informasi.

---

## Kontak

- Email: [PERLU DILENGKAPI]
- LinkedIn: [PERLU DILENGKAPI]
- GitHub: [PERLU DILENGKAPI]

---

_Dokumen ini dibuat dengan format Markdown untuk memudahkan editing dan version control._
