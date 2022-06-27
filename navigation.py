import sys
import os
import pickle
from lib.algo1 import *
from lib.sort import *
import math

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
    value:None
    nextNode=None

class boatNode:
    name=None
    X=None
    Y=None
    direction=None

#========================================================


def fecha(lineas):
    cont=0
    year=0
    for j in range(0,len(lineas[0])-1): #Se recorre la primer linea del texto para ver la fecha
        if lineas[0][j]=="0" or lineas[0][j]=="1" or lineas[0][j]=="2" or lineas[0][j]=="3" or lineas[0][j]=="4" or lineas[0][j]=="5" or lineas[0][j]=="6" or lineas[0][j]=="7" or lineas[0][j]=="8" or lineas[0][j]=="9" or lineas[0][j]=="/":
            cont+=1
        else:
            print(f"Error: Fecha no encontrada")  
            quit()
        if cont==4:
            month=lineas[0][j]+lineas[0][j+1]
        elif cont>=7:
            yearn=string_to_num(lineas[0][j])
            year=year*10+yearn
    return month,year

#========================================================

def dias(month,year):
    if month=="02":
        if not year % 4 and (year % 100 or not year % 400):
            size=29
        else:
            size=28
    elif month=="01" or month=="03" or month=="05" or month=="07" or month=="8" or month=="10" or month=="12":
        size=31
    else:
        size=30
    return size

#========================================================

def string_to_num(num):
    if num=="1":
        X=1
    elif num=="2":
        X=2
    elif num=="3":
        X=3
    elif num=="4":
        X=4
    elif num=="5":
        X=5
    elif num=="6":
        X=6
    elif num=="7":
        X=7
    elif num=="8":
        X=8
    elif num=="9":
        X=9
    elif num=="0":
        X=0
    return X
    
#========================================================

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

#===========================================================
#Esta función devuelve un array con la dirección del barco
def directionvector(direction):
	
	v1=Array(2,0)

	#Cuando tiene dirección Norte
	if direction=="N":
		v1[1]=1
		v1[0]=0

    #Cuando tiene dirección Sur
	elif direction=="S":
		v1[1]=-1
		v1[0]=0

    #Cuando tiene dirección Este
	elif direction=="E":
		v1[0]=1
		v1[1]=0

    #Cuando tiene dirección Oeste
	elif direction=="W":
		v1[0]=-1
		v1[1]=0

    #Cuando tiene dirección Noroeste
	elif direction=="NW":
		v1[1]=1
		v1[0]=-1

    #Cuando tiene dirección Noreste
	elif direction=="NE":
		v1[1]=1
		v1[0]=1

    #Cuando tiene dirección Sureste
	elif direction=="SE":
		v1[1]=-1
		v1[0]=1

    #Cuando tiene dirección Suroeste
	elif direction=="SW":
		v1[1]=-1
		v1[0]=-1

	return v1

#========================================================
#Función que crea la lista de distancias del primer día
def firstDay(estructura):
    
    boats=estructura.head

    while boats.nextNode!=None:

        otherBoats=boats.nextNode

        while otherBoats!=None:
            
            #Se crean los nodos respectivos de la lista
            node=Linkedlist()
            node.value=distanNode()

            #Se copian los nombres de los barcos involucrados
            node.value.name=boats.value.name
            node.value.nearboat=otherBoats.value.name

            #Se crea el array que contendra el vector distancia
            node.value.vectorLength=Array(2,0)
            
            #Se ingresan los valores del vector distancia restando la ubicación del primer barco con la ubicación del segundo
            node.value.vectorLength[0]=otherBoats.value.X-boats.value.X
            node.value.vectorLength[1]=otherBoats.value.Y-boats.value.Y
            
            #se saca los vectores direccion 
            V1=directionvector(boats.value.direction)
            V2=directionvector(otherBoats.value.direction)
            
            #Se crea el array que contendra el vector modificador
            node.value.vectorMod=Array(2,0)
            
            #Se ingresa los valores del vector modificador con la resta de las direcciones de ambos barcos
            node.value.vectorMod[0]=V2[0]-V1[0]
            node.value.vectorMod[1]=V2[1]-V1[1]

            #se calcula la distancia entre los dos barcos
            node.value.distan=math.sqrt((node.value.vectorLength[0]**2)+(node.value.vectorLength[1]**2))
            
            #Se agrega el nodo a la lista de distancias
            node.nextNode=estructura.distanList
            estructura.distanList=node
            
            otherBoats=otherBoats.nextNode
            
        boats=boats.nextNode
        
    return estructura

