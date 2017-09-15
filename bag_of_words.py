#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.tools.plotting import table
dsMovies = open('movies.dat','r',encoding = "ISO-8859-1")
from math import sqrt

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
list_final =[]
# file = open('testfile.txt','w') 
# for palavra in list_filter_movies:
# 	dict_unique = {}
# 	dict_words={}	
# 	#print (palavra)
# 	#import ipdb;ipdb.set_trace()
# 	for filme in list_filmes:
# 		#print(filme)
# 		palavra_in_titulo = 0
# 		titulo_split = filme.split(" ")
# 		titulo_split = [element.lower() for element in titulo_split] #transformo todos os itens da lista para minusculo
# 		if palavra.lower() in titulo_split:
# 			palavra_in_titulo = 1

# 		dict_unique.update({filme.lower():palavra_in_titulo})
# 	dict_words.update({palavra:dict_unique})
# 	file.write(str(dict_words)+'\n')
# 	list_final.append(dict_words)
	

# file.close()



for filme in list_filmes:
	dict_unique ={}
	dict_words={}
	for palavra in list_filter_movies:
		#print(filme)
		palavra_in_titulo = 0
		titulo_split = filme.split(" ")
		titulo_split = [element.lower() for element in titulo_split] #transformo todos os itens da lista para minusculo
		if palavra.lower() in titulo_split:
			palavra_in_titulo = 1

		dict_unique.update({palavra:palavra_in_titulo})

	dict_words.update({filme:dict_unique})
	list_final.append(dict_words)

#print (list_final)


dict_test = {}
for obj in list_final:
	for key, value in obj.items():
		#print(str(key)+''+str(value))
		dict_test.update({key:value})



matriz = pd.DataFrame(dict_test) #transforma o dicionario em matriz.




def calculate_docs(list1,list2):

	list_values_up = [x*y for x,y in zip(list1, list2)]
	print(list1)
	print(list2)
	print(list_values_up)

	doc1 = 0
	doc2 = 0

	for l1 in list1:
		if l1 == 1:
			doc1+=1

	for l2 in list2:
		if l2 == 1:
			doc2+=1


	division = sum(list_values_up) / (sqrt(doc1)*sqrt(doc2))

	print (division)

	

l_=[]

dict_final={}

#Faz o dicionario final para fazer o calculo. Padrão do dicionario: {nome_do_filme:[1,0,0,1]} . O valor é a linha do "documento"
for nome_filme,v in dict_test.items():
	
	temp = []
	for key, value in v.items():
		temp.append(value)

	dict_final.update({nome_filme:temp})
	

print(dict_final)


for k1,v1 in dict_final.items():
	for k2,v2 in dict_final.items():
		if v2 != v1:
			calculate_docs(v1,v2)





# #Método para exportar a matriz como png
# def matrix_to_png(a):
# 	a.index = [item for item in a.index] # Format date

# 	fig, ax = plt.subplots(figsize=(40, 15)) # set size frame
# 	ax.xaxis.set_visible(False)  # hide the x axis
# 	ax.yaxis.set_visible(False)  # hide the y axis
# 	ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
# 	tabla = table(ax, a, loc='upper right', colWidths=[0.01]*len(a.columns))  # where df is your data frame
# 	tabla.auto_set_font_size(False) # Activate set fontsize manually
# 	tabla.set_fontsize(20) # if ++fontsize is necessary ++colWidths
# 	tabla.scale(4,5) # change size table
# 	plt.savefig('table.png', transparent=True)




#matrix_to_png(matriz)










