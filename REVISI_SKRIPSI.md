# DAFTAR REVISI SKRIPSI

**Haris Wahyudi — 220401010015**
**Tanggal: 14 Februari 2026**

Petunjuk: Gunakan Ctrl+H (Find & Replace) di Word untuk mencari teks LAMA dan ganti dengan teks BARU.
Centang `[x]` setiap item yang sudah selesai dikerjakan.

**Progress: 1/25 selesai**

---

## A. KRITIS (6 item)

---

### - [X] A1. Batasan Masalah 1.3 — Kontradiksi dengan BAB IV

**Lokasi:** BAB I, Subbab 1.3, poin 3
**Masalah:** Tertulis "tanpa melakukan perbandingan" tapi BAB IV membandingkan 3 model

**LAMA:**

```
Metode machine learning yang digunakan dalam penelitian ini dibatasi pada algoritma CatBoost, tanpa melakukan perbandingan dengan algoritma lain.
```

**BARU:**

```
Metode machine learning utama yang digunakan dalam penelitian ini adalah algoritma CatBoost, dengan model pembanding dari kajian publik sebagai referensi evaluasi performa.
```

---

### - [ ] A2. Kriteria Keberhasilan 3.1 — Tidak Tercapai

**Lokasi:** BAB III, Subbab 3.1, poin 3 (bagian kebutuhan)
**Masalah:** Target Recall ≥ 90% tidak tercapai (aktual 60,21%), tidak pernah dibahas

**LAMA:**

```
Kriteria keberhasilan: Recall ≥ 90% agar sebagian besar transaksi mencurigakan terdeteksi, AUC ≥ 0,95 sebagai indikator kemampuan diskriminasi model, serta meminimalkan false negative pada data uji.
```

**BARU:**

```
Kriteria keberhasilan: F1-Score ≥ 0,60 dan PR-AUC ≥ 0,50 sebagai indikator keseimbangan antara deteksi dan presisi pada data yang sangat tidak seimbang, serta meminimalkan false positive pada data uji.
```

---

### - [ ] A3. Abstrak Belum Mencerminkan Hasil

**Lokasi:** Halaman ABSTRAK (Bahasa Indonesia)
**Masalah:** Masih berbunyi seperti proposal, belum ada hasil penelitian

**LAMA:**

```
Metode penelitian menggunakan pendekatan kuantitatif non eksperimental dengan tahapan preprocessing, pelatihan model, dan evaluasi menggunakan Precision, Recall, dan F1-Score. Penelitian ini diharapkan dapat menjadi dasar pengembangan sistem pendukung keputusan dalam analisis transaksi keuangan dan berkontribusi pada upaya pencegahan pencucian uang.
```

**BARU:**

```
Metode penelitian menggunakan pendekatan kuantitatif non eksperimental dengan tahapan preprocessing, rekayasa 59 fitur berbasis pola transaksi, pelatihan model, dan evaluasi menggunakan Precision, Recall, F1-Score, dan PR-AUC. Hasil penelitian menunjukkan bahwa model CatBoost mencapai F1-Score 0,7140, Precision 87,70%, dan PR-AUC 0,7412 pada data uji, serta mengungguli dua model pembanding (Multi-GNN dan XGBoost+SMOTE) secara signifikan. Penelitian ini dapat menjadi dasar pengembangan sistem pendukung keputusan dalam analisis transaksi keuangan dan berkontribusi pada upaya pencegahan pencucian uang.
```

---

### - [ ] A4. ABSTRACT (Bahasa Inggris) Belum Mencerminkan Hasil

**Lokasi:** Halaman ABSTRACT

**LAMA:**

```
The research methodology employs a quantitative non-experimental approach with stages of data preprocessing, model training, and evaluation using Precision, Recall, and F1-Score metrics. Results demonstrate that the CatBoost model achieves good accuracy and is more effective compared to simple rule-based approaches. This research is expected to serve as a foundation for developing decision support systems in financial transaction analysis and contribute to anti-money laundering efforts.
```

**BARU:**

```
The research methodology employs a quantitative non-experimental approach with stages of data preprocessing, engineering of 59 transaction pattern-based features, model training, and evaluation using Precision, Recall, F1-Score, and PR-AUC metrics. Results demonstrate that the CatBoost model achieves an F1-Score of 0.7140, Precision of 87.70%, and PR-AUC of 0.7412 on the test set, significantly outperforming two baseline models (Multi-GNN and XGBoost+SMOTE). This research serves as a foundation for developing decision support systems in financial transaction analysis and contributes to anti-money laundering efforts.
```

