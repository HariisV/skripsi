# Draft: Bagian 2.3.5 Metrik Kinerja Model (Gabungan Confusion Matrix + Metrik)

# Menggantikan subbab 2.3.5 dan 2.3.6 yang terpisah

Perubahan struktur:

- 2.3.5 _Confusion Matrix_ → **dihapus** (kontennya masuk ke awal subbab baru)
- 2.3.6 _Matrik Evaluasi_ → **diubah jadi 2.3.5 Metrik Kinerja Model** (gabungan)
- Nomor subbab 2.4 ke bawah **tidak berubah**
- Daftar Isi: hapus baris "2.3.5 Confusion Matrix" dan "2.3.6 Matrik Evaluasi", ganti dengan "2.3.5 Metrik Kinerja Model"
- Gambar 2.3 di Daftar Gambar: nama tetap, tidak berubah

Referensi yang digunakan:

- **[3]** Google Developers (sudah ada) — accuracy pada imbalanced data
- **[7]** Evidently AI (sudah ada) — confusion matrix
- **[20]** Jensen & Iosifidis (sudah ada) — evaluasi AML, trade-off precision-recall
- **[26]** Leevy et al. (sudah ada) — AUPRC sebagai metrik utama fraud detection
- **[28]** Damayanti et al. (sudah ada) — confusion matrix (Indonesia)
- **[29]** Samir et al. (baru) — JTIIK Indonesia, empat metrik evaluasi
- **[30]** Sofaer et al. (baru) — AUC-PR untuk kejadian langka/data imbalanced
- **[31]** George et al. (baru) — SLR fraud detection, F1-score & PR-AUC lebih informatif dari accuracy & ROC-AUC pada imbalanced

---

## Teks Bagian 2.3.5 (Versi Final Gabungan)

### 2.3.5 Metrik Kinerja Model

Metrik kinerja model digunakan untuk menilai seberapa baik model klasifikasi membedakan kelas yang diprediksi berdasarkan kondisi aktual data. Penilaian ini dilakukan dengan membandingkan label aktual dan label prediksi yang dihasilkan model secara sistematis, sehingga diperoleh gambaran kuantitatif tentang sejauh mana model dapat diandalkan dalam skenario nyata. Salah satu cara yang umum digunakan untuk merangkum perbandingan tersebut adalah _confusion matrix_, yaitu tabel evaluasi yang menunjukkan hubungan antara label aktual dan label prediksi pada tugas klasifikasi [7]. Damayanti et al. menyatakan bahwa _confusion matrix_ dapat menggambarkan kinerja model klasifikasi secara komprehensif dan menjadi dasar untuk menghitung berbagai metrik kinerja seperti _accuracy_, _precision_, dan _recall_ [28]. Karena seluruh metrik evaluasi diturunkan dari komponen _confusion matrix_, pemahaman terhadap struktur matriks ini menjadi prasyarat penting sebelum menginterpretasikan nilai metrik manapun.

Pada klasifikasi biner (misalnya transaksi normal dan pencucian uang/_laundering_), _confusion matrix_ berbentuk matriks 2×2 sebagaimana ditunjukkan pada Gambar 2.3.

Gambar 2.3 Ilustrasi _Confusion Matrix_ untuk Klasifikasi Biner [7]

Komponen pada _confusion matrix_ didefinisikan sebagai berikut:

- TP (_True Positive_): transaksi _laundering_ yang diprediksi sebagai _laundering_ (terdeteksi benar).
- TN (_True Negative_): transaksi normal yang diprediksi sebagai normal (terdeteksi benar).
- FP (_False Positive_): transaksi normal yang diprediksi sebagai _laundering_ (salah deteksi/_false alarm_).
- FN (_False Negative_): transaksi _laundering_ yang diprediksi sebagai normal (tidak terdeteksi/lolos).

