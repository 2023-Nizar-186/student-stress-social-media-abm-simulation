# Simulasi Tingkat Stres Mahasiswa Akibat Social Comparison di Media Sosial Menggunakan Agent-Based Modeling

Project ini merupakan simulasi tingkat stres mahasiswa akibat fenomena *social comparison* di media sosial menggunakan pendekatan **Agent-Based Modeling (ABM)** dan library **SimPy**.

Simulasi ini dibuat untuk mata kuliah **Pemodelan dan Simulasi Data**.

---

## Identitas

| Keterangan | Detail |
|---|---|
| Nama | Ahmad Nizar Rusdiawan |
| NIM | 202310370311186 |
| Kelas | A |
| Semester | 6 |

---

## Deskripsi Project

Project ini memodelkan perilaku mahasiswa sebagai agen yang memiliki tingkat kecemasan atau **anxiety**. Setiap agen dapat mengalami peningkatan kecemasan akibat beberapa faktor, seperti:

- Paparan media sosial
- Perbandingan sosial
- Tekanan akademik
- Kualitas tidur
- Distorsi kognitif
- Resiliensi individu

Simulasi juga menambahkan intervensi berupa **CBT (Cognitive Behavioral Therapy)** untuk melihat dampaknya terhadap penurunan tingkat kecemasan mahasiswa.

---

## Tujuan Project

Tujuan dari project ini adalah:

1. Membuat model simulasi tingkat stres mahasiswa berbasis ABM.
2. Menganalisis pengaruh social comparison terhadap anxiety.
3. Membandingkan beberapa skenario intervensi CBT.
4. Menggunakan Monte Carlo Simulation untuk melihat hasil yang lebih stabil.
5. Menampilkan hasil simulasi dalam bentuk tabel dan visualisasi.

---

## Metode yang Digunakan

Project ini menggunakan beberapa pendekatan berikut:

- Agent-Based Modeling
- Discrete Event Simulation
- SimPy
- Monte Carlo Simulation
- Analisis skenario *what-if*
- Visualisasi data menggunakan Matplotlib

---

## Variabel Model

### Variabel Internal Agen

| Variabel | Keterangan |
|---|---|
| Anxiety | Tingkat kecemasan agen |
| Resilience | Kemampuan agen untuk pulih |
| Cognitive Distortion | Faktor yang memperbesar persepsi stres |

### Variabel Eksternal Agen

| Variabel | Keterangan |
|---|---|
| Media Exposure | Durasi penggunaan media sosial |
| Sleep Quality | Kualitas tidur |
| Academic Pressure | Tekanan akademik |
| Social Comparison | Intensitas perbandingan sosial |

---

## Skenario Simulasi

Project ini membandingkan beberapa skenario:

1. **Tanpa Intervensi**
   - Agen tidak mendapatkan CBT.

2. **CBT Reaktif**
   - CBT diberikan ketika anxiety melewati ambang batas tertentu.

3. **CBT Preventif**
   - CBT diberikan secara rutin untuk mencegah anxiety meningkat.

4. **High Cognitive Distortion**
   - Skenario ketika agen memiliki distorsi kognitif tinggi.

---

## Struktur Folder

```text
student-stress-social-media-abm-simulation/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── Pemodelan_dan_Simulasi_Data_REVISI.ipynb
│
├── data/
│   └── README.md
│
├── results/
│   ├── figures/
│   └── tables/
│
└── docs/
    └── laporan-ringkas.md