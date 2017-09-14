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

#Filtra o dataset
count = 0
for row in dsMovies:
	if count<3:
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
	else:
		break

	count +=1

file = open('testfile.txt','w') 
for palavra in list_filter_movies:
	dict_unique = {}
	dict_words={}	
	#print (palavra)
	#import ipdb;ipdb.set_trace()
	for filme in list_filmes:
		#print(filme)
		count_word = 0
		titulo_split = filme.split(" ")
		titulo_split = [element.lower() for element in titulo_split]
		if palavra.lower() in titulo_split:
			count_word = 1

		dict_unique.update({filme.lower():count_word})
	dict_words.update({palavra:dict_unique})

	file.write(str(dict_words)+'\n')

file.close()







