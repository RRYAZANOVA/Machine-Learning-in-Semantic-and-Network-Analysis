#!/usr/bin/env python
# coding: utf-8

# Рязанова Маргарита, ПМ22-6

# # Задание

# 1. Скачать или получить любой датасет
# 2. При помощи библиотеки networkx построить граф на основе датасета

# # Решение

# Набор данных содержит героев и комиксы, а также отношения между ними. Набор данных разделен на три файла:
# - 
# nodes.csv : Содержит два столбца (узел, тип), указывающие имя и тип (комикс, герой) узло  в- 
# edge.csv : Содержит два столбца (герой, комикс), указывающие, в каких комиксах появляются гер   о- и.
# hero-edge.csv : Содержит сеть героев, которые появляются вместе в комиксvel/

# In[18]:


import numpy as np 
import pandas as pd 
import networkx as nx
import matplotlib.pyplot as plt


# In[19]:


nodes = pd.read_csv('C://Users//222868//Downloads//nodes.csv')
print(nodes.head())


# In[20]:


edges = pd.read_csv('C://Users//222868//Downloads//edges.csv')
print(edges.head())


# In[21]:


hero_network = pd.read_csv('C://Users//222868//Downloads//hero-network.csv')
print(hero_network.head())


# In[24]:


Thor = hero_network[hero_network['hero1']=='THOR/DR. DONALD BLAK'].sample(25)
Thor.head()


# In[25]:


Cap = Subset = hero_network[hero_network['hero1']=='CAPTAIN AMERICA'].sample(25)
Cap.head()


# In[26]:


IronMan = hero_network[hero_network['hero1'].str.contains('IRON MAN/TONY STARK')].sample(25)
IronMan.head()


# In[28]:


Subset = pd.concat([Thor,Cap,IronMan],axis = 0)
Subset.head()


# In[14]:


G = nx.from_pandas_edgelist(Subset, 'hero1', 'hero2')
plt.figure(figsize = (20,20))
nx.draw(G, with_labels=True, node_size = 8)
plt.show()


# In[15]:


list(G.neighbors('CAPTAIN AMERICA'))


# In[16]:


degrees = [len(list(G.neighbors(n))) for n in G.nodes()]
[str(x) + '----' + str(y) for x,y in zip(G.nodes(),degrees)]


# In[17]:


H=nx.from_pandas_edgelist(hero_network, 'hero1', 'hero2')
nx.shortest_path(H,'THOR/DR. DONALD BLAK','MOON KNIGHT DOPPELGA')

