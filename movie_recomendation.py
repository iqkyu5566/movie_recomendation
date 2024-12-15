# -*- coding: utf-8 -*-
"""Movie_Recomendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WSoVFqYUvDQg9uD57f_Uo_6yMfUtGYbh

Proyek Machine Learning :
**Rekomendasi Film**

Topik : Rekomendasi Film

Tujuan : Memberikan rekomendasi film berdasarkan preferensi konsumen dengan memanfaatkan popularitas

Dataset yang digunakan : https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system?select=ratings.csv

Melakukan Import terhadap Library yang diperlukan
"""

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import re

"""pandas: Digunakan untuk memanipulasi data dalam
bentuk tabel (DataFrame).
numpy: Digunakan untuk operasi numerik.

matplotlib.pyplot dan seaborn: Digunakan untuk visualisasi data.

**DATA UNDERSTANDING**
"""

movies = pd.read_csv("/content/movies.csv")

movies.head()

movies.isna().sum()

print("Jumlah duplikat:", movies.duplicated().sum())

movies.describe()

rating = pd.read_csv("/content/ratings.csv")

rating.head()

rating.isna().sum()

rating.describe()

#Menggabungkan tabel movie dan ratings
movie_review = pd.merge(movies, rating, on='movieId')
movie_review

"""**Exploratory Data Analysis (EDA)**

---

Tahap eksplorasi sangat penting untuk memahami variabel-variabel dalam data serta hubungan antar variabel. Pemahaman ini akan memandu kita dalam memilih pendekatan atau algoritma yang tepat. Sebaiknya, eksplorasi data dilakukan terhadap seluruh variabel untuk memperoleh gambaran yang komprehensif. Exploratory Data Analysis (EDA) memiliki peran krusial dalam memahami dataset secara mendalam dan menyeluruh.

---

Berikut adalah beberapa pertanyaan yang akan kita jawab dengan menggunakan EDA untuk sistem rekomendasi Film, berdasarkan informasi yang diberikan:



Dengan EDA, kita bisa mengeksplorasi berbagai pola yang muncul dalam dataset film yang diberikan oleh pengguna, serta menganalisis preferensi dan tren terkait film.

*Kita akan mengeksplorasi data sesuai dengan pertanyaan diatas.*

**1. Bagaimana distribusi rating yang diberikan oleh pengguna terhadap film?**

Pertanyaan ini akan membantu kita memahami sebaran rating yang diberikan oleh pengguna, apakah ada kecenderungan rating tinggi atau rendah, dan apakah rating lebih sering diberikan pada film-film tertentu.
"""

import matplotlib.pyplot as plt

