#this file is fro those who wants to practise BS4 different methods() how they are implemented and what output it gives. index.html file is used as a scrapper to practise on.
#Have Fun !!

from bs4 import BeautifulSoup
import lxml
import os

with open('index.html' , 'r') as file:
    body = file.read()

# path = os.getcwd()
# print(path)
# html = os.path.join(path, 'index.htm')
# print(html)

# with open(html, 'r') as file:
#     body = file.read()

soup = BeautifulSoup(body, 'lxml')
# soup = soup.prettify()
# print(soup)

#get the title
# title_tag = soup.title
# print(title_tag)
# print(title_tag.name)
# print(title_tag.get_text())

# #get the paragraph
# paragraph = soup.p
# print(paragraph)
# print(paragraph.name)
# print(paragraph.get_text())

#get the first div
# first_div = soup.find('div')
# print(first_div)
# print(first_div.get_text())

#get all the divs
# all_divs = soup.find_all('div')
# print(all_divs)
# for div in all_divs:
#     print('------')
#     print('------')
#     print('------')
#     print(div)

# get the first movie
# first_movie = soup.find('div',class_='movie')
# first_movie = soup.select('.movie')[0]
# print(first_movie)
# print(first_movie.get_text())

#get all movies 
# all_movies = soup.find_all('div', class_='movie')
# all_movies = soup.select(selector = '.movie')
# for movie in all_movies:
#     print('----')
#     print(movie.get_text())

#get all the link of the movies
# all_movie_links = soup.find_all('a')
# for link in all_movie_links:
#     print(link.get('href'))

#get element by id
# movie_box = soup.select_one('#movie-box')
# print(movie_box)
# print(movie_box.get_text())

#parent/childern
# parent = movie_box.parent
# print(parent)

# children = movie_box.children
# for child in children:
#     print('-----')
#     print(child)

# movie = soup.find('div', class_='movie')
# parent = movie.find_parent()
# print(parent)
# print('------')
# print('------')
# print('------')
# parent = movie.find_parent('div')
# print(parent)

interstellar = soup.find(text='Interstellar')
print(interstellar)
print(interstellar.find_parent())
print(interstellar.find_parent('div'))
print(interstellar.find_parent('a'))