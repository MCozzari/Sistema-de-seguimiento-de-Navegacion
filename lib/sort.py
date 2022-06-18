from lib.algo1 import *
from random import *
from math import *

class distanNode:
    name=None
    nearboat=None
    distan=None
    vectorLength=None
    vectorMod=None
    nextNode=None

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
        if NodeA.distan<NodeB.distan:
          #Asignacion de valores si cumple la condicion
          NodeAux=distanNode()
          NodeAux.distan=NodeB.distan
          NodeAux.name=NodeB.name
          NodeAux.nearboat=NodeB.nearboat
          NodeAux.vectorLength=NodeB.vectorLength
          NodeAux.vectorMod=NodeB.vectorMod
          NodeAux.nextNode=NodeB.nextNode
          NodeB.distan=NodeA.distan
          NodeB.name=NodeA.name
          NodeB.nearboat=NodeA.nearboat
          NodeB.vectorLength=NodeA.vectorLength
          NodeB.vectorMod=NodeA.vectorMod          
          NodeA.distan=NodeAux.distan
          NodeA.name=NodeAux.name
          NodeA.nearboat=NodeAux.nearboat
          NodeA.vectorLength=NodeAux.vectorLength
          NodeA.vectorMod=NodeAux.vectorMod
        NodeB=NodeB.nextNode
      NodeA=NodeA.nextNode
    return Q

