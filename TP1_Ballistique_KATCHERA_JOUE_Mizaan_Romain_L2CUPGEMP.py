    #!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" '
@author: mizaankatchera/romainjoue
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
import matplotlib.animation as animation


""" Affichage de la trajectoire d'une pokéball sur un pikachu en fonction des paramètres initiaux"""

#Intialisation des variables: 

x0,y0 = 0,0                            #position initiale pokeball
g = 9.81                               #constante de pesanteur
xc,yc=100,10                            #position initiale pikachu
vmin=m.sqrt((g*(xc**2+yc**2)/(2*yc)))  #vitesse minimale
v0=vmin+5                              #vitesse initiale (devant être supérieur à vmin)
  
#Equations

a=m.atan(yc/xc)                                #calcul angle 

t1=(np.sqrt(xc**2+yc**2)/v0)                   #moment de l'impact

t=np.arange(0,t1+0.03,0.05)                     #valeurs de t

v0x=v0*m.cos(a)
x2=v0x*t                           #composante verticale de la pokeball en fonction du temps
y2=-(g/2)*(x2/v0x)**2+m.tan(a)*x2  #composante horizontale de la pokeball en fonction du temps
y3=-(g/2)*t**2+yc                  #composante verticale de pikachu en fonction du temps


#Coordonnées impact (à t1)

xi=xc               #distance impact
yi=-(g/2)*t1**2+yc  #hauteur impact


fig = plt.figure()
plt.xlim(0,xc+10)                             # limites pour l’abscisse
plt.ylim(0,yc+10)                             # limites pour l’ordonnée
pokeball,=plt.plot([],[],'ko',ms=10,mfc='r')  #configuration pour l'animation de la pokeball
pikachu,=plt.plot([],[],'ko',ms=10,mfc='y')   #configuration pour l'animation du pikachu


#Animation Pokeball et Pikachu

def animate(k):
        pokeball.set_data(x2[:k],y2[:k])
        pikachu.set_data(xc,y3[:k])
        return pokeball,pikachu, 


   
animation = animation.FuncAnimation(fig=fig, func=animate, frames=len(t), blit=True, interval=140, repeat=True)
plt.annotate('v0', xy=(xc/4,yc/4),xytext=(0,0),arrowprops=dict(facecolor='b',arrowstyle='->')) #vecteur directeur de la vitesse initiale
plt.annotate('•',xy=(xi-0.30,yi),size=15)   #marquage de la position de la capture
plt.grid() #insertion d'une grille.
Pika= plt.Rectangle((0, 0), 0, 0, color = 'yellow') 
Poke= plt.Rectangle((0, 0), 0, 0, color = 'red')
plt.legend([Pika, Poke], ['Pikachu', 'Pokéball'], markerscale = 100, frameon = False, fontsize = 10) #Insertion de la légende
plt.xlabel("Distance (en m)") #Nom de l'axe Ox.
plt.ylabel("Hauteur (en m)") #Nom de l'axe Oy.
plt.title("Trajectoire d'une pokeball sur un pikachu en chute libre") #Insertion du titre.
plt.show() #Affichage.