#========================================================
#Función que calcula las distancias de los barcos los demas días del mes
def otherDay(estructura, old):

    #Se crean los nodos respectivos de la lista
    node=Linkedlist()
    node.value=distanNode()

    #Se copian los nombres de los barcos involucrados utilizando la lista anterior de distancias
    node.value.name=old.value.name
    node.value.nearboat=old.value.nearboat
	
    #Se crean los arrays necesarios
    node.value.vectorLength=Array(2,0)
    node.value.vectorMod=Array(2,0)
	
    #Se copian los valores del anterior vector modificador
    node.value.vectorMod[0]=old.value.vectorMod[0]
    node.value.vectorMod[1]=old.value.vectorMod[1]
	
    #Se ingresa los nuevos valores del vector distancia sumando el anterior vector distancia con el vector modificador
    node.value.vectorLength[0]=old.value.vectorLength[0]+node.value.vectorMod[0]
    node.value.vectorLength[1]=old.value.vectorLength[1]+node.value.vectorMod[1]
    
    #Se calcula la distancia entre los barcos con el vector distancia
    node.value.distan=math.sqrt((node.value.vectorLength[0]**2)+(node.value.vectorLength[1]**2))

    #Se agraga el nodo al inicio de la lista de distancias
    estructura.distanList=node
    currentnode=estructura.distanList

    old=old.nextNode

    #En este bucle se crea lo mismo pero con la diferencia es que al final el nodo se agrega al final de la lista
    while old!=None:

        #Se crean los nodos respectivos de la lista
        node=Linkedlist()
        node.value=distanNode()
        
        #Se copian los nombres de los barcos involucrados utilizando la lista anterior de distancias
        node.value.name=old.value.name
        node.value.nearboat=old.value.nearboat
        
        #Se crean los arrays necesarios
        node.value.vectorLength=Array(2,0)
        node.value.vectorMod=Array(2,0)
        
        #Se copian los valores del anterior vector modificador
        node.value.vectorMod[0]=old.value.vectorMod[0]
        node.value.vectorMod[1]=old.value.vectorMod[1]
        
        #Se ingresa los nuevos valores del vector distancia sumando el anterior vector distancia con el vector modificador
        node.value.vectorLength[0]=old.value.vectorLength[0]+node.value.vectorMod[0]
        node.value.vectorLength[1]=old.value.vectorLength[1]+node.value.vectorMod[1]
        
        #Se calcula la distancia entre los barcos con el vector distancia
        node.value.distan=math.sqrt((node.value.vectorLength[0]**2)+(node.value.vectorLength[1]**2))
        
        #Se agraga el nodo al final de la lista de distancias
        currentnode.nextNode=node
        currentnode=currentnode.nextNode
        
        old=old.nextNode
	
    return estructura.distanList

#========================================================
#Función que crea las listas de distancias de cada día del mes
def distanDays(estructura):

    #Se recorre por todos los días
	for i in range(0,len(estructura)):

        #Cuando es el primer día del mes
		if i==0:
			estructura[0]=firstDay(estructura[0])
			InsertionSort(estructura[0].distanList)
		
        #Cuando es otro día
		else:
			
			estructura[i].distanList=otherDay(estructura[i],estructura[i-1].distanList)
			InsertionSort(estructura[i].distanList)
    
    #Se devuelve la estructura con todas las listas de distancias completas y ordenadas
	return estructura


def completar_estructura(lineas,estructura,size):

    for i in range(1,len(lineas)):
        cont=0
        nombre=lineas[i][0]
        X=0
        Y=0
        direction=""
        verif2=False
        for j in range(1,len(lineas[i])-1):
            verif=True
            if lineas[i][j]!=" " and cont==0:
                nombre=nombre+lineas[i][j]
            elif lineas[i][j]==" ":
                cont+=1
                verif=False
            elif lineas[i][j]=="-":
                verif2=True
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==1 and verif==True and verif2==False:
                num=string_to_num(lineas[i][j]) #Se convierte los numeros de String a caracter
                X=X*10+num
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==2 and verif==True and verif2==False:
                num=string_to_num(lineas[i][j])
                Y=Y*10+num
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==1 and verif==True and verif2==True:
                num=string_to_num(lineas[i][j])
                X=X*10-num
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==2 and verif==True and verif2==True:
                num=string_to_num(lineas[i][j])
                Y=Y*10-num                
            elif lineas[i][j]!=" " and cont==3 and verif==True:
                direction=direction + lineas[i][j]
        addhead(estructura[0],nombre,X,Y,direction)
        for k in range (1,size):
            if direction=="N":
                Y=Y+1
            elif direction=="S":
                Y=Y-1
            elif direction=="E":
                X=X+1
            elif direction=="W":
                X=X-1
            elif direction=="NW":
                Y=Y+1
                X=X-1
            elif direction=="NE":
                Y=Y+1
                X=X+1
            elif direction=="SE":
                Y=Y-1
                X=X+1
            elif direction=="SW":
                Y=Y-1
                X=X-1
            addhead(estructura[k],nombre,X,Y,direction)
    return estructura
#========================================================

def crear_estructura(local_path):
    with open(local_path) as informe:
        lineas=informe.readlines()
        month,year=fecha(lineas)
        size=dias(month,year)
        estructura=Array(size,dayNode()) #Se crea una tabla hash, con un tamaño segun los dias
        for i in range(0, len(estructura)):
            estructura[i]=dayNode()
        estructura=completar_estructura(lineas,estructura,size)
    estructura=distanDays(estructura)
    return estructura
