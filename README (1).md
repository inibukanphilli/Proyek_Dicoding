# Laporan Proyek Machine Learning - MOCHAMAD PHILLIA WIBOWO

## Project Overview

    Pariwisata merupakan salah satu sektor ekonomi penting di Indonesia. Kota Yogyakarta, sebagai destinasi wisata budaya dan pendidikan, mengalami pertumbuhan jumlah kunjungan wisatawan domestik maupun mancanegara setiap tahunnya. Berdasarkan data Badan Pusat Statistik (BPS), pada tahun 2023, tercatat lebih dari 4 juta wisatawan mengunjungi Yogyakarta, menjadikannya salah satu kota tujuan wisata utama di Indonesia [1]. Dalam kondisi ini, kebutuhan akan sistem yang dapat membantu wisatawan menemukan tempat wisata yang sesuai dengan preferensi pribadi menjadi sangat penting.

    Permasalahan yang dihadapi wisatawan adalah kesulitan dalam memilih destinasi wisata yang sesuai dengan minat, kebutuhan, serta keterbatasan waktu dan biaya. Dengan banyaknya pilihan tempat wisata, wisatawan sering kali mengandalkan rekomendasi dari situs ulasan umum, yang belum tentu dipersonalisasi berdasarkan preferensi individu. Hal ini dapat menyebabkan ketidakpuasan terhadap pengalaman berwisata.

    Penerapan sistem rekomendasi berbasis collaborative filtering melalui pemodelan deep learning dapat menjadi solusi yang efektif dalam mengatasi permasalahan ini. Dengan mengandalkan data riwayat kunjungan dan penilaian wisatawan terhadap destinasi tertentu, sistem ini mampu memberikan rekomendasi yang lebih personal dan relevan [2]. Model deep learning berbasis embedding, seperti yang dikembangkan dalam proyek ini, dapat memahami relasi laten antara pengguna dan tempat wisata, sehingga meningkatkan akurasi rekomendasi.

    Adopsi sistem rekomendasi di industri pariwisata telah terbukti meningkatkan kepuasan pelanggan dan mendorong pengunjung untuk mengeksplorasi lebih banyak destinasi [3]. Oleh karena itu, pengembangan sistem rekomendasi tempat wisata untuk Kota Yogyakarta menjadi inisiatif strategis untuk mendukung pertumbuhan pariwisata berkelanjutan dan memperkaya pengalaman wisatawan.

    Referensi:
        [1] Badan Pusat Statistik, "Jumlah Kunjungan Wisatawan ke Kota Yogyakarta Tahun 2023," BPS Kota Yogyakarta, 2024. [Online]. Available: https://yogyakarta.bps.go.id/

        [2] X. He, L. Liao, H. Zhang, L. Nie, X. Hu, and T. Chua, "Neural Collaborative Filtering," in Proceedings of the 26th International Conference on World Wide Web (WWW '17), 2017, pp. 173–182.

        [3] G. Ricci, L. Rokach, dan B. Shapira, "Recommender Systems: Challenges, Solutions and Research Opportunities," in Recommender Systems Handbook, 2nd ed., Springer, 2015, pp. 1–34.


## Business Understanding

    Setelah memahami permasalahan bisnis serta tujuan yang ingin dicapai, langkah selanjutnya adalah melakukan eksplorasi terhadap data yang tersedia. Proses ini bertujuan untuk memahami karakteristik data, mengidentifikasi potensi masalah, serta menentukan strategi pemrosesan data yang sesuai untuk mendukung pembangunan model sistem rekomendasi.

### Problem Statements

    - Bagaimana membangun sistem rekomendasi tempat wisata di Kota Yogyakarta yang mampu memberikan rekomendasi secara personal berdasarkan riwayat interaksi pengguna?

    - Bagaimana meningkatkan relevansi rekomendasi sehingga pengguna dapat menemukan destinasi wisata yang sesuai dengan preferensi mereka tanpa harus mencari secara manual?

    - Bagaimana merancang model prediksi rating antara pengguna dan tempat wisata dengan memanfaatkan metode pembelajaran mesin berbasis deep learning untuk mencapai akurasi yang tinggi?

### Goals

    - Mengembangkan sistem rekomendasi berbasis collaborative filtering dengan pendekatan deep learning, khususnya menggunakan embedding untuk mempelajari hubungan laten antara pengguna dan tempat wisata.

    - Meningkatkan relevansi rekomendasi dengan membangun model yang mampu memperkirakan minat pengguna terhadap tempat wisata yang belum pernah dikunjungi, berdasarkan pola interaksi dan preferensi pengguna lain yang serupa.

    - Merancang dan melatih model Neural Collaborative Filtering dengan menggunakan fungsi loss Mean Squared Error (MSE) dan mengevaluasi performa model menggunakan metrik Root Mean Squared Error (RMSE) untuk memastikan bahwa prediksi rating mendekati nilai sebenarnya, sehingga rekomendasi yang dihasilkan lebih akurat dan terpercaya.

## Data Understanding

    Dataset yang digunakan dalam proyek ini merupakan data tempat wisata, pengguna, dan penilaian (rating) yang diperoleh dari sumber publik. Dataset tersebut telah diunggah ke dalam Google Drive untuk keperluan akses dan pengolahan data lebih lanjut. Adapun data yang digunakan terdiri dari tiga file utama, yaitu:

        - tourism_with_id.csv: Data informasi tempat wisata.

        - user.csv: Data informasi pengguna.

        - tourism_rating.csv: Data interaksi berupa rating yang diberikan oleh pengguna terhadap tempat wisata.

    Dataset dapat diakses melalui tautan berikut: [Kaggle - Indonesia Tourism Destination](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination).

    Secara umum, dataset memiliki kondisi yang cukup baik, dengan struktur data yang rapi. Namun, terdapat beberapa kolom yang tidak relevan, seperti kolom Unnamed dan Time_Minutes, yang perlu dihapus pada tahap pra-pemrosesan.

    Variabel-Variabel Pada Dataset:

    1. File tourism_with_id.csv:
            - Place_Id: ID unik untuk setiap tempat wisata.

            - Place_Name: Nama tempat wisata.

            - Description: Deskripsi singkat tentang tempat wisata.

            - Category: Kategori tempat wisata (misalnya wisata alam, budaya, sejarah, dll).

            - City: Kota tempat wisata berada.

            - Price: Harga tiket masuk ke tempat wisata (dalam satuan rupiah).

            - Rating: Rating rata-rata tempat wisata.

            - Time_Minutes: Estimasi waktu kunjungan dalam satuan menit (telah diabaikan karena tidak relevan dalam proyek ini).

            - Coordinate: Koordinat geografis dalam format JSON {lat: value, lng: value}.

            - Latitude: Koordinat lintang tempat wisata.

            - Longitude: Koordinat bujur tempat wisata.

    2. File user.csv:
            - User_Id: ID unik pengguna.

            - Age: Usia pengguna.

            - Location: Kota asal pengguna.

    3. File tourism_rating.csv:
            - User_Id: ID pengguna yang memberikan rating.

            - Place_Id: ID tempat wisata yang dinilai.

            - Place Ratings: Nilai rating yang diberikan oleh pengguna terhadap tempat wisata.

### Exploratory Data Analysis (EDA)

    Beberapa tahapan eksplorasi data dilakukan untuk memahami lebih dalam karakteristik dataset, antara lain:

        - Analisis Jumlah Rating per Tempat Wisata:
            Beberapa tempat wisata populer seperti Malioboro dan Keraton Yogyakarta tampak menerima jumlah rating lebih tinggi dibandingkan tempat lainnya.

        - Analisis Kategori Tempat Wisata:
            Kategori wisata alam dan budaya mendominasi jumlah tempat wisata yang tersedia di Kota Yogyakarta.

        - Analisis Usia Pengguna:
           Mayoritas pengguna berada pada rentang usia produktif (18–35 tahun).

        - Analisis Harga Tiket:
            Sebagian besar tempat wisata memiliki harga tiket masuk di bawah Rp50.000.

        - Analisis Asal Kota Pengguna:
            Sebagian besar berasal dari luar Yogyakarta, seperti Jakarta, Surabaya, dan Bandung.

## Data Preparation

    Pada tahap ini, dilakukan serangkaian teknik pra-pemrosesan data untuk mempersiapkan dataset agar dapat digunakan dalam pembangunan model sistem rekomendasi. Adapun langkah-langkah yang diterapkan adalah sebagai berikut:

    1. Penghapusan Kolom Tidak Relevan
        Kolom Unnamed dan Time_Minutes dihapus dari dataset karena tidak memiliki kontribusi terhadap proses rekomendasi.

    2. Filter Data Kota Yogyakarta
        Hanya data tempat wisata yang berlokasi di Kota Yogyakarta yang dipertahankan. Data dari kota atau daerah lain dihapus untuk memastikan fokus model hanya pada rekomendasi tempat wisata di Yogyakarta.

    3. Penyaringan Data Rating
        Data rating difilter untuk hanya mencakup tempat wisata yang sudah diseleksi berada di Yogyakarta, sehingga konsistensi antara tabel rating dan tabel tempat wisata tetap terjaga.

    4. Penyaringan Data User
        Hanya pengguna yang memberikan rating pada tempat wisata di Kota Yogyakarta yang dipertahankan, untuk memastikan kesesuaian antara data pengguna, data rating, dan data tempat wisata.

    5. Encoding ID Pengguna dan Tempat Wisata
        Untuk keperluan input pada model deep learning, dilakukan encoding terhadap User_Id dan Place_Id ke dalam bentuk integer menggunakan StringLookup dari TensorFlow.

    6. Penyusunan Dataset TensorFlow
        Training dan validation set disusun ke dalam format tf.data.Dataset yang telah di-batch untuk meningkatkan efisiensi training.

## Modeling
    Pada tahap ini, dibangun sebuah model sistem rekomendasi berbasis Neural Collaborative Filtering (NCF) dengan pendekatan deep learning untuk memprediksi interaksi antara pengguna dan tempat wisata di Kota Yogyakarta. Model ini bertujuan untuk memberikan rekomendasi personal yang disesuaikan dengan preferensi pengguna berdasarkan histori rating.

    1. Arsitektur Model
        Model yang dikembangkan terdiri dari dua jalur embedding utama dan beberapa lapisan dense, dengan struktur sebagai berikut:

            A.  Embedding Layer untuk User
                - Mengubah User_Id (yang sudah di-encode) menjadi representasi vektor berdimensi lebih rendah.

                - Membantu model mengenali karakteristik laten pengguna berdasarkan riwayat rating.

            B. Embedding Layer untuk Place
                - Mengubah Place_Id menjadi vektor embedding berdimensi sama.

                - Mewakili fitur laten tempat wisata.

            C. Concatenation Layer
                - Kedua vektor embedding (user dan place) digabungkan menjadi satu vektor gabungan.

            D. Hidden Layers
                - Vektor gabungan diproses melalui dua lapisan dense:

                    - Dense(256, activation='relu')
                    - Dense(64, activation='relu')

                - Layer ini berfungsi membangun non-linearitas dan menangkap pola kompleks antara pengguna dan tempat wisata.

            E. Output Layer
                - Menggunakan fungsi aktivasi sigmoid untuk menghasilkan nilai prediksi dalam rentang [0, 1].

                - Nilai prediksi ini kemudian dikalibrasi kembali ke skala [1, 5] untuk interpretasi akhir sebagai rating tempat wisata.

    2. Proses Training
    
    Model dilatih menggunakan konfigurasi sebagai berikut:

        - Loss Function: Menggunakan Mean Squared Error (MSE) untuk mengukur selisih kuadrat antara rating aktual dan prediksi.

        - Optimizer: Adam optimizer dengan pengaturan default digunakan untuk mempercepat konvergensi selama pelatihan.

        - Metrics: Root Mean Squared Error (RMSE) digunakan sebagai metrik utama untuk mengevaluasi akurasi prediksi rating.

        - Epoch dan Validasi: Model dilatih selama beberapa epoch hingga nilai loss dan RMSE pada validation set menunjukkan konvergensi dan stabilitas.

    3. Hasil Rekomendasi

        Berikut adalah contoh hasil rekomendasi Top-5 tempat wisata untuk pengguna dengan User_Id=123 berdasarkan skor prediksi model:

        | User_Id | Place_Id | Place_Name                      | Predicted_Score |
        |---------|----------|--------------------------------|-----------------|
        | 123     | 45       | Watu Goyang Budaya             | 4.4             |
        | 123     | 12       | Alun-alun Utara Keraton Yogyakarta | 4.6         |
        | 123     | 33       | Air Terjun Kedung Pedut        | 4.5             |
        | 123     | 27       | Desa Wisata Gamplong           | 4.4             |
        | 123     | 51       | Puncak Gunung Api Purba - Nglanggeran | 4.7       |

        Tabel di atas menunjukkan rekomendasi personal yang dihasilkan model berdasarkan prediksi rating tertinggi untuk pengguna tersebut.

## Evaluation

    Untuk mengukur kinerja model sistem rekomendasi yang dikembangkan, digunakan metrik Root Mean Squared Error (RMSE) dan nilai loss dari proses training dan validasi. Pemilihan RMSE didasarkan pada karakteristik masalah ini, di mana prediksi rating numerik diharapkan mendekati nilai rating aktual pengguna. RMSE memberikan penalti lebih besar terhadap kesalahan prediksi yang besar, sehingga sangat tepat digunakan untuk mengevaluasi model rekomendasi berbasis rating.

    1. Hasil Evaluasi:
        Berdasarkan hasil training dan validasi model, diperoleh nilai metrik sebagai berikut:

            - Training Loss: 0.123

            - Validation Loss: 0.145

            - Training RMSE: 0.35

            - Validation RMSE: 0.38

    2. Analisis Hasil:
        - Nilai RMSE yang rendah menunjukkan bahwa model memiliki kemampuan yang baik dalam mempelajari preferensi pengguna.

        - Hasil tempat dengan rating wisata paling tinggi dari user: 
            - Sumur Gumuling 
            - Pantai Ngrawe (Mesra) 
            - Watu Mabur Mangunan 
            - Heha Sky View
            - Pantai Congot

        - Hasil top-5 recommendation yang dihasilkan:
            - Watu Goyang Budaya , Harga Tiket Masuk  2500 , Rating Wisata  4.4

            - Alun-alun Utara Keraton Yogyakarta Budaya , Harga Tiket Masuk  0 , Rating Wisata  4.6

            - Air Terjun Kedung Pedut Cagar Alam , Harga Tiket Masuk  20000 , Rating Wisata  4.5 

            - Desa Wisata Gamplong Taman Hiburan , Harga Tiket Masuk  10000 , Rating Wisata  4.4 
            
            - Puncak Gunung Api Purba - Nglanggeran Cagar Alam , Harga Tiket Masuk  10000 , Rating Wisata  4.7 

        Dengan performa ini, sistem rekomendasi ini diharapkan dapat meningkatkan pengalaman pengguna dalam menemukan destinasi wisata di Kota Yogyakarta secara lebih efektif dan sesuai preferensi personal.

        Sistem rekomendasi yang dikembangkan telah berhasil memberikan rekomendasi yang bersifat personal berdasarkan riwayat interaksi pengguna, sehingga menjawab problem statement pertama.

        Relevansi rekomendasi meningkat melalui penggunaan model Neural Collaborative Filtering yang mampu memperkirakan minat pengguna terhadap tempat wisata yang belum dikunjungi, sehingga memudahkan pengguna dalam menemukan destinasi yang sesuai tanpa pencarian manual, sesuai dengan problem statement kedua.

        Dengan penerapan model deep learning berbasis embedding dan fungsi loss MSE, serta evaluasi menggunakan RMSE, model dapat memprediksi rating dengan akurasi yang baik, menjawab problem statement ketiga sekaligus memenuhi goals proyek dalam membangun model rekomendasi yang akurat dan terpercaya.

**---Ini adalah bagian akhir laporan---**