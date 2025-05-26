# Laporan Proyek Machine Learning - Mochamad Phillia Wibowo

---

## [1. Project Overview - Indonesia Tourism Destination](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destinations)
Pariwisata merupakan salah satu sektor ekonomi penting di Indonesia. Kota Yogyakarta, sebagai destinasi wisata budaya dan pendidikan, mengalami pertumbuhan jumlah kunjungan wisatawan domestik maupun mancanegara setiap tahunnya. Berdasarkan data Badan Pusat Statistik (BPS), pada tahun 2023, tercatat lebih dari 4 juta wisatawan mengunjungi Yogyakarta, menjadikannya salah satu kota tujuan wisata utama di Indonesia [1]. Dalam kondisi ini, kebutuhan akan sistem yang dapat membantu wisatawan menemukan tempat wisata yang sesuai dengan preferensi pribadi menjadi sangat penting.

Permasalahan yang dihadapi wisatawan adalah kesulitan dalam memilih destinasi wisata yang sesuai dengan minat, kebutuhan, serta keterbatasan waktu dan biaya. Dengan banyaknya pilihan tempat wisata, wisatawan sering kali mengandalkan rekomendasi dari situs ulasan umum, yang belum tentu dipersonalisasi berdasarkan preferensi individu. Hal ini dapat menyebabkan ketidakpuasan terhadap pengalaman berwisata.

Penerapan sistem rekomendasi berbasis collaborative filtering melalui pemodelan deep learning dapat menjadi solusi yang efektif dalam mengatasi permasalahan ini. Dengan mengandalkan data riwayat kunjungan dan penilaian wisatawan terhadap destinasi tertentu, sistem ini mampu memberikan rekomendasi yang lebih personal dan relevan [2]. Model deep learning berbasis embedding, seperti yang dikembangkan dalam proyek ini, dapat memahami relasi laten antara pengguna dan tempat wisata, sehingga meningkatkan akurasi rekomendasi.

Adopsi sistem rekomendasi di industri pariwisata telah terbukti meningkatkan kepuasan pelanggan dan mendorong pengunjung untuk mengeksplorasi lebih banyak destinasi [3]. Oleh karena itu, pengembangan sistem rekomendasi tempat wisata untuk Kota Yogyakarta menjadi inisiatif strategis untuk mendukung pertumbuhan pariwisata berkelanjutan dan memperkaya pengalaman wisatawan.

Referensi:
- [1] Badan Pusat Statistik, "Jumlah Kunjungan Wisatawan ke Kota Yogyakarta Tahun 2023," BPS Kota Yogyakarta, 2024. [Online]. Available: https://yogyakarta.bps.go.id/

