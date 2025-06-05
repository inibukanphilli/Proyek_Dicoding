# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 200 dan memiliki lebih dari 1000 karyawan yang tersebar di berbagai wilayah di Indonesia. Sebagai perusahaan yang sangat bergantung pada kinerja sumber daya manusianya dalam menjalankan aktivitas operasional, manajemen karyawan menjadi faktor krusial untuk menjaga keberlangsungan dan pertumbuhan usaha.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Saat ini, perusahaan tengah menghadapi tantangan serius terkait jumlah tenaga kerja yang tersedia. Tingkat attrition yang mencapai 10% berpotensi menyebabkan kehilangan talenta terbaik, meningkatnya biaya untuk proses rekrutmen dan pelatihan, serta penurunan efisiensi kerja. Jika tidak segera ditangani secara tepat, kondisi ini dapat berdampak negatif terhadap keberlanjutan bisnis dalam jangka panjang.

### Permasalahan Bisnis

Beberapa masalah yang sedang dihadapi oleh perusahaan Jaya Jaya Maju antara lain:
1. Tingkat attrition yang mencapai 10% menimbulkan potensi gangguan terhadap kelancaran operasional perusahaan.
2. Terbatasnya pemahaman perusahaan dalam hal pengelolaan sumber daya manusia secara efektif.
3. Belum adanya kejelasan mengenai faktor-faktor utama yang memicu terjadinya attrition di kalangan karyawan.

### Cakupan Proyek

Cakupan proyek yang dilakukan yaitu:
1. Analisis Data Eksploratif (EDA)
   - Melakukan eksplorasi awal terhadap dataset untuk memahami pola dan tren yang muncul, serta menggali informasi penting yang berkaitan dengan kondisi karyawan.

2. Identifikasi Faktor Penyebab Tingkat Attrition
   - Menggunakan metode seleksi fitur untuk mengidentifikasi variabel-variabel yang berpengaruh terhadap attrition.
   - Mengembangkan model prediktif berbasis machine learning dengan pendekatan klasifikasi untuk memperkirakan kemungkinan terjadinya attrition berdasarkan data yang tersedia.
   
3. Pengembangan Dashboard Bisnis
   - Mendesain serta membangun dashboard interaktif dengan memanfaatkan Docker dan Metabase, yang berfungsi untuk memantau kondisi karyawan secara real-time guna mendukung pengambilan keputusan oleh tim HR.

### Persiapan

Sumber data: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

```
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
```

Username dan Password:
```
   User     :boyphilli4@gmail.com
   Password :07Juni2002$
```
## Business Dashboard

Adapun business board dibuat beberapa segmen yaitu:
1. Berdasarkan tingkat kepuasan karyawan pada perusahan

   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Tingkat%20Kepuasan%20Karyawan%20pada%20Perusahaan.png)


   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dalam segmen kepuasan karyawan, terdapat tiga faktor utama yaitu lingkungan, pekerjaan, dan hubungan antar karyawan. Kepuasan terhadap lingkungan (environment satisfaction) lebih banyak berada pada tingkat 4, sementara kepuasan terhadap pekerjaan (job satisfaction) berada pada tingkat 3, dan kepuasan terhadap hubungan antar karyawan (relationship satisfaction) berada pada tingkat 3 hingga tingkat 4. Namun, pada setiap grafik yang ditampilkan, sekitar 19-20% karyawan memberikan penilaian pada tingkat 1, dan sekitar 18-20% berada pada tingkat 2. Jika digabungkan, hal ini menunjukkan bahwa sekitar sepertiga karyawan merasa tidak puas dengan perusahaan terutama dalam aspek lingkungan, pekerjaan, dan hubungan antar karyawan.
   
2. Berdasarkan komposisi karyawan dan posisi
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Komposisi%20karyawan%20dan%20posisi.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Komposisi karyawan dan posisinya ditampilkan dalam tiga grafik, yaitu Department by Attrition, Job Role by Attrition, dan Gender by Attrition. Pada grafik Department by Attrition, jumlah karyawan terbanyak di perusahaan Jaya Jaya Maju terdapat di departemen Research, yang juga mengalami tingkat attrition tertinggi, diikuti oleh departemen Development. Sebaliknya, departemen Human Resource memiliki jumlah karyawan paling sedikit dan mengalami tingkat attrition yang paling rendah. Pada grafik Job Role by Attrition, posisi dengan tingkat attrition tertinggi adalah pada job role "Other," yang juga memiliki jumlah karyawan terbanyak. Sedangkan pada grafik Gender by Attrition, mayoritas karyawan laki-laki bekerja di Jaya Jaya Maju dan mereka juga menjadi kelompok dengan tingkat attrition paling tinggi.
   
