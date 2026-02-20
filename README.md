# CHECKLIST EDIT — Tugas Akhir Haris Wahyudi

> File: `TUGAS AKHIR HarisW (1).md`
> Last reviewed: 2026-02-20

---

## ✅ Sudah Selesai

- [x] Daftar Pustaka [1]–[7] sudah ada
- [x] Daftar Pustaka [8]–[13] sudah ditambahkan (CRISP-DM, Mariscal, Yang, Kadir, Altman detail, CatBoost docs)
- [x] Sitasi [10] dan [11] di Subbab 2.3.4 (CatBoost) sudah benar
- [x] Daftar Pustaka [14]–[20] sudah ditambahkan (Syukur, Hanjani, Ramineni, Pratama, Florek, Egressy, Jensen — via scite)
- [x] Subbab 2.3.3 di-rewrite dengan kutipan per pola (4 artikel baru: [21]–[24])
- [x] Daftar Pustaka [21]–[24] sudah ditambahkan (Dumitrescu, Cardoso/LaundroGraph, Song, Irwin — via scite)

---

## ❌ Yang Perlu Diedit

### 1. LEMBAR PENGESAHAN (sekitar baris 78–96)

| Item                  | Status                       |
| --------------------- | ---------------------------- |
| Nama Dosen Penguji I  | ❌ Kosong (`………………………………..`) |
| Nama Dosen Penguji II | ❌ Kosong (`………………………………`)   |
| Ditetapkan di         | ❌ Kosong                    |
| Tanggal               | ❌ Kosong                    |

### 2. DAFTAR ISI — Subbab Deployment Belum Masuk (baris ~259–261)

Subbab berikut **ada di isi skripsi** tapi **belum tercantum** di DAFTAR ISI:

- `3.6 Implementasi Deployment`
- `3.6.1 Arsitektur Deployment`
- `3.6.2 Simulasi Screening Realtime`

**Action:** Tambahkan 3 baris ini di DAFTAR ISI setelah entry `3.5.5 Feature Importance`.

### 3. DAFTAR GAMBAR — Gambar 4.1 Placeholder (baris 313)

```
Gambar 4.1 Perbandingan Performa Model Lain…...…………………………. 45
```

Ini terlihat **placeholder / duplikat** dari Gambar 3.20 yang sudah ada.

**Action:** Hapus atau perbaiki judul Gambar 4.1 sesuai isi BAB IV. Jika memang tidak ada gambar terpisah di BAB IV, hapus saja entri ini.

### 4. DAFTAR TABEL — Tabel 3.11 Tidak Terdaftar (baris ~340)

Tabel 3.11 "Peringkat 10 Fitur Terpenting" **ada di isi** (baris 1252) tapi **tidak tercantum** di DAFTAR TABEL.

**Action:** Tambahkan di DAFTAR TABEL setelah Tabel 3.10:

```
Tabel 3.11 Peringkat 10 Fitur Terpenting 40
```

### 5. ⚠️ CROSS-REFERENCE SALAH di BAB IV & V

**Ini yang paling kritis!** Referensi ke tabel/gambar di BAB IV dan BAB V banyak yang menggunakan **nomor lama** (mungkin dari draft sebelumnya) dan tidak sesuai dengan penomoran tabel/gambar yang sebenarnya.

| Lokasi              | Tertulis          | Seharusnya      | Konteks                                   |
| ------------------- | ----------------- | --------------- | ----------------------------------------- |
| Baris 1366 (§4.1.1) | `Tabel 3.4`       | **Tabel 3.10**  | Performa Model CatBoost per Split         |
| Baris 1368 (§4.1.1) | `Tabel 3.3`       | **Tabel 3.9**   | Detail Confusion Matrix pada Data Uji     |
| Baris 1370 (§4.1.1) | `Tabel 3.2`       | **Tabel 3.8**   | Analisis Performa pada Berbagai Threshold |
| Baris 1376 (§4.1.2) | `Tabel 3.1`       | **Tabel 3.7**   | Hasil Pembagian Data Kronologis           |
| Baris 1374 (§4.1.2) | `Gambar 3.8`      | **Gambar 3.16** | Performa CatBoost per Split               |
| Baris 1439 (§4.2)   | `Tabel 3.5`       | **Tabel 3.11**  | Peringkat 10 Fitur Terpenting             |
| Baris 1439 (§4.2)   | `Tabel 3.4`       | **Tabel 3.10**  | Performa Model per Split                  |
| Baris 1441 (§4.2)   | `Gambar 3.9–3.10` | **Gambar 3.17** | Feature Importance Top 20                 |
| Baris 1450 (§4.2)   | `Tabel 3.2`       | **Tabel 3.8**   | Analisis Threshold                        |
| Baris 1468 (§5.1)   | `Tabel 3.5`       | **Tabel 3.11**  | Peringkat 10 Fitur Terpenting             |
| Baris 1470 (§5.1)   | `Tabel 3.4`       | **Tabel 3.10**  | Performa Model per Split                  |

### 6. Penelitian Terdahulu — ~~Referensi di Daftar Pustaka Belum Lengkap~~ ✅ SUDAH DITAMBAHKAN

Tabel 2.1 (baris ~439) memuat **8 penelitian** — sekarang **semua sudah punya entri** di DAFTAR PUSTAKA:

