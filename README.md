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

- Pernyataan Masalah 1: Pengguna mengalami kesulitan dalam menemukan film yang sesuai dengan preferensi mereka di tengah banyaknya pilihan yang tersedia.
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

![Dataset](https://github.com/iqkyu5566/movie_recomendation/blob/main/img/1.png?raw=true)

### Exploratory Data Analysis (EDA)

Tahap eksplorasi sangat penting untuk memahami variabel-variabel dalam data serta hubungan antar variabel. Pemahaman ini akan memandu kita dalam memilih pendekatan atau algoritma yang tepat. Sebaiknya, eksplorasi data dilakukan terhadap seluruh variabel untuk memperoleh gambaran yang komprehensif. Exploratory Data Analysis (EDA) memiliki peran krusial dalam memahami dataset secara mendalam dan menyeluruh.

---

Berikut adalah beberapa pertanyaan yang akan kita jawab dengan menggunakan EDA untuk sistem rekomendasi Film, berdasarkan informasi yang diberikan:

Dengan EDA, kita bisa mengeksplorasi berbagai pola yang muncul dalam dataset film yang diberikan oleh pengguna, serta menganalisis preferensi dan tren terkait film.

**1. Bagaimana distribusi rating yang diberikan oleh pengguna terhadap film?**

Pertanyaan ini akan membantu kita memahami sebaran rating yang diberikan oleh pengguna, apakah ada kecenderungan rating tinggi atau rendah, dan apakah rating lebih sering diberikan pada film-film tertentu.

![EDA1](https://github.com/iqkyu5566/movie_recomendation/blob/main/img/eda1.png?raw=true)

**Apakah ada hubungan antara jumlah rating yang diberikan oleh pengguna dengan rating rata-rata yang mereka berikan?**

Pertanyaan ini bertujuan untuk mengeksplorasi apakah pengguna yang memberikan lebih banyak rating cenderung memberikan rating yang lebih tinggi atau lebih rendah secara konsisten. Misalnya, apakah pengguna yang aktif menilai banyak film cenderung memberikan rating tinggi pada semua film atau lebih cenderung memberi rating lebih rendah.

Untuk menjawab pertanyaan ini, kita akan menghitung jumlah rating yang diberikan oleh masing-masing pengguna dan mengukur rata-rata rating mereka. Kemudian, kita dapat memvisualisasikan hubungan antara jumlah rating yang diberikan dan rating rata-rata yang diberikan oleh pengguna.

![EDA2](https://github.com/iqkyu5566/movie_recomendation/blob/main/img/eda2.png?raw=true)

## Data Preparation

Langkah-langkah berikut telah dilakukan untuk mempersiapkan data sebelum digunakan dalam model:

1.  Membersihkan Data: Menghapus data yang tidak relevan atau duplikat, serta menangani nilai yang hilang.

    #Mengatasi Missing Value
    data = data.dropna()
    #Mengatasi Missing Value
    data.isnull().sum()

            0
        movieId	0
        title	0
        genres	0
        userId	0
        rating	0
        timestamp	0

        dtype: int64

        # Membuang data duplikat pada variabel preparation
        preparation = preparation.drop_duplicates('title')
        preparation

Transformasi Data: Mengonversi kolom data menjadi list

    #konversi data menjadi list
    #Mengonversi data series 'title' menjadi dalam bentuk list
    title_list = preparation['title'].tolist()

    #Mengonversi data series 'genres' menjadi dalam bentuk list
    genres_list = preparation['genres'].tolist()

    #Mengonversi data series 'rating' menjadi dalam bentuk list
    rating_list = preparation['rating'].tolist()

    print(len(title_list))
    print(len(genres_list))
    print(len(rating_list))


    #Membuat Dictonary untuk menentukan pasangan Key - Value pada data yang telah di siapkan
    movie_new = pd.DataFrame({'title': title_list, 'genres': genres_list, 'rating': rating_list})
    movie_new

    #konversi semuanya ke object
    movie_new = movie_new.astype(object)

Membuat TF-IDF

        fantasy	imax	film	war	romance	noir	western	sci	drama	horror
        title
        M.F.A. (2017)	0.0	0.0	0.0	0.0	0.000000	0.0	0.0	0.000000	0.000000	0.000000
        Night Must Fall (1937)	0.0	0.0	0.0	0.0	0.000000	0.0	0.0	0.000000	0.000000	0.000000
        Pathey Holo Deri	0.0	0.0	0.0	0.0	0.777904	0.0	0.0	0.000000	0.628384	0.000000
        Invisible Woman, The (2013)	0.0	0.0	0.0	0.0	0.777904	0.0	0.0	0.000000	0.628384	0.000000
        Alexia (2013)	0.0	0.0	0.0	0.0	0.000000	0.0	0.0	0.000000	0.000000	0.720578
        Newness (2017)	0.0	0.0	0.0	0.0	0.777904	0.0	0.0	0.000000	0.628384	0.000000
        The Nurse (2017)	0.0	0.0	0.0	0.0	0.000000	0.0	0.0	0.000000	0.000000	1.000000
        Perfect Sense (2011)	0.0	0.0	0.0	0.0	0.470713	0.0	0.0	0.562960	0.380238	0.000000
        Dirty Dancing: Havana Nights (2004)	0.0	0.0	0.0	0.0	1.000000	0.0	0.0	0.000000	0.000000	0.000000
        Dead of Night (1977)	0.0	0.0	0.0	0.0	0.000000	0.0	0.0	0.480693	0.000000	0.332499

Feature Engineering: Membuat fitur baru seperti content_similarity untuk menghitung kesamaan antar film berdasarkan title dan genres.
Hasilnya :

    array([[1., 1., 1., ..., 0., 0., 0.],
           [1., 1., 1., ..., 0., 0., 0.],
           [1., 1., 1., ..., 0., 0., 0.],
           ...,
           [0., 0., 0., ..., 1., 1., 1.],
           [0., 0., 0., ..., 1., 1., 1.],
           [0., 0., 0., ..., 1., 1., 1.]])

Dataframe hasil dari variabel cosine_sim dengan baris dan kolom berupa nama film

![Hasil ConsineSimilarity](https://github.com/iqkyu5566/movie_recomendation/blob/main/img/2.png?raw=true)

Dengan cosine similarity, kita berhasil mengidentifikasi tingkat kesamaan antara satu film dengan film lainnya. Shape (10000, 10000) mengindikasikan ukuran matriks kesamaan dari data yang kita miliki. Matriks ini berukuran 10000 film x 10000 film, yang menunjukkan tingkat kesamaan antara 10000 film yang ada dalam dataset. Namun, kita tidak dapat menampilkan keseluruhan matriks karena ukurannya yang sangat besar, sehingga hanya sebagian kecil yang dapat kita tampilkan.

Pada contoh di atas, matriks yang ditampilkan mencakup sebagian dari 10000 film, di mana baris vertikal (sumbu Y) mewakili film yang diuji, dan kolom horizontal (sumbu X) mewakili film yang dibandingkan. Dalam hal ini, kita hanya memilih untuk menampilkan 5 film pada sumbu horizontal dan 5 film pada sumbu vertikal dari matriks kesamaan yang lebih besar.

Perhatikan angka-angka yang ada di dalam matriks tersebut, yang mewakili cosine similarity antara film pada baris dan kolom yang bersesuaian. Misalnya, film "Smile (2009)" memiliki tingkat kesamaan 0.305 dengan "Cult (2013)", 0.721 dengan "Coven (2000)", dan 0.000 dengan "Burmese Harp, The (Biruma no tategoto) (1956)". Nilai-nilai ini menunjukkan sejauh mana dua film tersebut memiliki kesamaan berdasarkan genre, rating, atau fitur lain yang digunakan dalam perhitungan cosine similarity.

Sebagai contoh, film "Smile (2009)" dan "Necromancer (1988)" memiliki tingkat kesamaan yang cukup tinggi, yaitu 0.305. Ini mengindikasikan bahwa kedua film ini memiliki karakteristik atau fitur yang cukup mirip. Di sisi lain, film "Ugly (2013)" tidak memiliki kesamaan yang signifikan dengan film lainnya dalam subset ini, yang tercermin dari nilai-nilai 0.0 di seluruh kolomnya.

Secara keseluruhan, matriks ini memungkinkan kita untuk mengidentifikasi pasangan-pasangan film yang memiliki kemiripan berdasarkan kriteria yang digunakan dalam perhitungan similarity, yang dapat digunakan untuk membuat sistem rekomendasi film yang lebih akurat.

## Modeling

Pada tahap ini, kita membangun model sistem rekomendasi berbasis Content-Based Filtering menggunakan Cosine Similarity. Kosinus similiarity menghitung kesamaan antara dua vektor berdasarkan sudutnya, yang dapat diukur dengan rumus:

![Rumus 1](https://github.com/iqkyu5566/movie_recomendation/blob/main/img/r1.png?raw=true)

Model ini akan mengambil judul film yang diberikan, menghitung kesamaan dengan film lainnya, dan memberikan rekomendasi berdasarkan skor kesamaan tertinggi.

    # Misalnya, Anda ingin mendapatkan rekomendasi untuk film berjudul 'Smile (2009)'
    recommended_movies = movie_recommendations('Smile (2009)', cosine_sim_df, data[['title', 'genres']], k=10)

    # Menampilkan rekomendasi
    print(recommended_movies)

hasilnya :

     title           genres
    3265                                      Dogs (1976)  Horror|Thriller
    3266                                Sanitarium (2013)  Horror|Thriller
    3267                         Sadako vs. Kayako (2016)  Horror|Thriller
    3268                                 Cassadaga (2011)  Horror|Thriller
    3269                           The Evil Within (2017)  Horror|Thriller
    3270                               Lake Placid (1999)  Horror|Thriller
    3271                             Strait-Jacket (1964)  Horror|Thriller
    3272                           Innkeepers, The (2011)  Horror|Thriller
    3273  Thirteen Ghosts (a.k.a. Thir13en Ghosts) (2001)  Horror|Thriller
    3276                                   Shrooms (2007)  Horror|Thriller

# Evaluation

Untuk mengevaluasi kinerja model, kita menggunakan beberapa metrik yang relevan dengan sistem rekomendasi:

1.  Precision: Mengukur seberapa banyak rekomendasi yang diberikan relevan dengan pengguna.
    ![Precission](https://github.com/iqkyu5566/movie_recomendation/blob/main/img/r2.png?raw=true)

2.  Recall: Mengukur seberapa banyak item relevan yang berhasil direkomendasikan.
    ![Recall](https://github.com/iqkyu5566/movie_recomendation/blob/main/img/r3.png?raw=true)

        # Menghitung True Positives (TP), False Positives (FP), False Negatives (FN)
        tp = len(set(ground_truth) & set(recommended_titles))  # Intersection antara ground_truth dan recommended_titles
        fp = len(set(recommended_titles) - set(ground_truth))  # Film yang direkomendasikan tapi tidak relevan
        fn = len(set(ground_truth) - set(recommended_titles))  # Film relevan yang tidak direkomendasikan

        # Menghitung Precision dan Recall
        precision = tp / (tp + fp) if tp + fp > 0 else 0
        recall = tp / (tp + fn) if tp + fn > 0 else 0

        # Menampilkan hasil Precision dan Recall
        print(f"Precision: {precision:.2f}")
        print(f"Recall: {recall:.2f}")

hasilnya :

    Precision: 1.00
    Recall: 0.01

Hasil Precision: 1.00 dan Recall: 0.01 menunjukkan dua hal yang berbeda:

1. Precision: 1.00
   Precision yang tinggi (1.00) berarti bahwa semua rekomendasi yang diberikan oleh sistem relevan. Artinya, semua film yang direkomendasikan (dalam daftar recommended_titles) benar-benar ada dalam ground truth yang relevan.

Contoh: Jika sistem merekomendasikan 10 film, maka semua 10 film itu ada di dalam ground truth, yang berarti tidak ada rekomendasi yang salah (False Positive).

2. Recall: 0.01
   Namun, Recall yang sangat rendah (0.01) menunjukkan bahwa hanya sebagian kecil film relevan yang direkomendasikan oleh sistem. Dengan kata lain, sistem hanya berhasil merekomendasikan sebagian kecil dari film yang relevan yang ada dalam ground truth.

Contoh: Jika ground truth berisi 100 film relevan, tetapi sistem hanya berhasil merekomendasikan 1 film dari 100 yang relevan, maka Recall akan rendah meskipun Precision tinggi.

Apa yang bisa diambil dari hasil ini?
Precision yang tinggi menunjukkan bahwa sistem Anda melakukan rekomendasi yang sangat baik untuk film relevan yang dipilih. Namun, ini tidak cukup jika Recall Anda rendah.
Recall yang rendah mengindikasikan bahwa meskipun rekomendasi yang diberikan akurat, sistem tidak dapat menemukan banyak film relevan. Sistem mungkin hanya memberikan beberapa rekomendasi atau tidak cukup eksploratif dalam memberikan lebih banyak film relevan.

Cara yang bisa dilakukan lagi :
Meningkatkan Diversitas dalam Rekomendasi Pastikan bahwa sistem memberikan rekomendasi film yang lebih beragam namun tetap relevan. Jika sistem terlalu fokus pada beberapa film saja, maka Recall akan sangat rendah. Anda bisa mencoba menggunakan pendekatan diversifikasi atau memilih film dengan kesamaan genre yang lebih luas.

Perbaiki Penyesuaian Filter Genre Pastikan bahwa film yang direkomendasikan tidak hanya berdasarkan genre yang sangat sempit, sehingga rekomendasi lebih bervariasi tetapi tetap relevan. Jika genre terlalu spesifik, sistem mungkin tidak menemukan banyak pilihan relevan.

Model Peningkatan Rekomendasi Jika menggunakan sistem content-based filtering, coba juga tambahkan elemen collaborative filtering (misalnya, berdasarkan rating pengguna) untuk meningkatkan jumlah film relevan yang ditemukan.

## Conclusion

Precision yang tinggi menunjukkan bahwa sistem memberikan rekomendasi yang relevan, namun Recall yang rendah berarti sistem gagal untuk menemukan cukup banyak film relevan.
Meningkatkan k, memperluas genre yang dipertimbangkan, atau menambah elemen collaborative filtering dapat membantu meningkatkan Recall.