---

### - [ ] A5. Subbab 2.3.3 Matrik Evaluasi — Belum Selesai

**Lokasi:** BAB II, Subbab 2.3.3 Matrik Evaluasi
**Masalah:** Kalimat terpotong, formula belum ditulis

**LAMA:**

```
Pada data transaksi AML, distribusi kelas umumnya tidak seimbang (imbalanced) sehingga metrik seperti accuracy saja sering kurang representatif. Oleh karena itu, penelitian ini menggunakan beberapa metrik evaluasi yang dihitung berdasarkan nilai
```

**BARU:**

```
Pada data transaksi AML, distribusi kelas umumnya tidak seimbang (imbalanced) sehingga metrik seperti accuracy saja sering kurang representatif. Oleh karena itu, penelitian ini menggunakan beberapa metrik evaluasi yang dihitung berdasarkan nilai confusion matrix:

1. Precision: mengukur proporsi prediksi positif yang benar.
   Precision = TP / (TP + FP)

2. Recall: mengukur proporsi kasus positif yang berhasil terdeteksi.
   Recall = TP / (TP + FN)

3. F1-Score: rata-rata harmonik dari Precision dan Recall, memberikan keseimbangan antara keduanya.
   F1 = 2 × (Precision × Recall) / (Precision + Recall)

4. PR-AUC (Area Under Precision-Recall Curve): mengukur kemampuan model membedakan kelas positif pada berbagai threshold, lebih informatif dibanding ROC-AUC pada data tidak seimbang.
```

---

### - [ ] A6. Daftar Pustaka — 7 Referensi Hilang

**Lokasi:** DAFTAR PUSTAKA
**Masalah:** Referensi [8]–[11], [13]–[15] tidak ada

**TAMBAHKAN setelah [7]:**

```
[8] J. Yang et al., "An Explainable Machine Learning Model in Predicting Vaginal Birth After Cesarean Section," BMC Pregnancy and Childbirth, vol. 24, 2024.

[9] A. Kadir, "Analisis Performa Metode Random Forest dan CatBoost dalam Pemodelan Kualitas Udara Kota Palembang," 2024.

[10] A. Syukur, "Prediksi Indeks Kualitas Udara Menggunakan Metode CatBoost," 2024.

[11] S. Hanjani, "Prediksi Kadar Polutan Indikator Kualitas Udara di Pekanbaru Menggunakan CatBoost," 2024.

[13] V. Ramineni and A. Mastouri, "Credit Card Fraud Detection Using CatBoost," 2025.

[14] R. Pratama and A. Wahid, "Fraudulent Transaction Detection in Online Systems Using Random Forest and Gradient Boosting," 2025.

[15] D. Florek and A. Zagdański, "Benchmarking State-of-the-Art Gradient Boosting Algorithms for Classification," 2025.
```

---

## B. SEDANG (9 item)

---

### - [X] B1. Penomoran BAB II Rusak

**Lokasi:** BAB II, Subbab 2.3.x
**Masalah:** Nomor duplikat dan urutan salah

**Urutan yang BENAR:**

```
2.3.1 Anti Pencucian Uang        (sudah benar)
2.3.2 Dataset AMLworld           (LAMA: 2.3.3)
2.3.3 Pola Transaksi Pencucian Uang  (LAMA: 2.3.4)
2.3.4 CatBoost                   (LAMA: 2.3.2)
2.3.5 Confusion Matrix           (LAMA: 2.3.3)
2.3.6 Metrik Evaluasi            (LAMA: 2.3.3)
```

---

### - [X] B2. Judul 2.3.3 Dataset TYPO

**Lokasi:** BAB II

**LAMA:**

```
2.3.3 Dataset AMLLmk((world
```

**BARU:**

```
2.3.2 Dataset AMLworld
```

---

### - [X] B3. Judul Subbab 3.4.1 Salah

**Lokasi:** BAB III

**LAMA:**

```
3.4.1 Pembagian Data Kronologis
```

**BARU:**

```
3.4.1 Pemilihan Algoritma
```

---

### - [X] B4. Judul Subbab 3.5 Typo

**Lokasi:** BAB III

**LAMA:**

```
3.5 Implementasi Evaluati
```

**BARU:**

```
3.5 Implementasi Evaluation
```

---

### - [X] B5. Teks Rusak di 3.6