Nilai TP, TN, FP, dan FN tersebut kemudian digunakan sebagai dasar perhitungan seluruh metrik kinerja model. Samir et al. menjelaskan bahwa metrik yang umum digunakan untuk menilai kinerja model klasifikasi secara komprehensif adalah _accuracy_, _precision_, _recall_, dan _F1-score_, karena masing-masing metrik menyoroti aspek yang berbeda dari kemampuan model [29]. Namun, pada kasus _anti-money laundering_ (AML), distribusi kelas umumnya sangat tidak seimbang (_highly imbalanced_), karena jumlah transaksi _laundering_ (kelas minoritas) dapat jauh lebih sedikit dibanding transaksi normal (kelas mayoritas) — dalam dataset tertentu rasionya dapat mencapai 1:99 atau lebih ekstrem. Pada kondisi seperti ini, _accuracy_ saja dapat memberikan gambaran yang menyesatkan. Fenomena ini dikenal sebagai _accuracy paradox_: model yang selalu memprediksi seluruh transaksi sebagai "normal" tanpa pernah mendeteksi satu pun transaksi _laundering_ tetap mampu menghasilkan _accuracy_ di atas 99%, karena nilai TN yang sangat besar mendominasi pembilang [3]. George et al. dalam tinjauan sistematis terhadap 118 studi _machine learning_ untuk deteksi _fraud_ menyimpulkan bahwa _precision_, _recall_, _F1-score_, dan PR-AUC memberikan penilaian yang jauh lebih bermakna terhadap sistem deteksi _fraud_ dibandingkan _accuracy_ semata, terutama pada distribusi kelas yang tidak seimbang [31]. Oleh sebab itu, Jensen dan Iosifidis menekankan bahwa evaluasi AML sebaiknya berfokus pada metrik yang sensitif terhadap kelas minoritas, seperti _precision_, _recall_, _F1-score_, serta _area under the precision-recall curve_ (AUC-PR), karena metrik-metrik ini tidak "tertipu" oleh dominasi kelas mayoritas [20].

Berikut definisi dan penjelasan masing-masing metrik yang digunakan pada penelitian ini.

#### 2.3.5.1 _Accuracy_

_Accuracy_ mengukur proporsi prediksi yang benar terhadap seluruh data:

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

Metrik ini berguna untuk gambaran umum pada dataset yang seimbang, karena pembilangnya memperhitungkan baik prediksi benar pada kelas positif (TP) maupun kelas negatif (TN). Namun, pada data yang sangat tidak seimbang seperti data transaksi keuangan, nilai TN yang sangat besar akan mendominasi pembilang sehingga _accuracy_ tampak tinggi meskipun model sama sekali gagal mendeteksi kelas minoritas — inilah inti dari _accuracy paradox_ yang telah disebutkan sebelumnya [3]. Misalnya, jika hanya 0,5% transaksi merupakan _laundering_, model yang selalu memprediksi "normal" akan mencapai _accuracy_ 99,5%, padahal model tersebut tidak berguna secara operasional. Oleh karena itu, dalam penelitian ini _accuracy_ dilaporkan sebagai informasi pelengkap, tetapi bukan sebagai dasar utama evaluasi model.

#### 2.3.5.2 _Precision_

_Precision_ mengukur ketepatan prediksi positif, yaitu proporsi transaksi yang benar-benar _laundering_ dari seluruh transaksi yang diprediksi sebagai _laundering_:

$$\text{Precision} = \frac{TP}{TP + FP}$$

Pada konteks AML, setiap prediksi positif yang keliru (FP) berarti satu transaksi normal yang ditandai sebagai mencurigakan dan memerlukan investigasi manual oleh tim _compliance_. Sistem berbasis aturan (_rule-based_) di perbankan konvensional dikenal memiliki tingkat FP yang sangat tinggi — sebagian besar peringatan yang dihasilkan ternyata bukan merupakan kasus _laundering_ yang sesungguhnya, sehingga menyebabkan beban kerja investigasi yang besar [3]. _Precision_ yang tinggi berarti bahwa model dapat menekan jumlah _false alarm_ ini, sehingga setiap peringatan yang dihasilkan lebih dapat diandalkan oleh tim _compliance_ dan sumber daya investigasi dapat dialokasikan secara lebih efisien [20].

#### 2.3.5.3 _Recall_

_Recall_ (juga disebut _sensitivity_ atau _true positive rate_) mengukur kemampuan model menemukan transaksi _laundering_, yaitu proporsi transaksi _laundering_ yang berhasil terdeteksi dari seluruh transaksi _laundering_ yang sebenarnya ada:

$$\text{Recall} = \frac{TP}{TP + FN}$$

Dalam AML, _recall_ merupakan metrik yang sangat kritis karena setiap FN berarti satu transaksi _laundering_ yang lolos dari sistem deteksi tanpa terdeteksi. Transaksi yang tidak terdeteksi tersebut berpotensi memfasilitasi kegiatan ilegal yang berkelanjutan dan dapat menimbulkan konsekuensi hukum serta regulasi bagi lembaga keuangan yang bersangkutan. Namun, meningkatkan _recall_ secara agresif — misalnya dengan menurunkan _threshold_ prediksi — cenderung menaikkan jumlah FP, yang berarti akan menurunkan _precision_. Dinamika ini dikenal sebagai _precision-recall trade-off_, yang merupakan tantangan mendasar dalam desain sistem deteksi AML: model harus mampu mendeteksi sebanyak mungkin transaksi _laundering_ (_recall_ tinggi) sekaligus menjaga agar jumlah _false alarm_ tetap dapat dikelola (_precision_ yang memadai) [20].

#### 2.3.5.4 _F1-Score_

_F1-score_ merupakan rata-rata harmonik (_harmonic mean_) dari _precision_ dan _recall_:

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

Berbeda dengan rata-rata aritmetika biasa, rata-rata harmonik memberikan penalti lebih besar apabila salah satu dari dua komponen bernilai rendah. Sebagai ilustrasi: jika _precision_ = 0,90 tetapi _recall_ = 0,10, maka rata-rata aritmetika menghasilkan 0,50 (kesan "setengah lumayan"), sedangkan rata-rata harmonik menghasilkan F1 = 0,18 — nilai yang jauh lebih rendah dan mencerminkan secara akurat bahwa model gagal mendeteksi sebagian besar kasus _laundering_. Samir et al. menyatakan bahwa F1-_score_ oleh sebab itu lebih sesuai untuk kasus dengan distribusi kelas yang tidak merata, karena nilai F1 hanya akan tinggi apabila _precision_ maupun _recall_ keduanya bernilai memuaskan [29]. George et al. menegaskan hal ini dalam tinjauan sistematis mereka, menyimpulkan bahwa F1-_score_ sebagai rata-rata harmonik dari _precision_ dan _recall_ memberikan evaluasi yang lebih holistik dan merupakan metrik yang lebih dapat diandalkan dibanding _accuracy_ pada tugas deteksi _fraud_ dengan distribusi kelas yang tidak seimbang [31]. Dalam penelitian ini, F1-_score_ digunakan sebagai salah satu acuan utama dalam proses penyetelan _threshold_ (_threshold optimization_) agar model dapat menyeimbangkan kemampuan deteksi dan ketepatan peringatan secara optimal [20].

#### 2.3.5.5 PR-AUC / AUPRC

PR-AUC (atau AUPRC, _Area Under the Precision-Recall Curve_) adalah luas area di bawah kurva _precision–recall_ yang diplot untuk berbagai nilai _threshold_. Prinsip kerjanya adalah sebagai berikut: setiap nilai _threshold_ yang dipilih akan menghasilkan satu pasangan nilai (_precision_, _recall_) berdasarkan matriks konfusi yang terbentuk pada ambang tersebut. Dengan memvariasikan _threshold_ dari 0 hingga 1, diperoleh serangkaian titik yang membentuk kurva _precision–recall_. PR-AUC merangkum luas area di bawah kurva ini menjadi satu nilai skalar antara 0 dan 1, sehingga kinerja model dapat dinilai secara agregat tanpa bergantung pada satu nilai _threshold_ tunggal yang ditetapkan secara arbitrer.

