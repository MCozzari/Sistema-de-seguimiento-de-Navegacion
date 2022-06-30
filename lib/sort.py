from lib.algo1 import *
from lib.linkedlist import *
from math import *
from random import *




def MergeSortR(L1, L2):
#Funcion wrapper
  resultado=Linkedlist()

  #Se ordenan los valores y se juntan las listas
  while length(L1)>0 and length (L2)>0:
    if access(L1, 1).distan<=access(L2, 1).distan:
      resultado=enqueue(resultado, access(L1, 1))
      L1=delete(L1, access(L1, 1))
      if L1==None:
        L1=Linkedlist()  
    else:
      resultado=enqueue(resultado, access(L2, 1))
      L2=delete(L2, access(L2, 1))  
      if L2==None:
        L2=Linkedlist()    
  if length(L1)>0:
    currentNode=L1
    while currentNode!=None:
      resultado=enqueue(resultado, currentNode.value)
      currentNode=currentNode.nextNode
  if length(L2)>0:
    currentNode=L2
    while currentNode!=None:
      resultado=enqueue(resultado, currentNode.value)
      currentNode=currentNode.nextNode  
  return resultado    


#Funcion principal
def MergeSort(L):
  if length(L)<=1:
    return L
  else:
    #Se realiza la particion en dos listas
    left=Linkedlist()
    right=Linkedlist()
    medio=trunc(length(L)/2)
    currentNode=L

    for i in range(0, length(L)):
      if currentNode!=None:
        if i<medio:
          left=enqueue(left, currentNode.value)
        else:
          right=enqueue(right, currentNode.value)
        currentNode=currentNode.nextNode

    #Recursividad
    left=MergeSort(left)
    right=MergeSort(right)
    accessleft=access(left, length(left))
    accessright=access(right, 1)
    #Si ambas listas se encuentran ordenadas, se juntan y se devuelven
    if accessleft.distan<=accessright.distan:
      currentNode=right
      while currentNode!=None:
        left=enqueue(left, currentNode.value)
        currentNode=currentNode.nextNode
      return left
    
    Resultado=MergeSortR(left, right)
    return Resultado

