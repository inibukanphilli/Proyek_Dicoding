# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 200 yang memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Sebagai perusahaan yang bergantung pada sumber daya manusia yang menjelankan operasionalnya, pengelolaan karyawan menjadi aspek penting dalam menjaga stabilitas dan pertumbuhan bisnis.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Namun, saat ini perusahaan mengalami tantangan siginifikan terhadap jumlah karyawan yang bekerja. Perusahaan mengalami Attrition rate sebesar 10% yang berisiko padakehilangan talenta terbaik, meningkatnya biaya rekrutmen dan pelatihan serta penurunan produktivitas. Kondisi ini dapat menghambat kelangsungan bisnis dan merugikan dalam jangka panjang jika tidak ditangani dengan tepat.

### Permasalahan Bisnis

Permasalahan yang dihadapi oleh perusahaan Jaya Jaya Maju:
1. Perusahaan mengalami Attrition rate sebesar 10% yang berisiko pada keberlangsungan operasional perusahaan
2. Kurangnya wawasan terhadap manajemen karyawan
3. Perusahaan belum dapat mengidentifikasi faktor-faktor yang mempengaruhi Attrition karyawan pada perusahaan

### Cakupan Proyek

Cakupan proyek yang dilakukan yaitu:
1. EDA
   - Melakukan eksplorasi terhadap kondisi dataset dan menemukan trend pada dataset untuk menemukan informasi yang relevan
3. Identifikasi faktor-faktor Attrition Rate:
   - Melakukan identifikasi dengan pendekatan seleksi fitur pada dataset
   - Membangun sistem yang dapat memprediksi berdasarkan data-data yang diberikan dengan pendekatan machine learning pada klasifikasi
   
3. Membangun Business Dashboard
   - Merancang dan mengimplementasikan dashboard interaktif menggunakan Docker Metabase yang dapat memantau secara real time kondisi karyawan di perusahaan untuk membantu divisi HR

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


   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pada segmen kepuasan karyawan terlihat dibagi 3 faktor yaitu lingkungan, pekerjaan dan hubungan sesama karyawan. Pada Environtment    satisfication lebih dominan terhadap tingkat 4, pada job satisfication berada pada tingkat 3 dan relationship satisfication berada pada tingkat 3 dan               tingkat 4. Namun pada setiap grafik yang ditampilkan, tingkat 1 pada setiap grafik sekitar 19-20% dan tingkat pada setiap grafik 18-20%, jika digabung ada          sekitar 1/3 karyawan yang tidak puas terhadap perusahaan pada bidang lingkungan, pekerjaan dan hubungan.
   
2. Berdasarkan komposisi karyawan dan posisi
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Komposisi%20karyawan%20dan%20posisi.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pada komposisi karyawan dan posisi dibagi 3 grafik yaitu Department by Attrition, Job role attrition dan Gender attrition.  Pada      department by attrition, jumlahkaryawan yang bekerja di Jaya Jaya Maju paling banyak di departemen Research, tetapi departemen mengalami banyak Attrition dan       development dan paling kecil yaitu departemen Human Resource dan departemen paling sedikit mengalami Attrition. Pada jobrole by attrition, pada jobrole paling      banyak mengalami Attrition dan jumlah karyawan yang bekerja sebagai jobrole Other. Pada grafik terakhir yaitu gender by attrition, jumlah karyawan laki-laki        paling bekerja di perusahaan Jaya Jaya Maju dan paling banyak mengalami Attrition.
   
3. Berdasarkan tingkatan performansi dan pekerjaa pada karyawan
   
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Berdasarkan%20Tingkatan%20Performansi%20dan%20Pekerja%20Pada%20Karyawan.png)
   
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pada segment ini dibagi menjadi 3 yaitu berdasarkan Performance rating, tingkat pekerjaan dan keterlibatan bekerja. Pada             Performance didapatkan bahwa performance didominasi pada tingkat 3 dan tingkat 4 menandakan bahwa karyawan di perusahaan Jaya Jaya Majuse memiliki performance      yang baik. Pada Job level, didominasi pada tingkat 1 dan tingkat 2 menandakan tingkatan pekerjaan di Jaya Jaya Maju tergolong mudah. Pada Grafik terakhir yaitu    job involment bahwa tingkat keterlibatan kerja karyawan pada tingkat 3.
   
4. Karyawan Overtime (Lembur) yang bekerja
   ![Dashboard](https://raw.githubusercontent.com/inibukanphilli/Proyek_Dicoding/refs/heads/main/Attrition%20by%20Overtime.png)

   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Berdasarkan grafik diatas, dapat disimpulkan bahwa kategori usia didominasi oeh kategori Early Career (18-25) dan Mid Career (36-     45). Namun tingkat attrition karyawan paling tinggi pada Early Career (18-25)


## Conclusion

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Proyek ini dapat melakukan prediksi terhadap karyawan yang pengunduran diri diperusahaan Jaya Jaya Maju, dengan menggunakan pendekatan machine learning sistem dapat memprediksi berdasarkan data yang diberikan. Selain itu, setelah dilakukan machine learning dan fitur selection bahwa pada dataset semuanya berkontribusi pada penentuan nilai klasifikasi. Hal ini dapat dilihat ketika melakukan seleksi fitur akurasi prediksi turun dari prediksi semua kolom pada dataset. Namun, berdasarkan fitur seleksi didapatkan 10 faktor utama yaitu Gender, Envirotment Satisfication, JobInvolment, Job Level, JobSatisfication, Overtime, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, WorkLifeBalance.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Selain itu, dengan diterapkannya sistem Dashboard yang interaktif menggunakan Docker Metabase, dapat memantau kondisi teknisi dari karyawan, mengidentifikasi Attrition rate berdasarkan data serta memudahkan dalam pengambilan keputusan.Dengan adanya sistem pemantauan ini diharapkan dapat proaktif dalam manajemen karyawan dan menurunkan Attrition rate serta memaksimalkan kinerja stabilitas perusahaan

### Rekomendasi Action Items (Optional)

Rekomendasi Action Items yang dapat dilakukan oleh perusahaan Jaya-Jaya Maju untuk menangani masalah tersebut:

- Membangun dan menerapkan sistem peringatan dini( Early Warning)
  
  Membangun sistem dengan pendekatan supervised machine learning klasifikasi untuk memprediksi karyawan apakah karyawan akan melakukan pengunduran diri atau tidak    berdasarkan data-data yang tersedia
  
- Membangun Dashboard yang interaktif ke sistem HR

  Membangun dan mengimplentasikan dashboard interaktif yang memonitor kinerja dan kondisi perusahaan yang kemudian di integrasi pada sistem karyawa pada divisi HRD
  
- Melakukan survey secara berkala dan meninjau ulang kebijakan perusahaan

  Melakukan survey kepada karyawan seperti menyangkut kepuasaan karyawan terhadap perusahaan, gaji yang diterima dan lain-lain kemudian peninjauan ulang dan          menerapkan rencana strategis untuk menghadapi masalah tersebut
  

