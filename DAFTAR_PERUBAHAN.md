# DAFTAR PERUBAHAN — Panduan Migrasi ke ori.md

File ini berisi **semua perubahan substansial** yang perlu dipindahkan ke `ori.md`.
Perubahan hanya formatting (bold/italic syntax `__` → `**`, tab → spasi) **TIDAK** dicantumkan di sini.

---

## 1. Tabel 2.1 — Tambah Nomor Sitasi pada Nama Peneliti

**Lokasi di ori.md:** Baris 482–542 (di dalam Tabel 2.1 Penelitian Terdahulu)

| Baris ori.md | SEBELUM                        | SESUDAH                               |
| ------------ | ------------------------------ | ------------------------------------- |
| **482**      | `Syukur \(2024\)`              | `Syukur \(2024\) \[14\]`              |
| **494**      | `Hanjani \(2024\)`             | `Hanjani \(2024\) \[15\]`             |
| **518**      | `Ramineni & Mastouri \(2025\)` | `Ramineni & Mastouri \(2025\) \[16\]` |
| **530**      | `Pratama & Wahid \(2025\)`     | `Pratama & Wahid \(2025\) \[17\]`     |
| **542**      | `Florek & Zagdański \(2025\)`  | `Florek & Zagdański \(2025\) \[18\]`  |

---

## 2. Paragraf Setelah Tabel 2.1 — Tambah [20] dan Perbaikan Spasi

**Lokasi di ori.md:** Baris 552

**SEBELUM:**

```
Berdasarkan tinjauan terhadap literatur sebelumnya, penelitian ini  mengadaptasi metodologi deteksi transaksi mencurigakan yang mengombinasikan algoritma *CatBoost* dengan teknik *feature engineering* berbasis pola transaksi\. Metode ini dipilih karena kemampuannya dalam menangani klasifikasi transaksi pada data keuangan yang memiliki fitur *kategorikal* dominan dan ketidakseimbangan kelas ekstrem, sebagaimana telah dibuktikan efektivitasnya dalam berbagai penelitian terdahulu\.
```

**SESUDAH** (2 perubahan: hapus spasi ganda + tambah `\[20\]` di akhir):

```
Berdasarkan tinjauan terhadap literatur sebelumnya, penelitian ini mengadaptasi metodologi deteksi transaksi mencurigakan yang mengombinasikan algoritma *CatBoost* dengan teknik *feature engineering* berbasis pola transaksi\. Metode ini dipilih karena kemampuannya dalam menangani klasifikasi transaksi pada data keuangan yang memiliki fitur *kategorikal* dominan dan ketidakseimbangan kelas ekstrem, sebagaimana telah dibuktikan efektivitasnya dalam berbagai penelitian terdahulu \[20\]\.
```

**Detail perubahan:**

1. `penelitian ini  mengadaptasi` → `penelitian ini mengadaptasi` (hapus 1 spasi berlebih)
2. `penelitian terdahulu\.` → `penelitian terdahulu \[20\]\.` (tambah sitasi [20] di akhir kalimat)

---

## 3. Bagian 2.3.3 — Rewrite Seluruh Deskripsi 8 Pola Transaksi

**Lokasi di ori.md:** Baris 584–625

### 3a. Paragraf pembuka (Baris 586)

**SEBELUM:**

```
*Dataset IBM AML Transactions *memodelkan delapan pola pencucian uang yang umum digunakan oleh pelaku untuk menyamarkan asal\-usul dana \[12\]\. Kedelapan pola tersebut diilustrasikan sebagai berikut:
```

**SESUDAH** (tambah 1 kalimat di tengah):

```
*Dataset IBM AML Transactions *memodelkan delapan pola pencucian uang yang umum digunakan oleh pelaku untuk menyamarkan asal\-usul dana \[12\]\. Pola\-pola tersebut merepresentasikan berbagai skema aliran dana ilegal yang telah diidentifikasi dalam literatur deteksi pencucian uang\. Kedelapan pola tersebut diilustrasikan sebagai berikut:
```

### 3b. Fan-out (Baris 594)