Sofaer et al. menunjukkan secara formal bahwa AUC-PR lebih sesuai untuk kejadian langka (_rare events_) atau data tidak seimbang dibanding AUC-ROC, karena kurva PR tidak melibatkan TN sama sekali dalam perhitungannya — berbeda dengan kurva ROC yang menggunakan _false positive rate_ (FPR = FP / (FP + TN)) sebagai sumbu-x sehingga nilai TN yang besar pada kelas mayoritas dapat "menggelembungkan" nilai AUC-ROC dan memberikan kesan kinerja yang lebih baik dari kenyataan [30]. Sejalan dengan itu, George et al. dalam tinjauan sistematis terhadap 118 studi _machine learning_ untuk deteksi _fraud_ menyimpulkan bahwa AUC-ROC dapat menglebih-lebihkan (_overstate_) kinerja model pada konteks data tidak seimbang, dan PR-AUC menjadi semakin diutamakan (_increasingly preferred_) untuk tugas deteksi _fraud_ karena berfokus pada kinerja kelas minoritas [31]. Leevy et al. juga menggunakan AUPRC sebagai metrik utama dalam evaluasi deteksi _fraud_ pada dataset dengan ketidakseimbangan kelas yang ekstrem, karena metrik ini lebih mampu membedakan performa model secara nyata di antara kelas positif [26]. Dengan demikian, dalam penelitian AML yang menggunakan data tidak seimbang ini, PR-AUC dijadikan sebagai metrik evaluasi utama, sementara _precision_, _recall_, dan _F1-score_ memberikan interpretasi operasional yang lebih granular terhadap performa model pada _threshold_ keputusan yang dipilih [20].

---

## Entri DAFTAR PUSTAKA Baru

Tambahkan setelah [28] (tidak ada perubahan pada [1]–[28]):

```
[29] M. Samir, Purnawansyah, and H. Darwis, "Fourier Descriptor Pada Klasifikasi Daun Herbal Menggunakan Support Vector Machine Dan Naive Bayes," JTIIK (Jurnal Teknologi Informasi dan Ilmu Komputer), vol. 10, no. 6, pp. 1205–1212, 2023. DOI: 10.25126/jtiik.1067309.

[30] H. R. Sofaer, J. A. Hoeting, and C. S. Jarnevich, "The area under the precision-recall curve as a performance metric for rare binary events," Methods in Ecology and Evolution, vol. 10, no. 4, pp. 565–577, 2019. DOI: 10.1111/2041-210x.13140.

[31] M. J. George, Md. K. Alam, and Md. T. Hasan, "Machine learning for fraud detection in digital banking: a systematic literature review," vol. 03, no. 01, pp. 37–61, 2023. DOI: 10.63125/913ksy63.
```

---

## Ringkasan Perubahan vs Teks Asli

| Lokasi                      | Perubahan                                                                                             |
| --------------------------- | ----------------------------------------------------------------------------------------------------- |
| Judul subbab                | 2.3.5 _Confusion Matrix_ + 2.3.6 _Matrik Evaluasi_ → **2.3.5 Metrik Kinerja Model**                   |
| Gambar 2.3                  | Tetap dipertahankan, referensi [7] dipertahankan                                                      |
| Keterangan TP/TN/FP/FN      | Dipertahankan (format bullet, label "Komponen")                                                       |
| Paragraf konteks imbalanced | Diperluas: tambah _accuracy paradox_ + contoh angka + [3][20][29][31]                                |
| Accuracy                    | Diperluas: formula + _accuracy paradox_ + contoh numerik 99.5% + bukan metrik utama [3]              |
| Precision                   | Diperluas: formula + konteks AML (_false alarm_) + beban _compliance_ team [3][20]                   |
| Recall                      | Diperluas: formula + konsekuensi FN (hukum/regulasi) + _precision-recall trade-off_ eksplisit [20]   |
| F1-Score                    | Diperluas: contoh numerik (precision=0.90, recall=0.10 → F1=0.18) + _threshold optimization_ [29][31][20] |
| PR-AUC                      | Diperluas: mekanisme kurva + TN exclusion formal (Sofaer) + _overstate_ AUC-ROC (George) [30][31][26][20] |
| DAFTAR PUSTAKA              | Tambah [29], [30], [31]; [3][20][26] dipakai ulang (sudah ada)                                        |
| Subbab 2.3.6                | **Dihapus** (konten sudah masuk ke 2.3.5)                                                             |
| Daftar Isi                  | Hapus "2.3.5 Confusion Matrix" dan "2.3.6 Matrik Evaluasi", ganti dengan "2.3.5 Metrik Kinerja Model" |
