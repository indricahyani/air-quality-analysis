# Air Quality Analysis Dashboard

## Deskripsi Proyek

Proyek ini merupakan analisis data kualitas udara di Beijing menggunakan dataset Beijing Multi-Site Air Quality. Dataset mencakup data pengukuran kualitas udara dari 12 stasiun pemantauan selama periode Maret 2013 hingga Februari 2017.

Analisis dilakukan untuk memahami pola konsentrasi polutan udara berdasarkan lokasi, waktu, dan kondisi cuaca. Hasil analisis kemudian disajikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Link Dashboard

Dashboard dapat diakses secara online melalui tautan berikut:

**[Air Quality Analysis Dashboard](https://beijing-airquality-analysis-dashboard.streamlit.app/)**

## Tujuan Analisis

Analisis ini bertujuan untuk menjawab beberapa pertanyaan bisnis berikut:

1. Bagaimana perbandingan rata-rata konsentrasi PM2.5 dan PM10 pada 12 stasiun pemantauan kualitas udara di Beijing selama periode Maret 2013 hingga Februari 2017, dan stasiun mana yang mencatat konsentrasi rata-rata tertinggi?
2. Bagaimana pola rata-rata konsentrasi PM2.5 berdasarkan jam dan bulan pada 12 stasiun pemantauan kualitas udara di Beijing selama periode Maret 2013 hingga Februari 2017, dan apakah pola tersebut berbeda antarstasiun?
3. Bagaimana perbedaan rata-rata konsentrasi PM2.5 berdasarkan kondisi kecepatan angin dan curah hujan pada 12 stasiun pemantauan kualitas udara di Beijing selama periode Maret 2013 hingga Februari 2017?

Selain itu, dilakukan analisis lanjutan berupa:
- Analisis korelasi antarvariabel menggunakan Pearson Correlation.
- Pengelompokan stasiun berdasarkan rata-rata konsentrasi PM2.5 ke dalam kategori rendah, sedang, dan tinggi.

## Fitur Dashboard

Dashboard interaktif yang dikembangkan menggunakan Streamlit memiliki beberapa fitur utama:
- Filter data berdasarkan stasiun pemantauan.
- Filter data berdasarkan rentang tanggal.
- Ringkasan jumlah data serta rata-rata konsentrasi PM2.5 dan PM10.
- Visualisasi perbandingan konsentrasi PM2.5 dan PM10 pada setiap stasiun.
- Visualisasi pola konsentrasi PM2.5 berdasarkan jam, bulan, dan stasiun.
- Visualisasi konsentrasi PM2.5 berdasarkan kategori kecepatan angin dan curah hujan.
- Visualisasi analisis korelasi dan pengelompokan stasiun.
- Fitur untuk melihat dan mengunduh dataset berdasarkan filter yang dipilih.

## Struktur Direktori

```text
submission/
├── dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── data/
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   ├── PRSA_Data_Changping_20130301-20170228.csv
│   ├── PRSA_Data_Dingling_20130301-20170228.csv
│   ├── PRSA_Data_Dongsi_20130301-20170228.csv
│   ├── PRSA_Data_Guanyuan_20130301-20170228.csv
│   ├── PRSA_Data_Gucheng_20130301-20170228.csv
│   ├── PRSA_Data_Huairou_20130301-20170228.csv
│   ├── PRSA_Data_Nongzhanguan_20130301-20170228.csv
│   ├── PRSA_Data_Shunyi_20130301-20170228.csv
│   ├── PRSA_Data_Tiantan_20130301-20170228.csv
│   ├── PRSA_Data_Wanliu_20130301-20170228.csv
│   └── PRSA_Data_Wanshouxigong_20130301-20170228.csv
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt

```

## Menjalankan Notebook

Notebook digunakan untuk melakukan proses analisis data, mulai dari pengumpulan data, penilaian data, pembersihan data, eksplorasi data, hingga visualisasi dan penarikan kesimpulan.

Notebook dapat dijalankan menggunakan Google Colab dengan langkah-langkah berikut:

1. Buka [Google Colab](https://colab.research.google.com/).
2. Pilih menu **File → Upload notebook**.
3. Unggah file `notebook.ipynb`.
4. Unggah file ZIP yang berisi 12 dataset CSV melalui panel Files di Google Colab, kemudian ekstrak file tersebut ke direktori yang sesuai dengan path pada notebook.
5. Jalankan seluruh sel notebook secara berurutan dari awal hingga akhir.
6. Pastikan seluruh proses berjalan tanpa error.

## Instalasi dan Menjalankan Dashboard

1. Pastikan Python sudah terpasang.
2. Buka terminal pada direktori utama proyek.
3. Instal seluruh library yang dibutuhkan dengan perintah:

```bash
pip install -r requirements.txt
```

4. Jalankan dashboard menggunakan perintah:

```bash
python -m streamlit run dashboard/dashboard.py
```

5. Buka alamat lokal yang ditampilkan pada terminal, biasanya:

```text
http://localhost:8501
```

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman yang digunakan untuk proses analisis data dan pengembangan dashboard.
- **Pandas**: Mengolah, membersihkan, menggabungkan, dan menganalisis dataset.
- **Matplotlib**: Membuat visualisasi data dalam bentuk grafik.
- **Seaborn**: Membuat visualisasi statistik dengan tampilan yang lebih informatif.
- **Streamlit**: Mengembangkan dashboard interaktif berbasis web.
- **Google Colab**: Menjalankan notebook dan melakukan proses analisis data secara online.

## Kesimpulan

Berdasarkan hasil analisis, konsentrasi PM2.5 dan PM10 menunjukkan variasi pada setiap stasiun pemantauan. Pola konsentrasi PM2.5 juga mengalami perubahan berdasarkan waktu, dengan konsentrasi tertinggi berdasarkan jam terjadi pada pukul 22.00 dan berdasarkan bulan terjadi pada Desember.

Analisis kondisi cuaca menunjukkan bahwa rata-rata konsentrasi PM2.5 cenderung lebih rendah pada kecepatan angin yang lebih tinggi dan saat terjadi hujan. Hasil analisis korelasi juga menunjukkan hubungan positif yang kuat antara PM2.5 dan PM10, serta hubungan negatif antara PM2.5 dan kecepatan angin.

Secara keseluruhan, hasil analisis menunjukkan bahwa kualitas udara di Beijing memiliki variasi berdasarkan lokasi, waktu, dan kondisi cuaca. Dashboard interaktif yang dikembangkan diharapkan dapat membantu pengguna memahami pola tersebut melalui visualisasi data yang lebih mudah diakses.