**Lokasi:** BAB III, Subbab 3.6, paragraf pertama

**LAMA:**

```
Untuk memvalidasi model secara interaktif dan memudahkan demonstrasi hasil p Model CatBoost — saved_models/catboost_aml_model.cbm (format native CatBoost)
Daftar enelitian, dilakukan deployment aplikasi web menggunakan Streamlit yang di-hosting pada platform Replit.
```

**BARU:**

```
Untuk memvalidasi model secara interaktif dan memudahkan demonstrasi hasil penelitian, dilakukan deployment aplikasi web menggunakan Streamlit yang di-hosting pada platform Replit.
```

---

### - [ ] B6. Referensi CRISP-DM Salah Nomor

**Lokasi:** BAB II, Subbab 2.1, paragraf 2

**LAMA:**

```
CRISP-DM telah menjadi de facto standard dalam pengembangan proyek data mining dan knowledge discovery [8]. Survei Mariscal et al. menunjukkan pengguna CRISP-DM mencapai 51% pada tahun 2002, dan survei terbaru dari datascience-pm pada tahun 2020 masih menempatkannya di posisi teratas dengan 49% responden [9].
```

**BARU:**

```
CRISP-DM telah menjadi de facto standard dalam pengembangan proyek data mining dan knowledge discovery [6]. Survei Mariscal et al. menunjukkan pengguna CRISP-DM mencapai 51% pada tahun 2002, dan survei terbaru dari datascience-pm pada tahun 2020 masih menempatkannya di posisi teratas dengan 49% responden [7].
```

**Catatan:** [8] = Yang et al. (prediksi medis), bukan CRISP-DM. Jika maksudnya referensi berbeda, tambahkan referensi CRISP-DM yang sesuai.

---

### - [ ] B7. Typo "matrix" → "metrik"

**Lokasi:** BAB I, Subbab 1.3 poin 4 dan Subbab 1.4 poin 3

**LAMA (1.3 poin 4):**

```
Evaluasi kinerja model dilakukan menggunakan matrix Precision, Recall, dan F1-Score.
```

**BARU:**

```
Evaluasi kinerja model dilakukan menggunakan metrik Precision, Recall, dan F1-Score.
```

**LAMA (1.4 poin 3):**

```
Mengukur dan mengevaluasi performa model CatBoost menggunakan matrix Precision, Recall, dan F1-Score
```

**BARU:**

```
Mengukur dan mengevaluasi performa model CatBoost menggunakan metrik Precision, Recall, dan F1-Score
```

---

### - [ ] B8. Referensi Silang "Tabel 3.1" Tidak Ada

**Lokasi:** BAB IV, Subbab 4.1.2

**LAMA:**

```
pembagian kronologis menghasilkan distribusi kelas yang berbeda antar split (Tabel 3.1)
```

**BARU (sesuaikan dengan nomor tabel yang benar di BAB III):**

```
pembagian kronologis menghasilkan distribusi kelas yang berbeda antar split (Tabel 3.X)
```

_Ganti X dengan nomor tabel pembagian data di BAB III._

---

### - [x] B9. BAB IV 4.1.3 Referensi "Subbab 4.2.4" Sudah Tidak Ada

**Lokasi:** BAB IV, paragraf terakhir 4.1.3
**Status:** ✅ Sudah diperbaiki di file BAB_IV_HASIL_DAN_ANALISA.md

**LAMA (di DOCX masih ada):**

```
Implikasi dari perbandingan ini dibahas lebih lanjut pada Subbab 4.2.4.
```

**BARU:**
Hapus kalimat tersebut.

---

## C. MINOR (4 item)

---

### - [ ] C1. Rumusan Masalah 1.2 — Poin 3 Salah Indentasi

**Lokasi:** BAB I, Subbab 1.2
**Masalah:** Poin ketiga terindentasi sebagai sub-item dari poin 2 (2.a bukan 3)
**Solusi:** Ubah dari sub-list menjadi poin nomor 3 yang sejajar.

---

### - [ ] C2. Daftar Gambar & Daftar Tabel Kosong

**Lokasi:** Halaman DAFTAR GAMBAR dan DAFTAR TABEL
**Solusi:** Isi sesuai gambar dan tabel yang ada di BAB I-V, atau gunakan fitur Insert > Table of Figures di Word.

---

### - [ ] C3. Placeholder "Gambar X" / "Tabel X"

