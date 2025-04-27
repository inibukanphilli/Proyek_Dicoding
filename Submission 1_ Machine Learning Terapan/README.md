# Laporan Proyek Machine Learning - MOCHAMAD PHILLIA WIBOWO

## Domain Proyek

Dalam era perkembangan teknologi digital saat ini, pemanfaatan model klasifikasi gambar berbasis machine learning menjadi semakin penting di berbagai bidang, termasuk dalam pengelolaan data hewan. Klasifikasi gambar hewan seperti kucing, anjing, dan satwa liar dapat digunakan dalam banyak aplikasi, mulai dari sistem monitoring hewan peliharaan, sistem keamanan berbasis kamera, hingga membantu penelitian konservasi satwa di habitat alami.

Masalah yang dihadapi adalah banyaknya jumlah gambar hewan yang perlu diidentifikasi secara otomatis dan akurat dalam waktu singkat. Jika dilakukan secara manual, proses ini tentu memakan waktu, tenaga, dan sangat rentan terhadap kesalahan manusia. Oleh karena itu, pengembangan model machine learning untuk klasifikasi gambar menjadi solusi efektif untuk meningkatkan efisiensi dan akurasi dalam pengelolaan informasi gambar hewan.

Menurut studi yang dilakukan oleh Krizhevsky et al. (2012) dalam ImageNet Classification with Deep Convolutional Neural Networks, penggunaan Convolutional Neural Network (CNN) mampu secara signifikan meningkatkan akurasi dalam tugas pengenalan gambar kompleks, termasuk kategori hewan.

  [ImageNet Classification with Deep Convolutional Neural Network](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) 