**SEBELUM:**

```
Satu rekening pengirim \(v\) mengirimkan dana ke rekening lain  yang berbeda\. Pola ini merepresentasikan tahap penyebaran dana \(*layering*\) untuk mengaburkan sumber dana\.
```

**SESUDAH:**

```
Satu rekening pengirim \(v\) mengirimkan dana ke banyak rekening lain yang berbeda\. Dumitrescu et al\. mengidentifikasi pola ini sebagai *volcano node*, yaitu simpul dengan lalu\-lintas keluar yang sangat tinggi dalam graf transaksi perbankan, yang mengindikasikan tahap penyebaran dana \(*layering*\) untuk mengaburkan sumber dana \[21\]\.
```

**Detail:** `rekening lain  yang` → `banyak rekening lain yang` (hapus spasi ganda, tambah "banyak"). Tambah penjelasan Dumitrescu "volcano node" + sitasi [21].

### 3c. Fan-in (Baris 598)

**SEBELUM:**

```
Banyak rekening pengirim mengirimkan dana ke satu rekening penerima \(v\)\. Pola ini merepresentasikan tahap pengumpulan dana \(*integration*\) di mana dana dari berbagai sumber dikumpulkan kembali\.
```

**SESUDAH:**

```
Banyak rekening pengirim mengirimkan dana ke satu rekening penerima \(v\)\. Pola ini dikenal sebagai *blackhole node* dalam analisis graf, yaitu simpul dengan lalu\-lintas masuk yang dominan, yang merepresentasikan tahap pengumpulan dana \(*integration*\) di mana dana dari berbagai sumber dikumpulkan kembali ke satu titik \[21\]\.
```

**Detail:** Tambah "blackhole node" + sitasi [21].

### 3d. Gather-Scatter (Baris 602)

**SEBELUM:**

```
Kombinasi *fan\-in* dan *fan\-out* pada satu rekening yang sama \(v\)\. Rekening v menerima dana dari banyak sumber kemudian menyebarkannya ke banyak tujuan, berfungsi sebagai titik transit pencucian uang\.
```

**SESUDAH:**

```
Kombinasi *fan\-in* dan *fan\-out* pada satu rekening yang sama \(v\)\. Rekening v menerima dana dari banyak sumber kemudian menyebarkannya ke banyak tujuan, berfungsi sebagai titik transit pencucian uang\. Song et al\. menunjukkan bahwa skema pencucian uang sering kali melibatkan subgraf yang menghubungkan entitas ilegal ke entitas legal melalui serangkaian lapisan transaksi, di mana rekening perantara berperan sebagai titik agregasi dan distribusi dana \[23\]\.
```

**Detail:** Tambah kalimat Song et al. + sitasi [23] di akhir.

### 3e. Scatter-Gather (Baris 606)

**SEBELUM:**

```
Satu rekening pengirim \(v\) menyebarkan dana ke beberapa rekening perantara, yang kemudian mengalirkan dana tersebut ke satu rekening penerima \(u\)\. Pola ini melibatkan rekening perantara yang sama pada sisi penyebaran dan pengumpulan\.
```

**SESUDAH:**

```
Satu rekening pengirim \(v\) menyebarkan dana ke beberapa rekening perantara, yang kemudian mengalirkan dana tersebut ke satu rekening penerima \(u\)\. Pola ini mencerminkan skema *peeling chain* yang diidentifikasi oleh Song et al\., yaitu jalur berlapis di mana dana mengalir dari sumber ilegal menuju tujuan legal melalui serangkaian lapisan transaksi yang dirancang untuk menyamarkan jejak \[23\]\.
```

**Detail:** Ganti kalimat kedua dengan penjelasan "peeling chain" + sitasi [23].

### 3f. Simple Cycle (Baris 610)

**SEBELUM:**

```
Rangkaian transaksi yang membentuk siklus tertutup — dana yang dikirim dari satu rekening akhirnya kembali ke rekening asal melalui serangkaian rekening perantara\. Keberadaan siklus merupakan indikator kuat pencucian uang karena pelaku berusaha "membersihkan" dana melalui aliran berputar\.
```

