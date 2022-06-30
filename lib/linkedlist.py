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
  cont=0  #Creamos un cont para usarlo despues
  NodeA=L
  while (NodeA.value!=None and cont<position-1):  #Si NodeA es distinto a None y cont no supera position-1
    NodeA=NodeA.nextNode #Se pasa al siguiente Node
    cont+=1 #Se aumenta el cont
  if position==0: #Se verifica si la posicion es 0
    L=add(L,element) #En caso de que posicion sea 0 se invoca la funcion add
    return L
  elif NodeA!=None: #Sino si NodeA es distinto a 0
    NodeB=Linkedlist() #Se define otro Node
    NodeB.value=element #Se le da el valor de element
    NodeA.nextNode=NodeB #Se igualan los Nodes siguientes
    return L
  else: #Sino
    return None #Se regresa None

#delete(L,element)
#Descripción: Elimina un elemento de la lista que representa el TAD secuencia.
#Poscondición: Se debe desvincular el Node a eliminar.
#Entrada:	la	lista	sobre	el	cual	se	quiere realizar la eliminación (Linkedlist) y el valor del elemento (element) a eliminar.
#Salida:	Devuelve	la	posición	donde	se	encuentra	el	elemento	a eliminar. Devuelve None si el elemento a eliminar no se encuentra.

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

#length(L)
#Descripción: Calcula el número de elementos de la lista que representa el TAD secuencia.
#Entrada:	La	lista	sobre	la	cual	se	quiere	calcular	el	número	de elementos.
#Salida: Devuelve el número de elementos.

def length(L):
  cont=0  #Se crea un cont para usarlo despues
  NodeA=L
  if NodeA.value!=None and NodeA.nextNode!=None:
    while (NodeA!=None): #Se crea un while para que se repita hasta terminar la lista
      cont+=1 #Se aumenta el cont
      NodeA=NodeA.nextNode #Se pasa al siguiente Node
  elif NodeA.value!=None:
    cont+=1
  return cont #Se regresa la posicion

#access(L,position)
#Descripción: Permite acceder a un elemento de la lista en una posición determinada.
#Entrada: La lista (LinkedList) y la position del elemento al cual se quiere acceder.
#Salida: Devuelve el valor de un elemento en una position de la lista, devuelve None si no existe elemento para dicha posición.

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

#update(L,element,position)
#Descripción: Permite cambiar el valor de un elemento de la lista en una posición determinada
#Entrada: La lista (LinkedList) y la position sobre la cual se quiere asignar el valor de	element.
#Salida: Devuelve None si no existe elemento para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.

def update(L,element,position):
  cont=0 #Se crea un cont que se usara despues
  NodeA=L
  while(NodeA!=None): #Se crea un while para verificar que NodeA sea distinto a Node
    if cont==position:  #Si cont es igual a posicion:
      NodeA.value=element #Le damos a NodeA.value el valor de element
      return cont #Se regresa el cont
    else: #Sino
      NodeA=NodeA.nextNode  #Se pasa al siguiente NodeA
      cont+=1 #Se aumenta el cont
  return None #Se devuelve None si nunca cont es igual a la posicion

def imprimir(L):
  currentNode=L
  while currentNode!=None:
    print (currentNode.value, end=" ")
    currentNode=currentNode.nextNode
  print("")
  return

def enqueue(Q,element):
  Q=insert(Q,element,length(Q))
  return Q