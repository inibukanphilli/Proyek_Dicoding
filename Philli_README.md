# Proyek Pertama : Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Perusahaan ini memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih menghadapi tantangan dalam mengelola karyawan secara efektif. Hal ini menyebabkan tingginya tingkat attrition rate (rasio jumlah karyawan yang keluar terhadap total karyawan) yang mencapai lebih dari 10%.

### Permasalahan Bisnis

Permasalahan utama yang dihadapi perusahaan adalah tingginya attrition rate karyawan yang dapat mengganggu kestabilan operasional dan produktivitas perusahaan. Manajemen perlu mengidentifikasi berbagai faktor yang mempengaruhi tingginya tingkat keluar masuk karyawan tersebut agar dapat mengambil langkah strategis untuk mengurangi tingkat attrisi dan mempertahankan talenta yang berharga di dalam perusahaan.

### Cakupan Proyek

Proyek ini akan berfokus pada identifikasi faktor-faktor yang menyebabkan tingginya attrition rate di Jaya Jaya Maju melalui analisis data karyawan. Selain itu, proyek akan mencakup pembuatan business dashboard yang dapat membantu manajer departemen HR memantau dan menganalisis berbagai faktor terkait dengan tingkat attrisi karyawan secara real-time. Dashboard tersebut akan menyediakan informasi yang relevan untuk mendukung pengambilan keputusan yang lebih tepat dan strategis dalam mengelola sumber daya manusia.

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
1. Perbandingan Kepuasan Karyawan Di Perusahaan

   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Tingkat%20Kepuasan%20Karyawan%20pada%20Perusahaan.png)


   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Dalam segmen kepuasan karyawan, terdapat tiga faktor utama yaitu lingkungan, pekerjaan, dan hubungan antar karyawan. Kepuasan terhadap lingkungan (environment satisfaction) lebih banyak berada pada tingkat 4, sementara kepuasan terhadap pekerjaan (job satisfaction) berada pada tingkat 3, dan kepuasan terhadap hubungan antar karyawan (relationship satisfaction) berada pada tingkat 3 hingga tingkat 4. Namun, pada setiap grafik yang ditampilkan, sekitar 19-20% karyawan memberikan penilaian pada tingkat 1, dan sekitar 18-20% berada pada tingkat 2. Jika digabungkan, hal ini menunjukkan bahwa sekitar sepertiga karyawan merasa tidak puas dengan perusahaan terutama dalam aspek lingkungan, pekerjaan, dan hubungan antar karyawan.

2. Karyawan Bertahan dan Keluar Berdasarkan Lembur
   
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Attrition%20by%20Overtime.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan grafik diatas, dapat disimpulkan bahwa karyawan yang bekerja lembur cenderung memiliki tingkat attrition yang lebih tinggi. Ini menunjukkan bahwa lembur berpotensi menjadi faktor risiko terhadap keputusan karyawan untuk keluar dari perusahaan, kemungkinan disebabkan oleh beban kerja berlebih, kelelahan, atau kurangnya work-life balance.

3. Kondisi Karyawan Bertahan dan Keluar Berdasarkan Unit Perusahaan dan Tanggung Jawab Karyawan 

   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Komposisi%20karyawan%20dan%20posisi.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Komposisi karyawan dan posisinya ditampilkan dalam tiga grafik, yaitu Department by Attrition, Job Role by Attrition, dan Gender by Attrition. Pada grafik Department by Attrition, jumlah karyawan terbanyak di perusahaan Jaya Jaya Maju terdapat di departemen Research, yang juga mengalami tingkat attrition tertinggi, diikuti oleh departemen Development. Sebaliknya, departemen Human Resource memiliki jumlah karyawan paling sedikit dan mengalami tingkat attrition yang paling rendah. Pada grafik Job Role by Attrition, posisi dengan tingkat attrition tertinggi adalah pada job role "Other," yang juga memiliki jumlah karyawan terbanyak. Sedangkan pada grafik Gender by Attrition, mayoritas karyawan laki-laki bekerja di Jaya Jaya Maju dan mereka juga menjadi kelompok dengan tingkat attrition paling tinggi.

