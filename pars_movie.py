from bs4 import BeautifulSoup
import requests
import pandas as pd

soup = BeautifulSoup(requests.get('https://yupest.github.io/nti/%D0%9D%D0%A2%D0%98-2022/films/').text, 'html.parser') #Заходим на искомый сайт

movies_list = [] #В этот список будем записывать словари с данными фильмов
for item in soup.find_all('div', {'movie-head'}): #Проходимся по всем блокам с фильмами
    movie_head = item.find('h1').text.split() #Выделяем название
    emotions = [i.text for i in item.find_all('li', {'emotion'})] #Так как будем разделять по эмоциям, заранее их выделяем в список
    for i in range(len(emotions)): #В цикле рабиваем каждый фильм по его эмоциям и записывает всю информацию в словари
        movies_list.append({'Код фильма': int(movie_head[0]),
                            'Название': ' '.join(movie_head[1:]),
                            'Жанры': ', '.join([i.text for i in item.find_all('li', {'genre'})]),
                            'Рейтинг': float(item.find('li', {'name': 'rating_film'}).text),
                            'Эмоции': emotions[i],
                            'Рейтинг эмоций': [float(i.text) for i in item.find_all('div', {'s-text'})][i]})

df = pd.DataFrame(movies_list) #Сохраняем в ехсель табличку
df.to_excel('movies.xlsx')