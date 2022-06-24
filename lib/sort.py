from lib.algo1 import *
from random import *
from math import *


def InsertionSort(Q):
  if Q==None:
    return None
  else:
    NodeA=Q.nextNode #empieza del segundo
    #Bucle que se ejecutará por cada nodo de la lista
    while NodeA!=None:
      NodeB=Q
      #Bucle que se ejecutará hasta el current node
      while NodeB!=NodeA:
        if NodeA.value.distan<NodeB.value.distan:
          #Asignacion de valores si cumple la condicion
          NodeAux=NodeB.value
          NodeB.value=NodeA.value       
          NodeA.value=NodeAux
        NodeB=NodeB.nextNode
      NodeA=NodeA.nextNode
    return Q

