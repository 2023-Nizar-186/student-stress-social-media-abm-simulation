# Dataset

Folder ini digunakan untuk menyimpan seluruh dataset yang digunakan dalam project:

**Simulasi Tingkat Stres Mahasiswa Akibat Social Comparison di Media Sosial Menggunakan Agent-Based Modeling**

## Struktur Dataset

Dataset dapat berupa:

- Data hasil observasi
- Data sintetik (synthetic data)
- Data hasil simulasi
- Data hasil Monte Carlo Simulation
- Data pendukung penelitian

## Catatan

Karena ukuran file dataset dapat berubah dan cukup besar, file dataset utama tidak selalu disimpan pada repository GitHub.

Jika dataset tidak tersedia pada repository, pengguna dapat:

1. Menghasilkan ulang dataset melalui notebook.
2. Menggunakan file yang tersedia pada folder output hasil simulasi.
3. Mengikuti instruksi pada notebook untuk menghasilkan data baru.

## Format yang Didukung

- CSV (.csv)
- Excel (.xlsx)
- JSON (.json)

## Contoh Struktur

```text
data/
├── raw/
│   └── data_awal.csv
│
├── processed/
│   └── data_bersih.csv
│
└── simulation/
    └── hasil_simulasi.csv
```

## Keterangan

- **raw/** : data mentah sebelum preprocessing.
- **processed/** : data setelah preprocessing.
- **simulation/** : data yang dihasilkan dari simulasi Agent-Based Modeling.

## Lisensi

Dataset yang digunakan hanya untuk keperluan akademik dan pembelajaran.