#========================================================

def create(local_path):
    if os.path.exists(local_path):
        sistema=crear_estructura(local_path)
        with open("informe.bin", "bw") as crear_informe:
            pickle.dump(sistema, crear_informe)
            print("Sistema de Navegacion creado con exito")
    
    else:
        print("Error: No se encontro el Path ingresado")

#========================================================
#Función que busca la ubicación de un barco en especifico en tal día
def search(date,name):

    #Se abre a donde se encuentra la estructura anteriormente creada
	with open('informe.bin','br') as leer_estructura:
		navigation=pickle.load(leer_estructura)
	
		#Se agarra la lista de barcos del día 
		currentnode=navigation[date-1].head
        
        #Se busca el barco
		while currentnode!=None:
            
            #Cuando se encuentra el barco
			if currentnode.value.name==name:
				position=Array(2,0) #Se crea un array que se guardaran la posición del barco

                #Se carga la posición y se devuelve
				position[0]=currentnode.value.X
				position[1]=currentnode.value.Y
				return print(position) 
                
			currentnode=currentnode.nextNode

        #Esto es cuando no se encuentra el barco
		return print("No se encontró el barco")

#========================================================

def adddistan(lista,Node):
    NodeA=Linkedlist()
    NodeA.value=distanNode()
    NodeA.value.name=Node.value.name
    NodeA.value.nearboat=Node.value.nearboat
    NodeA.value.distan=Node.value.distan
    if lista==None:
        lista=NodeA
        return lista
    else:
        NodeA.nextNode=lista
        lista=NodeA
        return lista

def closer(date):
    date=String(date)
    n=0
    for i in range (0,len(date)):
        j=string_to_num(date[i])
        n=n*10+j
    Node=None
    n-=1
    with open('informe.bin','br') as leer_estructura:
        estructura=pickle.load(leer_estructura)
        Node=estructura[n].distanList
        lista=None
        while Node!=None:
            if Node.value.distan<Node.nextNode.value.distan:
                lista=adddistan(lista,Node)
                break
            elif Node.value.distan==Node.nextNode.value.distan:
                lista=adddistan(lista,Node)
            Node=Node.nextNode
        while lista!=None:
            print("Los Barcos, con menor distancia son: ", lista.value.name, " y ", lista.value.nearboat, " con una distancia de ", lista.value.distan)
            lista=lista.nextNode

#========================================================
#Función que devuelve los dias y los barcos que tuvieron en riesgo de colición        
def collision():

    #Se abre a donde se encuentra la estructura anteriormente creada
	with open('informe.bin','br') as leer_estructura:
		estructura=pickle.load(leer_estructura)
		
        #Esta variable es para saber si hubo riesgo de colición
		trueCollision=False
		
        #Recorre por los días
		for i in range(0,len(estructura)):
			
			currentnode=estructura[i].distanList
			
            #Al tener la lista ordenada de menor a mayor, entonces solo se verifica si el primer 
            #nodo de la lista de distancia tuvo riesgo de colición
			if currentnode.value.distan<=1:
				
                #Si tuvo entonces se cambia de la variable a True 
				trueCollision=True

                #Se indica que día se encontró el riesgo de colición
				print("el día",i+1,"los siguientes barcos estuvieron en riesgo de colición:")

				#Y el siguente bucle muestra los riesgos de colición del día en forma de lista
				while currentnode!=None and currentnode.value.distan<=1:
					print("-",currentnode.value.name," y ",currentnode.value.nearboat)
					currentnode=currentnode.nextNode

        #Esto es cuando no se encontraron ningún riesgo de colición
		if not trueCollision:
			return print(False)

		return
#========================================================
#Función que muestra el ranking de los 10 acercamientos	entre los barcos del día			
def collision_ranking(date):

    #Se abre a donde se encuentra la estructura anteriormente creada
	with open('informe.bin','br') as leer_estructura:
		estructura=pickle.load(leer_estructura)

        #Se agarra la lista de distancias del día 
		currentnode=estructura[date-1].distanList
		i=0

        #Bucle que recorrela lista de distancias hasta el decimo nodo o que se acabe la lista 
		while currentnode!=None and i<10:
			i=i+1
            
            #Se imprime la posición del ranking, los barcos involucrados y a que distancia estaban
			print("Puesto",i,":",currentnode.value.name,"y",currentnode.value.nearboat,"con una distancia de", currentnode.value.distan)
			currentnode=currentnode.nextNode


#========================================================
            

if len(sys.argv) == 3:
    if strcmp(String(sys.argv[1]), String('-create')):
        # Ejecutar '-create'
        create(sys.argv[2])
    elif strcmp(String(sys.argv[1]), String('-search')):
        # Ejecutar '-search'
        search(sys.argv[2],sys.argv[3])
    elif strcmp(String(sys.argv[1]), String('-closer')):
        #Ejecutar '-closer'
        closer(sys.argv[2])


