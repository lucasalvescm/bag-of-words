#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dsMovies = open('movies.dat','r',encoding = "ISO-8859-1")


#Atributos
list_all_movies = [] #Lista com os nomes de todos os filmes
list_filter_movies =[] #Lista com os nomes de todos os filmes sem repitir
list_words_exclude = ['the','is','of','in','that','and','our'] #Palavras para desconsiderar
list_filmes = []

#Filtra o dataset
count = 0
for row in dsMovies:
	if count<10:
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
list_final =[]
file = open('testfile.txt','w') 
for palavra in list_filter_movies:
	dict_unique = {}
	dict_words={}	
	#print (palavra)
	#import ipdb;ipdb.set_trace()
	for filme in list_filmes:
		#print(filme)
		palavra_in_titulo = 0
		titulo_split = filme.split(" ")
		titulo_split = [element.lower() for element in titulo_split] #transformo todos os itens da lista para minusculo
		if palavra.lower() in titulo_split:
			palavra_in_titulo = 1

		dict_unique.update({filme.lower():palavra_in_titulo})
	dict_words.update({palavra:dict_unique})
	file.write(str(dict_words)+'\n')
	list_final.append(dict_words)
	

file.close()
dict_test = {}
for obj in list_final:
	for key, value in obj.items():
		dict_test.update({key:value})


a = pd.DataFrame(dict_test)

print (a)















