# DeltaGroup_JC_DS_OL_16_C_FinalProject

# HR Analytics : Saudi Arabia Used Car Dataset

## Created by:  Group Delta Class C

## Business Problem Understanding

### Context:
Sebagai negara yang baru seja mengalami urbanisasi yang pesat sejak 1970-an, kota-kota di Arab Saudi tumbuh semakin meluas dan umumnya menyebabkan adanya *urban sprawling*. Senada dengan teori model perencanaan kota konsentrik yang dikemukakan oleh Ernest Burgess bahwa umumnya kota memiliki pusat tunggal dan bertumbuh menjalar ke berbagai sisi perifer, hal tersebut bisa ditemui pada penataan berbagai kota di Arab Saudi, seperti di [Riyadh](https://edufixers.com/urban-sprawl-management-in-riyadh-saudi-arabia/), sebagai ibukota Arab Saudi dan di [Jeddah](https://academic.oup.com/ijlct/article/16/3/1008/6224156#304470444), sebagai pusat pelabuhan Arab Saudi. Hal tersebut menyebabkan adanya zona residensial baru di pinggir kota dan daerah pusatnya lambat laun bertransformasi menjadi daerah komersial seutuhnya.

Sekelumit fakta tersebut membuat kota-kota di Arab Saudi umumnya memiliki paradigma *car-centric* untuk bisa mengakomodasi kebutuhan transportasi penduduknya dari tempat mereka bernaung ke tempat mereka mendulang untung. Hal ini setidaknya ditandai dengan penjualan mobil di Arab Saudi yang cenderung selalu meningkat, dan setidaknya pada 2024, penjualan mobil di Arab Saudi berada pada [masa puncaknya selama 8 tahun terakhir](https://www.focus2move.com/saudi-arabia-auto-market/), dan per 2023, sudah ada sekiranya [645.700 mobil](https://www.statista.com/statistics/1497936/saudi-arabia-number-of-passenger-cars-sold/) yang terjual atau sudah dalam registrasi, angka tersebut 24,3% lebih banyak dari tahun sebelumnya. Setali tiga uang dengan tren penjualan mobil baru, penjualan mobil bekas pun juga mengalami tren positif dengan valuasinya yang diprediksi akan [menjadi 9,67 milyar dolar AS pada tahun 2030](https://www.mordorintelligence.com/industry-reports/saudi-arabia-used-car-market) dari prediksi valuasi tahun ini sebesar 6,87 milyar dolar AS. Hal ini disebabkan selain urbanisasi yang disebut pada paragraf sebelumnya, terdapat juga faktor-faktor lain seperti kualitas mobil bekas yang umumnya kian membaik; murahnya harga pembelian dan bahkan operasional mobil bekas, seperti bensin, dengan bilangan oktan 95 saja (di Indonesia setara dengan Pertamax Green 95) dipatok sebesar 2,33 riyal Saudi (sebesar 10.144,82 rupiah per kurs 19 Februrari 2025); dan juga sudah menjamurnya *e-commerce platform* untuk mobil bekas di Arab Saudi seperti Yalla Motor, Car Switch, Halta2ee, Kavak, dan Syarah, *platform* yang menyediakan data sebagai basis analisis dan prediksi pemodelan penjualan mobil bekas pada kesempatan ini. Tak ayal, berbisnis mobil yang menjadi bekas di negara *petrodollar* yang terbilang baru ini menjadi ceruk yang cukup menarik, apalagi selain didesak keadaan, dan sepertinya akan semakin melesat dengan peningkatan transportasi umum seperti dibangunnya Riyadh Metro per 2024 lalu, kepemilikan mobil di Arab Saudi juga menjadi penanda status sosial dengan banyaknya kepemilikan mobil SUV, baik yang baru maupun yang bekas.

Membeli mobil bekas bisa menjadi keputusan yang sulit bagi pelanggan di Arab Saudi. Banyak faktor yang mempengaruhi harga dan keputusan pembelian, seperti merek, tahun produksi, jarak tempuh, dan fitur tambahan. Pelanggan menginginkan transparansi dalam harga serta keandalan dalam informasi kendaraan. Di sisi lain, penjual mobil bekas juga ingin menentukan harga optimal untuk menarik pelanggan sambil tetap mendapatkan keuntungan maksimal.

Pasar mobil bekas di Arab Saudi semakin kompetitif. Perusahaan, dealer, atau platform penjualan mobil ingin memahami faktor-faktor yang memengaruhi harga mobil bekas untuk membantu pelanggan menetapkan harga yang kompetitif dan menarik pembeli.
### Problem Statement:
Harga jual mobil bekas dipengaruhi oleh berbagai faktor, baik internal (karakteristik mobil) maupun eksternal (lokasi jualnya). Tantangan utama adalah menentukan harga yang sesuai dengan pasar. Jika harga terlalu tinggi, mobil bekas akan sulit terjual. Sebaliknya, jika terlalu rendah, keuntungan maksimal sulit dicapai.

### Objective:
Mengidentifikasi faktor utama yang memengaruhi harga mobil bekas melalui analisa deskriptif dari data yang ada.

Membuat model prediktif untuk memprediksi harga jual mobil bekas berdasarkan fitur-fitur yang tersedia. Model ini dapat membantu dealer mobil dalam menentukan harga yang sesuai dengan nilai pasar.

## Target:

### H0 (Null Hypothesis):
Tidak ada hubungan yang signifikan antara atribut kendaraan (seperti merek, tahun, spesifikasi, dll.) dan harga jual.
### H1 (Alternative Hypothesis):
Ada hubungan yang signifikan antara atribut kendaraan (seperti merek, tahun, spesifikasi, dll.) dan harga jual.

## Goals :
- Memahami pola dan hubungan antara atribut mobil bekas dan harga.
- Membangun model prediksi harga mobil bekas yang dapat membantu dalam pengambilan keputusan harga.
- Memberikan rekomendasi berbasis data untuk menetapkan harga kompetitif di pasar mobil bekas.

##  Analytic Approach
- Exploratory Data Analysis (EDA): Menganalisis distribusi harga, hubungan antar atribut, dan mencari pola yang relevan.
- Feature Engineering: Menyiapkan atribut yang relevan untuk model prediktif (misalnya, encoding kategori, normalisasi numerik, dll.).
- Model Building: Menggunakan algoritma machine learning (misalnya, regresi linier, random forest, XGBoost) untuk memprediksi harga berdasarkan atribut mobil.
- Evaluation: Menilai performa model menggunakan metrik evaluasi yang sesuai

## Metric Evaluation:
- Mean Absolute Error (MAE)
Mengukur rata-rata perbedaan absolut antara nilai aktual dan nilai prediksi. MAE menunjukkan seberapa besar kesalahan prediksi dalam satuan data yang sebenarnya. Semakin kecil nilai MAE, semakin akurat modelnya.

- Mean Absolute Percentage Error (MAPE)
Mengukur rata-rata kesalahan prediksi dalam bentuk persentase terhadap nilai aktual. Berguna untuk memahami akurasi prediksi secara relatif. Semakin kecil nilai MAPE, semakin baik model dalam memprediksi data.

- Root Mean Squared Error (RMSE)
Mengukur akar rata-rata dari kuadrat kesalahan prediksi. RMSE memberikan penalti yang lebih besar untuk kesalahan besar, sehingga lebih sensitif terhadap outlier dibandingkan MAE. Nilai RMSE yang lebih kecil menunjukkan model yang lebih akurat.

## Attribute Information

Dataset ini terdiri dari 8.035 entri dengan 13 kolom, yang mencakup berbagai informasi mengenai mobil bekas yang dijual di Arab Saudi. Berikut adalah deskripsi setiap kolom:


|Atribut     |Tipe Data  |Deskripsi|
|------------|-----------|-----------------------------------------------------|
|Make        |String     | Merek mobil                                         |
|Type        |String     | Tipe atau model   mobil                             |
|Year        |Integer    | Tahun produksi mobil                                |
|Origin      |String     | Negara asal mobil                                   |
|Color       |String     | Warna mobil                                         |
|Options     |String     | Kelengkapan                                         |
|Engine_Size |Float      | Kapasitas mesin (liter)                             |
|Fuel_Type   |String     | Jenis bahan bakar                                   |
|Gear_Type   |String     | Jenis transmisi                                     |
|Mileage     |Integer    | Jarak tempuh kendaraan (kilometer)                  |
|Region      |String     | Wilayah lokasi mobil dijual                         |
|Price       |Integer    | Harga mobil (dalam Riyal Saudi)                     |
|Negotiable  |Boolean    | Indikator apakah harga bisa dinegosiasi (True/False)|

## Cara menajalankan model dengan Streamlit

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi Streamlit:

1. Pastikan Anda sudah menginstal semua library yang diperlukan dengan menjalankan perintah berikut di terminal atau command prompt:

````pip install pandas numpy scikit-learn==1.5.2 xgboost streamlit````


2. Setelah instalasi selesai, jalankan aplikasi Streamlit menggunakan perintah berikut:
````streamlit run app.py````

3. Akses aplikasi di browser Anda menggunakan URL yang ditampilkan, seperti `http://localhost:8501`.

4. Masukkan data yang diperlukan ke dalam aplikasi untuk melihat hasil prediksi harga mobil bekas.

Jika Anda mengalami kesalahan saat menjalankan aplikasi, pastikan semua file seperti `app.py` dan `xgb_model.pkl` tersedia di direktori proyek Anda.


## Link Dashboard Tableau Public
https://public.tableau.com/app/profile/putra.hardi.ramadhan/viz/FinalProjectWork_17403866169210/Dashboard1?publish=yes

## Link Model Streamlit
