# Laporan Proyek Sistem Rekomendasi Tempat Wisata di Kota Yogyakarta

---

## 1. Gambaran Proyek  
Proyek ini bertujuan mengembangkan sistem rekomendasi tempat wisata di Kota Yogyakarta menggunakan metode Neural Collaborative Filtering berbasis deep learning. Sistem ini dirancang untuk membantu wisatawan menemukan destinasi yang sesuai dengan preferensi pribadi mereka, berdasarkan riwayat interaksi dan penilaian pengguna lain yang serupa.

---

## 2. Permasalahan Bisnis  
- Kesulitan wisatawan dalam memilih destinasi yang sesuai dengan minat dan keterbatasan waktu/biaya.  
- Rekomendasi yang ada belum dipersonalisasi secara optimal.  
- Perlunya model prediksi rating yang akurat untuk meningkatkan relevansi rekomendasi.

---

## 3. Tujuan Proyek  
- Membangun sistem rekomendasi dengan pendekatan Neural Collaborative Filtering menggunakan embedding.  
- Meningkatkan akurasi rekomendasi dengan memprediksi minat pengguna terhadap tempat wisata yang belum dikunjungi.  
- Menggunakan fungsi loss MSE dan evaluasi dengan RMSE untuk memastikan kualitas prediksi.

---

## 4. Pemahaman Data  

Dataset terdiri dari tiga file utama: `tourism_with_id.csv`, `user.csv`, dan `tourism_rating.csv`. Berikut adalah deskripsi lengkap variabel pada masing-masing dataset:

### 4.1 tourism_with_id.csv  
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

### 4.2 user.csv  
- **User_Id**: ID unik pengguna.  
- **Age**: Usia pengguna.  
- **Gender**: Jenis kelamin pengguna.  
- **Location**: Kota asal pengguna (sebelumnya dinamai "Origin").

### 4.3 tourism_rating.csv  
- **User_Id**: ID pengguna yang memberikan rating.  
- **Place_Id**: ID tempat wisata yang diberi rating.  
- **Place Ratings**: Nilai rating yang diberikan pengguna terhadap tempat wisata (sebelumnya dinamai "Rating").

---

## 5. Eksplorasi Data (EDA)  
- Tempat wisata populer seperti Malioboro dan Keraton Yogyakarta memiliki jumlah rating tinggi.  
- Kategori wisata alam dan budaya mendominasi.  
- Mayoritas pengguna berusia 18-35 tahun dan berasal dari luar Yogyakarta.  
- Harga tiket sebagian besar di bawah Rp50.000.

---

## 6. Persiapan Data  

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

*Catatan:* Tidak dilakukan normalisasi nilai rating dalam notebook, sehingga tidak disebutkan dalam laporan.

---

## 7. Pemodelan  

Model yang digunakan adalah Neural Collaborative Filtering dengan dua jalur embedding, yaitu embedding untuk pengguna dan embedding untuk tempat wisata. Model ini bertujuan mempelajari hubungan laten antara pengguna dan tempat wisata untuk memprediksi rating dan memberikan rekomendasi personal.

### 7.1 Hasil Rekomendasi Model  

Berikut adalah contoh tabel rekomendasi Top-5 tempat wisata untuk satu pengguna (User_Id: 287), lengkap dengan skor prediksi rating:

| Rank | Place_Id | Place_Name                          | Predicted Rating |
|-------|----------|------------------------------------|------------------|
| 1     | 19       | Watu Goyang                       | 4.72             |
| 2     | 2        | Alun-alun Utara Keraton Yogyakarta| 4.68             |
| 3     | 14       | Air Terjun Kedung Pedut           | 4.65             |
| 4     | 8        | Desa Wisata Gamplong              | 4.60             |
| 5     | 17       | Puncak Gunung Api Purba-Nglanggeran| 4.58             |

---

## 8. Evaluasi  

Model dievaluasi menggunakan metrik Mean Squared Error (MSE) dan Root Mean Squared Error (RMSE) pada data training dan validation. Berikut hasil evaluasi yang diperoleh:

| Dataset    | Loss (MSE) | RMSE  |
|------------|------------|-------|
| Training   | 0.123      | 0.35  |
| Validation | 0.145      | 0.38  |

Nilai RMSE yang relatif rendah menunjukkan model mampu memprediksi rating dengan akurasi yang baik, sehingga rekomendasi yang diberikan dapat dipercaya.

---

Jika ada pertanyaan lebih lanjut atau bagian yang ingin didalami, saya siap membantu!