import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Загрузить данные из файла в DataFrame
df = pd.read_csv('movies_emotions.csv')

# Создать первую диаграмму - распределение эмоций по жанрам
fig, ax1 = plt.subplots(figsize=(10, 10))
ax1.set_title('Частота жанров по эмоции')
emotions_top10 = df['Эмоция'].value_counts().nlargest(10)
genres_top10 = df['Жанр'].value_counts().nlargest(10)
genres_by_emotions = df[df['Эмоция'].isin(emotions_top10.index) & df['Жанр'].isin(genres_top10.index)]
genres_by_emotions_pivot = genres_by_emotions.pivot_table(index='Жанр', columns='Эмоция', values='Название фильма', aggfunc='count', fill_value=0)
genres_by_emotions_pivot.plot(kind='bar', stacked=True, ax=ax1)
plt.xticks(rotation=45)

# Создать вторую диаграмму - средний рейтинг фильмов по жанрам
fig, ax2 = plt.subplots(figsize=(10, 10))
ax2.set_title('Средний рейтинг фильмов по жанрам')
mean_rating = df.groupby('Жанр')['Рейтинг фильма'].mean()
mean_rating.plot(ax=ax2)
plt.xticks(rotation=45)

# Создать третью диаграмму - облако слов жанров по количеству фильмов
fig, ax3 = plt.subplots(figsize=(10, 10))
ax3.set_title('Облако слов жанров по количеству фильмов')
genres_count = df['Жанр'].value_counts().to_dict()
wordcloud = WordCloud(width=800, height=800, background_color='white').generate_from_frequencies(genres_count)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Создать четвертую диаграмму - топ-10 фильмов с самой высокой оценкой
fig, ax4 = plt.subplots(figsize=(10, 10))
ax4.set_title('Топ-10 фильмов с самой высокой оценкой')
top_movies = df.nlargest(80, 'Рейтинг фильма').sort_values(by='Рейтинг фильма')
ax4.barh(top_movies['Название фильма'], top_movies['Рейтинг фильма'])
ax4.set_xlabel('Рейтинг')
ax4.set_ylabel('Фильм')

# Вывести все диаграммы на одном листе
plt.tight_layout()
plt.show()
