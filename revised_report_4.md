# Laporan Proyek Machine Learning - Mochamad Phillia Wibowo

---

## 1. [Project Overview] (https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination)
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

Dataset terdiri dari tiga file utama: `tourism_with_id.csv`, `user.csv`, dan `tourism_rating.csv`. Berikut adalah deskripsi lengkap variabel pada masing-masing dataset:

### 3.1 tourism_with_id.csv  
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
- **User_Id**: ID unik pengguna.  
- **Age**: Usia pengguna.  
- **Gender**: Jenis kelamin pengguna.  
- **Location**: Kota asal pengguna.

### 3.3 tourism_rating.csv  
- **User_Id**: ID pengguna yang memberikan rating.  
- **Place_Id**: ID tempat wisata yang diberi rating.  
- **Place Ratings**: Nilai rating yang diberikan pengguna terhadap tempat wisata.

---

## 4. Exploratory Data Analysis (EDA)  
- Tempat wisata populer seperti Malioboro dan Keraton Yogyakarta memiliki jumlah rating tinggi.  
- Kategori wisata alam dan budaya mendominasi.  
- Mayoritas pengguna berusia 18-35 tahun dan berasal dari luar Yogyakarta.  
- Harga tiket sebagian besar di bawah Rp50.000.

---

## 5. Data Preparation

Langkah-langkah persiapan data yang dilakukan sesuai dengan implementasi di notebook adalah sebagai berikut:

1. **Penghapusan kolom tidak relevan**  
   Menghapus kolom yang tidak diperlukan untuk pemodelan agar data lebih ringkas dan fokus.

2. **Filter data hanya untuk Kota Yogyakarta**  
   Memilih data tempat wisata yang hanya berada di Kota Yogyakarta untuk fokus analisis.

3. **Penyaringan data rating**  
   Memastikan data rating hanya mencakup pengguna dan tempat wisata yang relevan setelah filter.

4. **Penyaringan data user**  
   Memastikan data pengguna yang digunakan sesuai dengan data rating dan tempat wisata.

5. **Encoding ID pengguna dan tempat wisata**  
   Mengubah ID pengguna dan tempat wisata menjadi format numerik yang dapat diproses oleh model embedding.

6. **Penyusunan dataset TensorFlow**  
   Menyusun dataset dalam format `tf.data.Dataset` untuk efisiensi pelatihan model.

---

## 7. Modeling

Model yang digunakan adalah Neural Collaborative Filtering dengan dua jalur embedding, yaitu embedding untuk pengguna dan embedding untuk tempat wisata. Model ini bertujuan mempelajari hubungan laten antara pengguna dan tempat wisata untuk memprediksi rating dan memberikan rekomendasi personal.

### 7.1 Arsitektur Model
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

### 7.2 Proses Training
    
Model dilatih menggunakan konfigurasi sebagai berikut:

   - Loss Function: Menggunakan Mean Squared Error (MSE) untuk mengukur selisih kuadrat antara rating aktual dan prediksi.

   - Optimizer: Adam optimizer dengan pengaturan default digunakan untuk mempercepat konvergensi selama pelatihan.

   - Metrics: Root Mean Squared Error (RMSE) digunakan sebagai metrik utama untuk mengevaluasi akurasi prediksi rating.

   - Epoch dan Validasi: Model dilatih selama beberapa epoch hingga nilai loss dan RMSE pada validation set menunjukkan konvergensi dan stabilitas.

### 7.3 Hasil Rekomendasi Model  

Berikut adalah contoh tabel rekomendasi Top-5 tempat wisata untuk satu pengguna (User_Id: 287), lengkap dengan skor prediksi rating:

| No | Nama Tempat                         | Kategori      | Harga Tiket Masuk | Rating Wisata |
|----|-----------------------------------|---------------|-------------------|--------------|
| 1  | Watu Goyang                       | Budaya        | 2500              | 4.4          |
| 2  | Alun-alun Utara Keraton Yogyakarta| Budaya        | 0                 | 4.6          |
| 3  | Air Terjun Kedung Pedut           | Cagar Alam    | 20000             | 4.5          |
| 4  | Desa Wisata Gamplong              | Taman Hiburan | 10000             | 4.4          |
| 5  | Puncak Gunung Api Purba - Nglanggeran | Cagar Alam | 10000             | 4.7          |

---

## 8. Evaluasi  

Model dievaluasi menggunakan metrik Mean Squared Error (MSE) dan Root Mean Squared Error (RMSE) pada data training dan validation. Berikut hasil evaluasi yang diperoleh:

| Dataset    | Loss (MSE) | RMSE  |
|------------|------------|-------|
| Training   | 0.123      | 0.35  |
| Validation | 0.145      | 0.38  |

Nilai RMSE yang relatif rendah menunjukkan model mampu memprediksi rating dengan akurasi yang baik, sehingga rekomendasi yang diberikan dapat dipercaya.

---