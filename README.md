# 🎬 Sistem Rekomendasi Film !

Aplikasi Python berbasis terminal atau CLI yang merekomendasikan film berdasarkan **genre favorit** dan **rating minimal**. Serta ada juga fitur visualisasi interaktif berupa **pie chart** dan **bar chart**.

---

## 📦 Fitur

✅ Membaca data film dari file `CSV`  
✅ Rekomendasi berdasarkan genre & rating minimal  
✅ Hasil diurutkan berdasarkan rating tertinggi  
✅ Visualisasi jumlah & kualitas film per genre  

---

## 📁 Struktur Folder

```
rekomendasi_film/
├── main.py                    # Program utama
├── data_loader.py             # Memuat data dari CSV
├── recommender.py             # Logika filter dan urutkan rekomendasi
├── visual.py                  # Visualisasi menggunakan Matplotlib
├── data/
│   └── film.csv               # Data film berupa file CSV
├── img/
│   ├── genre_pie.png          # Foto Pie Chart
│   └── genre_rating_bar.png   # Foto Bar Chart
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

Jika belum install library matplotlib untuk visualisasi:

```bash
pip install matplotlib
```

Setelah itu, memasukkan Genre dan Rating:

- **Genre**, misalnya: `Aksi`
- **Rating minimal**, misalnya: `7.5`

Kemudian program akan menyimpan atau menampilkan grafik berupa bar chart dan juga pie chart yang masuk ke dalam folder `img`.

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
```

---

## 👥 Anggota Kelompok

- **ABIYU NEYAD MECCADA** (20240040200)  
- **FAUZAN NURPADILAH** (20240040041)  
- **MOCHAMAD RAMDHAN IRAWAN** (20240040199)  
- **RIFALDI AKMAL FAUZAN** (20240040030)
