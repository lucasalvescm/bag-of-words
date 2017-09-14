#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

dsMovies = open('movies.dat','r',encoding = "ISO-8859-1")


#Atributos
list_all_movies = [] #Lista com os nomes de todos os filmes
list_filter_movies =[] #Lista com os nomes de todos os filmes sem repitir
list_words_exclude = ['the','is','of','in','that','and','our'] #Palavras para desconsiderar
list_filmes = []
dict_words={}
#Filtra o dataset
for row in dsMovies:
	vectorRow = row.split('::')
	objRow={
		'id': vectorRow[0],
		'nome': vectorRow[1],
		'genero': vectorRow[2]
	}
	list_filmes.append(objRow['nome'])
	movie_name = vectorRow[1].lower()
	movie_name = movie_name[0:len(movie_name) -7] #remove o ano do nome
	movie_name = movie_name.split(' ') #separa o nome de cada filme

	#Faz o filtro das palavras a desconsiderar e adiciona a lista de filmes
	for name in movie_name:
		if name not in list_words_exclude:
			list_all_movies.append(name)
			if name not in list_filter_movies:
				list_filter_movies.append(name)

file = open('testfile.txt','w') 
for palavra in list_filter_movies:
	dict_unique = {}
	count_word = 0
	#import ipdb;ipdb.set_trace()
	for filme in list_filmes:
		titulo_split = filme.split(" ")
		for titulo in titulo_split:
			if palavra.lower() == titulo.lower():
				count_word+=1
		dict_unique.update({filme.lower():count_word})
	dict_words.update({palavra:dict_unique})
	file.write(str(dict_words)+'\n')

file.close()

#print (dict_words)












# print(list_filter_movies)
# print(len(list_filter_movies))
# print(list_all_movies)
# print(len(list_all_movies))






