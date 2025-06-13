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
1. Aspek Demografis

   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Aspek%20Demografis.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan grafik Karyawan yang lebih muda, belum menikah, dan berasal dari bidang HR atau Marketing cenderung memiliki tingkat pengunduran diri (attrition) yang lebih tinggi. Sementara itu, tingkat pendidikan dan jenis kelamin tidak terlalu berpengaruh secara signifikan terhadap keputusan resign.

2. Aspek Pekerjaan
   
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Aspek%20Pekerjaan.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan grafik diatas, dapat disimpulkan bahwa Karyawan yang bekerja di Sales, memiliki level pekerjaan rendah, lembur, dan melakukan perjalanan dinas sesekali (Travel_Rarely) cenderung lebih tinggi risiko resign. Posisi jabatan tinggi dan tidak lembur cenderung lebih stabil.

3. Aspek Kepuasan dan Keterlibatan
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Aspek%20Kepuasan%20dan%20Keterlibatan.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan grafik diatas, dapat disimpulkan bahwa attrition cenderung lebih tinggi pada karyawan yang memiliki tingkat kepuasan rendah (level 1 atau 2) dalam hal lingkungan kerja, kepuasan kerja, hubungan di tempat kerja, keseimbangan kerja-hidup, dan keterlibatan pekerjaan. Organisasi perlu fokus meningkatkan faktor-faktor ini untuk mengurangi attrition, terutama pada level kepuasan yang rendah.

4. Aspek Kompensasi
   
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Aspek%20Kompensasi.png)
   
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan grafik diatas, dapat disimpulkan bahwa tingkat attrition tersebar di berbagai level pendapatan dan tarif, tetapi secara umum lebih banyak karyawan yang bertahan (non-attrition) di semua kategori finansial. Tidak ada pola attrition yang sangat mencolok berdasarkan tingkat pendapatan atau tarif, sehingga faktor lain mungkin berperan lebih besar dalam pengunduran diri.

## Conclusion
1. Faktor Demografis
   - Karyawan yang lebih muda, belum menikah, dan bekerja di bidang HR atau Marketing memiliki kecenderungan lebih tinggi untuk resign.

   - Tingkat pendidikan dan jenis kelamin tidak terlalu signifikan dalam memengaruhi keputusan resign.

2. Faktor Pekerjaan
   - Karyawan di posisi Sales, level pekerjaan rendah, sering lembur, dan melakukan perjalanan dinas sesekali (Travel_Rarely) lebih berisiko resign.

   - Karyawan dengan jabatan tinggi dan jarang lembur cenderung lebih stabil.

3. Faktor Kepuasan
   - Kepuasan rendah (level 1-2) dalam lingkungan kerja, kepuasan kerja, hubungan kerja, work-life balance, dan keterlibatan pekerjaan berkontribusi besar terhadap attrition.

   - Perusahaan perlu meningkatkan aspek-aspek ini untuk mengurangi turnover karyawan.

4. Faktor Kompensasi
   - Tidak ada korelasi kuat antara pendapatan/tarif dengan attrition.

   - Faktor non-finansial (seperti kepuasan kerja dan lingkungan) lebih berpengaruh dibanding gaji.

### Rekomendasi Action Items (Optional)

Berikut adalah beberapa rekomendasi tindakan yang dapat dilakukan oleh perusahaan Jaya Jaya Maju untuk mengatasi permasalahan tersebut:

- Tingkatkan kepuasan kerja dengan program pengembangan karir, pelatihan, dan feedback rutin.
  
- Membangun Dashboard yang interaktif ke sistem HR
  
- Perbaiki work-life balance dengan mengurangi lembur dan meningkatkan fleksibilitas kerja.

- Fokus pada retensi karyawan muda & lajang melalui program mentoring dan engagement.

- Evaluasi beban kerja di departemen Sales & HR untuk mengurangi tekanan kerja.

- Monitor faktor kepuasan secara berkala menggunakan dashboard HR untuk deteksi dini risiko resign.
  