| No  | Peneliti                   | Pustaka | Sumber                                        |
| --- | -------------------------- | ------- | --------------------------------------------- |
| 1   | Yang et al. (2024)         | ✅ [10] | scite — DOI: 10.21203/rs.3.rs-5395796/v1      |
| 2   | Kadir (2024)               | ✅ [11] | —                                             |
| 3   | Syukur (2025)              | ✅ [14] | scite — DOI: 10.14421/jiska.2025.10.2.249-258 |
| 4   | Hanjani (2024)             | ✅ [15] | — (lokal, tidak ditemukan di scite)           |
| 5   | Altman et al. (2023)       | ✅ [12] | —                                             |
| 6   | Ramineni & Mastouri (2025) | ✅ [16] | — (tidak ditemukan di scite)                  |
| 7   | Pratama (2025)             | ✅ [17] | scite — DOI: 10.63913/jcl.v1i1.5              |
| 8   | Florek & Zagdański (2023)  | ✅ [18] | scite — arXiv:2305.17094                      |

**Tambahan referensi lain yang sudah dimasukkan:**
| Ref | Keterangan | Sumber |
|-----|------------|--------|
| [19] | Egressy et al. (2024) — Multi-GNN, disebut di BAB IV | arXiv:2306.11586 (AAAI 2024) |
| [20] | Jensen & Iosifidis (2023) — AML patterns survey | scite — DOI: 10.1109/access.2023.3239549 |

**Masih perlu diedit:** Teks di BAB IV baris ~1441 menyebut "Florek & Zagdański (2025)" dan baris ~1384 menyebut "Egressy et al. (2024)" **tanpa nomor referensi** `[n]`. Tambahkan `[18]` dan `[19]` di teks tersebut.

### 7. LAMPIRAN Kosong (baris ~1511)

Halaman LAMPIRAN hanya berisi heading tanpa konten.

**Action:** Isi dengan lampiran yang relevan (kode program, screenshot tambahan, dll.) atau hapus dari DAFTAR ISI jika tidak diperlukan.

---

## 📋 Ringkasan Prioritas

| Prioritas | Item                                                | Dampak                              |
| --------- | --------------------------------------------------- | ----------------------------------- |
| 🔴 Tinggi | Cross-reference salah (poin 5)                      | Pembaca bingung, dosen pasti notice |
| 🔴 Tinggi | Lembar Pengesahan kosong (poin 1)                   | Wajib diisi sebelum submit          |
| 🟡 Sedang | Tambahkan `[18]` dan `[19]` di teks BAB IV (poin 6) | Sitasi tanpa nomor referensi        |
| 🟡 Sedang | Daftar ISI/Gambar/Tabel tidak lengkap (poin 2-4)    | Ketidakcocokan daftar vs isi        |
| 🟢 Rendah | Lampiran kosong (poin 7)                            | Tergantung requirement kampus       |

---

## 📚 Referensi yang Ditambahkan via Scite

Berikut referensi yang ditemukan melalui pencarian MCP scite dan sudah dimasukkan ke DAFTAR PUSTAKA:

### Pola Transaksi AML (Fan-out, Fan-in, Cycle, dll.)

Pola-pola ini (Fan-out, Fan-in, Gather-Scatter, Scatter-Gather, Simple Cycle, Random, Bipartite, Stack) sudah tercakup dalam referensi utama dan 4 artikel pendukung:

- **[12]** Altman et al. — sumber dataset IBM AML + definisi 8 pola transaksi
- **[20]** Jensen & Iosifidis — survey komprehensif metode statistik & ML untuk AML (IEEE Access, 2023)
- **[21]** Dumitrescu et al. — graph anomaly detection (volcano/blackhole nodes) → Fan-out & Fan-in
- **[22]** Cardoso et al. (LaundroGraph) — bipartite graph AML → Bipartite & Stack
- **[23]** Song et al. — subgraph & peeling chain → Gather-Scatter & Scatter-Gather
- **[24]** Irwin et al. — 184 typologies analysis → Simple Cycle & Random

### Penelitian Terdahulu (Tabel 2.1)

| Ref  | Paper                                                 | DOI / Source                     |
| ---- | ----------------------------------------------------- | -------------------------------- |
| [14] | Syukur et al. — Prediksi Kualitas Udara (CatBoost)    | 10.14421/jiska.2025.10.2.249-258 |
| [15] | Hanjani — Prediksi Kadar Polutan Pekanbaru (CatBoost) | lokal, tidak di scite            |
| [16] | Ramineni & Mastouri — Credit Card Fraud (CatBoost)    | tidak ditemukan di scite         |
| [17] | Pratama — Fraudulent Transaction Detection (RF & GB)  | 10.63913/jcl.v1i1.5              |
| [18] | Florek & Zagdański — Benchmarking Gradient Boosting   | arXiv:2305.17094                 |

### Model Pembanding

| Ref  | Paper                                               | DOI / Source                 |
| ---- | --------------------------------------------------- | ---------------------------- |
| [19] | Egressy et al. — Multi-GNN for Directed Multigraphs | arXiv:2306.11586 (AAAI 2024) |

---

## 🗂️ Struktur Workspace

```
judol-detection/
├── TUGAS AKHIR HarisW (1).md          ← File skripsi utama
├── README.md                           ← File ini
├── source-code/
│   ├── CatBoost/                       ← Kode utama CatBoost AML
│   │   ├── catboost_aml_improved.ipynb
│   │   ├── app.py / streamlit_app.py
│   │   └── saved_models/
│   └── refrensi/
│       ├── roc-auc-97.ipynb
│       └── Multi-GNN/                  ← Model pembanding
└── simulasi-replit/
```
