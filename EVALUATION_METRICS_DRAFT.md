# Draft: Bagian 2.3.6 Metrik Evaluasi (Menggantikan Teks Dummy)

Referensi baru:

- **[29]** Samir et al. (2023) — JTIIK (Jurnal Teknologi Informasi dan Ilmu Komputer), Universitas Brawijaya — jurnal berbahasa Indonesia, mendefinisikan empat metrik evaluasi: _Accuracy_, _Precision_, _F1-score_, dan _Recall_
- **[30]** Sofaer et al. (2019) — _Methods in Ecology and Evolution_ — membuktikan keunggulan AUC-PR dibanding AUC-ROC untuk kejadian langka dan data tidak seimbang (_imbalanced_)

---

## Teks Bagian 2.3.6 (Versi Baru — Menggantikan Teks Dummy)

### 2.3.6 Metrik Evaluasi

Pada data transaksi AML, distribusi kelas umumnya tidak seimbang (_imbalanced_), sehingga metrik _accuracy_ saja sering kurang representatif. Model yang memprediksi seluruh transaksi sebagai normal pun dapat mencapai akurasi di atas 99% karena proporsi kelas minoritas yang sangat kecil [3]. Oleh karena itu, penelitian ini menggunakan empat metrik evaluasi yang dihitung berdasarkan nilai TP, TN, FP, dan FN dari _confusion matrix_ (Subbab 2.3.5). Samir et al. menjelaskan bahwa empat metrik yang umum digunakan untuk menilai kinerja suatu model klasifikasi adalah _accuracy_, _precision_, _recall_, dan _F1-score_ [29].

**Precision** mengukur proporsi prediksi positif yang benar terhadap seluruh prediksi positif yang dihasilkan model:

$$\text{Precision} = \frac{TP}{TP + FP}$$

Nilai _precision_ yang tinggi mengindikasikan bahwa model jarang menghasilkan _false alarm_ (FP rendah), sehingga tim kepatuhan tidak dibebani oleh investigasi yang tidak perlu [3].

**Recall** (atau _Sensitivity_) mengukur proporsi data positif yang berhasil terdeteksi oleh model:

$$\text{Recall} = \frac{TP}{TP + FN}$$

Dalam konteks AML, _recall_ yang tinggi berarti model berhasil mendeteksi sebagian besar transaksi _laundering_ sehingga transaksi mencurigakan tidak lolos tanpa terdeteksi [3].

**F1-Score** merupakan rata-rata harmonik dari _precision_ dan _recall_, yang menyeimbangkan kedua metrik tersebut secara sekaligus:

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

F1-Score sangat berguna pada data tidak seimbang karena memberikan bobot yang sama terhadap _false positive_ maupun _false negative_, sehingga lebih informatif dibandingkan akurasi pada kasus deteksi anomali [29].

**PR-AUC** (_Area Under the Precision-Recall Curve_) merupakan metrik berbasis kurva yang merangkum _trade-off_ antara _precision_ dan _recall_ pada berbagai nilai _threshold_. Sofaer et al. membuktikan bahwa AUC-PR lebih robust terhadap data tidak seimbang dibandingkan AUC-ROC, karena AUC-PR tidak memperhitungkan _true negative_ (TN) yang berlimpah dalam kelas mayoritas sehingga tidak melebih-lebihkan performa model [30]. Dengan demikian, AUC-PR memberikan gambaran yang lebih jujur tentang kemampuan model dalam membedakan kelas minoritas (_laundering_) dari kelas mayoritas (transaksi normal).

---

## Entri DAFTAR PUSTAKA Baru

Tambahkan setelah [28]:

```
[29] M. Samir, Purnawansyah, and H. Darwis, "Fourier Descriptor Pada Klasifikasi Daun Herbal Menggunakan Support Vector Machine Dan Naive Bayes," JTIIK (Jurnal Teknologi Informasi dan Ilmu Komputer), vol. 10, no. 6, pp. 1205–1212, 2023. DOI: 10.25126/jtiik.1067309.

[30] H. R. Sofaer, J. A. Hoeting, and C. S. Jarnevich, "The area under the precision-recall curve as a performance metric for rare binary events," Methods in Ecology and Evolution, vol. 10, no. 4, pp. 565–577, 2019. DOI: 10.1111/2041-210x.13140.
```

---

## Ringkasan Perubahan vs Teks Dummy

| Lokasi           | Perubahan                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Paragraf pembuka | Pertahankan kalimat awal, lanjutkan (bukan terpotong), tambah sitasi **[3]** dan **[29]**  |
| Precision        | Tambah definisi + formula + sitasi **[3]**                                                 |
| Recall           | Tambah definisi + formula + sitasi **[3]**                                                 |
| F1-Score         | Tambah definisi + formula (rata-rata harmonik) + sitasi **[29]**                           |
| PR-AUC           | Tambah definisi + penjelasan keunggulan vs ROC-AUC untuk data imbalanced + sitasi **[30]** |
| DAFTAR PUSTAKA   | Tambah entri **[29]** (JTIIK Indonesia) dan **[30]** (Sofaer et al.)                       |

---

## Catatan Referensi

- **[3]** sudah ada di DAFTAR PUSTAKA: _Google Developers, "Classification: Accuracy, Precision, Recall, and related metrics," 2025._ — dipakai ulang di 2.3.6
- **[28]** sudah ada (dari 2.3.5) — tidak perlu dicantumkan ulang di paragraf 2.3.6 kecuali diinginkan
- **[29]** baru — jurnal Indonesia JTIIK Brawijaya, relevan untuk empat metrik evaluasi
- **[30]** baru — jurnal internasional bereputasi, spesifik tentang keunggulan AUC-PR pada data imbalanced/kejadian langka
