#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

dsMovies = open('movies.dat','r',encoding = "ISO-8859-1")


list_titulos = []

#Filtra o dataset de filmes por genero
for row in dsMovies:
    
    vectorRow = row.split('::')
    objRow = {
        'id': vectorRow[0],
        'nome': vectorRow[1],
        'genero': vectorRow[2]
    }
    if objRow['genero'] not in list_titulos:
        list_titulos.append( objRow['nome'])

print (list_titulos)