# Visualisasi distribusi rating yang diberikan oleh pengguna
plt.figure(figsize=(10,6))
plt.hist(movie_review['rating'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribusi Rating yang Diberikan oleh Pengguna')
plt.xlabel('Rating')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

"""**Apakah ada hubungan antara jumlah rating yang diberikan oleh pengguna dengan rating rata-rata yang mereka berikan?**

Pertanyaan ini bertujuan untuk mengeksplorasi apakah pengguna yang memberikan lebih banyak rating cenderung memberikan rating yang lebih tinggi atau lebih rendah secara konsisten. Misalnya, apakah pengguna yang aktif menilai banyak film cenderung memberikan rating tinggi pada semua film atau lebih cenderung memberi rating lebih rendah.

Untuk menjawab pertanyaan ini, kita akan menghitung jumlah rating yang diberikan oleh masing-masing pengguna dan mengukur rata-rata rating mereka. Kemudian, kita dapat memvisualisasikan hubungan antara jumlah rating yang diberikan dan rating rata-rata yang diberikan oleh pengguna.
"""

# Menghitung jumlah rating yang diberikan oleh setiap pengguna
user_rating_count = movie_review.groupby('userId')['rating'].count()

# Menghitung rating rata-rata yang diberikan oleh setiap pengguna
user_avg_rating = movie_review.groupby('userId')['rating'].mean()

# Menggabungkan jumlah rating dan rating rata-rata dalam satu dataframe
user_rating_summary = pd.DataFrame({
    'rating_count': user_rating_count,
    'avg_rating': user_avg_rating
})

# Visualisasi hubungan antara jumlah rating dan rating rata-rata
plt.figure(figsize=(10,6))
plt.scatter(user_rating_summary['rating_count'], user_rating_summary['avg_rating'], alpha=0.5, color='purple')
plt.title('Hubungan antara Jumlah Rating dan Rating Rata-Rata Pengguna')
plt.xlabel('Jumlah Rating yang Diberikan')
plt.ylabel('Rating Rata-Rata Pengguna')
plt.grid(True)
plt.show()

# Menghitung korelasi antara jumlah rating dan rating rata-rata
correlation = user_rating_summary['rating_count'].corr(user_rating_summary['avg_rating'])
print(f"Korelasi antara jumlah rating dan rating rata-rata: {correlation}")

"""**DATA PREPARATION**"""

data = movie_review
data.head()

#Mengatasi Missing Value
data = data.dropna()

#Mengatasi Missing Value
data.isnull().sum()

fix_rating = data.sort_values('genres', ascending=False)
fix_rating

#Variabel preparation
preparation = fix_rating[['title', 'genres', 'rating']]
preparation.sort_values('genres', ascending=True)

# Membuang data duplikat pada variabel preparation
preparation = preparation.drop_duplicates('title')
preparation

import pandas as pd

# Misalkan title_list, genres_list, rating_list sudah ada dan berisi data

# Ambil 10000 data pertama
preparation = preparation.head(10000)

# Menampilkan data movie_new_10000
print(preparation)

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

movie_new.info()

"""**Model Development dengan Content Based Filtering**

Setelah melakukan serangkaian tahapan :
- Data Understanding.
- Univariate Exploratory Data Analysis.
- Data Preprocessing.
- Data Preparation.

sekarang saatnya untuk kita mengembangkan model sistem rekomendasi dalam hal ini kita menggunakan pendekatan content based filtering.
"""

data = movie_new
data.sort_values('genres', ascending=True)

#TF-IDF Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

#inisialisasi TF-IDF Vectorizer
tf = TfidfVectorizer()

#melakukan perhitungan TF IDF pada followers
tf.fit(data['genres'])

#Mapping array dari fitur index integer ke fitur utama
tf.get_feature_names_out()

#Melakukan fit lalu di transformasikan dalam bentuk matrix
tf_matrix = tf.fit_transform(data['genres'])
tf_matrix.shape

#Mengubah vektor tf-idf dalam bentuk matrix dengan fungsi todense()
tf_matrix.todense()

#Membuat dataframe untuk melihat tf-id matrix, kolomnya di isi dengan dataframe title dan author order by matriks yang bernilai 1
pd.DataFrame(
    tf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.title
).sample(10, axis=1).sample(10, axis=0)

# #Consine Similarity
# # Pada tahap sebelumnya, kita telah berhasil mengidentifikasi korelasi antara movie dengan kategori movienya. Sekarang, kita akan menghitung derajat kesamaan (similarity degree) antar restoran dengan teknik cosine similarity. Di sini, kita menggunakan fungsi cosine_similarity dari library sklearn.
from sklearn.metrics.pairwise import cosine_similarity

# # Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama film
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['title'], columns=data['title'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap film
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""Dengan cosine similarity, kita berhasil mengidentifikasi tingkat kesamaan antara satu film dengan film lainnya. Shape (10000, 10000) mengindikasikan ukuran matriks kesamaan dari data yang kita miliki. Matriks ini berukuran 10000 film x 10000 film, yang menunjukkan tingkat kesamaan antara 10000 film yang ada dalam dataset. Namun, kita tidak dapat menampilkan keseluruhan matriks karena ukurannya yang sangat besar, sehingga hanya sebagian kecil yang dapat kita tampilkan.

Pada contoh di atas, matriks yang ditampilkan mencakup sebagian dari 10000 film, di mana baris vertikal (sumbu Y) mewakili film yang diuji, dan kolom horizontal (sumbu X) mewakili film yang dibandingkan. Dalam hal ini, kita hanya memilih untuk menampilkan 5 film pada sumbu horizontal dan 5 film pada sumbu vertikal dari matriks kesamaan yang lebih besar.

Perhatikan angka-angka yang ada di dalam matriks tersebut, yang mewakili cosine similarity antara film pada baris dan kolom yang bersesuaian. Misalnya, film "Smile (2009)" memiliki tingkat kesamaan 0.305 dengan "Cult (2013)", 0.721 dengan "Coven (2000)", dan 0.000 dengan "Burmese Harp, The (Biruma no tategoto) (1956)". Nilai-nilai ini menunjukkan sejauh mana dua film tersebut memiliki kesamaan berdasarkan genre, rating, atau fitur lain yang digunakan dalam perhitungan cosine similarity.

Sebagai contoh, film "Smile (2009)" dan "Necromancer (1988)" memiliki tingkat kesamaan yang cukup tinggi, yaitu 0.305. Ini mengindikasikan bahwa kedua film ini memiliki karakteristik atau fitur yang cukup mirip. Di sisi lain, film "Ugly (2013)" tidak memiliki kesamaan yang signifikan dengan film lainnya dalam subset ini, yang tercermin dari nilai-nilai 0.0 di seluruh kolomnya.

Secara keseluruhan, matriks ini memungkinkan kita untuk mengidentifikasi pasangan-pasangan film yang memiliki kemiripan berdasarkan kriteria yang digunakan dalam perhitungan similarity, yang dapat digunakan untuk membuat sistem rekomendasi film yang lebih akurat.
"""

def movie_recommendations(title, similarity_data, items, k=50):
    # Mencari indeks film yang sesuai dengan judul yang diberikan
    idx = similarity_data.index.get_loc(title)

    # Mengambil nilai similarity untuk film yang dicari
    similarity_scores = similarity_data.iloc[idx]

    # Menemukan k film dengan kesamaan tertinggi selain film yang dicari
    similar_indexes = similarity_scores.argsort()[-(k+1):-1][::-1]  # Ambil k film teratas dan urutkan secara menurun

    # Menampilkan hasil rekomendasi, dengan menghapus film yang sama dengan input (title)
    recommendations = similarity_data.index[similar_indexes]

    # Menyaring film berdasarkan genre yang sama dengan film yang dicari
    movie_genre = items[items['title'] == title]['genres'].values[0]
    recommended_movies = items[items['genres'] == movie_genre]

    # Hanya ambil k film teratas yang memiliki genre yang sama
    recommended_movies = recommended_movies.head(k)

    return recommended_movies

# Misalnya, Anda ingin mendapatkan rekomendasi untuk film berjudul 'Smile (2009)'
recommended_movies = movie_recommendations('Smile (2009)', cosine_sim_df, data[['title', 'genres']], k=10)

# Menampilkan rekomendasi
print(recommended_movies)

"""**EVALUATION**"""

# Misalnya, kita ingin mendapatkan ground truth dari film yang memiliki genre yang sama
genre = 'Horror|Thriller'  # Misalnya genre yang relevan
ground_truth = data[data['genres'] == genre]['title'].tolist()

print(f"Ground truth for genre {genre}: {ground_truth}")

# Mendapatkan rekomendasi untuk film tertentu (misalnya 'Smile (2009)')
recommended_movies = movie_recommendations('Smile (2009)', cosine_sim_df, data[['title', 'genres']], k=10)

# Ambil daftar judul film dari hasil rekomendasi
recommended_titles = recommended_movies['title'].tolist()

# Tampilkan rekomendasi
print("Recommended titles:", recommended_titles)

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

from sklearn.metrics import confusion_matrix

# Membuat label biner untuk ground truth dan recommended titles
y_true = [1 if movie in ground_truth else 0 for movie in recommended_titles]
y_pred = [1] * len(recommended_titles)  # Semua film yang direkomendasikan dianggap relevan (1)

# Menampilkan confusion matrix
print(confusion_matrix(y_true, y_pred))