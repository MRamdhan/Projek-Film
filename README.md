# 🎬 Sistem Rekomendasi Film ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Matplotlib](https://img.shields.io/badge/Matplotlib-Used-yellow) ![Status](https://img.shields.io/badge/Status-Selesai-green)

Aplikasi Python berbasis terminal/CLI yang merekomendasikan film berdasarkan **genre favorit** dan **rating minimal**. Dilengkapi dengan visualisasi interaktif berupa **pie chart** dan **bar chart**.

---

## 📦 Fitur

✅ Membaca data film dari file `CSV`  
✅ Rekomendasi berdasarkan genre & rating minimal  
✅ Hasil diurutkan berdasarkan rating tertinggi  
✅ Visualisasi jumlah & kualitas film per genre  
✅ Penanganan error input (genre/rating/file)  
✅ Struktur modular dan mudah dikembangkan  

---

## 📁 Struktur Folder

```
rekomendasi_film/
├── main.py                # Program utama
├── data_loader.py         # Memuat data dari CSV
├── recommender.py         # Logika filter dan urutkan rekomendasi
├── visual.py              # Visualisasi data dengan Matplotlib
├── data/
│   └── film.csv           # Data film
├── img/
│   ├── genre_pie.png
│   └── genre_rating_bar.png
└── README.md
```

---

## ▶️ Cara Menjalankan

1. Buka terminal / CMD
2. Masuk ke folder `rekomendasi_film`
3. Jalankan perintah:

```bash
python main.py
```

Jika belum install pustaka visualisasi:

```bash
pip install matplotlib
```

---

## 💡 Contoh Hasil Program

```
===============================
  SISTEM REKOMENDASI FILM
===============================
Masukkan genre favorit: Aksi
Masukkan rating minimal: 7.5

Rekomendasi Film:
1. John Wick (2014) - Rating: 8.0
2. Mad Max: Fury Road (2015) - Rating: 7.9
3. The Raid (2011) - Rating: 7.6

Grafik disimpan di:
- img/genre_pie.png
- img/genre_rating_bar.png
```

---

## 📊 Visualisasi

- 🥧 **Pie Chart**: Jumlah film per genre
- 📊 **Bar Chart**: Rata-rata rating per genre

> Grafik otomatis disimpan saat program dijalankan.

---

## 📌 Saran Pengembangan

💡 Filter berdasarkan tahun rilis  
💡 Rekomendasi multi-genre  
💡 Export hasil rekomendasi ke file  
💡 Antarmuka GUI (Tkinter) atau Web (Flask/Streamlit)  

---

## 📃 Lisensi

Proyek ini dibuat untuk tujuan pembelajaran. Bebas digunakan dan dimodifikasi. Tidak untuk dijual.

---
