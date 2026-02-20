# Draft: Bagian 2.3.4 CatBoost (Diperkaya dengan Kutipan Tambahan)

Bagian ini adalah rancangan teks baru untuk **subbab 2.3.4 CatBoost** di skripsi,
dengan tambahan kutipan dari sumber resmi dan tiga makalah baru yang ditemukan via scite:

- **[13]** CatBoost Developers — situs resmi catboost.ai (sudah ada di DAFTAR PUSTAKA)
- **[25]** Dorogush et al. (2018) — makalah teknis CatBoost, implementasi library
- **[26]** Leevy et al. (2023) — studi CatBoost untuk fraud detection (imbalanced data)
- **[27]** Alothman et al. (2022) — CatBoost untuk credit fraud detection dengan data tidak seimbang

---

## Teks Bagian 2.3.4 (Versi Baru)

### 2.3.4 CatBoost

CatBoost (*Categorical Boosting*) adalah pustaka *open-source* berkinerja tinggi untuk
*gradient boosting* pada pohon keputusan yang dikembangkan oleh para peneliti dan
insinyur Yandex [13]. Algoritma ini dirancang dengan lima karakteristik unggulan: (1)
kualitas tinggi tanpa penyetelan parameter ekstensif; (2) dukungan fitur kategorikal
secara native tanpa konversi manual; (3) pelatihan GPU yang cepat dan skalabel; (4)
skema *gradient boosting* yang inovatif untuk mengurangi *overfitting*; serta (5)
inferensi yang cepat bahkan untuk tugas sensitif latensi [13]. CatBoost telah
digunakan dalam berbagai aplikasi industri skala besar, antara lain sistem *anti-bot*
Cloudflare, prediksi tujuan perjalanan di Careem, hingga sistem deteksi partikel di
CERN [13].

Prokhorenkova et al. menjelaskan bahwa CatBoost memiliki dua inovasi utama [5].
Pertama, *ordered target encoding* yang menangani fitur kategorikal dengan menghitung
statistik target secara sekuensial berdasarkan urutan data, sehingga menghindari
kebocoran informasi target yang umum terjadi pada metode *encoding* tradisional.
Kedua, *ordered boosting* yang menggunakan subset data berbeda untuk setiap observasi
dalam penghitungan gradien, sehingga mengurangi bias prediksi dan meningkatkan
kemampuan generalisasi model. Dorogush et al. selanjutnya menjelaskan bahwa CatBoost
menggunakan *oblivious decision trees* — pohon keputusan yang seimbang dan setiap
level hanya memiliki satu kondisi pemisahan — sehingga struktur ini secara inheren
lebih tahan terhadap *overfitting* dibandingkan pohon keputusan asimetris yang umum
digunakan algoritma *boosting* lainnya [25].

Keunggulan tersebut menjadikan CatBoost relevan untuk analisis data transaksi
finansial yang umumnya memiliki proporsi fitur kategorikal tinggi dan bersifat
sekuensial. Dorogush et al. menegaskan bahwa CatBoost menangani fitur kategorikal
secara langsung tanpa pra-pemrosesan tambahan, sekaligus meningkatkan ketahanan
terhadap *overfitting* dan mengurangi kebutuhan *preprocessing* [25]. Algoritma ini
juga dilengkapi kemampuan bawaan untuk menangani nilai yang hilang serta mekanisme
regularisasi yang mengurangi risiko *overfitting*. Leevy et al. memvalidasi keunggulan
CatBoost dalam konteks data tidak seimbang melalui eksperimen pada *Credit Card Fraud
Detection Dataset* dan *Medicare Part D dataset*, di mana CatBoost mencatatkan nilai
AUPRC 0,8567 dan 0,8124 — tertinggi di antara delapan algoritma klasifikasi yang
diuji, termasuk *Random Forest* dan *XGBoost* [26]. Selain itu, Alothman et al.
menunjukkan bahwa CatBoost yang dikombinasikan dengan optimasi *hyperparameter*
Bayesian efektif mendeteksi penipuan kredit pada data dengan rasio ketidakseimbangan
yang ekstrem [27]. Efektivitas CatBoost juga telah divalidasi dalam berbagai
penelitian lain, di antaranya Yang et al. yang menunjukkan keunggulan CatBoost dengan
AUC 0,767 dibandingkan enam algoritma lainnya [10], serta Kadir yang melaporkan
akurasi CatBoost sebesar 96,28% dibandingkan *Random Forest* 94,88% [11].

---

#### Representasi Matematis CatBoost

Model CatBoost dapat direpresentasikan sebagai model aditif:

$$F(x) = \sum_{t=1}^{T} f_t(x)$$

di mana $f_t(x)$ merupakan pohon keputusan pada iterasi ke-$t$, dan $T$ menyatakan
jumlah iterasi.

Fungsi objektif yang diminimalkan:

$$\mathcal{L}(F) = \sum_{i=1}^{n} L\bigl(y_i,\, F(x_i)\bigr)$$

dengan $y_i$ adalah label aktual, $F(x_i)$ adalah prediksi model, dan $L(\cdot)$
adalah fungsi *loss* (misalnya *log loss* untuk klasifikasi biner).

---

## Referensi yang Perlu Diperbarui/Ditambahkan di DAFTAR PUSTAKA

**Perbarui entri [13]** (sudah ada, ganti isi menjadi lebih lengkap mencakup halaman utama):

```
[13] CatBoost Developers, "CatBoost: High performance gradient boosting on decision trees," catboost.ai. [Online]. Available: https://catboost.ai (diakses 21 Feb. 2026).
```

**Tambahkan tiga entri baru setelah [24]:**

```
[25] A. V. Dorogush, V. Ershov, and A. Gulin, "CatBoost: gradient boosting with categorical features support," arXiv preprint arXiv:1810.11363, 2018.

[26] J. L. Leevy, J. Hancock, and T. M. Khoshgoftaar, "Investigating the effectiveness of one-class and binary classification for fraud detection," Journal of Big Data, vol. 10, no. 1, 2023. DOI: 10.1186/s40537-023-00825-1.

[27] R. B. Alothman, H. A. Talib, and M. S. Mohammed, "Fraud detection under the unbalanced class based on gradient boosting," Eastern-European Journal of Enterprise Technologies, vol. 2, no. 2 (116), pp. 6–12, 2022. DOI: 10.15587/1729-4061.2022.254922.
```

---

## Ringkasan Perubahan vs Teks Asli

| Lokasi | Perubahan |
|---|---|
| Paragraf BARU (sebelum Prokhorenkova) | Tambah paragraf pengenalan dari catboost.ai: definisi, 5 fitur, contoh penerapan industri + sitasi **[13]** |
| Paragraf 1, kalimat akhir | Tambah kalimat *oblivious decision trees* (Dorogush) + sitasi **[25]** |
| Paragraf 2, kalimat 2 | Tambah kalimat Dorogush (penanganan kategorik tanpa preprocessing) + sitasi **[25]** |
| Paragraf 2, kalimat 4–5 | Tambah kalimat Leevy et al. (AUPRC 0,8567 / 0,8124) + sitasi **[26]** |
| Paragraf 2, kalimat 6 | Tambah kalimat Alothman et al. (Bayesian optimization) + sitasi **[27]** |
| [8] dan [9] di kalimat terakhir | Sudah diubah ke [10] dan [11] (sesuai DAFTAR_PERUBAHAN.md #4) |
| DAFTAR PUSTAKA | Update [13] (catboost.ai); tambah entri [25], [26], [27] |
