# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:01:03 2023

@author: icalc
"""
# Grafo como uma lista de adjacência

from pilha import Pilha
from grafoMatriz import Grafo as GrafoMatriz

class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]
        
	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w, distancia):
        self.listaAdj[v].append((w,distancia))
        self.listaAdj[w].append((v,distancia))
        self.m+=1
     
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        for aresta in self.listaAdj[v]:
            if aresta[0] == w: 
                self.listaAdj[v].remove(aresta)
            break
            
        for aresta in self.listaAdj[w]:
            if aresta[0] == v: 
                self.listaAdj[w].remove(aresta)
            break

        self.m-=1
    
    def inserirVND(self):

        self.listaAdj.append([])
        self.n += 1

    # Ex 29
    def removeVND(self, v):
        # enquanto houver elemento na lista de adjacência de "v"
        while len(self.listaAdj[v]) > 0:
            # armazena valor do vértice a ser removido
            vizinho = self.listaAdj[v][0][0]
            # remove na lista de adjacênciade "v" e na lista de adjacência de "vizinho"
            self.removeA(v, vizinho)
            self.m -= 1
        
        # percorre todos os vértices de índice maior que "v"
        for i in range((v+1),self.n):
            # empurra os vértices para um índice anterior na lista
            self.listaAdj[i-1] = self.listaAdj[i]
        # remove o último vértice (duplicado)
        for i in range(self.n):
            for j in range(len(self.listaAdj[i])):
                if self.listaAdj[i][j][0] > v:
                    self.listaAdj[i][j] = (self.listaAdj[i][j][0] - 1, self.listaAdj[i][j][1]) # cria nova tupla

        self.n -= 1 # decrementa variável n (vértices)s
        self.listaAdj.pop()
    
    #def visitarNo(self, v):
    #    print(f"{v}", end=" ")
    
    # função auxiliar da busca em profundidade
    def marcarNo(self, nosMarcados, nroNosMarcados, v):
        nosMarcados.append(v)
        nroNosMarcados += 1
        return nroNosMarcados

    # função auxiliar da busca em profundidade
    def noAdjacente(self, n, nosMarcados):
        for i in range(len(self.listaAdj[n])):
            adjacente = self.listaAdj[n][i][0]
            if (adjacente not in nosMarcados):
                return adjacente
        return -1
    
    # busca em profundidade enviada anteriormente (com alguns ajustes)
    def percursoProfundidade(self, v):
        nroNosMarcados = 0
        nosMarcados = []
        p = Pilha()
        #self.visitarNo(v) # print nó v
        nroNosMarcados = self.marcarNo(nosMarcados, nroNosMarcados, v) # adiciona nó v ao vetor de nós marcados
        p.push(v)
        while (not p.isEmpty()):
            n = p.pop()
            m = self.noAdjacente(n, nosMarcados) # verifica se há nó adjacente, se houver retorna nó adjacente
            while (m != -1):
                #self.visitarNo(m)
                p.push(n)
                nroNosMarcados = self.marcarNo(nosMarcados, nroNosMarcados, m)
                n = m
                m = self.noAdjacente(n, nosMarcados)

        # verifica se o número de vértices
        num_vertices = self.n
        if (nroNosMarcados == num_vertices):
            return True
        else:
            return False

    def gravarInfo(self, arquivo):

        for i in range(self.n):
            for j in range(len(self.listaAdj[i])):
                arquivo.write(f"{i+1}, {self.listaAdj[i][j][0] + 1}, {self.listaAdj[i][j][1]} km\n")
        
	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a LISTA de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{(i+1):2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                vizinho = self.listaAdj[i][w][0] + 1
                distancia = self.listaAdj[i][w][1]

                print(f"({vizinho:d} , {distancia:.2f})", end=" ") 

        print("\n\nfim da impressao do grafo." )
        