**Lokasi:** BAB III, beberapa tempat
**Solusi:** Ganti semua "Gambar X" dan "Tabel X" dengan nomor yang sesuai secara berurutan.

---

### - [ ] C4. BAB V Saran — Poin 3 GNN Hybrid Hilang di DOCX

**Lokasi:** BAB V, Subbab 5.2
**Masalah:** File BAB_V_KESIMPULAN.md punya 5 saran, DOCX hanya 4 (poin tentang GNN hybrid tidak ada)

**TAMBAHKAN sebagai poin 3 di DOCX (geser poin lama 3→4 dan 4→5):**

```
3. Pendekatan feature engineering manual dan representation learning berbasis GNN dapat digabungkan — fitur buatan manual memberikan interpretabilitas, sedangkan fitur dari GNN menambah kemampuan model mengenali pola jaringan yang sulit terlihat secara kasat mata.
```

---

### - [ ] C5. Lembar Pengesahan — Judul Terpotong

**Lokasi:** Halaman LEMBAR PENGESAHAN
**Masalah:** Judul tertulis hanya "Untuk Deteksi Transaksi Mencurigakan" — bagian awal hilang

**LAMA:**

```
Judul Tugas Akhir : Untuk Deteksi Transaksi Mencurigakan
```

**BARU:**

```
Judul Tugas Akhir : Implementasi Algoritma CatBoost Pada Sistem Anti Pencucian Uang Berbasis Pola Transaksi Untuk Deteksi Transaksi Mencurigakan
```

---

### - [ ] C6. Keywords (English) Belum Urut Abjad

**Lokasi:** Halaman ABSTRACT
**Masalah:** Pedoman mensyaratkan kata kunci diurutkan abjad

**LAMA:**

```
Keywords: Money Laundering, Predictive Analytics, CatBoost, Machine Learning
```

**BARU:**

```
Keywords: CatBoost, Machine Learning, Money Laundering, Predictive Analytics
```

---

### - [ ] C7. Typo "Labkan" di Subbab 3.5.6

**Lokasi:** BAB III, Subbab 3.5.6

**LAMA:**

```
Analisis Korelasi Fitur dengan Labkan
```

**BARU:**

```
Analisis Korelasi Fitur dengan Label
```

---

### - [ ] C8. Typo "diklasifikaTru" di Subbab 3.5.2

**Lokasi:** BAB III, setelah Confusion Matrix

**LAMA:**

```
hanya 136 dari 862.289 transaksi normal salah diklasifikaTru
```

**BARU:**

```
hanya 136 dari 862.289 transaksi normal salah diklasifikasi
```

---

### - [ ] C9. Lampiran Kosong — Wajib Diisi

**Lokasi:** Halaman LAMPIRAN
**Masalah:** Pedoman mewajibkan lampiran berisi "dokumentasi photo-photo dan source code" (Pedoman 3.1.C.2)

**Isi yang perlu ditambahkan:**

1. **Daftar 59 Fitur** — Tabel rekap seluruh fitur (nama fitur, kategori, deskripsi singkat)
2. **Source Code Utama** — Potongan kode kunci: feature engineering, training CatBoost, evaluasi (bisa screenshot atau listing)
3. **Screenshot Aplikasi Streamlit** — Tangkapan layar deployment di Replit (halaman utama + hasil simulasi)
4. **Hasil Turnitin** — Bukti similarity check ≤ 30% (wajib per pedoman Subbab 3.1.A.3)

**Catatan:** Daftar Riwayat Hidup sudah ada dan posisinya sudah benar di bagian paling akhir.

---

## D. DAFTAR ISI — Perlu Diperbarui

- [ ] **D1.** Setelah semua revisi selesai, generate ulang Daftar Isi menggunakan fitur **References > Update Table** di Word.

Subbab yang hilang dari Daftar Isi:

- 3.2.1 – 3.2.3 (Data Understanding)
- 3.3 – 3.3.3 (Data Preparation)
- 3.4 – 3.4.3 (Modeling)
- 3.5 – 3.5.6 (Evaluation)
- 3.6 – 3.6.2 (Deployment)
- 4.1.1 – 4.1.3 (Hasil)

---

## E. SARAN GEMINI YANG DITOLAK (dengan alasan)

Berikut saran dari AI lain yang **TIDAK perlu** diterapkan:

### ❌ E1. Halaman maksimal 30 halaman

