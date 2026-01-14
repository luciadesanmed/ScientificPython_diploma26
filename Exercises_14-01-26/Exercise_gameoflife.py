# Implement Conway's game of life using numpy array to hold data. Neighbours are defined as adjacent cells:
#Any LIVING cell with 2 or 3 neighbours survives.
#Any DEAD cell with 3 neighbours comes alive.
#Any OTHER LIVING cell dies.
#All deaths and births occur simultaneously

#So, at each step you need:
 #calculate the number of neighnours
 #set "dead" or "alive" status according to the above plot

#Implement everything in a class. For initial conditions: two files "ships.txt" and "guns.txt" are provided in data folder (but feel free to create your own if you wish), you can read them like
import numpy as np
import matplotlib.pyplot as plt

#Initial conditions: 1 is alive, 0 is dead

def game_of_life(field):
 #Calculate the number of neighbours:
 ncol=len(field)
 nrow=len(field[0])
 new=np.zeros((ncol,nrow))
    
 for i in range(ncol): #ncol
  for j in range(nrow): #nrow
   status=0
   celda=field[i][j]
      
   for ii in [-1,0,1]:
    for jj in [-1,0,1]:
     if ii==0 and jj==0:
      continue
     di=i+ii
     dj=j+jj
     if 0<=di<ncol and 0<=dj<nrow:
      status+=field[di][dj]

   if celda==1:
    if status==2 or status==3:
     new[i][j]=1
   elif celda==0:
     if status==3:
      new[i][j]=1
       
 return new

start_field=np.genfromtxt("/home/desan/ScientificPython/ScientificPython_diploma26/data/ships.txt").transpose()
#start_field=np.genfromtxt("prueba.txt").transpose()
plt.imshow(start_field)
plt.show()
field=game_of_life(start_field)
for i in range(50):
 plt.imshow(field)
 plt.pause(0.5)
 field=game_of_life(field)
plt.show()


 