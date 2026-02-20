__TUGAS AKHIR__

__Implementasi Algoritma *CatBoost* Pada Sistem Anti Pencucian Uang Berbasis Pola Transaksi Untuk Deteksi Transaksi Mencurigakan__

Sebagai Salah Satu Syarat untuk Memperoleh Gelar Sarjana Komputer pada 

PJJ Informatika



__Oleh:__

__220401010015, Haris Wahyudi__

__PROGRAM STUDI PJJ INFORMATIKA  
UNIVERSITAS SIBER ASIA  
AGUSTUS 2025__

# <a id="_Toc222169378"></a>LEMBAR KEABSAHAN TUGAS AKHIR

Saya yang bertanda\-tangan di bawah ini:

Nama	: Haris Wahyudi  
NIM                            	: 220401010015  
Program Studi	: PJJ Informatika  
Judul Tugas Akhir	: Implementasi Algoritma *CatBoost* Pada Sistem Anti 	  Pencucian Uang Berbasis Pola Transaksi Untuk 		  Deteksi Transaksi Mencurigakan  


1. Tugas Akhir disusun secara ilmiah yang memenuhi aspek orisinalitas, valid dan dapat dipertanggungjawabkan\. 
2. Tugas Akhir disusun tidak menggunakan *Generative AI* untuk perbantuan penulisan kalimat/paragraf/bab\.
3. Data yang digunakan dalam penelitian adalah data yang bersumber pada penerapan metode usulan/dari sumber ilmiah lain/dari instansi yang berizin secara resmi

Jika di kemudian hari ditemukan hal\-hal yang melanggar ketentuan penyusunan Tugas Akhir, saya siap bersedia dan menerima Sanksi Akademik dari Universitas Siber Asia\.

Demikian pernyataan ini saya buat\.

Batam, 26 November 2025

Yang membuat pernyataan,

Haris Wahyudi

# <a id="_tyn9g549ovi"></a><a id="_Toc222169379"></a>PERNYATAAN ORIGINALITAS DAN PUBLIKASI

Saya yang bertanda\-tangan di bawah ini:

Nama	: Haris Wahyudi

NIM                             	: 220401010015

Program Studi	: PJJ Informatika

Judul Tugas Akhir	: Implementasi Algoritma *CatBoost* Pada Sistem Anti  
		Pencucian Uang Berbasis Pola Transaksi Untuk 			Deteksi Transaksi Mencurigakan

Menyatakan dengan sesungguhnya bahwa Tugas Akhir ini merupakan hasil penelitian, pemikiran dan pemaparan asli saya sendiri\. Saya tidak mencantumkan tanpa pengakuan bahan \- bahan yang telah dipublikasikan sebelumnya atau ditulis oleh orang lain, atau sebagai bahan yang pernah diajukan untuk gelar atau ijazah pada Universitas Siber Asia atau perguruan tinggi lainnya\. 

Apabila dikemudian hari terdapat penyimpangan dan ketidakbenaran dalam pernyataan ini, maka saya bersedia menerima sanksi akademik sesuai dengan peraturan yang berlaku di Universitas Siber Asia\.

Demikian pernyataan ini saya buat\. 

Batam, 26 November 2025

Yang membuat pernyataan,

Haris Wahyudi

# <a id="_ypzrc0km4093"></a><a id="_Toc222169380"></a>LEMBAR PENGESAHAN

Tugas Akhir ini diajukan oleh :

Nama	: Haris Wahyudi  
NIM                                      : 220401010015  
Program Studi	: PJJ Informatika  
Judul Tugas Akhir	: Implementasi Algoritma *CatBoost* Pada Sistem Anti

		Pencucian Uang Berbasis Pola Transaksi Untuk 			Deteksi Transaksi Mencurigakan

Telah berhasil dipertahankan dihadapan Dewan Penguji dan diterima sebagai bagian persyaratan yang diperlukan untuk memperoleh gelar Sarjana Komputer pada Program Studi PJJ Informatika Universitas Siber Asia\.

Ketua Sidang / Dosen Penguji I

Dosen Penguji II

………………………………\.\.

………………………………

Dosen Pembimbing

Ketua Program Studi

Cian Ramadhona Hassolthine, S\.Kom,

Syahid Abdullah, S\.Si, M\.Kom\.

Ditetapkan di : 

Tanggal : <a id="_lm6x29gl1tag"></a>

# <a id="_Toc222169381"></a>ABSTRAK

Pencegahan pencucian uang memerlukan identifikasi rekening berisiko yang akurat\. Namun, pendekatan manual dan berbasis aturan sederhana sering kali tidak efektif karena kompleksitas pola transaksi\. Penelitian ini mengembangkan model analisis prediktif berbasis pola transaksi menggunakan algoritma *CatBoost* untuk mendukung kebijakan pemblokiran rekening\. *Dataset* sintetis digunakan untuk merepresentasikan karakteristik transaksi keuangan seperti frekuensi, nilai, dan aktivitas rekening\. *CatBoost* dipilih karena mampu menangani fitur kategorikal secara efisien tanpa *encoding* kompleks\. Metode penelitian menggunakan pendekatan kuantitatif non eksperimental dengan tahapan *preprocessing*, rekayasa 59 fitur berbasis pola transaksi, pelatihan model, dan evaluasi menggunakan *Precision, Recall*, F1\-Score, dan PR\-AUC\. Hasil penelitian menunjukkan bahwa model CatBoost mencapai F1\-Score 0,7140, Precision 87,70%, dan PR\-AUC 0,7412 pada data uji, serta mengungguli dua model pembanding \(Multi\-GNN dan XGBoost\+SMOTE\) secara signifikan\. Penelitian ini dapat menjadi dasar pengembangan sistem pendukung keputusan dalam analisis transaksi keuangan dan berkontribusi pada upaya pencegahan pencucian uang\.

Kata Kunci: Pencucian uang, Analisis prediktif*, CatBoost, Machine learning*\.

# <a id="_6krc5i3aapal"></a><a id="_Toc222169382"></a>ABSTRACT

*Prevention of money laundering requires accurate identification of at\-risk accounts\. However, manual approaches and simple rule\-based methods are often ineffective due to the complexity of transaction patterns\. This research develops a predictive analytics model based on transaction patterns using the CatBoost algorithm to support account blocking policies\. Synthetic datasets are used to represent characteristics of financial transactions, such as transaction frequency, transaction value, and account activity patterns\. CatBoost is selected because it can efficiently handle categorical features without complex encoding processes\.* *The research methodology employs a quantitative non\-experimental approach with stages of data preprocessing, engineering of 59 transaction pattern\-based features, model training, and evaluation using Precision, Recall, F1\-Score, and PR\-AUC metrics\. Results demonstrate that the CatBoost model achieves an F1\-Score of 0\.7140, Precision of 87\.70%, and PR\-AUC of 0\.7412 on the test set, significantly outperforming two baseline models \(Multi\-GNN and XGBoost\+SMOTE\)\. This research serves as a foundation for developing decision support systems in financial transaction analysis and contributes to anti\-money laundering efforts\.*

*Keywords: CatBoost, Machine Learning, Money Laundering, Predictive Analytics*

# <a id="_yzgii5awj0to"></a><a id="_Toc222169383"></a>KATA PENGANTAR

Puji dan syukur penulis panjatkan ke hadirat Tuhan Yang Maha Esa atas rahmat dan karunia\-Nya sehingga penulis dapat menyelesaikan Tugas Akhir berjudul “Implementasi Algoritma *CatBoost* Pada Sistem Anti Pencucian Uang Berbasis Pola Transaksi Untuk Deteksi Transaksi Mencurigakan” sebagai salah satu syarat memperoleh gelar Sarjana Komputer pada Program Studi Informatika PJJ Universitas Siber Asia\.

Topik ini dipilih karena deteksi transaksi mencurigakan penting dalam upaya anti pencucian uang\. Namun, proses identifikasi masih sering dilakukan secara manual dan berbasis aturan sederhana\. Oleh karena itu, penelitian ini menerapkan Algoritma *CatBoost* untuk membantu mengenali pola transaksi secara lebih konsisten\.

Penulis menyadari bahwa penyusunan Tugas Akhir ini tidak lepas dari dukungan dan bimbingan berbagai pihak\. Oleh karena itu, penulis menyampaikan terima kasih kepada:

1. Ibu Cian Ramadhona Hassolthine, S\.Kom\., M\.Kom\., selaku dosen pembimbing yang telah memberikan arahan, bimbingan, dan masukan selama proses penyusunan Tugas Akhir ini\.
2. Seluruh dosen Program Studi Informatika PJJ Universitas Siber Asia yang telah memberikan ilmu dan pengalaman selama kuliah\.
3. Orang tua dan keluarga penulis yang senantiasa memberikan doa, dukungan, dan motivasi\.
4. Rekan\-rekan penulis yang telah memberikan dukungan dan diskusi selama proses penyusunan penelitian ini\.

Akhir kata, penulis berharap Tuhan Yang Maha Esa berkenan membalas segala kebaikan semua pihak yang telah membantu\. Semoga Tugas Akhir ini membawa manfaat bagi pengembangan ilmu\.

Batam, 26 November 2025

Penulis

# <a id="_2t4oyrj4i8m"></a><a id="_Toc222169384"></a>DAFTAR ISI