3. Berdasarkan tingkatan performansi dan pekerjaa pada karyawan
   
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Tingkatan%20Performansi%20dan%20Pekerja%20Pada%20Karyawan.png)
   
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Segmen ini dibagi menjadi tiga bagian, yaitu berdasarkan Performance Rating, Tingkat Pekerjaan, dan Keterlibatan Kerja. Pada aspek Performance Rating, mayoritas karyawan berada pada tingkat 3 dan 4, yang menunjukkan bahwa karyawan di perusahaan Jaya Jaya Maju memiliki kinerja yang baik. Untuk Job Level, didominasi oleh tingkat 1 dan 2, yang mengindikasikan bahwa tingkat kompleksitas pekerjaan di Jaya Jaya Maju tergolong rendah atau mudah. Sedangkan pada grafik terakhir mengenai Job Involvement, tingkat keterlibatan kerja karyawan sebagian besar berada pada tingkat 3.
   
4. Karyawan Overtime (Lembur) yang bekerja
   
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Attrition%20by%20Overtime.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan grafik diatas, dapat disimpulkan bahwa karyawan yang bekerja lembur cenderung memiliki tingkat attrition yang lebih tinggi. Ini menunjukkan bahwa lembur berpotensi menjadi faktor risiko terhadap keputusan karyawan untuk keluar dari perusahaan, kemungkinan disebabkan oleh beban kerja berlebih, kelelahan, atau kurangnya work-life balance.


## Conclusion

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Proyek ini mampu memprediksi karyawan yang akan mengundurkan diri dari perusahaan Jaya Jaya Maju dengan menggunakan metode machine learning. Sistem melakukan prediksi berdasarkan data yang tersedia. Selain itu, hasil machine learning dan proses pemilihan fitur menunjukkan bahwa seluruh data pada dataset berperan dalam menentukan hasil klasifikasi. Hal ini terlihat dari penurunan akurasi prediksi saat fitur-fitur tertentu dihilangkan dibandingkan menggunakan semua kolom pada dataset. Namun, melalui proses seleksi fitur, diperoleh 10 faktor utama yang berpengaruh, yaitu Gender, Environment Satisfaction, Job Involvement, Job Level, Job Satisfaction, Overtime, Performance Rating, Relationship Satisfaction, Stock Option Level, dan Work-Life Balance.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Selain itu, penerapan sistem dashboard interaktif berbasis Docker Metabase memungkinkan pemantauan kondisi teknisi dan karyawan secara real-time, mengidentifikasi tingkat attrition berdasarkan data yang ada, serta mempermudah proses pengambilan keputusan. Dengan adanya sistem pemantauan ini, diharapkan manajemen karyawan dapat bersikap lebih proaktif sehingga mampu menurunkan tingkat attrition dan meningkatkan stabilitas serta kinerja perusahaan secara keseluruhan.

### Rekomendasi Action Items (Optional)

Berikut adalah beberapa rekomendasi tindakan yang dapat dilakukan oleh perusahaan Jaya Jaya Maju untuk mengatasi permasalahan tersebut:

- Membangun dan menerapkan sistem peringatan dini( Early Warning)
  
  Membangun sistem dengan pendekatan supervised machine learning klasifikasi untuk memprediksi karyawan apakah karyawan akan melakukan pengunduran diri atau tidak    berdasarkan data-data yang tersedia
  
- Membangun Dashboard yang interaktif ke sistem HR

  Merancang dan mengimplementasikan dashboard interaktif yang dapat memantau kinerja dan kondisi perusahaan secara real-time, kemudian mengintegrasikannya ke dalam sistem karyawan di divisi HRD.
  
- Melakukan survei rutin dan mengevaluasi kembali kebijakan perusahaan

  Melaksanakan survei berkala kepada karyawan mengenai kepuasan kerja, kompensasi, dan aspek lainnya, kemudian meninjau ulang kebijakan yang ada serta menyusun strategi baru untuk menangani masalah yang ditemukan.
  

