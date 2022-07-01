class dayNode:
    head=None
    distanList=None
    

class distanNode:
    name=None
    nearboat=None
    distan=None
    vectorLength=None
    vectorMod=None

class Linkedlist:
    value=None
    nextNode=None

class boatNode:
    name=None
    X=None
    Y=None
    direction=None



def addhead(estructura,nombre,X,Y,direction):
    
    Node=Linkedlist()
    Node.value=boatNode()
    Node.value.name=nombre
    Node.value.X=X
    Node.value.Y=Y
    Node.value.direction=direction
    if estructura==None:
        estructura.head=Node
    else:
        Node.nextNode=estructura.head
        estructura.head=Node


def add(lista,Node): 
    NodeA=Linkedlist()
    NodeA.value=distanNode()
    NodeA.value=Node
    if lista==None:
        lista=NodeA
    else:
        NodeA.nextNode=lista
        lista=NodeA
    if lista.nextNode.nextNode==None and lista.nextNode.value==None:
      lista.nextNode=None
    return lista


def search(L,element):
  cont=0  
  NodeA=L
  while (NodeA!=None) : 
    if NodeA.value==element: 
      return cont    
    NodeA=NodeA.nextNode
    cont+=1


def insert(L,element,position):
  cont=0 
  NodeA=L
  while (NodeA.value!=None and cont<position-1):  #Si NodeA es distinto a None y cont no supera position-1
    NodeA=NodeA.nextNode 
    cont+=1 
  if position==0: #Se verifica si la posicion es 0
    L=add(L,element) 
    return L
  elif NodeA!=None: #Sino si NodeA es distinto a 0
    NodeB=Linkedlist() 
    NodeB.value=element
    NodeA.nextNode=NodeB 
    return L
  else: #Sino
    return None #Se regresa None



def delete(L,element):
	Posicion=search(L,element)
	if Posicion!=None:
		currentnode=L
		while currentnode!=None:
			if L.value==element:
				L=L.nextNode
				break
			elif currentnode.nextNode.value==element:
				currentnode.nextNode=currentnode.nextNode.nextNode
				break
			currentnode=currentnode.nextNode
	return L



def length(L):
  cont=0  #Se crea un cont para usarlo despues
  NodeA=L
  if NodeA.value!=None and NodeA.nextNode!=None:
    while (NodeA!=None): #Se crea un while para que se repita hasta terminar la lista
      cont+=1 
      NodeA=NodeA.nextNode 
  elif NodeA.value!=None:
    cont+=1
  return cont #Se regresa la posicion


def access(L,position):
  valor=None
  currentNode=L
  contador=1
  while currentNode!=None:
    if contador==position:
      valor=currentNode.value
      break
    contador=contador+1
    currentNode=currentNode.nextNode

  return valor

def enqueue(Q,element):
  Q=insert(Q,element,length(Q))
  return Q