**SESUDAH:**

```
Rangkaian transaksi yang membentuk siklus tertutup — dana yang dikirim dari satu rekening akhirnya kembali ke rekening asal melalui serangkaian rekening perantara\. Irwin et al\. dalam analisis terhadap 184 tipologi pencucian uang menemukan bahwa teknik pemindahan dana secara berputar merupakan salah satu metode *layering* yang paling sering digunakan untuk menyamarkan jejak audit \[24\]\. Keberadaan siklus merupakan indikator kuat pencucian uang\.
```

**Detail:** Tambah kalimat Irwin et al. + sitasi [24] di tengah, kalimat terakhir dipersingkat.

### 3g. Random (Baris 614)

**SEBELUM:**

```
Serupa dengan *cycle* tetapi dana tidak kembali ke rekening asal\. Pola ini merepresentasikan perpindahan dana acak antar rekening yang dimiliki atau dikendalikan oleh pelaku, termasuk melalui perusahaan cangkang \(*shell companies*\)\.
```

**SESUDAH:**

```
Serupa dengan *cycle* tetapi dana tidak kembali ke rekening asal\. Pola ini merepresentasikan perpindahan dana acak antar rekening yang dimiliki atau dikendalikan oleh pelaku, termasuk melalui perusahaan cangkang \(*shell companies*\)\. Irwin et al\. mencatat bahwa pelaku pencucian uang cenderung menggunakan kombinasi teknik yang beragam dan tampak acak pada fase *placement* maupun *layering* untuk mempertahankan tingkat anonimitas yang tinggi \[24\]\.
```

**Detail:** Tambah kalimat Irwin et al. + sitasi [24] di akhir.

### 3h. Bipartite (Baris 618)

**SEBELUM:**

```
Dana dipindahkan dari sekumpulan rekening *input* ke sekumpulan rekening *output* melalui transaksi yang menghubungkan kedua kelompok tersebut\. Pola ini menyerupai struktur *layering* berlapis\.
```

**SESUDAH:**

```
Dana dipindahkan dari sekumpulan rekening *input* ke sekumpulan rekening *output* melalui transaksi yang menghubungkan kedua kelompok tersebut\. Cardoso et al\. merepresentasikan jaringan interaksi keuangan sebagai graf bipartit antara nasabah dan transaksi untuk mendeteksi pergerakan anomali, menunjukkan bahwa struktur bipartit efektif dalam mengungkap pola *layering* berlapis pada transaksi perbankan \[22\]\.
```

**Detail:** Ganti kalimat kedua dengan penjelasan Cardoso et al. + sitasi [22].

### 3i. Stack (Baris 622)

**SEBELUM:**

```
Perluasan dari pola *bipartite* dengan menambahkan lapisan perantara tambahan, sehingga membentuk struktur berlapis\-lapis yang lebih kompleks dan sulit ditelusuri\.
```

**SESUDAH:**

```
Perluasan dari pola *bipartite* dengan menambahkan lapisan perantara tambahan, sehingga membentuk struktur berlapis\-lapis yang lebih kompleks dan sulit ditelusuri\. Cardoso et al\. mendemonstrasikan bahwa navigasi melalui jaringan interaksi keuangan yang berlapis\-lapis merupakan tantangan utama dalam proses *review* AML, karena aliran dana seringkali melewati entitas yang tidak terhubung langsung dengan subjek investigasi \[22\]\.
```

**Detail:** Tambah kalimat Cardoso et al. + sitasi [22] di akhir.

---

## 4. Bagian 2.3.4 CatBoost — Ubah Nomor Sitasi

**Lokasi di ori.md:** Baris 630

**SEBELUM:**

```
...di antaranya Yang et al\. yang menunjukkan keunggulan CatBoost dengan AUC 0\.767 dibandingkan enam algoritma lainnya \[8\], serta Kadir yang melaporkan akurasi CatBoost sebesar 96\.28% dibandingkan Random Forest 94\.88% \[9\]\.
```

**SESUDAH:**

