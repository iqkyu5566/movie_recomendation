# Laporan Proyek Machine Learning - Ilham Julian Efendi

## Project Overview

Rekomendasi film merupakan salah satu masalah yang sering ditemui dalam platform streaming atau platform digital lainnya. Seiring dengan berkembangnya jumlah konten yang tersedia, sulit bagi pengguna untuk memilih film yang sesuai dengan preferensi mereka. Sistem rekomendasi yang tepat akan memudahkan pengguna dalam menemukan konten yang sesuai dengan minat mereka.

Proyek ini bertujuan untuk mengembangkan sistem rekomendasi berbasis pembelajaran mesin, dengan menggunakan data film dan model cosine similarity untuk memberikan rekomendasi film yang relevan. Dengan memanfaatkan teknik analisis data, proyek ini berfokus pada pengembangan model yang efisien dalam memberikan rekomendasi kepada pengguna.

Rekomendasi film berbasis machine learning dapat meningkatkan pengalaman pengguna dan meningkatkan engagement di platform yang menyediakan konten film.

Referensi:

Recommender Systems: Collaborative Filtering Based Recommendation System: A survey (https://www.researchgate.net/profile/Ramachandram-Sirandas/publication/267261428_Collaborative_Filtering_Based_Recommendation_System_A_survey/links/549ac4af0cf2fedbc30e3254/Collaborative-Filtering-Based-Recommendation-System-A-survey.pdf)

## Business Understanding

Pada bagian ini, kita akan mengklarifikasi masalah yang ingin diselesaikan melalui proyek ini.

Bagian laporan ini mencakup:

### Problem Statements

- Pernyataan Masalah 1: Pengguna mengalami kesulitan dalam menemukan film yang sesuai dengan   preferensi mereka di tengah banyaknya pilihan yang tersedia.
- Pernyataan Masalah 2: Platform streaming membutuhkan sistem rekomendasi yang dapat meningkatkan kepuasan pengguna dan mengurangi tingkat churn.

### Goals

1. Tujuan 1: Mengembangkan sistem rekomendasi film yang dapat memberikan rekomendasi film yang relevan berdasarkan kesamaan film.
2. Tujuan 2: Meningkatkan pengalaman pengguna dengan memberikan saran film yang akurat dan meningkatkan waktu yang dihabiskan pengguna pada platform.

### Solution statements
    Untuk mencapai tujuan di atas, dua pendekatan solusi yang dapat digunakan adalah:

      - Model berbasis Content-Based Filtering:
      Menggunakan cosine similarity antara fitur film (seperti genre, deskripsi, dll.) untuk memberikan rekomendasi berdasarkan kesamaan konten.
      - Model berbasis Collaborative Filtering:
      Memanfaatkan data interaksi pengguna (rating atau preferensi) untuk merekomendasikan film yang disukai oleh pengguna dengan preferensi serupa.

## Data Understanding
Data yang digunakan dalam proyek ini berasal dari dataset film yang tersedia di MovieLens Dataset (https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system?select=ratings.csv). Dataset ini mencakup berbagai informasi mengenai film, termasuk judul, genre, deskripsi, dan rating dari pengguna.

Beberapa fitur pada dataset ini meliputi:

title: Judul film.
genres: Kategori genre film, seperti action, drama, comedy, dll.
description: Deskripsi singkat tentang film.
user_ratings: Rating yang diberikan oleh pengguna terhadap film.
Pada tahap awal, kita akan memeriksa data untuk memastikan kualitas dan konsistensi dari dataset tersebut. Beberapa teknik visualisasi data dan analisis eksploratif akan digunakan untuk memahami distribusi data dan korelasi antar fitur.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data beserta insight atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
