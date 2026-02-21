# Draft: Bagian 2.3.5 Confusion Matrix (Diperkaya dengan Referensi Bahasa Indonesia)

Referensi Indonesia baru:
- **[28]** Damayanti et al. (2023) — JATI (Jurnal Mahasiswa Teknik Informatika), ITN Malang — jurnal berbahasa Indonesia tentang evaluasi klasifikasi menggunakan confusion matrix

---

## Teks Bagian 2.3.5 (Versi Baru)

### 2.3.5 *Confusion Matrix*

*Confusion matrix* adalah tabel evaluasi yang menunjukkan perbandingan antara label aktual (*ground truth*) dan label prediksi model pada kasus klasifikasi [7]. Damayanti et al. menegaskan bahwa *confusion matrix* menggambarkan performa suatu model klasifikasi dan dapat digunakan untuk menghitung beberapa metrik evaluasi, yaitu *accuracy*, *precision*, dan *recall* [28]. Untuk klasifikasi biner (misalnya: transaksi normal vs *laundering*), *confusion matrix* berbentuk matriks 2×2 sebagai berikut:

Gambar 2.3 Ilustrasi *Confusion Matrix* untuk Klasifikasi Biner [7]

Keterangan:

A. TP (*True Positive*): transaksi *laundering* yang berhasil terdeteksi sebagai *laundering*.
B. TN (*True Negative*): transaksi normal yang berhasil terdeteksi sebagai normal.
C. FP (*False Positive*): transaksi normal yang salah terdeteksi sebagai *laundering* (*false alarm*).
D. FN (*False Negative*): transaksi *laundering* yang salah terdeteksi sebagai normal (*laundering* lolos).

Secara matematis, keempat komponen tersebut didefinisikan sebagai:

$$TP = \sum_{i=1}^{n} \mathbb{I}(y_i=1 \wedge \hat{y}_i=1), \quad TN = \sum_{i=1}^{n} \mathbb{I}(y_i=0 \wedge \hat{y}_i=0)$$

$$FP = \sum_{i=1}^{n} \mathbb{I}(y_i=0 \wedge \hat{y}_i=1), \quad FN = \sum_{i=1}^{n} \mathbb{I}(y_i=1 \wedge \hat{y}_i=0)$$

Dalam konteks *anti-money laundering*, kesalahan FN umumnya lebih berisiko karena transaksi *laundering* tidak terdeteksi, sedangkan FP menambah beban investigasi karena menghasilkan *alert* yang tidak valid.

---

## Entri DAFTAR PUSTAKA Baru

Tambahkan setelah [27]:

```
[28] I. Damayanti, T. N. Padilah, and U. Enri, "Pengaruh Pembobotan Emoji terhadap Evaluasi Algoritme Naïve Bayes pada Komentar Pelecehan Seksual," JATI (Jurnal Mahasiswa Teknik Informatika), vol. 7, no. 2, pp. 1423–1428, 2023. DOI: 10.36040/jati.v7i2.6868.
```

---

## Ringkasan Perubahan vs Teks Asli

| Lokasi | Perubahan |
|---|---|
| Paragraf 1, kalimat 2 | Tambah kalimat Damayanti et al. (definisi confusion matrix dalam konteks Indonesia) + sitasi **[28]** |
| Formula TP/TN/FP/FN | Sudah ada di teks asli, dipertahankan dalam format matematika |
| DAFTAR PUSTAKA | Tambah entri [28] |