```
...di antaranya Yang et al\. yang menunjukkan keunggulan CatBoost dengan AUC 0\.767 dibandingkan enam algoritma lainnya \[10\], serta Kadir yang melaporkan akurasi CatBoost sebesar 96\.28% dibandingkan Random Forest 94\.88% \[11\]\.
```

**Detail:**

- `\[8\]` → `\[10\]` (karena [8] sekarang Chapman, Yang pindah ke [10])
- `\[9\]` → `\[11\]` (karena [9] sekarang Mariscal, Kadir pindah ke [11])

---

## 5. BAB IV §4.1.3 — Tambah Sitasi [19] Setelah Egressy

**Lokasi di ori.md:** Baris 1439

**SEBELUM:**

```
1. Arsitektur Multi\-GNN \(GIN\) yang dilaporkan oleh Egressy et al\. \(2024\),
```

**SESUDAH:**

```
1. Arsitektur Multi\-GNN \(GIN\) yang dilaporkan oleh Egressy et al\. \(2024\) \[19\],
```

**Detail:** Tambah `\[19\]` sebelum koma. (Juga hapus spasi sebelum koma)

---

## 6. BAB IV §4.2 — Tambah Sitasi [18] Setelah Florek

**Lokasi di ori.md:** Baris 1502

**SEBELUM:**

```
...sejalan dengan temuan Florek & Zagdański \(2025\) bahwa gradient boosting sering kompetitif dengan deep learning pada data tabular\.
```

**SESUDAH:**

```
...sejalan dengan temuan Florek & Zagdański \(2025\) \[18\] bahwa gradient boosting sering kompetitif dengan deep learning pada data tabular\.
```

**Detail:** Tambah `\[18\]` setelah `\(2025\)`.

---

## 7. DAFTAR PUSTAKA — Tambah Entri [8]–[24]

**Lokasi di ori.md:** Baris 1541–1558

Saat ini DAFTAR PUSTAKA di ori.md hanya punya [1]–[7] dan [12]. Perlu ditambahkan [8]–[13] serta [14]–[24].

### Langkah-langkah:

**a.** Ubah entri [12] yang sudah ada (baris 1557) menjadi lebih detail:

**SEBELUM:**

```
 \[12\] E\. Altman et al\., "Realistic Synthetic Financial Transactions for Anti\-Money Laundering Models," 2023\.
```

**SESUDAH:**

```
\[12\] E\. Altman et al\., "Realistic Synthetic Financial Transactions for Anti\-Money Laundering Models," NeurIPS Datasets and Benchmarks Track, 2023\.
```

(Tambah "NeurIPS Datasets and Benchmarks Track" dan hapus spasi di awal baris)

**b.** Tambahkan entri-entri baru berikut **SETELAH** [7] dan **SEBELUM** [12]:

```
\[8\] P\. Chapman et al\., "CRISP\-DM 1\.0: Step\-by\-step data mining guide," SPSS Inc\., 2000\.

\[9\] G\. Mariscal, Ó\. Marbán, and C\. Fernández, "A survey of data mining and knowledge discovery process models and methodologies," The Knowledge Engineering Review, vol\. 25, no\. 2, pp\. 137–166, 2010\. DOI: 10\.1017/S0269888910000032\.

\[10\] M\. Yang et al\., "An Explainable Machine Learning Model in Predicting Vaginal Birth After Cesarean Section," Research Square \(Preprint\), 2024\. DOI: 10\.21203/rs\.3\.rs\-5395796/v1\.

\[11\] A\. Kadir, "Analisis Performa Metode Random Forest dan CatBoost dalam Pemodelan Kualitas Udara Kota Palembang," 2024\.
```

**c.** Tambahkan [13] **SETELAH** [12]:

```
\[13\] CatBoost Developers, "CatBoost Documentation: Training Parameters," catboost\.ai\. \[Online\]\. Available: https://catboost\.ai/en/docs/concepts/python\-reference\_catboostclassifier \(diakses 5 Feb\. 2026\)\.
```

**d.** Tambahkan [14]–[24] **SETELAH** [13]:

```
\[14\] M\. A\. A\. Syukur, Suhartono, and T\. Chamidy, "Prediksi Kualitas Udara Menggunakan Metode CatBoost," JISKA \(Jurnal Informatika Sunan Kalijaga\), vol\. 10, no\. 2, pp\. 249–258, 2025\. DOI: 10\.14421/jiska\.2025\.10\.2\.249\-258\.

\[15\] N\. S\. Hanjani, "Prediksi Kadar Polutan Indikator Kualitas Udara di Pekanbaru Menggunakan CatBoost," 2024\.

\[16\] V\. Ramineni and T\. Mastouri, "Credit Card Fraud Detection Using CatBoost," 2025\.

\[17\] S\. F\. Pratama, "Fraudulent Transaction Detection in Online Systems Using Random Forest and Gradient Boosting," Journal of Cyber Law, vol\. 1, no\. 1, 2025\. DOI: 10\.63913/jcl\.v1i1\.5\.

\[18\] P\. Florek and A\. Zagdański, "Benchmarking State\-of\-the\-Art Gradient Boosting Algorithms for Classification," arXiv preprint arXiv:2305\.17094, 2023\.

\[19\] B\. Egressy et al\., "Provably Powerful Graph Neural Networks for Directed Multigraphs," in Proc\. AAAI Conference on Artificial Intelligence, 2024\. arXiv:2306\.11586\.

\[20\] R\. I\. T\. Jensen and A\. Iosifidis, "Fighting Money Laundering With Statistics and Machine Learning," IEEE Access, vol\. 11, pp\. 8889–8903, 2023\. DOI: 10\.1109/access\.2023\.3239549\.

\[21\] B\. Dumitrescu, A\. Bălțoiu, and Ș\. Budulan, "Anomaly Detection in Graphs of Bank Transactions for Anti Money Laundering Applications," IEEE Access, vol\. 10, pp\. 47699–47714, 2022\. DOI: 10\.1109/access\.2022\.3170467\.

\[22\] M\. Cardoso, P\. Saleiro, and P\. Bizarro, "LaundroGraph: Self\-Supervised Graph Representation Learning for Anti\-Money Laundering," in Proc\. 3rd ACM International Conference on AI in Finance \(ICAIF "22\), pp\. 130–138, 2022\. DOI: 10\.1145/3533271\.3561727\.

\[23\] K\. Song, M\. A\. Dhraief, and M\. Xu, "Identifying Money Laundering Subgraphs on the Blockchain," in Proc\. 5th ACM International Conference on AI in Finance \(ICAIF "24\), pp\. 195–203, 2024\. DOI: 10\.1145/3677052\.3698635\.

\[24\] A\. S\. M\. Irwin, K\-K\. R\. Choo, and L\. Liu, "An analysis of money laundering and terrorism financing typologies," Journal of Money Laundering Control, vol\. 15, no\. 1, pp\. 85–111, 2011\. DOI: 10\.1108/13685201211194745\.
```

---

## RINGKASAN PERUBAHAN

| #   | Lokasi (baris ori.md)   | Jenis Perubahan     | Deskripsi Singkat                                                    |
| --- | ----------------------- | ------------------- | -------------------------------------------------------------------- |
| 1   | 482, 494, 518, 530, 542 | Tambah sitasi       | [14]–[18] setelah nama peneliti di Tabel 2.1                         |
| 2   | 552                     | Tambah sitasi + fix | [20] di akhir paragraf + hapus spasi ganda                           |
| 3   | 586–622                 | Rewrite konten      | Seluruh deskripsi 8 pola transaksi diperkaya dengan sitasi [21]–[24] |
| 4   | 630                     | Ubah nomor sitasi   | [8]→[10], [9]→[11] di paragraf CatBoost                              |
| 5   | 1439                    | Tambah sitasi       | [19] setelah Egressy et al.                                          |
| 6   | 1502                    | Tambah sitasi       | [18] setelah Florek & Zagdański                                      |
| 7   | 1541–1558               | Tambah pustaka      | Entri [8]–[13] dan [14]–[24] di DAFTAR PUSTAKA                       |