4. Distribusi Rating pada Level dan Keterlibatan Pekerjaan serta Penilaian Kerja
   
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Tingkatan%20Performansi%20dan%20Pekerja%20Pada%20Karyawan.png)
   
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Segmen ini dibagi menjadi tiga bagian, yaitu berdasarkan Performance Rating, Tingkat Pekerjaan, dan Keterlibatan Kerja. Pada aspek Performance Rating, mayoritas karyawan berada pada tingkat 3 dan 4, yang menunjukkan bahwa karyawan di perusahaan Jaya Jaya Maju memiliki kinerja yang baik. Untuk Job Level, didominasi oleh tingkat 1 dan 2, yang mengindikasikan bahwa tingkat kompleksitas pekerjaan di Jaya Jaya Maju tergolong rendah atau mudah. Sedangkan pada grafik terakhir mengenai Job Involvement, tingkat keterlibatan kerja karyawan sebagian besar berada pada tingkat 3.

## Conclusion

- Proyek berhasil memprediksi karyawan yang akan mengundurkan diri dari perusahaan Jaya Jaya Maju dengan metode machine learning.

- Sistem prediksi dibuat berdasarkan data karyawan yang tersedia.

- Hasil dari machine learning dan proses seleksi fitur menunjukkan bahwa seluruh fitur di dataset berperan penting dalam klasifikasi.

- Penurunan akurasi prediksi terjadi jika beberapa fitur dihilangkan, menegaskan kontribusi setiap fitur.

- Melalui seleksi fitur, diperoleh 10 faktor utama yang paling berpengaruh terhadap attrition:

   - Gender
   - Environment Satisfaction (Kepuasan Lingkungan Kerja)
   - Job Involvement (Keterlibatan Kerja)
   - Job Level (Tingkat Jabatan)
   - Job Satisfaction (Kepuasan Kerja)
   - Overtime (Lembur)
   - Performance Rating (Penilaian Kinerja)
   - Relationship Satisfaction (Kepuasan Hubungan Kerja)
   - Stock Option Level
   - Work-Life Balance (Keseimbangan Kerja dan Kehidupan)

- Implementasi dashboard interaktif berbasis Docker Metabase mendukung pemantauan kondisi karyawan secara real-time.

- Dashboard memudahkan identifikasi tingkat attrition dan berbagai faktor penyebabnya.

- Sistem dashboard membantu manajemen mengambil keputusan yang lebih cepat dan tepat untuk mengurangi tingkat attrition.

- Diharapkan dengan sistem ini, manajemen bisa bersikap lebih proaktif dalam mengelola sumber daya manusia.

- Akhirnya, proyek ini diharapkan meningkatkan stabilitas dan kinerja keseluruhan perusahaan.

### Rekomendasi Action Items (Optional)

Berikut adalah beberapa rekomendasi tindakan yang dapat dilakukan oleh perusahaan Jaya Jaya Maju untuk mengatasi permasalahan tersebut:

- Membangun dan menerapkan sistem peringatan dini( Early Warning)
  
  Membangun sistem dengan pendekatan supervised machine learning klasifikasi untuk memprediksi karyawan apakah karyawan akan melakukan pengunduran diri atau tidak    berdasarkan data-data yang tersedia
  
- Membangun Dashboard yang interaktif ke sistem HR

  Merancang dan mengimplementasikan dashboard interaktif yang dapat memantau kinerja dan kondisi perusahaan secara real-time, kemudian mengintegrasikannya ke dalam sistem karyawan di divisi HRD.
  
- Melakukan survei rutin dan mengevaluasi kembali kebijakan perusahaan

  Melaksanakan survei berkala kepada karyawan mengenai kepuasan kerja, kompensasi, dan aspek lainnya, kemudian meninjau ulang kebijakan yang ada serta menyusun strategi baru untuk menangani masalah yang ditemukan.
  