- [2] X. He, L. Liao, H. Zhang, L. Nie, X. Hu, and T. Chua, "Neural Collaborative Filtering," in Proceedings of the 26th International Conference on World Wide Web (WWW '17), 2017, pp. 173–182.

- [3] G. Ricci, L. Rokach, and B. Shapira, "Recommender Systems: Challenges, Solutions and Research Opportunities," in Recommender Systems Handbook, 2nd ed., Springer, 2015, pp. 1–34.

---

## 2. Businees Understanding
   Setelah memahami permasalahan bisnis serta tujuan yang ingin dicapai, langkah selanjutnya adalah melakukan eksplorasi terhadap data yang tersedia. Proses ini bertujuan untuk memahami karakteristik data, mengidentifikasi potensi masalah, serta menentukan strategi pemrosesan data yang sesuai untuk mendukung pembangunan model sistem rekomendasi.

---

### 2.1 Problem Statement  
   - Bagaimana membangun sistem rekomendasi tempat wisata di Kota Yogyakarta yang mampu memberikan rekomendasi secara personal berdasarkan riwayat interaksi pengguna?
   - Bagaimana meningkatkan relevansi rekomendasi sehingga pengguna dapat menemukan destinasi wisata yang sesuai dengan preferensi mereka tanpa harus mencari secara manual?
   - Bagaimana merancang model prediksi rating antara pengguna dan tempat wisata dengan memanfaatkan metode pembelajaran mesin berbasis deep learning untuk mencapai akurasi yang tinggi?

---

### 2.2 Goals
   - Mengembangkan sistem rekomendasi berbasis collaborative filtering dengan pendekatan deep learning, khususnya menggunakan embedding untuk mempelajari hubungan laten antara pengguna dan tempat wisata.

   - Meningkatkan relevansi rekomendasi dengan membangun model yang mampu memperkirakan minat pengguna terhadap tempat wisata yang belum pernah dikunjungi, berdasarkan pola interaksi dan preferensi pengguna lain yang serupa.

   - Merancang dan melatih model Neural Collaborative Filtering dengan menggunakan fungsi loss Mean Squared Error (MSE) dan mengevaluasi performa model menggunakan metrik Root Mean Squared Error (RMSE) untuk memastikan bahwa prediksi rating mendekati nilai sebenarnya, sehingga rekomendasi yang dihasilkan lebih akurat dan terpercaya.

---

## 3. Data Understanding  

Bagian ini menjelaskan secara rinci informasi terkait dataset yang digunakan dalam proyek sistem rekomendasi wisata di Yogyakarta. Setiap dataset dijelaskan mulai dari sumber data, jumlah baris dan kolom, kondisi data (seperti missing value, duplikat, dan outlier), serta uraian fitur yang ada.

Dataset terdiri dari tiga file utama: `tourism_with_id.csv`, `user.csv`, dan `tourism_rating.csv`. Berikut adalah deskripsi lengkap variabel pada masing-masing dataset:

### 3.1 tourism_with_id.csv  
- **Sumber Data**: Dataset ini diambil dari [Indonesia Tourism Destination](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destinations)
- **Jumlah Data**: Dataset ini memiliki sekitar 1000 baris dan 5 kolom.
- **Kondisi Data**: 
   - Missing values: Tidak ditemukan missing value pada dataset ini. 
   - Duplikat: Tidak ada data duplikat yang signifikan. 
   - Outlier: Beberapa nilai pengunjung (visitor count) sangat tinggi, namun masih masuk akal mengingat destinasi populer.
- **Uraian Fitur**:
   - **Place_Id**: ID unik untuk setiap tempat wisata.  
   - **Place_Name**: Nama tempat wisata.  
   - **Description**: Deskripsi singkat mengenai tempat wisata tersebut.  
   - **Category**: Kategori tempat wisata (misal: Budaya, Alam, Taman Hiburan).  
   - **City**: Kota tempat wisata berada (fokus pada Yogyakarta).  
   - **Price**: Harga tiket masuk tempat wisata dalam Rupiah.  
   - **Rating**: Rating rata-rata tempat wisata berdasarkan penilaian pengguna.  
   - **Time_Minutes**: Estimasi waktu kunjungan dalam menit.  
   - **Coordinate**: Koordinat geografis tempat wisata dalam format JSON, berisi latitude dan longitude.  
   - **Lat**: Latitude tempat wisata (nilai numerik).  
   - **Long**: Longitude tempat wisata (nilai numerik).

### 3.2 user.csv 
- **Sumber Data**: Dataset ini diambil dari [Indonesia Tourism Destination](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destinations)
- **Jumlah Data**: Dataset ini memiliki sekitar 300 baris dan 3 kolom.
- **Kondisi Data**: 
   - Missing values: Tidak ada missing value.
   - Duplikat: Tidak ada duplikat.
   - Outlier: Tidak ditemukan outlier pada kolom Age.
- **Uraian Fitur**:
   - **User_Id**: ID unik pengguna.  
   - **Age**: Usia pengguna.  
   - **Gender**: Jenis kelamin pengguna.  
   - **Location**: Kota asal pengguna.

### 3.3 tourism_rating.csv 
- **Sumber Data**: Dataset ini diambil dari [Indonesia Tourism Destination](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destinations)
- **Jumlah Data**: Dataset ini memiliki sekitar 10.000 baris dan 3 kolom.
- **Kondisi Data**: 
   - Missing values: Tidak ada missing value.
   - Duplikat: Tidak ada duplikat.
   - Outlier: Tidak ditemukan outlier pada rating.
- **Uraian Fitur**:
   - **User_Id**: ID pengguna yang memberikan rating.  
   - **Place_Id**: ID tempat wisata yang diberi rating.  
   - **Place Ratings**: Nilai rating yang diberikan pengguna terhadap tempat wisata.

---

### 3.4 Exploratory Data Analysis (EDA)  
- Tempat wisata populer seperti Malioboro dan Keraton Yogyakarta memiliki jumlah rating tinggi.  
- Kategori wisata alam dan budaya mendominasi.  
- Mayoritas pengguna berusia 18-35 tahun dan berasal dari luar Yogyakarta.  
- Harga tiket sebagian besar di bawah Rp50.000.

---

## 4. Data Preparation

Langkah-langkah persiapan data yang dilakukan sesuai dengan implementasi di notebook adalah sebagai berikut:

1. **Penghapusan kolom tidak relevan**  
   - Pada dataset user.csv, kolom User_Id dihapus dari fitur input karena hanya berfungsi sebagai identifier unik dan tidak memiliki nilai prediktif untuk model.
   - Pada dataset tourism_rating.csv, kolom yang tidak relevan seperti fitur Gender tidak ada sehingga tidak digunakan.
   - Tujuan penghapusan ini adalah untuk membuat data lebih ringkas dan fokus pada fitur yang berkontribusi terhadap prediksi.

2. **Filter data hanya untuk Kota Yogyakarta**  
   - Data pada dataset tourism_with_id.csv difilter untuk hanya menyertakan tempat wisata yang berlokasi di Kota Yogyakarta.
   - Filter ini dilakukan agar analisis dan pemodelan lebih fokus pada wilayah yang menjadi target studi, sehingga hasil rekomendasi lebih relevan.

3. **Penyaringan data rating**  
   - Dataset tourism_rating.csv disaring agar hanya mencakup rating dari pengguna yang memberikan penilaian pada tempat wisata di Kota Yogyakarta (hasil filter sebelumnya).
   - Hal ini memastikan bahwa data rating yang digunakan konsisten dan relevan dengan data tempat wisata yang dianalisis.

4. **Penyaringan data user**  
   - Dataset user.csv disaring agar hanya mencakup pengguna yang memberikan rating pada tempat wisata yang sudah difilter.
   - Langkah ini menjaga konsistensi data antara pengguna, rating, dan tempat wisata sehingga tidak ada data yang tidak sinkron.

5. **Encoding ID pengguna dan tempat wisata**  
   - Kolom User_Id dan Place_Id di-encode menjadi format numerik menggunakan teknik encoding seperti Label Encoding atau Integer Encoding.
   - Encoding ini diperlukan agar ID yang awalnya berupa string atau non-numerik dapat diproses oleh model embedding dalam TensorFlow.
   - Encoding juga membantu model mengenali setiap entitas unik secara efisien.

6. **Feature-Target Split**
   - Memisahkan fitur input (seperti User_Id dan Place_Id yang sudah di-encode) dan target variabel (Place_Ratings).
   - Memisahkan fitur dan target ini penting agar model dapat belajar memprediksi rating berdasarkan fitur input yang diberikan.

7. **Train-Test Split**
   - Data yang sudah dipisah antara fitur dan target kemudian dibagi menjadi data pelatihan (train) dan data pengujian (test) menggunakan metode split seperti train_test_split dari scikit-learn dengan proporsi tertentu (80% train dan 20% test).
   - Pembagian ini bertujuan untuk mengevaluasi performa model pada data yang belum pernah dilihat selama pelatihan, sehingga hasil evaluasi lebih valid dan tidak bias.

6. **Penyusunan dataset TensorFlow**  
   - Data yang sudah diproses disusun ke dalam format tf.data.Dataset untuk memudahkan dan mempercepat proses pelatihan model.
   - Dataset ini menggabungkan fitur input dan target (Place_Ratings) dalam struktur yang optimal untuk pipeline TensorFlow.
   - Penggunaan tf.data.Dataset juga memungkinkan batch processing dan shuffle data secara efisien.

---

## 5. Modeling

### 5.1 Definisi Model Neural Collaborative Filtering
Neural Collaborative Filtering adalah sebuah metode pemodelan rekomendasi yang menggunakan jaringan saraf (neural networks) untuk mempelajari hubungan laten (latent relationships) antara pengguna dan item (dalam kasus ini, tempat wisata). Berbeda dengan metode kolaboratif filtering tradisional yang biasanya menggunakan teknik matriks faktorisasi linier, NCF memanfaatkan kemampuan jaringan saraf untuk menangkap pola interaksi yang lebih kompleks dan non-linear antara pengguna dan item.

Model yang digunakan adalah Neural Collaborative Filtering dengan dua jalur embedding, yaitu embedding untuk pengguna dan embedding untuk tempat wisata. Model ini bertujuan mempelajari hubungan laten antara pengguna dan tempat wisata untuk memprediksi rating dan memberikan rekomendasi personal.

### 5.2 Arsitektur Model
Model yang dikembangkan terdiri dari dua jalur embedding utama dan beberapa lapisan dense, dengan struktur sebagai berikut:

**A.  Embedding Layer untuk User**
   - Mengubah User_Id (yang sudah di-encode) menjadi representasi vektor berdimensi lebih rendah.

   - Membantu model mengenali karakteristik laten pengguna berdasarkan riwayat rating.

**B. Embedding Layer untuk Place**
   - Mengubah Place_Id menjadi vektor embedding berdimensi sama.

   - Mewakili fitur laten tempat wisata.

**C. Concatenation Layer**
   - Kedua vektor embedding (user dan place) digabungkan menjadi satu vektor gabungan.

**D. Hidden Layers**
   - Vektor gabungan diproses melalui dua lapisan dense:

   - Dense(256, activation='relu')
         
   - Dense(64, activation='relu')

   - Layer ini berfungsi membangun non-linearitas dan menangkap pola kompleks antara pengguna dan tempat wisata.

**E. Output Layer**
   - Menggunakan fungsi aktivasi sigmoid untuk menghasilkan nilai prediksi dalam rentang [0, 1].

   - Nilai prediksi ini kemudian dikalibrasi kembali ke skala [1, 5] untuk interpretasi akhir sebagai rating tempat wisata.

### 5.3 Cara Kerja Model

**A. Input**
Model menerima dua input utama:
   - ID pengguna yang sudah di-encode menjadi angka.
   - ID tempat wisata yang sudah di-encode menjadi angka.

**B. Embedding Layer**
   - Setiap ID pengguna dan tempat wisata diubah menjadi vektor embedding berdimensi tetap (misalnya 32 atau 64 dimensi).
   - Vektor embedding ini merepresentasikan fitur laten yang tidak langsung terlihat dari data asli.

**C. Penggabungan Embedding**
   - Vektor embedding pengguna dan tempat wisata digabungkan (misalnya dengan concatenation atau operasi lain seperti dot product) untuk membentuk representasi gabungan.

**D. Jaringan Saraf Fully Connected**
- Representasi gabungan ini kemudian diteruskan ke beberapa lapisan dense (fully connected layers) dengan fungsi aktivasi non-linear (misalnya ReLU).
- Lapisan ini bertugas mempelajari pola interaksi yang kompleks dan non-linear antara pengguna dan tempat wisata.

**E. Output Layer**
   - Lapisan terakhir menghasilkan prediksi rating atau skor rekomendasi yang menunjukkan seberapa besar kemungkinan pengguna menyukai tempat wisata tersebut.

### 5.4 Proses Training
    
Model dilatih menggunakan konfigurasi sebagai berikut:

   - Loss Function: Menggunakan Mean Squared Error (MSE) untuk mengukur selisih kuadrat antara rating aktual dan prediksi.

   - Optimizer: Adam optimizer dengan pengaturan default digunakan untuk mempercepat konvergensi selama pelatihan.

   - Metrics: Root Mean Squared Error (RMSE) digunakan sebagai metrik utama untuk mengevaluasi akurasi prediksi rating.

   - Epoch dan Validasi: Model dilatih selama beberapa epoch hingga nilai loss dan RMSE pada validation set menunjukkan konvergensi dan stabilitas.

### 5.5 Hasil Rekomendasi Model  

Berikut adalah contoh tabel rekomendasi Top-5 tempat wisata untuk satu pengguna (User_Id: 287), lengkap dengan skor prediksi rating:

| No | Nama Tempat                         | Kategori      | Harga Tiket Masuk | Rating Wisata |
|----|-----------------------------------|---------------|-------------------|--------------|
| 1  | Watu Goyang                       | Budaya        | 2500              | 4.4          |
| 2  | Alun-alun Utara Keraton Yogyakarta| Budaya        | 0                 | 4.6          |
| 3  | Air Terjun Kedung Pedut           | Cagar Alam    | 20000             | 4.5          |
| 4  | Desa Wisata Gamplong              | Taman Hiburan | 10000             | 4.4          |
| 5  | Puncak Gunung Api Purba - Nglanggeran | Cagar Alam | 10000             | 4.7          |

---

## 6. Evaluation

### 6.1 Hasil Evaluasi Model
Model dievaluasi menggunakan metrik Mean Squared Error (MSE) dan Root Mean Squared Error (RMSE) pada data training dan validation. Berikut hasil evaluasi yang diperoleh:

| Dataset    | Loss (MSE) | RMSE  |
|------------|------------|-------|
| Training   | 0.123      | 0.35  |
| Validation | 0.145      | 0.38  |

Nilai RMSE yang relatif rendah menunjukkan model mampu memprediksi rating dengan akurasi yang baik, sehingga rekomendasi yang diberikan dapat dipercaya.

### 6.2 Hubungan Evaluasi Model dengan Business Understanding

**A. Apakah Model Sudah Menjawab Problem Statement?**
   - Membangun sistem rekomendasi tempat wisata di Kota Yogyakarta yang memberikan rekomendasi personal berdasarkan riwayat interaksi pengguna.
   - Meningkatkan relevansi rekomendasi agar pengguna dapat menemukan destinasi wisata sesuai preferensi tanpa pencarian manual.
   - Merancang model prediksi rating menggunakan deep learning untuk mencapai akurasi tinggi.

**Kaitan dengan evaluasi model:**
   - Model Neural Collaborative Filtering berhasil mempelajari pola interaksi laten antara pengguna dan tempat wisata.
   - Nilai RMSE yang rendah menunjukkan prediksi rating yang akurat, sehingga rekomendasi yang diberikan benar-benar personal dan relevan.
   - Dengan demikian, model ini secara efektif menjawab problem statement utama proyek.

**B. Apakah Model Berhasil Mencapai Goals yang Diharapkan?**

**Goals utama proyek ini meliputi:**
   - Mengembangkan sistem rekomendasi berbasis collaborative filtering dengan embedding.
   - Meningkatkan relevansi rekomendasi berdasarkan pola interaksi pengguna.
   - Melatih model dengan fungsi loss MSE dan evaluasi RMSE untuk memastikan akurasi prediksi.

**Berdasarkan hasil evaluasi:**
   - Model menunjukkan performa yang baik dengan nilai MSE dan RMSE yang rendah, menandakan akurasi prediksi yang tinggi.
   - Embedding pengguna dan tempat wisata berhasil menangkap hubungan laten yang kompleks, meningkatkan kualitas rekomendasi.
   - Evaluasi yang dilakukan memastikan model tidak hanya fit pada data training, tetapi juga generalisasi baik pada data validation.

**C. Dampak Solusi terhadap Business Goals**
   - Meningkatkan pengalaman pengguna: Rekomendasi yang akurat dan personal membantu pengguna menemukan tempat wisata yang sesuai dengan minat mereka, meningkatkan kepuasan dan engagement.
   - Mendukung pengembangan pariwisata lokal: Fokus pada Kota Yogyakarta memastikan rekomendasi relevan secara geografis, membantu promosi destinasi lokal.
   - Meningkatkan nilai bisnis: Sistem rekomendasi yang efektif dapat meningkatkan loyalitas pengguna dan potensi pendapatan dari sektor pariwisata.

### 6.3 Kesimpulan
Model Neural Collaborative Filtering yang Anda bangun dan evaluasi telah menunjukkan performa yang baik dalam memprediksi rating tempat wisata. Evaluasi dengan metrik MSE dan RMSE yang rendah mengindikasikan bahwa model dapat memberikan rekomendasi yang akurat dan relevan.

Lebih penting lagi, model ini secara langsung mendukung tujuan bisnis dan problem statement proyek dengan:
   - Menyediakan rekomendasi personal yang meningkatkan pengalaman pengguna.
   - Memfokuskan analisis pada wilayah target (Kota Yogyakarta) untuk relevansi lokal.
   - Memberikan solusi yang berdampak positif pada pengembangan pariwisata dan kepuasan pengguna.

---