Selain itu, laporan terbaru dari Stanford Vision Lab (ImageNet Large Scale Visual Recognition Challenge, Russakovsky et al., 2015) menunjukkan bahwa sistem klasifikasi berbasis deep learning telah mencapai tingkat akurasi mendekati kinerja manusia dalam pengenalan objek di gambar.

  [ImageNet Large Scale Visual Recognition Challenge](https://hci.stanford.edu/publications/2015/scenegraphs/imagenet-challenge.pdf) 

## Business Understanding

Setelah memahami latar belakang permasalahan dan tujuan yang ingin dicapai dalam proyek ini, langkah selanjutnya adalah melakukan eksplorasi terhadap data yang akan digunakan. Proses ini akan membantu dalam memahami struktur, karakteristik, serta kualitas data, sehingga dapat menentukan strategi yang tepat untuk tahap pemodelan selanjutnya. Oleh karena itu, bagian berikutnya akan membahas Data Understanding secara lebih rinci.

### Problem Statements

- Bagaimana membangun model klasifikasi gambar yang mampu membedakan gambar kucing, anjing, dan hewan liar secara akurat?
- Bagaimana mengatasi ketidakseimbangan jumlah data antar kelas dalam dataset?
- Bagaimana memastikan bahwa model dapat bekerja optimal tidak hanya pada data pelatihan, tetapi juga pada data baru yang belum pernah dilihat sebelumnya (generalization)?

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Membangun model CNN berbasis deep learning yang dapat mengklasifikasikan gambar kucing, anjing, dan hewan liar dengan akurasi minimal 85%.
Model dikembangkan dan dilatih menggunakan dataset terstruktur, serta dievaluasi menggunakan metrik akurasi, precision, recall, dan f1-score.
- Menerapkan strategi penanganan ketidakseimbangan data seperti pemberian class weight saat pelatihan.
Ini untuk memastikan semua kelas memiliki kontribusi yang setara dalam proses pelatihan, sehingga meningkatkan kemampuan model dalam mengenali semua kelas dengan adil.
- Menggunakan teknik validasi silang dan callbacks (early stopping) untuk mencegah overfitting dan memastikan model memiliki kemampuan generalisasi yang baik.
Dengan teknik ini, pelatihan model dihentikan secara otomatis saat kinerja validasi mencapai kriteria tertentu, sehingga model lebih siap untuk digunakan dalam dunia nyata.

## Data Understanding

Pada proyek ini, data yang digunakan adalah dataset gambar hewan yang terdiri dari tiga kategori, yaitu kucing (cat), anjing (dog), dan hewan liar (wild).Dataset ini diperoleh dari sumber internet yang open source untuk keperluan penelitian/belajar seperti dibawah ini saya menggunakan kaggle.

  [UCI Machine Learning Repository](https://www.kaggle.com/datasets/andrewmvd/animal-faces/data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- cat : Kumpulan gambar yang berisi berbagai jenis kucing.
- dog : Kumpulan gambar yang berisi berbagai jenis anjing.
- wild : Kumpulan gambar hewan liar selain kucing dan anjing, seperti serigala atau hewan lain dari alam liar.

## Data Preparation

Pada tahap ini, dilakukan beberapa teknik persiapan data untuk memastikan dataset siap digunakan dalam proses pelatihan model deep learning. Berikut urutan teknik yang diterapkan:

- Rescaling (Normalisasi Pixel)

  Setiap gambar pada dataset dinormalisasi dengan membagi nilai pikselnya dengan 255, sehingga rentang nilai berubah dari 0-255 menjadi 0-1. Teknik ini bertujuan untuk mempercepat proses pelatihan dan meningkatkan stabilitas model, karena nilai input yang lebih kecil cenderung mempercepat konvergensi model neural network.

- Data Augmentation

  Augmentasi data dilakukan untuk meningkatkan keragaman gambar pelatihan, seperti melalui rotasi, flipping, perubahan kecerahan, dan transformasi geometris. Hal ini penting untuk mengurangi overfitting dan membuat model lebih general terhadap data baru.

- Data Splitting (Pemisahan Data)

  Dataset dibagi menjadi tiga bagian, yaitu data training (80%), data validation (20%), dan data testing (terpisah).

- Pengaturan Batch Size dan Target Size

  Gambar disiapkan dalam batch berukuran 32 gambar dengan ukuran yang telah ditentukan 150x150 piksel. Pengaturan ini membantu mengoptimalkan penggunaan memori saat proses pelatihan.

- Penanganan Kelas Tidak Seimbang (Class Weights)

  Karena jumlah gambar pada masing-masing kelas tidak seimbang, diterapkan perhitungan class weights agar model tidak bias terhadap kelas mayoritas. Teknik ini membantu memperbaiki distribusi prediksi dan meningkatkan akurasi keseluruhan.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

- Arsitektur Model

  Model menggunakan arsitektur CNN bertingkat yang terdiri dari beberapa blok Conv2D, BatchNormalization, MaxPooling, dan Dropout. Struktur lapisan bertujuan untuk mengekstraksi fitur penting dari gambar dan mencegah overfitting.

- Detail Lapisan Model

  - Input Layer : Gambar berukuran 150x150 piksel dengan 3 channel warna (RGB).

  - Convolutional Layers

    - Dua layer Conv2D berturut-turut dengan 32 filter ukuran 3x3.

    - Dua layer Conv2D dengan 64 filter ukuran 5x5.

    - Dua layer Conv2D dengan 128 filter ukuran 7x7.

    - Dua layer Conv2D dengan 128 filter ukuran 11x11.

    Setiap convolutional layer menggunakan aktivasi ReLU dan diikuti oleh BatchNormalization, MaxPooling2D, dan Dropout untuk meningkatkan generalisasi model.

  - Fully Connected Layers
    
    Setelah flattening, terdapat dua dense layer: satu dengan 256 neuron dan satu lagi dengan 128 neuron, masing-masing menggunakan aktivasi ReLU. Dropout juga diterapkan untuk mengurangi overfitting.

  - Output Layer
    Dense layer dengan 3 neuron (sesuai jumlah kelas) dan fungsi aktivasi softmax untuk klasifikasi multikelas.

- Kompilasi Model

  - Optimizer : RMSprop, yang cocok untuk mempercepat konvergensi pada dataset yang besar dan kompleks.

  - Loss Function : Categorical Crossentropy, karena masalah ini merupakan klasifikasi multikelas.

  - Metrics : Accuracy, untuk mengevaluasi performa prediksi model selama pelatihan dan validasi.

- Custom Callback

  Digunakan callback CustomCallback yang menghentikan pelatihan secara otomatis apabila model telah mencapai kriteria tertentu, yaitu val_accuracy ≥ 0.85 dan val_loss ≤ 0.55. Teknik ini bertujuan untuk mencegah overfitting dan menghemat sumber daya komputasi.

- Penyesuaian Bobot Kelas

  Diterapkan bobot kelas pada saat training agar model tidak berat sebelah terhadap kelas dengan jumlah data yang lebih banyak.

- Proses Training

  Model dilatih menggunakan data training dengan jumlah epoch maksimal 50, batch size 32, validation data dari validation set, class weight, serta callback untuk monitoring training.

## Evaluation

Dalam proyek ini, dilakukan evaluasi performa model menggunakan beberapa metrik evaluasi utama, yaitu Akurasi, Precision, Recall, dan F1-Score. Penggunaan beberapa metrik ini bertujuan untuk memberikan gambaran menyeluruh terhadap kemampuan model dalam mengklasifikasikan gambar ke dalam kategori yang benar.

1. Penjelasan Metrik Evaluasi
  - Akurasi mengukur proporsi prediksi yang benar dibandingkan dengan seluruh prediksi yang dilakukan. Rumusnya:
  
  Akurasi = Jumlah Prediksi Benar / Total Prediksi 
  
  - Precision mengukur proporsi prediksi positif yang benar-benar positif. Rumusnya: 

  Precision = True Positive / True Positive + False Positive

  - Recall mengukur proporsi data positif yang berhasil diprediksi dengan benar. Rumusnya:
  
  Recall = True Positive / True Positive + False Negative

  - F1-Score adalah harmonisasi antara precision dan recall, dan berguna ketika diperlukan keseimbangan antara keduanya. Rumusnya:
  
  F1-Score = 2 x (Precision x Recall / Precision + Recall) 

2. Hasil Evaluasi

- Accuracy

  Akurasi diukur pad data training, validation, dan testing. Model mencapai:

    - Akurasi 97,31% pada data training, dengan loss sebesar 0,0762.

    - Akurasi 92,71% pada data testing, dengan loss sebesar 0,1950.
  
  Nilai akurasi yang tinggi pada data testing menunjukkan bahwa model mampu melakukan generalisasi dengan baik terhadap data yang belum pernah dilihat.

- Confusion Matrix

  Visualisasi confusion matrix memperlihatkan bahwa model cukup seimbang dalam mengklasifikasikan ketiga kelas (cat, dog, wild). Setiap kategori memperlihatkan jumlah prediksi benar yang dominan dibandingkan kesalahan klasifikasi, yang memperkuat tingkat akurasi model.

- Classification Report

  Berdasarkan hasil classification report, diperoleh metrik sebagai berikut:

    - Kelas Cat : Precision 0,95 | Recall 0,94 | F1-Score 0,94

    - Kelas Dog : Precision 0,94 | Recall 0,90 | F1-Score 0,92

    - Kelas Wild : Precision 0,89 | Recall 0,94 | F1-Score 0,92

    - Overall :

      - Accuracy : 93%

      - Macro Average (rata-rata precision, recall, f1-score) : 93%

      - Weighted Average : 93%

  Hasil ini menunjukkan bahwa model memberikan performa yang konsisten di seluruh kelas, dengan sedikit variasi antar kategori.

**---Ini adalah bagian akhir laporan---**