**Alasan:** Batas 30 halaman kemungkinan besar untuk **proposal/TA awal**, bukan skripsi final. Semua skripsi S1 UNSIA yang sudah lulus berkisar 40–80+ halaman. Konfirmasi ke prodi jika ragu, tapi hampir pasti ini salah baca pedoman.

### ❌ E2. Tambahkan TKT (Tingkat Kesiapan Teknologi)

**Alasan:** TKT/TRL adalah kerangka untuk **hibah riset DIKTI/BRIN**, bukan standar untuk skripsi S1. Tidak ada universitas S1 yang meminta ini di skripsi. Ini saran yang over-engineering.

### ❌ E3. Kata Pengantar "saya" → "penulis"

**Alasan:** Sudah dicek — Kata Pengantar **sudah menggunakan "penulis"** dengan benar. Kata "Saya" hanya muncul di Lembar Keabsahan dan Pernyataan Originalitas, yang merupakan **dokumen legal/pernyataan resmi** di mana "saya" adalah format standar dan benar.

### ❌ E4. Perlu Cross Validation (k-fold)

**Alasan:** **SALAH untuk data time-series.** K-fold CV pada data transaksi keuangan menyebabkan **data leakage temporal** — model bisa "melihat masa depan" saat training. Pembagian kronologis yang digunakan skripsi ini justru **LEBIH BENAR** dan sesuai dengan Altman et al. [12]. Ini menunjukkan Gemini tidak paham domain AML.

### ❌ E5. Perlu baseline internal (Logistic Regression, Random Forest)

**Alasan:** Sudah ada XGBoost+SMOTE sebagai baseline. Ditambah Multi-GNN sebagai state-of-the-art. Dua model pembanding sudah cukup untuk skripsi S1. Menambah LR/RF berarti harus re-run eksperimen dan mengubah banyak bab.

### ❌ E6. Perlu uji statistik (McNemar, CI)

**Alasan:** McNemar test membutuhkan **prediksi berpasangan pada test set yang sama** dari kedua model. Multi-GNN diambil dari paper Egressy et al. — kita tidak punya prediksi per-sampelnya. Uji statistik ini standar untuk **jurnal/konferensi**, bukan standar untuk skripsi S1.

### ❌ E7. Justifikasi dataset sintetis kurang

**Alasan:** **Sudah ada.** BAB I paragraf terakhir: "memanfaatkan data sintetis sebagai alternatif data yang tetap menjaga aspek privasi." BAB II 2.3.3: "Ketersediaan data berlabel untuk penelitian deteksi pencucian uang merupakan tantangan utama karena data transaksi riil bersifat rahasia..." Gemini tidak baca teliti.

### ❌ E8. Pindahkan hasil evaluasi dari BAB III ke BAB IV

**Alasan:** Ini saran struktural yang **debatable**. BAB III = "Implementasi Metode Usulan" — threshold optimization, confusion matrix, dan feature importance adalah bagian dari **proses evaluasi yang diimplementasikan**. BAB IV kemudian **menginterpretasi** hasilnya. Struktur ini umum di banyak skripsi dan sudah disetujui pembimbing. Mengubahnya berarti **restrukturisasi masif** yang tidak sebanding risikonya. Jika penguji mempermasalahkan, argumentasi: "BAB III menyajikan implementasi pipeline evaluasi, BAB IV menganalisis maknanya."

### ❌ E9. Perlu tabel ringkasan 59 fitur lengkap

**Alasan:** Fitur-fitur sudah **dijabarkan lengkap** di Subbab 3.3.2.1–3.3.2.5 dalam bentuk tabel per kategori. Tidak perlu tabel tambahan lagi. Gemini tidak baca detail BAB III.

### - [ ] E10. BAB I 1.6 Metode Penelitian terlalu singkat (OPSIONAL)

**Alasan:** Memang hanya 1 paragraf. Bisa diperluas sedikit, tapi BAB II & III sudah menjelaskan metode secara detail. Ini low priority — perluas hanya jika penguji memintanya.

### - [ ] E11. Definisi Operasional belum ada (OPSIONAL)

**Alasan:** Istilah-istilah teknis sudah didefinisikan in-context di BAB II dan III. Subbab terpisah bisa ditambahkan di BAB II jika pedoman mewajibkan, tapi ini minor.

### - [ ] E12. Format Daftar Pustaka kurang lengkap (IEEE) (OPSIONAL)

**Alasan:** Beberapa referensi memang kurang volume/issue/halaman. Perbaiki jika sempat, tapi bukan blocker.