[LEMBAR KEABSAHAN TUGAS AKHIR	2](#_Toc222169378)

[PERNYATAAN ORIGINALITAS DAN PUBLIKASI	2](#_Toc222169379)

[LEMBAR PENGESAHAN	3](#_Toc222169380)

[ABSTRAK	4](#_Toc222169381)

[ABSTRACT	5](#_Toc222169382)

[KATA PENGANTAR	6](#_Toc222169383)

[DAFTAR ISI	7](#_Toc222169384)

[DAFTAR GAMBAR	10](#_Toc222169385)

[DAFTAR TABEL	11](#_Toc222169386)

[BAB I  PENDAHULUAN	12](#_Toc222169387)

[1\.1 Latar Belakang Masalah	12](#_Toc222169388)

[1\.2 Rumusan Masalah	13](#_Toc222169389)

[1\.3 Batasan Masalah	14](#_Toc222169390)

[1\.4 Tujuan Penelitian	14](#_Toc222169391)

[1\.5 Manfaat Penelitian	15](#_Toc222169392)

[1\.6 Metode Penelitian	15](#_Toc222169393)

[BAB II   LANDASAN METODE	16](#_Toc222169394)

[2\.1 Tahapan Penelitian	16](#_Toc222169395)

[2\.1\.1 Business Understanding	16](#_Toc222169396)

[2\.1\.2 Data Understanding	17](#_Toc222169397)

[2\.1\.3 Data Preparation	17](#_Toc222169398)

[2\.1\.4 Modeling	17](#_Toc222169399)

[2\.1\.5 Evaluation	18](#_Toc222169400)

[2\.1\.6 Deployment	18](#_Toc222169401)

[2\.2 Penelitian Terdahulu	18](#_Toc222169402)

[2\.3 Tinjauan Pustaka	19](#_Toc222169403)

[2\.3\.1 Anti Pencucian Uang	19](#_Toc222169404)

[2\.3\.2 Dataset AMLworld	21](#_Toc222169405)

[2\.3\.3 Pola Transaksi Pencucian Uang	21](#_Toc222169406)

[2\.3\.4 CatBoost	23](#_Toc222169407)

[2\.3\.5 Confusion Matrix	24](#_Toc222169408)

[2\.3\.6 Matrik Evaluasi	25](#_Toc222169409)

[2\.4 Metode	25](#_Toc222169410)

[2\.4\.1 Waktu dan Lokasi Penelitian	25](#_Toc222169411)

[2\.4\.2 Bahan dan Alat Penelitian	25](#_Toc222169412)

[BAB III  IMPLEMENTASI METODE USULAN	27](#_Toc222169413)

[3\.1 Business Understanding	27](#_Toc222169414)

[3\.2 Implementasi Data Understanding	28](#_Toc222169415)

[3\.2\.1 Deskripsi Dataset	28](#_Toc222169416)

[3\.2\.2 Pemuatan dan Pra\-pemrosesan Data	29](#_Toc222169417)

[3\.2\.3 eksplorasi data	29](#_Toc222169418)

[3\.3 Implementasi Data Preparation	30](#_Toc222169419)

[3\.3\.1 Normalisasi Timestamp	30](#_Toc222169420)

[3\.3\.2 Rekayasa Fitur \(Feature Engineering\)	30](#_Toc222169421)

[3\.3\.3 Pembagian Data Kronologis	34](#_Toc222169422)

[3\.4 Implementasi Modeling	35](#_Toc222169423)

[3\.4\.1 Pemilihan Algoritma	35](#_Toc222169424)

[3\.4\.2 Penanganan Ketidakseimbangan Kelas	36](#_Toc222169425)

[3\.4\.3 Konfigurasi dan Pelatihan Model	36](#_Toc222169426)

[3\.5 Implementasi Evaluation	37](#_Toc222169427)

[3\.5\.1 Optimasi Threshold	37](#_Toc222169428)

[3\.5\.2 Confusion Matrix	39](#_Toc222169429)

[3\.5\.3 Kurva Evaluasi	40](#_Toc222169430)

[3\.5\.4 Hasil Evaluasi per Split	40](#_Toc222169431)

[3\.5\.5 Feature Importance	41](#_Toc222169432)

[BAB IV  HASIL DAN ANALISA	45](#_Toc222169433)

[4\.1 HASIL	45](#_Toc222169434)

[4\.1\.1 Interpretasi Performa Model	45](#_Toc222169435)

[4\.1\.2 Makna Pola Performa Antar Split	45](#_Toc222169436)

[4\.1\.3 Perbandingan dengan Model Pembanding	46](#_Toc222169437)

[4\.2 ANALISA	47](#_Toc222169438)

[BAB V  KESIMPULAN	50](#_Toc222169439)

[5\.1 KESIMPULAN	50](#_Toc222169440)

[5\.2 SARAN	50](#_Toc222169441)

[DAFTAR PUSTAKA	52](#_Toc222169442)

[LAMPIRAN	53](#_Toc222169443)

[DAFTAR RIWAYAT HIDUP	54](#_Toc222169444)

# <a id="_zfnhtarztei6"></a><a id="_Toc222169385"></a>DAFTAR GAMBAR

[Gambar 2\.1 Alur Proses Penelitian dengan Metode CRISP\-DM	16](#_Toc222007374)

[Gambar 2\.2 Model Pola Pencucian Uang \[12\]	22](#_Toc222007375)

[Gambar 2\.3 Ilustrasi Confusion Matrix untuk Klasifikasi Biner \[7\]	24](#_Toc222007376)

[Gambar 3\.1 Kode Pra\-pemrosesan Data dan Encoding Atribut	28](#_Toc222169132)

[Gambar 3\.2 Distribusi Kelas Transaksi pada Dataset AMLworld HI\-Small	29](#_Toc222169133)

[Gambar 3\.3 Kode Normalisasi Timestamp	29](#_Toc222169134)

[Gambar 3\.4 Kode Rekayasa Fitur Berbasis Graf	30](#_Toc222169135)

[Gambar 3\.5 Kode Rekayasa Fitur Statistik Nilai Transaksi	31](#_Toc222169136)

[Gambar 3\.6 Kode Rekayasa Fitur Penomoran Mitra \(Port Numbering\)	32](#_Toc222169137)

[Gambar 3\.7 Kode Rekayasa Fitur Jarak Waktu Antar Transaksi	32](#_Toc222169138)

[Gambar 3\.8 Kode Rekayasa Fitur Pola Waktu dan Perilaku	33](#_Toc222169139)

[Gambar 3\.9 Kode Pembagian Data Kronologis	34](#_Toc222169140)

[Gambar 3\.10 Kode Penanganan Ketidakseimbangan Kelas	35](#_Toc222169141)

[Gambar 3\.11 Kode Konfigurasi Hyperparameter dan Pelatihan Model	36](#_Toc222169142)

[Gambar 3\.12 Kode Optimasi Threshold untuk Maksimasi F1\-Score	36](#_Toc222169143)

[Gambar 3\.13 Analisis Dampak Threshold pada Precision, Recall, dan F1\-Score	37](#_Toc222169144)

[Gambar 3\.14 Confusion Matrix pada Ketiga Split Data	38](#_Toc222169145)

[Gambar 3\.15 Kurva Precision\-Recall dan ROC	39](#_Toc222169146)

[Gambar 3\.16 Performa CatBoost per Split	40](#_Toc222169147)

[Gambar 3\.17 Feature Importance Top 20	40](#_Toc222169148)

[Gambar 3\.18 Halaman Awal Aplikasi Simulasi AML pada Replit	42](#_Toc222169149)

[Gambar 3\.19 Hasil Simulasi Screening Transaksi	43](#_Toc222169150)

[Gambar 3\.20 Perbandingan Performa Tiga Model	45](#_Toc222169151)

[Gambar 4\.1 Perbandingan Performa Model Lain…\.\.\.…………………………\.  45](#_Toc222010946)

# <a id="_Toc222169386"></a>DAFTAR TABEL

[Tabel 2\.1 Penelitian Terdahulu	18](#_Toc222172693)

[Tabel 2\.2 Bahan dan Alat	25](#_Toc222172694)

[Tabel 3\.1 Daftar Atribut dan Tipe Data Dataset	27](#_Toc222172701)

[Tabel 3\.2 Fitur Berbasis Graf	30](#_Toc222172702)

[Tabel 3\.3 Fitur Statistik Nilai Transaksi	31](#_Toc222172703)

[Tabel 3\.4 Fitur Penomoran Mitra Transaksi	32](#_Toc222172704)

[Tabel 3\.5 Fitur Jarak Waktu Antar Transaksi	32](#_Toc222172705)

[Tabel 3\.6 Fitur Pola Waktu dan Perilaku	33](#_Toc222172706)

[Tabel 3\.7 Hasil Pembagian Data Secara Kronologis	34](#_Toc222172707)

[Tabel 3\.8 Analisis Performa Model pada Berbagai Nilai Threshold	37](#_Toc222172708)

[Tabel 3\.9 Detail Confusion Matrix pada Data Uji	38](#_Toc222172709)

[Tabel 3\.10 Performa Model CatBoost pada Setiap Data Split	38](#_Toc222172710)  
[Tabel 4\.1 Perbandingan 3 Model	44](#_Toc222172810)

# <a id="_lr3z30wbj1r7"></a><a id="_Toc222169387"></a>BAB I   
PENDAHULUAN

## <a id="_ma3dprsp6qx"></a><a id="_Toc222169388"></a>1\.1 Latar Belakang Masalah

Pencegahan tindak pidana pencucian uang merupakan tantangan penting dalam menjaga integritas sistem keuangan\. Di Indonesia, upaya pencegahan dan pemberantasan pencucian uang memiliki landasan hukum yang mengatur peran analisis transaksi keuangan, termasuk penanganan transaksi keuangan mencurigakan sebagai bagian dari mekanisme pencegahan tindak pidana\. \[1\]

Seiring perkembangan perbankan digital dan sistem pembayaran elektronik, volume serta kompleksitas transaksi meningkat dan membuka peluang penyalahgunaan transaksi untuk menyamarkan asal\-usul dana\. Dalam praktik pencucian uang, prosesnya sering dijelaskan melalui tiga tahap, yaitu *placement*, *layering*, dan *integration*, yang membuat pola transaksi menjadi semakin berlapis dan sulit ditelusuri jika hanya mengandalkan pemeriksaan manual\. \[2\] 

Pendekatan konvensional yang berbasis aturan sederhana \(misalnya ambang batas nilai/frekuensi\) masih memiliki keterbatasan karena kurang adaptif terhadap pola yang dinamis\. Kondisi ini dapat memicu dua risiko utama yaitu transaksi mencurigakan yang tidak terdeteksi \(*false negative*\) dan transaksi normal yang terindikasi \(*false positive*\)\. Pada kasus seperti ini, pemanfaatan *machine learning* relevan karena mampu mempelajari pola transaksi yang kompleks dan menemukan keterkaitan antara faktor yang tidak mudah dirumuskan menjadi aturan statis\. Selain itu, evaluasi model pada kasus deteksi transaksi mencurigakan perlu memperhatikan ketidakseimbangan kelas, sehingga metrik seperti *precision*, *recall*, dan *F1\-score* lebih informatif dibanding sekadar akurasi\. \[3\]

Penelitian ini menekankan analisis berbasis pola transaksi, seperti frekuensi, nilai transaksi, dan karakteristik waktu transaksi\. Pola perilaku transaksi juga dapat direpresentasikan melalui fitur turunan yang umum digunakan pada analisis transaksi, misalnya konsep *Recency*, *Frequency*, dan *Monetary* \(RFM\) yang sering dipakai untuk menangkap pola perilaku berbasis waktu, intensitas, dan nilai transaksi\. \[4\] 

Dalam konteks pemodelan, penelitian ini menggunakan algoritma CatBoost karena dirancang untuk menangani fitur kategorikal secara efektif serta mengurangi risiko target *leakage* melalui mekanisme *ordered boosting*\. Karakteristik tersebut relevan untuk data transaksi yang umumnya memuat banyak atribut kategorikal \(misalnya jenis transaksi, kanal transaksi, kategori pihak terkait\) dan berpotensi menimbulkan bias apabila diproses tidak tepat\. \[5\]

Adapun prospek pengembangan ke depan dari penelitian ini adalah tersusunnya model deteksi transaksi mencurigakan berbasis pola transaksi yang dapat menjadi landasan dalam pengembangan sistem pendukung analisis anti pencucian uang\. *Outcome* yang diharapkan meliputi peningkatan konsistensi dalam deteksi dini transaksi mencurigakan serta pengurangan ketergantungan pada proses pemeriksaan manual\. Kebaruan penelitian ini terletak pada penerapan algoritma CatBoost dalam mendeteksi transaksi mencurigakan berbasis pola transaksi, dengan memanfaatkan data sintetis sebagai alternatif data yang tetap menjaga aspek privasi\.  
<a id="_tb55oupdcqcm"></a>

## <a id="_Toc222169389"></a>1\.2 Rumusan Masalah

<a id="_2y8t7xyvsu56"></a>Berdasarkan latar belakang dan urgensi penelitian yang telah diuraikan, penelitian ini mengidentifikasi beberapa permasalahan yang perlu untuk diatasi dan dikaji lebih lanjut\. Permasalahan\-permasalahan tersebut dirumuskan dalam pertanyaan penelitian sebagai berikut:

1. <a id="_92owziath9r5"></a>Pola transaksi keuangan yang semakin beragam membuat indikasi transaksi mencurigakan sulit dikenali, sehingga pemeriksaan manual dan aturan ambang batas sering menghasilkan alarm palsu atau transaksi mencurigakan yang terlewat\.
2. <a id="_69d5zjwbmfq0"></a>Data transaksi umumnya memiliki fitur kategorikal dan ketidakseimbangan kelas, sehingga proses klasifikasi transaksi mencurigakan dengan pendekatan yang tidak tepat dapat menurunkan akurasi deteksi dan meningkatkan kesalahan prediksi\.<a id="_dq339atwt29w"></a>
3. Performa deteksi transaksi mencurigakan perlu diukur secara terstandar, sehingga tanpa evaluasi menggunakan *Precision, Recall, dan F1\-Score*, kualitas model yang dibangun sulit dinilai dan dibandingkan\.<a id="_gqzrsughpbp9"></a>

## <a id="_Toc222169390"></a>1\.3 Batasan Masalah

Agar penelitian ini memiliki fokus yang jelas dan pembahasan yang terarah, maka batasan masalah dalam penelitian ini ditetapkan sebagai berikut:

1. Data yang digunakan dalam penelitian ini berupa *dataset* sintetis yang dirancang untuk merepresentasikan karakteristik transaksi keuangan, tanpa menggunakan data transaksi nasabah yang bersifat nyata atau sensitif\.
2. Pola transaksi keuangan yang dianalisis dibatasi pada beberapa atribut utama, yaitu frekuensi transaksi, nilai transaksi, dan aktivitas rekening, tanpa mempertimbangkan informasi identitas pribadi pemilik rekening\.
3. Metode *machine learning* utama yang digunakan dalam penelitian ini adalah algoritma CatBoost, dengan model pembanding dari kajian publik sebagai referensi evaluasi performa\.
4. Evaluasi kinerja model dilakukan menggunakan metrik* Precision*, *Recall*, dan *F1\-Score*\.<a id="_9iztf3z44t7b"></a>

## <a id="_Toc222169391"></a>1\.4 Tujuan Penelitian

<a id="_k3lo8vodgwiy"></a>Berdasarkan rumusan masalah yang telah ditetapkan, penulisan ini memiliki tujuan\-tujuan sebagai berikut:

1. Mengidentifikasi pola transaksi yang sering muncul pada transaksi mencurigakan untuk membantu proses deteksi dan klasifikasi dalam upaya anti pencucian uang\.
2. Mengembangkan dan melatih model klasifikasi menggunakan algoritma *CatBoost* untuk mengklasifikasikan rekening berisiko berdasarkan pola transaksi keuangan yang telah diidentifikasi\.
3. Mengukur dan mengevaluasi performa model *CatBoost* menggunakan metrik* Precision, Recall*, dan *F1\-Score* untuk menilai efektivitasnya dalam mendeteksi transaksi mencurigakan berbasis pola transaksi\.

## <a id="_menu751t779l"></a>

## <a id="_Toc222169392"></a>1\.5 Manfaat Penelitian

Manfaat penelitian ini diharapkan dapat memberikan kontribusi sebagai berikut:

1. Menambah referensi keilmuan di bidang informatika, khususnya penerapan *machine learning* untuk deteksi transaksi mencurigakan\.
2. Memberikan gambaran penerapan Algoritma CatBoost dalam mengolah data transaksi yang memiliki fitur kategorikal dan ketidakseimbangan kelas\.
3. Menjadi acuan awal bagi penelitian selanjutnya dalam pengembangan fitur berbasis pola transaksi untuk meningkatkan kualitas deteksi transaksi mencurigakan\.
4. Mendukung pengembangan sistem analisis transaksi berbasis data yang dapat membantu proses penapisan awal transaksi mencurigakan secara lebih konsisten\.<a id="_dhlzgtpgln9g"></a>

## <a id="_Toc222169393"></a>1\.6 Metode Penelitian

	Penelitian ini menggunakan metode klasifikasi berbasis machine learning untuk membantu mengidentifikasi transaksi yang berpotensi mencurigakan pada sistem anti pencucian uang berdasarkan pola transaksi\. Agar alur pengerjaan jelas dan tertata, penelitian mengikuti kerangka *CRISP\-DM \(Cross Industry Standard Process for Data Mining\)* yang umum digunakan dalam proyek analisis data\. *CRISP\-DM* sendiri terdiri dari enam tahap, yaitu *Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, dan Deployment\.*<a id="_laviyvdcdut5"></a><a id="_borlmknqnwz5"></a><a id="_cdbhcc99tskj"></a><a id="_1b2vhge7drv2"></a><a id="_6pc25qrv3sny"></a>

# <a id="_Toc222169394"></a>BAB II    
LANDASAN METODE                        

## <a id="_plajxp7l360q"></a><a id="_Toc222169395"></a>2\.1 Tahapan Penelitian

Penelitian ini mengadopsi metodologi *Cross\-Industry Standard Process for Data Mining \(CRISP\-DM\)*\. *CRISP\-DM* awalnya dikembangkan pada tahun 1996 oleh konsorsium lima perusahaan, yaitu Integral Solutions Ltd \(ISL\), Teradata, Daimler AG, NCR Corporation, dan OHRA, kemudian disempurnakan melalui serangkaian workshop antara tahun 1997–1999 dengan kontribusi lebih dari 300 organisasi \[6\]\. 

*CRISP\-DM* telah menjadi *de facto standard* dalam pengembangan proyek *data mining* dan *knowledge discovery* \[8\]\. Survei Mariscal et al\. menunjukkan pengguna *CRISP\-DM* mencapai 51% pada tahun 2002, dan survei terbaru dari datascience\-pm pada tahun 2020 masih menempatkannya di posisi teratas dengan 49% responden \[9\]\. Metodologi ini terdiri dari enam tahap utama yang saling terhubung\. 



<a id="_Toc222007374"></a>Gambar 2\.1 Alur Proses Penelitian dengan Metode CRISP\-DM<a id="_Toc222006297"></a> 

### <a id="_Toc222169396"></a>2\.1\.1 *Business Understanding*

	Tahap pertama dan paling fundamental dalam CRISP\-DM yang berfokus pada pemahaman kebutuhan proyek dari perspektif bisnis\. Pada tahap ini dilakukan identifikasi permasalahan yang ingin diselesaikan, penetapan tujuan bisnis beserta kriteria keberhasilannya, penilaian situasi termasuk ketersediaan sumber daya dan analisis risiko, serta penerjemahan tujuan bisnis menjadi tujuan data mining yang terukur\. Hasil dari tahap ini berupa rencana proyek awal yang menjadi acuan bagi seluruh tahap berikutnya \[7\]\.

### <a id="_Toc222169397"></a>2\.1\.2 *Data Understanding*

	Tahap pengumpulan dan eksplorasi data awal untuk mengenali karakteristik, kualitas, dan potensi permasalahan pada data\. Aktivitas yang dilakukan meliputi pengumpulan data dari sumber yang tersedia, pemeriksaan struktur dan atribut data seperti tipe kolom dan jumlah rekaman, eksplorasi data melalui statistik deskriptif dan visualisasi untuk menemukan pola awal, serta verifikasi kualitas data untuk mengidentifikasi permasalahan seperti missing values, outlier, dan inkonsistensi yang perlu ditangani pada tahap selanjutnya \[6\]\.

### <a id="_Toc222169398"></a>2\.1\.3 *Data Preparation*

	Tahap penyiapan adalah proses menyiapkan data supaya siap dipakai untuk membuat model, dan biasanya paling banyak memakan waktu dalam proyek data *mining*\. Kegiatannya meliputi: memilih bagian data yang benar\-benar dibutuhkan, membersihkan data dengan memperbaiki atau menghapus nilai yang keliru, membuat fitur baru dari informasi yang sudah ada \(*feature engineering*\), menggabungkan data dari beberapa sumber menjadi satu *dataset* yang rapi dan *nyambung*, serta mengatur format data agar cocok dengan kebutuhan algoritma\. Tahap ini biasanya dilakukan berulang karena saat membangun model bisa muncul masalah baru yang mengharuskan data diperbaiki lagi \[9\]\.

### <a id="_Toc222169399"></a>2\.1\.4 *Modeling*

Tahap pemilihan dan penerapan teknik pemodelan yang sesuai dengan tujuan data *mining*\. Pada tahap ini dilakukan pemilihan algoritma yang akan digunakan \(misalnya *klasifikasi, clustering, *atau* regresi*\), perancangan desain pengujian termasuk pembagian data menjadi set pelatihan dan pengujian, pembangunan model menggunakan data yang telah disiapkan, serta penilaian awal terhadap performa model secara teknis\. Apabila hasil penilaian menunjukkan perlunya penyesuaian data, proses dapat kembali ke tahap Data Preparation \[7\]\.

### <a id="_Toc222169400"></a>2\.1\.5 Evaluation

Tahap evaluation merupakan proses penilaian model secara menyeluruh untuk memastikan bahwa hasil yang diperoleh telah memenuhi kriteria keberhasilan yang ditetapkan pada tahap *Business* *Understanding*\. Berbeda dengan evaluasi teknis pada fase *Modeling*, pada tahap ini penilaian difokuskan untuk melihat apakah model benar\-benar mampu menjawab permasalahan bisnis yang telah dirumuskan\. Kegiatan yang dilakukan meliputi membandingkan hasil model dengan kriteria keberhasilan bisnis, meninjau kembali seluruh tahapan proses agar tidak ada langkah yang terlewat, serta menentukan tindak lanjut yang diperlukan, yaitu melanjutkan ke tahap *deployment*, melakukan iterasi perbaikan, atau menggunakan pendekatan lain \[7\]\.

### <a id="_Toc222169401"></a>2\.1\.6 *Deployment*

<a id="_Toc222169402"></a>Tahap *deployment* merupakan tahap akhir yang berfokus pada penerapan hasil analisis agar dapat digunakan secara praktis\. Ruang lingkup *deployment* dapat berbeda\-beda, mulai dari penyusunan laporan dan rekomendasi, hingga implementasi model prediksi secara penuh pada lingkungan produksi\. Aktivitas pada tahap ini meliputi perencanaan penerapan model, penyusunan strategi pemantauan dan pemeliharaan, penyusunan laporan akhir, serta peninjauan proyek secara menyeluruh\. Model yang sudah diterapkan perlu dipantau secara berkala karena karakteristik data dapat berubah dari waktu ke waktu, sehingga model mungkin perlu dilakukan pembaruan atau pelatihan ulang \[6\]\.

## 2\.2 Penelitian Terdahulu

Tabel 2\.1<a id="_Toc222172693"></a>  Penelitian Terdahulu

No

Peneliti

Judul Penelitian

Metode

Hasil Utama

Relevansi

1

Yang et al\. \(2024\)

An Explainable Machine Learning Model in Predicting Vaginal Birth After Cesarean Section

CatBoost, XGBoost, LightGBM, Random Forest

CatBoost terbaik dengan AUC 0\.767 internal, 0\.707 eksternal

Demonstrasi keunggulan CatBoost untuk data dengan fitur campuran

2

Kadir \(2024\)

Analisis Performa Metode Random Forest dan CatBoost dalam Pemodelan Kualitas Udara Kota Palembang

Random Forest dan CatBoost dengan optimasi parameter

CatBoost lebih unggul dengan akurasi 96\.28% dan RMSE 0\.56348

Konfirmasi efektivitas CatBoost dalam menangani data kompleks dengan multiple variabel

3

Syukur \(2024\)

Prediksi Indeks Kualitas Udara Menggunakan Metode CatBoost

CatBoost dengan GridSearchCV untuk optimasi parameter

Akurasi terbaik 97% pada pembagian data 90:10

Metodologi optimasi hyperparameter yang dapat diadaptasi

4

Hanjani \(2024\)

Prediksi Kadar Polutan Indikator Kualitas Udara di Pekanbaru Menggunakan CatBoost

CatBoost dengan preprocessing komprehensif

RMSE 10\.93, MAE 8\.65 pada PM2\.5

Metodologi preprocessing dan penanganan missing value/outlier

5

Altman et al\. \(2024\)

Realistic Synthetic Financial Transactions for Anti\-Money Laundering Models

LightGBM, XGBoost, GNN dengan Graph Feature Preprocessor

XGBoost dan LightGBM dengan fitur graf memberikan performa kuat

Sumber dataset utama; pola transaksi \(*fan\-in, fan\-out, cycles*\)\.

6

Ramineni & Mastouri \(2025\)

Credit Card Fraud Detection Using CatBoost

CatBoost, LightGBM, Gradient Boosting dengan SMOTE

CatBoost terbaik: akurasi 0\.998, F1\-score 0\.8103, AUC 0\.9971

Teknik penanganan imbalance \(SMOTE\); keunggulan CatBoost untuk data transaksi

7

Pratama & Wahid \(2025\)

Fraudulent Transaction Detection in Online Systems Using Random Forest and Gradient Boosting

Random Forest dan Gradient Boosting dengan fitur rekayasa

Precision 0\.96, Recall 0\.92, F1\-Score 0\.94

Konsep rekayasa fitur rasio; analisis jenis transaksi untuk deteksi anomali

8

Florek & Zagdański \(2025\)

Benchmarking State\-of\-the\-Art Gradient Boosting Algorithms for Classification

GBM, XGBoost, LightGBM, CatBoost dengan TPE dan randomized search

CatBoost kuat tanpa tuning; LightGBM meningkat setelah tuning

Justifikasi pemilihan CatBoost untuk data kompleks tanpa tuning ekstensif

Berdasarkan tinjauan terhadap literatur sebelumnya, penelitian ini  mengadaptasi metodologi deteksi transaksi mencurigakan yang mengombinasikan algoritma *CatBoost* dengan teknik *feature engineering* berbasis pola transaksi\. Metode ini dipilih karena kemampuannya dalam menangani klasifikasi transaksi pada data keuangan yang memiliki fitur *kategorikal* dominan dan ketidakseimbangan kelas ekstrem, sebagaimana telah dibuktikan efektivitasnya dalam berbagai penelitian terdahulu\.

Metode ini melibatkan penerapan *Cross\-Industry Standard Process for Data Mining \(CRISP\-DM\)* untuk mengidentifikasi pola transaksi mencurigakan dalam dataset IBM AML Transactions\. Dimulai dari pemahaman bisnis terkait tipologi pencucian uang, pemahaman karakteristik data transaksi, preprocessing data, rekayasa fitur berbasis pola \(fan\-in, fan\-out, scatter\-gather, cycles\), pemodelan dengan CatBoost, dan terakhir evaluasi menggunakan metrik F1\-Score dan AUC\-PR\. Analisis ini menggunakan model machine learning CatBoost untuk mengklasifikasikan transaksi sebagai normal atau mencurigakan\.

## <a id="_Toc222169403"></a>2\.3 Tinjauan Pustaka

### <a id="_4jaup23tw3di"></a><a id="_Toc222169404"></a>2\.3\.1 Anti Pencucian Uang

Pencucian uang \(*money laundering*\) merupakan proses menyamarkan asal\-usul uang yang diperoleh dari aktivitas ilegal agar tampak berasal dari sumber yang sah \[2\]\. Fenomena ini menjadi perhatian serius dalam sistem keuangan global karena berpotensi merusak integritas lembaga keuangan dan memfasilitasi berbagai tindak pidana lainnya\. Di berbagai negara, termasuk Indonesia melalui Undang\-Undang Nomor 8 Tahun 2010 \[1\], telah diberlakukan regulasi yang mengatur mekanisme deteksi, pelaporan, dan penanganan transaksi keuangan mencurigakan, termasuk kebijakan pemblokiran rekening sebagai upaya pencegahan\.

Kepli menjelaskan bahwa proses pencucian uang umumnya terdiri dari tiga tahap utama \[2\]:

- 
	- 
		- 
			1. *Placement*: Tahap penempatan dana ilegal ke dalam sistem keuangan formal, misalnya melalui penyetoran tunai dalam jumlah kecil \(*structuring/smurfing*\) untuk menghindari pelaporan\.
			2. *Layering*: Tahap pelapisan melalui serangkaian transaksi kompleks untuk memutus jejak audit dan menyamarkan asal\-usul dana\. Tahap ini sering melibatkan transfer antar rekening, antar bank, atau antar negara\.
			3. *Integration*: Tahap integrasi di mana dana yang telah "dibersihkan" dimasukkan kembali ke dalam ekonomi legal melalui investasi, pembelian aset, atau aktivitas bisnis\.

Kebijakan pemblokiran rekening merupakan salah satu instrumen penting dalam upaya pencegahan pencucian uang\. Pemblokiran dapat dilakukan berdasarkan analisis transaksi yang menunjukkan indikasi aktivitas mencurigakan, seperti:

1. Transaksi dengan nilai tidak wajar dibandingkan profil nasabah
2. Pola transaksi yang tidak sesuai dengan aktivitas bisnis yang dinyatakan
3. Transaksi berulang dengan pola tertentu yang mengindikasikan structuring
4. Transaksi dengan pihak\-pihak yang termasuk dalam daftar pantauan

### <a id="_Toc222169405"></a>2\.3\.2 Dataset IBM AML *Transactions*

            Ketersediaan data berlabel untuk penelitian deteksi pencucian uang merupakan tantangan utama karena data transaksi riil bersifat rahasia dan label target\-nya banyak transaksi *laundering* yang tidak pernah terdeteksi \[12\]\. Untuk mengatasi hal tersebut, Altman et al\. \[12\] mengembangkan sebuah generator transaksi keuangan sintetis berbasis *multi\-agent virtual world* yang menghasilkan *dataset* dengan label ground truth yang lengkap dan akurat\.

            Dataset IBM AML Transactions mensimulasikan seluruh tahapan pencucian uang, mulai dari *placement* \(penempatan\), *layering* \(pelapisan\), dan *integration* \(integrasi\)\. serta menghasilkan data transaksi dari berbagai entitas, seperti individu, perusahaan, dan bank, dengan karakteristik yang disesuaikan menggunakan statistik yang merepresentasikan kondisi dunia nyata \[12\]\. Keunggulan utama dataset sintetis ini dibandingkan data transaksi riil adalah kelengkapan label, dimana setiap transaksi diberi penanda legal/ilegal sekaligus dilacak hingga alur pergerakan dananya, hal yang umumnya sangat sulit atau hampir tidak mungkin dilakukan pada data riil\.

### <a id="_Toc222169406"></a>2\.3\.3 Pola Transaksi Pencucian Uang

*Dataset IBM AML Transactions *memodelkan delapan pola pencucian uang yang umum digunakan oleh pelaku untuk menyamarkan asal\-usul dana \[12\]\. Kedelapan pola tersebut diilustrasikan sebagai berikut:



<a id="_Toc222007375"></a>Gambar 2\.2 Model Pola Pencucian Uang \[12\]

1. *Fan\-out*

Satu rekening pengirim \(v\) mengirimkan dana ke rekening lain  yang berbeda\. Pola ini merepresentasikan tahap penyebaran dana \(*layering*\) untuk mengaburkan sumber dana\.

1. *Fan\-in*

Banyak rekening pengirim mengirimkan dana ke satu rekening penerima \(v\)\. Pola ini merepresentasikan tahap pengumpulan dana \(*integration*\) di mana dana dari berbagai sumber dikumpulkan kembali\.

1. *Gather\-Scatter*

Kombinasi *fan\-in* dan *fan\-out* pada satu rekening yang sama \(v\)\. Rekening v menerima dana dari banyak sumber kemudian menyebarkannya ke banyak tujuan, berfungsi sebagai titik transit pencucian uang\.

1. *Scatter\-Gather*

Satu rekening pengirim \(v\) menyebarkan dana ke beberapa rekening perantara, yang kemudian mengalirkan dana tersebut ke satu rekening penerima \(u\)\. Pola ini melibatkan rekening perantara yang sama pada sisi penyebaran dan pengumpulan\.

1. *Simple Cycle*

Rangkaian transaksi yang membentuk siklus tertutup — dana yang dikirim dari satu rekening akhirnya kembali ke rekening asal melalui serangkaian rekening perantara\. Keberadaan siklus merupakan indikator kuat pencucian uang karena pelaku berusaha "membersihkan" dana melalui aliran berputar\.

1. *Random*

Serupa dengan *cycle* tetapi dana tidak kembali ke rekening asal\. Pola ini merepresentasikan perpindahan dana acak antar rekening yang dimiliki atau dikendalikan oleh pelaku, termasuk melalui perusahaan cangkang \(*shell companies*\)\.

1. *Bipartite*

Dana dipindahkan dari sekumpulan rekening *input* ke sekumpulan rekening *output* melalui transaksi yang menghubungkan kedua kelompok tersebut\. Pola ini menyerupai struktur *layering* berlapis\.

1. *Stack*

Perluasan dari pola *bipartite* dengan menambahkan lapisan perantara tambahan, sehingga membentuk struktur berlapis\-lapis yang lebih kompleks dan sulit ditelusuri\.

             Pada seluruh pola di atas, pelaku pencucian uang menguasai atau mengendalikan semua rekening \(node\) yang terlibat, baik secara langsung maupun melalui perusahaan cangkang \[12\]\.

### <a id="_Toc222169407"></a>2\.3\.4 CatBoost

	CatBoost \(Categorical Boosting\) merupakan algoritma gradient boosting yang diperkenalkan pada tahun 2017\. Prokhorenkova et al\. menjelaskan bahwa CatBoost memiliki dua inovasi utama \[5\]\. Pertama, ordered target encoding yang menangani fitur kategorikal dengan menghitung statistik target secara sekuensial berdasarkan urutan data, sehingga menghindari kebocoran informasi target yang umum terjadi pada metode encoding tradisional\. Kedua, ordered boosting yang menggunakan subset data berbeda untuk setiap observasi dalam penghitungan gradien, sehingga mengurangi bias prediksi dan meningkatkan kemampuan generalisasi model\.

	Keunggulan tersebut menjadikan CatBoost relevan untuk analisis data transaksi finansial yang umumnya memiliki proporsi fitur kategorikal tinggi dan bersifat sekuensial\. Algoritma ini juga dilengkapi kemampuan bawaan untuk menangani nilai yang hilang serta mekanisme regularisasi yang mengurangi risiko overfitting\. Efektivitas CatBoost telah divalidasi dalam berbagai penelitian, di antaranya Yang et al\. yang menunjukkan keunggulan CatBoost dengan AUC 0\.767 dibandingkan enam algoritma lainnya \[10\], serta Kadir yang melaporkan akurasi CatBoost sebesar 96\.28% dibandingkan Random Forest 94\.88% \[11\]\.

Representasi Matematis CatBoost

Model CatBoost dapat direpresentasikan sebagai model aditif:

di mana    merupakan pohon keputusan pada iterasi ke\-t, dan T menyatakan jumlah iterasi\.

Fungsi objektif yang diminimalkan:

dengan   adalah label aktual,    adalah prediksi model, dan  adalah fungsi loss \(misalnya log loss untuk klasifikasi biner\)\.  


### <a id="_5dod2g2fadtz"></a><a id="_Toc222169408"></a>2\.3\.5 *Confusion Matrix*

		*Confusion matrix* adalah tabel evaluasi yang menunjukkan perbandingan antara label aktual \(*ground truth*\) dan label prediksi model pada kasus klasifikasi\. Untuk klasifikasi biner \(misalnya: transaksi normal vs *laundering*\), *confusion matrix* berbentuk matriks 2×2 sebagai berikut: 



<a id="_Toc222007376"></a>Gambar 2\.3 Ilustrasi Confusion Matrix untuk Klasifikasi Biner \[7\]

 

Keterangan:

1. TP \(*True Positive*\): transaksi laundering yang berhasil terdeteksi sebagai laundering\.
2. TN \(*True Negative*\): transaksi normal yang berhasil terdeteksi sebagai normal\.
3. FP \(*False Positive*\): transaksi normal yang salah terdeteksi sebagai *laundering* \(*false alarm*\)\.
4. FN \(*False Negative*\): transaksi laundering yang salah terdeteksi sebagai normal \(laundering lolos\)\.



      Dalam konteks anti\-money laundering, kesalahan FN umumnya lebih berisiko karena transaksi laundering tidak terdeteksi, sedangkan FP menambah beban investigasi karena menghasilkan alert yang tidak valid\.

### <a id="_bpl3k2c0v05z"></a><a id="_Toc222169409"></a>2\.3\.6 Matrik Evaluasi

Pada data transaksi AML, distribusi kelas umumnya tidak seimbang \(imbalanced\) sehingga metrik seperti accuracy saja sering kurang representatif\. Oleh karena itu, penelitian ini menggunakan beberapa metrik evaluasi yang dihitung berdasarkan nilai  

## <a id="_Toc222169410"></a>2\.4 Metode

### <a id="_Toc222169411"></a>2\.4\.1 Waktu dan Lokasi Penelitian

Penelitian ini dilaksanakan pada periode Januari \- Februari 2026 di Batam\. Pengumpulan data, pengembangan model, dan eksperimen dilakukan secara virtual menggunakan infrastruktur komputasi berbasis cloud\.

### <a id="_Toc222169412"></a>2\.4\.2 Bahan dan Alat Penelitian

<a id="_Toc222172694"></a>Tabel 2\.2 Bahan dan Alat

Komponen

Spesifikasi

Dataset

IBM AML Transactions, Menggunakan Versi HI\-Small

Bahasa Pemrograman

Python 3\.10

Algoritma Utama

*CatBoost Classifier*

Library Pendukung

Pandas, NumPy, Scikit\-learn, Matplotlib, Seaborn

Platform

Jupyter Notebook

Metrik Evaluasi

Precision, Recall, F1\-Score, AUC\-PR, Confusion Matrix

# <a id="_Toc222169413"></a>BAB III   
IMPLEMENTASI METODE USULAN

## <a id="_d6bhzmbz871e"></a><a id="_Toc222169414"></a>3\.1 Business *Understanding*

Masalah utama yang diangkat dalam penelitian ini adalah rendahnya kemampuan deteksi transaksi pencucian uang pada sistem keuangan\. Untuk menjelaskan kenapa masalah tersebut terjadi, berikut diuraikan faktor\-faktor penyebabnya:

- 
	- 
		- 
			1. Faktor Data \(Material\): Volume transaksi keuangan yang sangat besar dengan rasio transaksi mencurigakan yang sangat kecil \(kurang dari 0,1%\) menyebabkan pola pencucian uang tenggelam di antara jutaan transaksi normal\. Data yang sangat tidak seimbang ini menyulitkan proses identifikasi secara konvensional\.
			2. Faktor Metode \(Method\): Pendekatan berbasis aturan \(rule\-based\) yang umum digunakan oleh institusi keuangan cenderung kurang efektif karena aturan statis tidak mampu mengikuti pola pencucian uang yang terus berkembang dan semakin kompleks, seperti pola fan\-out, fan\-in, scatter\-gather, dan cycle\.
			3. Faktor Analisis \(Man\): Proses investigasi transaksi mencurigakan yang masih mengandalkan verifikasi manual membutuhkan waktu dan sumber daya yang besar, terutama ketika jumlah alarm palsu \(false positive\) sangat tinggi sehingga membebani tim kepatuhan \(compliance\)\.
			4. Faktor Akurasi \(Measurement\): Metrik evaluasi yang tidak tepat dapat memberikan gambaran performa yang menyesatkan\. Pada data yang sangat tidak seimbang, akurasi keseluruhan menjadi tidak relevan karena model yang memprediksi semua transaksi sebagai normal tetap memperoleh akurasi di atas 99%\.
			5. Faktor Teknologi \(Machine\): Kurangnya penerapan algoritma machine learning modern yang mampu menangani fitur kategorikal, ketidakseimbangan kelas, dan pola temporal secara bersamaan dalam satu kerangka kerja\.

Berdasarkan analisis permasalahan di atas, penelitian ini bertujuan membangun model deteksi transaksi mencurigakan menggunakan algoritma CatBoost dengan pendekatan feature engineering berbasis pola transaksi\. Berikut kebutuhan yang diidentifikasi pada tahap ini:

1. Membantu proses screening awal transaksi mencurigakan sehingga departement terkait dapat memprioritaskan investigasi pada transaksi yang benar\-benar berisiko tinggi\.
2. Menghasilkan model klasifikasi yang mampu membedakan transaksi normal dan transaksi laundering dengan tingkat deteksi yang tinggi\.
3. Data yang dibutuhkan: Dataset transaksi keuangan berlabel yang mencakup informasi pengirim, penerima, nominal, waktu, dan format pembayaran\.
4. Algoritma yang digunakan: CatBoost, dipilih karena kemampuannya menangani fitur kategorikal dan data tidak seimbang secara langsung \[13\]\.

## <a id="_Toc222169415"></a>3\.2 Implementasi Data Understanding

### <a id="_Toc222169416"></a>3\.2\.1 Deskripsi Dataset

Penelitian menggunakan dataset IBM AML Transactions varian HI\-Small \(High Illicit \- Small\) yang dikembangkan oleh Altman et al\. \[12\] sebagai *benchmark* deteksi AML\. *Dataset* transaksi ini memiliki atribut berikut: 

 

<a id="_Toc222172701"></a>Tabel 3\.1 Daftar Atribut dan Tipe Data Dataset

Atribut

Tipe Data

Deskripsi

Timestamp

Datetime

Waktu terjadinya transaksi

From Bank

Kategorikal

Bank pengirim

To Bank

Kategorikal

Bank penerima

Account

Kategorikal

Rekening pengirim

Account\.1

Kategorikal

Amount Received

Numerik

Nilai transaksi diterima

Amount Paid

Numerik

Nilai transaksi dibayarkan

Receiving Currency

Kategorikal

Mata uang penerima

Payment Currency

Kategorikal

Mata uang pembayaran

Payment Format

Kategorikal

Format pembayaran \(ACH, Wire, Cheque, dll\.\)

Is Laundering

Binary

Label \(0: Normal, 1: Mencurigakan\)

### <a id="_Toc222169417"></a>3\.2\.2 Pemuatan dan Pra\-pemrosesan Data

Data mentah dimuat dari berkas CSV dan diproses secara langsung dalam pipeline pra\-pemrosesan\. Tahapan yang dilakukan meliputi:

1. Parsing timestamp, Konversi format YYYY/MM/DD HH:MM menjadi nilai numerik relatif \(detik sejak transaksi pertama\) untuk memudahkan komputasi fitur temporal\.
2. Encoding akun, Penggabungan kolom Bank \+ Account menjadi integer ID unik menggunakan dictionary mapping\. Hal ini menghasilkan identifikasi akun yang unik lintas bank\.
3. Encoding kategorikal, Mata uang \(currency\) dan format pembayaran \(payment format\) di\-encode menjadi integer ID\.
4. Pengurutan kronologis, Data diurutkan berdasarkan timestamp untuk menjaga integritas temporal\.

**

<a id="_Toc222169132"></a>Gambar 3\.1 Kode Pra\-pemrosesan Data dan Encoding Atribut

### <a id="_Toc222169418"></a>3\.2\.3 Eksplorasi Data

Dataset memiliki 5\.078\.345 transaksi dengan distribusi kelas yang sangat tidak seimbang: Kelas jumlah proporsi  legitimate \(kelas 0\) 5\.073\.168 99,90%  illicit \(kelas 1\) 5\.177 0,10%  imbalance ratio  1:979  

Rasio ketidakseimbangan 1:979 menunjukkan bahwa kurang dari 1 dari setiap 1\.000 transaksi merupakan transaksi mencurigakan, mencerminkan kondisi realistis dalam data aml\.



<a id="_Toc222169133"></a>Gambar 3\.2 Distribusi Kelas Transaksi pada Dataset IBM AML Transactions HI\-Small

<a id="_Toc222006300"></a> 

## <a id="_Toc222169419"></a>3\.3 Implementasi Data Preparation

Tahap persiapan data dalam penelitian ini mencakup tiga aktivitas utama: normalisasi data, rekayasa fitur berbasis pola transaksi, serta pembagian data secara kronologis\.

### <a id="_Toc222169420"></a>3\.3\.1 Normalisasi Timestamp

Timestamp dinormalisasi secara relatif terhadap nilai minimum sehingga dimulai dari 0, memudahkan komputasi fitur temporal:



<a id="_Toc222169134"></a>Gambar 3\.3 Kode Normalisasi Timestamp

### <a id="_Toc222169421"></a>3\.3\.2 Rekayasa Fitur \(Feature Engineering\)

Fitur\-fitur dirancang untuk menangkap pola\-pola pencucian uang dari data tabular\. Seluruh perhitungan menggunakan operasi groupby yang efisien\. Total 59 fitur dihasilkan dari 6 kategori:

#### 3\.3\.2\.1 Fitur Berbasis Graf \(Graph\-based Features\)

Fitur ini menangkap pola topologi jaringan transaksi, termasuk degree \(jumlah koneksi\), diversitas neighbor, dan rasio fan\-out/fan\-in yang mengindikasikan pola layering:



<a id="_Toc222169135"></a>Gambar 3\.4 Kode Rekayasa Fitur Berbasis Graf

<a id="_Toc222172702"></a>Tabel 3\.2 Fitur Berbasis Graf

Fitur

Deskripsi

from\_out\_degree, to\_in\_degree

Jumlah transaksi keluar dan masuk per akun

from\_in\_degree, to\_out\_degree

Jumlah transaksi masuk milik si pengirim, dan keluar milik si penerima

from\_total\_degree, to\_total\_degree

Total seluruh transaksi per akun

from\_degree\_ratio, to\_degree\_ratio

Perbandingan antara jumlah kirim vs terima

from\_unique\_neighbors, to\_unique\_neighbors

Jumlah mitra transaksi yang berbeda\-beda per akun

from\_neighbor\_diversity, to\_neighbor\_diversity

Proporsi mitra unik dibanding total transaksi

fanout\_fanin\_ratio

Rasio fan\-out vs fan\-in

#### <a id="_wj9dv6203qab"></a>3\.3\.2\.2 Fitur Statistik Nilai Transaksi

Fitur ini mengukur pola nilai uang yang ditransaksikan oleh setiap akun\. Idenya adalah: setiap akun memiliki kebiasaan transaksi tertentu \(misalnya rata\-rata Rp 1 juta\)\. Jika tiba\-tiba ada transaksi Rp 50 juta dari akun tersebut, nilainya sangat menyimpang dari kebiasaan hal ini diukur menggunakan skor penyimpangan \(z\-score\)\.

____

<a id="_Toc222169136"></a>Gambar 3\.5 Kode Rekayasa Fitur Statistik Nilai Transaksi

<a id="_Toc222172703"></a>Tabel 3\.3 Fitur Statistik Nilai Transaksi

Fitur

Deskripsi

from\_amt\_mean/std/min/max/sum/median

Rata\-rata, simpangan baku, minimum, maksimum, total, dan median nilai transaksi per akun pengirim

to\_amt\_mean/std/min/max/sum/  
median

Statistik yang sama untuk akun penerima

amount\_diff, amount\_ratio

Selisih dan perbandingan antara jumlah yang dikirim dan diterima

from\_amt\_zscore, to\_amt\_zscore

Skor penyimpangan: mengukur seberapa jauh nilai transaksi ini dari kebiasaan normal akun tersebut\.

from\_amt\_frac, to\_amt\_frac

Proporsi nilai transaksi ini terhadap total volume seluruh transaksi akun

log\_amount\_paid, log\_amount\_received

Nilai transaksi yang di\-logaritma\-kan agar distribusi lebih merata dan mudah diproses model

cross\_amt\_ratio

Perbandingan rata\-rata nilai transaksi pengirim dengan rata\-rata nilai transaksi penerima

#### 3\.3\.2\.3 Fitur Penomoran Mitra Transaksi \(Port Numbering\)

Terinspirasi dari pendekatan Multi\-GNN \[12\], fitur ini memberikan nomor urut kepada setiap mitra transaksi baru berdasarkan waktu kemunculan pertamanya\. Misalnya, jika akun A pertama kali menerima transfer dari akun X, maka X diberi nomor 0\. Ketika akun A kemudian menerima dari akun Y \(mitra baru\), Y diberi nomor 1, dan seterusnya\. Nomor urut yang tinggi menunjukkan bahwa akun tersebut terus menambah mitra transaksi baru\. pola yang umum dalam pencucian uang\. 

____

<a id="_Toc222169137"></a>Gambar 3\.6 Kode Rekayasa Fitur Penomoran Mitra \(Port Numbering\)

<a id="_Toc222172704"></a>Tabel 3\.4 Fitur Penomoran Mitra Transaksi

Fitur

Deskripsi

in\_port

Nomor urut mitra pengirim yang pernah mengirim ke akun penerima ini

out\_port

Nomor urut mitra penerima yang pernah menerima dari akun pengirim ini

#### 3\.3\.2\.4 Fitur Jarak Waktu Antar Transaksi

Fitur ini mengukur berapa lama jeda waktu antara satu transaksi dengan transaksi berikutnya pada akun yang sama\. Jika sebuah akun tiba\-tiba melakukan banyak transaksi dalam waktu singkat \(jeda waktu sangat kecil\), ini bisa mengindikasikan aktivitas mencurigakan seperti pengiriman dana bertubi\-tubi\.



<a id="_Toc222169138"></a>Gambar 3\.7 Kode Rekayasa Fitur Jarak Waktu Antar Transaksi

<a id="_Toc222172705"></a>Tabel 3\.5 Fitur Jarak Waktu Antar Transaksi

Fitur

Deskripsi

in\_time\_delta

Jeda waktu \(dalam detik\) antara transaksi masuk berurutan pada akun penerima

out\_time\_delta

Jeda waktu \(dalam detik\) antara transaksi keluar berurutan dari akun pengirim

#### 3\.3\.2\.5 Fitur Pola Waktu dan Perilaku Transaksi

Fitur ini menangkap kebiasaan dan pola perilaku transaksi, seperti: jam berapa transaksi terjadi, seberapa sering dua akun yang sama saling bertransaksi, apakah nilai transaksi berupa angka bulat \(umum dalam pencucian uang\), dan apakah transaksi dilakukan ke diri sendiri\. 

____

<a id="_Toc222169139"></a>Gambar 3\.8 Kode Rekayasa Fitur Pola Waktu dan Perilaku

<a id="_Toc222172706"></a>Tabel 3\.6 Fitur Pola Waktu dan Perilaku

Fitur

Deskripsi

day, hour

Hari ke berapa dan jam berapa transaksi terjadi

hour\_sin, hour\_cos

Representasi jam secara melingkar agar model memahami bahwa jam 23 dan jam 0 berdekatan

is\_self\_tx

Penanda apakah transaksi dikirim ke akun sendiri \(bernilai 1 jika ya\)

same\_currency

Penanda apakah mata uang pengiriman dan penerimaan sama

from\_avg\_daily\_tx, to\_avg\_daily\_tx

Rata\-rata jumlah transaksi per hari untuk masing\-masing akun

pair\_tx\_count

Berapa kali pasangan pengirim\-penerima yang sama pernah bertransaksi

pair\_amt\_mean, pair\_amt\_sum

Rata\-rata dan total nilai transaksi untuk pasangan akun tertentu

is\_repeat\_pair

Penanda apakah pasangan pengirim\-penerima ini pernah bertransaksi sebelumnya

is\_round\_amount

Penanda apakah nilai transaksi berupa angka bulat \(kelipatan 100 atau 1\.000\)

### <a id="_Toc222169422"></a>3\.3\.3 Pembagian Data Kronologis

Data dibagi secara kronologis berbasis hari — bukan secara acak — agar model dilatih pada transaksi masa lalu dan dievaluasi pada transaksi masa depan\. Pendekatan ini sesuai dengan Altman et al\. \[12\] dan mencegah data leakage temporal\. Algoritma pembagian mencari kombinasi hari yang menghasilkan proporsi paling optimal mendekati rasio 60:20:20:

____

<a id="_Toc222169140"></a>Gambar 3\.9 Kode Pembagian Data Kronologis

<a id="_Toc222172707"></a>Tabel 3\.7 Hasil Pembagian Data Secara Kronologis

Split

Jumlah

Proporsi

Mencurigakan

Rasio Mencurigakan

Training

3\.248\.921

64,0%

2\.530

0,08%

Validation

965\.524

19,0%

1\.036

0,11%

Test

863\.900

17,0%

1\.611

0,19%

Perlu dicatat bahwa rasio transaksi mencurigakan meningkat pada split di hari\-hari terakhir \(0,08% menjadi 0,19%\), menunjukkan distribusi yang tidak seragam dan menambah tantangan prediksi pada data uji\.

## <a id="_Toc222169423"></a>3\.4 Implementasi Modeling

Tahap pemodelan merupakan inti dari proses CRISP\-DM, di mana data yang telah dipersiapkan digunakan untuk membangun model prediktif\. Pada penelitian ini, implementasi pemodelan mencakup tiga aspek utama: pemilihan algoritma yang sesuai dengan karakteristik data AML, strategi penanganan ketidakseimbangan kelas yang ekstrem, serta konfigurasi dan pelatihan model dengan hyperparameter yang dioptimalkan\.

### <a id="_Toc222169424"></a>3\.4\.1 Pemilihan Algoritma

Algoritma CatBoost dipilih berdasarkan beberapa pertimbangan yang relevan dengan karakteristik data AML:

1. Penanganan fitur kategorikal native, CatBoost menggunakan target statistics dan ordered boosting untuk memproses fitur kategorikal secara langsung tanpa encoding tambahan, yang menyederhanakan alur kerja pada data transaksi\.
2. Ordered boosting, Mekanisme yang menghitung statistik secara sekuensial sehingga mengurangi risiko target leakage, penting untuk data temporal\.
3. Regularisasi internal,  Mencegah overfitting pada data dengan distribusi kelas tidak seimbang\.
4. Performa pada data imbalanced, Mendukung scale\_pos\_weight yang memungkinkan kontrol bobot kelas positif secara eksplisit \[13\]\.

### <a id="_Toc222169425"></a>3\.4\.2 Penanganan Ketidakseimbangan Kelas

Karena transaksi mencurigakan sangat jarang \(hanya 1 dari setiap 979 transaksi\), model perlu diberi petunjuk agar lebih memperhatikan kelas minoritas 



<a id="_Toc222169141"></a>Gambar 3\.10 Kode Penanganan Ketidakseimbangan Kelas

### <a id="_Toc222169426"></a>3\.4\.3 Konfigurasi dan Pelatihan Model

Setelah menentukan strategi penanganan ketidakseimbangan kelas, langkah selanjutnya adalah mengkonfigurasi hyperparameter model CatBoost dan melakukan pelatihan\. 

Konfigurasi hyperparameter dirancang untuk menyeimbangkan antara kapasitas model dalam menangkap pola kompleks dan pencegahan overfitting, khususnya mengingat distribusi kelas yang sangat tidak seimbang\. Proses pelatihan menggunakan mekanisme early stopping yang memantau metrik F1\-Score pada data validasi untuk menentukan titik berhenti optimal\.



<a id="_Toc222169142"></a>Gambar 3\.11 Kode Konfigurasi Hyperparameter dan Pelatihan Model

## <a id="_Toc222169427"></a>3\.5 Implementasi Evaluation

### <a id="_Toc222169428"></a>3\.5\.1 Optimasi Threshold 

Pada data yang sangat tidak seimbang, threshold default 0,5 tidak optimal\. Dilakukan pencarian threshold terbaik pada data validasi yang memaksimalkan F1\-Score:



<a id="_Toc222169143"></a>Gambar 3\.12 Kode Optimasi Threshold untuk Maksimasi F1\-Score

__ __

Threshold optimal yang ditemukan adalah 0,67, lebih tinggi dari default 0,5\. Threshold yang lebih tinggi meningkatkan Precision \(mengurangi false positive\) dengan pengorbanan sedikit pada Recall\. 



<a id="_Toc222169144"></a>Gambar 3\.13 Analisis Dampak Threshold pada Precision, Recall, dan F1\-Score

          Gambar 3\.13 menunjukkan trade\-off antara Precision dan Recall pada berbagai nilai threshold\. Titik optimal \(★\) berada pada threshold = 0,67 yang menghasilkan F1\-Score tertinggi\.

<a id="_Toc222172708"></a>Tabel 3\.8 Analisis Performa Model pada Berbagai Nilai Threshold

Threshold

F1\-Score

Precision

Recall

0,30

0,4732

0,3366

0,7964

0,40

0,5619

0,4492

0,7498

0,50

0,6383

0,5909

0,6940

0,67

0,7140

0,8770

0,6021

0,70

0,7143

0,9147

0,5860

0,80

0,6710

0,9821

0,5096

0,90

0,5686

1,0000

0,3973

### <a id="_Toc222169429"></a>3\.5\.2 Confusion Matrix



<a id="_Toc222169145"></a>Gambar 3\.14 Confusion Matrix pada Ketiga Split Data

<a id="_Toc222172709"></a>Tabel 3\.9 Detail Confusion Matrix pada Data Uji

Prediksi Normal

Prediksi Mencurigakan

Aktual Normal

TN = 862\.153

FP = 136

Aktual Mencurigakan

FN = 641

TP = 970

Dari confusion matrix data uji:

1. False Positive Rate \(FPR\) = 0,0158% berarti hanya 136 dari 862\.289 transaksi normal salah diklasifikasi
2. True Positive Rate \(TPR/Recall\) = 60,21% berarti model berhasil mendeteksi 970 dari 1\.611 transaksi mencurigakan

### <a id="_Toc222169430"></a>3\.5\.3 Kurva Evaluasi

 

<a id="_Toc222169146"></a>Gambar 3\.15 Kurva Precision\-Recall dan ROC

           

           Gambar 3\.15 menunjukkan: \(kiri\) kurva Precision\-Recall dengan AP = 0,7412 pada data uji; \(kanan\) kurva ROC dengan AUC mendekati 1,0 pada ketiga split, mengindikasikan kemampuan diskriminasi model yang sangat baik\.

### <a id="_Toc222169431"></a>3\.5\.4 Hasil Evaluasi per Split  


<a id="_Toc222172710"></a>Tabel 3\.10 Performa Model CatBoost pada Setiap Data Split

Split

F1\-Score

Precision

Recall

PR\-AUC

Training

0,5584

0,8306

0,4206

0,5649

Validation

0,6147

0,8210

0,4913

0,6105

Test

0,7140

0,8770

0,6021

0,7412



<a id="_Toc222169147"></a>Gambar 3\.16 Performa CatBoost per Split

 

             Pola peningkatan performa dari training ke test menunjukkan bahwa model tidak mengalami overfitting dan mampu melakukan generalisasi dengan baik\. Hal ini mengindikasikan bahwa fitur yang direkayasa berhasil menangkap pola pencucian uang yang konsisten\.

### <a id="_Toc222169432"></a>3\.5\.5 Feature Importance



<a id="_Toc222169148"></a>Gambar 3\.17 Feature Importance Top 20

 

Menampilkan 20 fitur terpenting berdasarkan dua metode: \(kiri\) Prediction Values Change dan \(kanan\) Loss Function Change\.

Tabel 3\.11 Peringkat 10 Fitur Terpenting

Peringkat

Fitur

Importance \(%\)

1

Payment Format

29,02

2

pair\_tx\_count

7,08

3

from\_unique\_neighbors

4,83

4

in\_time\_delta

4,51

5

from\_in\_degree

3,55

6

out\_time\_delta

3,01

7

cross\_amt\_ratio

2,84

8

from\_total\_degree

2,64

9

from\_avg\_daily\_tx

2,58

10

is\_repeat\_pair

2,48

Analisis:

1. Payment Format menjadi fitur paling dominan \(29,02%\), menunjukkan bahwa format pembayaran memiliki korelasi kuat dengan pola pencucian uang\.
2. Fitur hasil rekayasa \(engineered features\) seperti pair\_tx\_count, from\_unique\_neighbors, dan in\_time\_delta menempati posisi 2–4, memvalidasi efektivitas pendekatan feature engineering berbasis pola transaksi\.
3. Fitur graph\-based \(from\_in\_degree, from\_total\_degree\) dan fitur temporal \(in\_time\_delta, out\_time\_delta\) turut berkontribusi signifikan\.

__3\.6 Implementasi Deployment__

              Untuk memvalidasi model secara interaktif dan memudahkan demonstrasi hasil penelitian, dilakukan deployment aplikasi web menggunakan Streamlit yang di\-hosting pada platform Replit\. Aplikasi ini memungkinkan pengguna menjalankan simulasi screening transaksi secara realtime menggunakan data asli dari dataset IBM AML Transactions\.

__3\.6\.1 Arsitektur Deployment__

Aplikasi deployment terdiri dari komponen berikut:

1. Model CatBoost — saved\_models/catboost\_aml\_model\.cbm \(format native CatBoost\)
2. Daftar fitur — saved\_models/feature\_cols\.json \(59 fitur yang digunakan\)
3. Dataset — HI\-Small\_Trans\.csv \(5\.078\.345 transaksi untuk simulasi\)
4. Aplikasi Streamlit — app\.py \(antarmuka web untuk simulasi screening\)

            Aplikasi di\-deploy ke Replit sehingga dapat diakses secara online tanpa perlu instalasi lokal\. Pipeline yang berjalan pada aplikasi identik dengan pipeline pada notebook penelitian: data mentah → parsing → feature engineering \(59 fitur\) → prediksi CatBoost → evaluasi\.

__3\.6\.2 Simulasi Screening Realtime__

__              __Fitur utama aplikasi adalah simulasi screening transaksi secara realtime, di mana sistem memproses transaksi satu per satu seperti sistem AML sesungguhnya\. Pengguna dapat mengatur:

1. Jumlah transaksi yang akan disimulasikan \(50–5\.000 transaksi\)
2. Persentase oversampling transaksi mencurigakan \(5–50%\) untuk memastikan variasi hasil
3. Kecepatan animasi \(Cepat, Normal, Lambat\)
4. Threshold prediksi \(melalui sidebar\) untuk menyesuaikan sensitivitas deteksi



<a id="_Toc222169149"></a>Gambar 3\.18 Halaman Awal Aplikasi Simulasi AML pada Replit

 

Setelah simulasi dimulai, sistem akan menampilkan proses klasifikasi transaksi secara langsung hingga seluruh data yang ditentukan selesai diproses\. Setiap transaksi dianalisis oleh model dan diberikan keputusan klasifikasi berdasarkan probabilitas yang dihasilkan serta threshold yang telah ditentukan sebelumnya\.



<a id="_Toc222169150"></a>Gambar 3\.19 Hasil Simulasi Screening Transaksi

Gambar 3\.19 menampilkan hasil akhir simulasi setelah seluruh transaksi selesai diproses\. Hasil tersebut menunjukkan bahwa model mampu melakukan identifikasi transaksi mencurigakan secara konsisten dan stabil selama proses simulasi berlangsung\. Pola deteksi yang dihasilkan selaras dengan performa model pada tahap eksperimen sebelumnya\.

Model yang dihasilkan dapat dijadikan dasar pengembangan sistem screening transaksi mencurigakan pada lingkungan nyata\. Penyesuaian threshold memungkinkan sistem diadaptasikan sesuai kebutuhan operasional, misalnya untuk meningkatkan ketelitian deteksi atau memperluas cakupan identifikasi transaksi berisiko\.

# <a id="_Toc222169433"></a>BAB IV   
HASIL DAN ANALISA

## <a id="_uxiourhbuuvs"></a><a id="_Toc222169434"></a>4\.1 HASIL

### <a id="_Toc222169435"></a>4\.1\.1 Interpretasi Performa Model

Hasil evaluasi pada data uji \(Tabel 3\.4\) menunjukkan F1\-Score 0,7140 dengan Precision 0,8770 dan Recall 0,6021\. Dari perspektif operasional, kedua metrik ini memiliki implikasi yang berbeda bagi institusi keuangan\.

Precision sebesar 87,70% berarti dari setiap 10 transaksi yang di\-flag oleh model, hampir 9 di antaranya memang merupakan transaksi mencurigakan\. Implikasi praktisnya adalah bahwa tim kepatuhan \(compliance\) tidak dibebani oleh volume alarm palsu yang tinggi — masalah klasik pada sistem AML berbasis aturan yang kerap menghasilkan ribuan false alarm per hari\. Dengan tingkat False Positive Rate hanya 0,0158% \(Tabel 3\.3\), model ini secara drastis mengurangi beban investigasi manual\.

Di sisi lain, Recall 60,21% menunjukkan bahwa model mendeteksi sekitar 6 dari 10 transaksi mencurigakan, sementara sisanya terlewat sebagai False Negative\. Dalam konteks AML, setiap transaksi yang tidak terdeteksi berpotensi memfasilitasi tindak pidana\. Namun, trade\-off antara Precision dan Recall ini merupakan keputusan desain yang disengaja melalui pemilihan threshold 0,67 — bukan kelemahan inheren model\. Sebagaimana ditunjukkan pada Tabel 3\.2, threshold dapat diturunkan ke 0,30 untuk meningkatkan Recall hingga 79,64%, dengan konsekuensi penurunan Precision menjadi 33,66%\.

### <a id="_Toc222169436"></a>4\.1\.2 Makna Pola Performa Antar Split

Fenomena peningkatan F1\-Score dari training \(0,5584\) ke test \(0,7140\) yang ditampilkan pada Gambar 3\.8 memerlukan interpretasi khusus\. Pada umumnya, model machine learning menunjukkan penurunan performa pada data yang belum pernah dilihat\. Peningkatan ini bukan mengindikasikan kebocoran data, melainkan disebabkan oleh dua faktor\.

Pertama, pembagian kronologis menghasilkan distribusi kelas yang berbeda antar split \(Tabel 3\.1\): rasio transaksi mencurigakan meningkat dari 0,08% pada training menjadi 0,19% pada test\. Dengan lebih banyak sampel positif, metrik F1\-Score secara matematis akan meningkat meskipun kemampuan diskriminasi model konstan\. Kedua, pola pencucian uang yang terjadi di periode akhir mungkin lebih konsisten dan mudah dikenali oleh fitur\-fitur yang telah direkayasa\.

Yang lebih penting adalah stabilitas Precision di seluruh split \(82–88%\)\. Konsistensi ini menunjukkan bahwa pola yang dipelajari model bersifat time\-invariant — model tidak menghasilkan prediksi positif secara sembarangan, melainkan secara konsisten mengidentifikasi transaksi dengan karakteristik tertentu, terlepas dari periode waktu\.

### <a id="_Toc222169437"></a>4\.1\.3 Perbandingan dengan Model Pembanding

Hasil model *CatBoost* dibandingkan dengan dua model pembanding yang diujikan pada *dataset* IBM AML Transactions *HI\-Small* yang sama: 

1. Arsitektur Multi\-GNN \(GIN\) yang dilaporkan oleh Egressy et al\. \(2024\), 
2. Pendekatan *XGBoost\+SMOTE* dari kajian publik pada platform *Kaggle*\. 

Multi\-GNN merepresentasikan paradigma representation learning berbasis graf, sementara XGBoost\+SMOTE merepresentasikan strategi oversampling sintetis yang umum diadopsi dalam riset AML\. Hasil Multi\-GNN dan XGBoost\+SMOTE diperoleh dari eksperimen ulang terhadap kode kajian publik pada dataset yang sama\.

<a id="_Toc222172810"></a>Tabel 4\.1 Perbandingan 3 Model

Metrik

Multi\-GNN \(GIN\)

XGBoost\+SMOTE

CatBoost 

Precision

23,76%

2,51%

87,70%

Recall

39,42%

72,98%

60,21%

F1\-Score

29,65%

4,86%

71,40%

PR\-AUC

0,2998

0,0887

0,7412



<a id="_Toc222169151"></a>Gambar 3\.20 Perbandingan Performa Tiga Model

 

 

CatBoost mengungguli kedua model pembanding secara signifikan pada F1\-Score dan Precision\. Dibanding Multi\-GNN, CatBoost mencatatkan peningkatan F1\-Score \+140,8% dan Precision \+269,1%\. Dibanding XGBoost\+SMOTE, F1\-Score CatBoost 14,7 kali lipat lebih tinggi dan Precision 35 kali lipat lebih presisi\.

Perbedaan paling mencolok terletak pada Precision: XGBoost\+SMOTE hanya mencapai 2,51% — artinya dari 100 transaksi yang di\-flag, hanya 2–3 yang benar\-benar merupakan pencucian uang\. Multi\-GNN sedikit lebih baik dengan 23,76%, namun masih berarti 3 dari 4 flag adalah alarm palsu\. CatBoost dengan Precision 87,70% menghasilkan hampir 9 dari 10 flag yang valid\. Secara absolut, XGBoost\+SMOTE menghasilkan 44\.106 False Positive dibandingkan hanya 136 pada CatBoost — perbedaan 324 kali lipat yang berdampak langsung pada beban investigasi tim kepatuhan\.

## <a id="_m8eebunlu540"></a><a id="_Toc222169438"></a>4\.2 ANALISA

Efektivitas CatBoost pada penelitian ini tidak terlepas dari kesesuaian antara karakteristik algoritma dan sifat data AML\. Mekanisme ordered target encoding memungkinkan fitur kategorikal diproses secara langsung, sehingga Payment Format dapat mempertahankan kekayaan informasinya dan menjadi fitur paling diskriminatif \(Tabel 3\.5\)\. Selain itu, konsistensi Precision lintas split \(Tabel 3\.4\) mengindikasikan bahwa ordered boosting berhasil mencegah prediction shift pada data temporal — hal yang krusial mengingat distribusi transaksi berubah dari waktu ke waktu\.

Hasil feature importance dan analisis korelasi \(Gambar 3\.9–3\.10\) mengkonfirmasi bahwa fitur\-fitur rekayasa berhasil menerjemahkan konsep domain AML menjadi sinyal numerik yang dapat dimanfaatkan model\. Fitur\-fitur berbasis graf menangkap pola layering, fitur temporal menangkap karakteristik structuring, dan fitur pasangan akun membedakan transaksi berulang yang lazim pada aktivitas normal dari koneksi baru yang kerap mengindikasikan pencucian uang\. Kesesuaian ini menjelaskan mengapa pendekatan feature engineering eksplisit mengungguli representation learning otomatis \(Multi\-GNN\) pada dataset ini — sejalan dengan temuan Florek & Zagdański \(2025\) bahwa gradient boosting sering kompetitif dengan deep learning pada data tabular\.

Perbandingan tiga model \(Tabel 4\.1\) juga memberikan bukti empiris bahwa strategi penanganan ketidakseimbangan kelas berpengaruh signifikan terhadap kualitas prediksi\. Pendekatan cost\-sensitive learning yang mempertahankan distribusi data asli terbukti lebih layak secara operasional dibanding oversampling sintetis yang menggeser batas keputusan terlalu agresif pada rasio ketidakseimbangan ekstrem\. Temuan ini memperkuat pentingnya pemilihan metrik evaluasi yang tepat: ROC\-AUC yang tampak tinggi dapat menyesatkan pada data sangat tidak seimbang, sementara PR\-AUC memberikan gambaran yang lebih jujur tentang kemampuan model membedakan kelas minoritas\.

Berdasarkan analisis di atas, kelebihan dari sistem yang dikembangkan meliputi:

1. Tingkat alarm palsu yang rendah, sehingga mengurangi beban investigasi manual dan menjawab permasalahan utama pada pendekatan konvensional\.
2. Interpretabilitas Keputusan, setiap prediksi dapat ditelusuri ke fitur\-fitur yang berkontribusi, memenuhi tuntutan transparansi regulasi AML\.
3. Efisiensi komputasi, model memproses jutaan transaksi dalam hitungan menit tanpa memerlukan GPU\.
4. Fleksibilitas operasional, threshold dapat disesuaikan dengan toleransi risiko institusi \(Tabel 3\.2\), dari mode sensitivitas tinggi hingga mode keyakinan tinggi\.
5. Keunggulan substansial atas kedua model pembanding pada metrik F1\-Score dan PR\-AUC\.

Meskipun demikian, terdapat beberapa keterbatasan:

1. Model dilatih pada data sintetis sehingga validasi pada data transaksi riil diperlukan sebelum penerapan operasional\.
2. Recall sebesar 60,21% berarti sebagian transaksi mencurigakan masih terlewat, meskipun dapat ditingkatkan melalui penyesuaian threshold\.
3. Dominasi satu fitur \(Payment Format\) menciptakan risiko ketergantungan yang menuntut pemantauan distribusi fitur secara berkala\.
4. Tidak tersedia mekanisme pembaruan otomatis, sehingga pola pencucian uang yang berevolusi memerlukan siklus retraining berkala\.<a id="_r0mpk0ez042h"></a>

# <a id="_pea1c1jnzpzr"></a><a id="_Toc222169439"></a>BAB V   
KESIMPULAN

## <a id="_hfav3jnuq2sk"></a><a id="_Toc222169440"></a>5\.1 KESIMPULAN

Pada penelitian yang telah dilakukan menunjukkan bahwa penerapan metode CRISP\-DM dengan menggunakan algoritma CatBoost untuk mendeteksi transaksi mencurigakan pada sistem anti pencucian uang berbasis pola transaksi adalah:

1. Penelitian ini berhasil mengidentifikasi pola transaksi yang relevan untuk deteksi pencucian uang melalui rekayasa 59 fitur dari enam kategori \(Subbab 3\.3\.2\), mencakup aspek jaringan, statistik nilai, penomoran mitra, jeda waktu, perilaku, dan format pembayaran\. Analisis feature importance \(Tabel 3\.5\) mengkonfirmasi bahwa fitur\-fitur tersebut mampu menangkap karakteristik tipologi pencucian uang yang dimodelkan dalam dataset IBM AML Transactions\.
2. Model klasifikasi CatBoost berhasil dikembangkan dan dilatih untuk mengklasifikasikan transaksi pada data dengan ketidakseimbangan kelas ekstrem \(rasio 1:979\)\. Model juga berhasil di\-deploy sebagai aplikasi web pada platform Replit \(Subbab 3\.6\), membuktikan kelayakan penerapan secara operasional\.
3. Evaluasi performa menunjukkan bahwa model CatBoost mencapai F1\-Score 0,7140, Precision 0,8770, dan PR\-AUC 0,7412 pada data uji \(Tabel 3\.4\)\. Perbandingan dengan dua model pembanding \(Tabel 4\.1\) menunjukkan keunggulan signifikan pada F1\-Score dan Precision, mengkonfirmasi efektivitas pendekatan feature engineering berbasis pola transaksi yang dikombinasikan dengan cost\-sensitive learning untuk kasus deteksi AML\.

## <a id="_exg5q7aiphd9"></a><a id="_Toc222169441"></a>5\.2 SARAN

Berdasarkan hasil penelitian yang telah dilakukan, saran yang dapat diberikan penulis:

1. Penelitian selanjutnya perlu menguji model pada data transaksi keuangan sesungguhnya, misalnya melalui kerja sama dengan bank atau lembaga keuangan, karena pola pencucian uang di dunia nyata bisa lebih beragam dibanding data simulasi\.
2. Untuk meningkatkan Recall, dapat dicoba penggabungan CatBoost dengan algoritma lain \(ensemble\) atau penambahan bobot yang lebih besar pada kelas mencurigakan saat pelatihan, sehingga lebih banyak transaksi mencurigakan yang berhasil terdeteksi\.
3. Perlu ditambahkan fitur\-fitur yang lebih tahan terhadap perubahan perilaku pelaku, misalnya berbasis urutan waktu transaksi atau pola transaksi berulang, untuk mengurangi ketergantungan model pada satu fitur dominan\.
4. Bagi institusi yang ingin menerapkan model serupa, threshold sebaiknya disesuaikan dengan kapasitas tim investigasi, dan model perlu dilatih ulang secara berkala mengikuti perubahan pola pencucian uang\. Model ini sebaiknya digunakan sebagai alat bantu penyaringan awal — bukan pengganti — proses investigasi manual\.

# <a id="_wk1c4nbwmmgu"></a><a id="_Toc222169442"></a>DAFTAR PUSTAKA

\[1\] Republik Indonesia, “Undang\-Undang Nomor 8 Tahun 2010 tentang Pencegahan dan Pemberantasan Tindak Pidana Pencucian Uang,” 2010\.

\[2\] M\. Y\. bin Zul Kepli, “Money Laundering: Analysis on the Placement, Layering and Integration,” IJBEL, 2017\.

\[3\] Google Developers, “Classification: Accuracy, Precision, Recall, and related metrics,” 2025\.

\[4\] V\. Van Vlasselaer et al\., “APATE: A novel approach for automated credit card transaction fraud detection…,” Decision Support Systems, 2015\.

\[5\] L\. Prokhorenkova et al\., “CatBoost: Unbiased boosting with categorical features,” NeurIPS, 2018\.

\[6\] A\. Rianti, N\. W\. A\. Majid, and A\. Fauzi, “CRISP\-DM: Metodologi Proyek Data Science,” in Prosiding Seminar Nasional Teknologi Informasi dan Bisnis \(SENATIB\) 2023, Universitas Duta Bangsa Surakarta, Jul\. 25, 2023, pp\. 107–114, e\-ISSN: 2962\-1968\.

\[7\] Evidently AI Team, "How to interpret a confusion matrix for a machine learning model," evidentlyai\.com\. \[Online\]\. Available: https://www\.evidentlyai\.com/classification\-metrics/confusion\-matrix \(diakses 5 Feb\. 2026\)\.

 \[12\] E\. Altman et al\., “Realistic Synthetic Financial Transactions for Anti\-Money Laundering Models,” 2023\.

<a id="_xjt95dcznnae"></a>

# <a id="_Toc222169443"></a>LAMPIRAN

<a id="_rj2912aqtocl"></a>

# <a id="_Toc222169444"></a>DAFTAR RIWAYAT HIDUP



Haris Wahyudi lahir di Medan pada tanggal  04 Oktober 2003\. Penulis merupakan mahasiswa Program Sarjana Ilmu Komputer di Universitas Siber Asia\. Selama menjalani pendidikan, penulis aktif mendalami bidang pengembangan perangkat lunak, kecerdasan buatan, dan komputasi awan\. Sistem pembelajaran daring memberikan fleksibilitas sehingga penulis dapat terus meningkatkan kemampuan akademik tanpa mengganggu aktivitas profesional\.

Di luar kegiatan perkuliahan, penulis memiliki pengalaman sebagai Fullstack Developer dan terlibat dalam berbagai proyek pengembangan aplikasi web maupun mobile\. Pengalaman tersebut memperkuat pemahaman penulis dalam merancang, membangun, dan mengelola sistem teknologi informasi yang digunakan oleh berbagai organisasi dan pengguna dalam skala besar\.

Melalui kombinasi antara pendidikan formal dan pengalaman praktis, penulis berkomitmen untuk terus berkembang, beradaptasi dengan perkembangan teknologi terbaru, serta berkontribusi pada dunia akademis maupun industri melalui karya dan inovasi di bidang teknologi informasi\. 

