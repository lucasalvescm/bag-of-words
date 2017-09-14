#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

dsMovies = open('movies.dat','r',encoding = "ISO-8859-1")


list_palavras = ['toy','story','sleepwalkers','kronos']

dict_words = {}
list_filmes = []

for row in dsMovies:
		vectorRow = row.split('::')
		objRow = {
			'id': vectorRow[0],
			'nome': vectorRow[1],
			'genero': vectorRow[2]
		}
		list_filmes.append(objRow['nome'])

for palavra in list_palavras:
	dict_unique = {}
	count_word = 0
	for filme in list_filmes:
		titulo_split = filme.split(" ")
		for titulo in titulo_split:
			if palavra.lower() == titulo.lower():
				count_word+=1
		dict_unique.update({filme.lower():count_word})				
	dict_words.update({palavra:dict_unique})	

print (dict_words)








