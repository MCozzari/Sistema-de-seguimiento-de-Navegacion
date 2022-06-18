from asyncio.base_futures import _FINISHED
import sys
import os
import pickle
from lib.algo1 import *
import time
import math

class dayNode:
    head=None
    distanList=None

class distanNode:
    name=None
    nearbote=None
    distan=None
    vectorLength=Array(2,0) #indica la distancia a traves de un vector
    vectorMod=Array(2,0) #es un vector que se suma al anterior para saber la distancia actual entre los dos barcos
    nextNode=None

class boatNode:
    name=None
    X=None
    Y=None
    direction=None
    nextNode=None

def create(local_path):
    if os.path.exists(local_path):
        sistema=crear_estructura(local_path)
        with open("informe.bin", "bw") as crear_informe:
            pickle.dump(sistema, crear_informe)
    
    else:
        print("Error: No se encontro el Path ingresado")

def crear_estructura(local_path):
    inicio=time.time()
    with open(local_path) as informe:
        lineas=informe.readlines()
        cont=0
        for j in range(0,len(lineas[0])):
            if lineas[0][j]=="0" or lineas[0][j]=="1" or lineas[0][j]=="2" or lineas[0][j]=="3" or lineas[0][j]=="4" or lineas[0][j]=="5" or lineas[0][j]=="6" or lineas[0][j]=="7" or lineas[0][j]=="8" or lineas[0][j]=="9" or lineas[0][j]=="/":
                cont+=1
            else:
                print(f"Error: Fecha no encontrada")  
                quit()
            if cont==4:
                mes=lineas[0][j]+lineas[0][j+1]
            elif cont==7:
                year=lineas[0][j]+lineas[0][j+1]+lineas[0][j+2]+lineas[0][j+3]
                break
        if mes=="02":
            if not year % 4 and (year % 100 or not year % 400):
                size=29
            else:
                size=28
        elif mes=="01" or mes=="03" or mes=="05" or mes=="07" or mes=="8" or mes=="10" or mes=="12":
            size=31
        else:
            size=30
        estructura=Array(size,dayNode())
        for i in range(0, len(estructura)):
            estructura[i]=dayNode()
        for i in range(1,len(lineas)):
            cont=0
            nombre=lineas[i][0]
            X=0
            Y=0
            direction=""
            for j in range(1,len(lineas[i])-1):
                verif=True
                if lineas[i][j]!=" " and cont==0:
                    nombre=nombre+lineas[i][j]
                elif lineas[i][j]==" ":
                    cont+=1
                    verif=False
                elif lineas[i][j]!=" " and cont==1 and verif==True:
                    num=string_to_num(lineas[i][j])
                    X=X*10+num
                elif lineas[i][j]!=" " and cont==2 and verif==True:
                    num=string_to_num(lineas[i][j])
                    Y=Y*10+num
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
                elif direction=="O":
                    X=X-1
                elif direction=="NO":
                    Y=Y+1
                    X=X-1
                elif direction=="NE":
                    Y=Y+1
                    X=X+1
                elif direction=="SE":
                    Y=Y-1
                    X=X+1
                elif direction=="SO":
                    Y=Y-1
                    X=X-1
                addhead(estructura[k],nombre,X,Y,direction)
    fin=time.time()
    print(fin-inicio)
    estructura=distanDays(estructura)

        

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
    


def addhead(estructura,nombre,X,Y,direction):
    Node=boatNode()
    Node.name=nombre
    Node.X=X
    Node.Y=Y
    Node.direction=direction
    if estructura==None:
        estructura.head=Node
    else:
        Node.nextNode=estructura.head
        estructura.head=Node

if len(sys.argv) == 3:
    if strcmp(String(sys.argv[1]), String('-create')):
        # Ejecutar '-create'
        create(sys.argv[2])


#===========================================================
def directionvector(direction):
	
	v1=Array(2,0)
	
	if direction=="N":
		v1[1]=1
        
	elif direction=="S":
		v1[1]=-1

	elif direction=="E":
		v1[0]=1

	elif direction=="O":
		v1[0]=-1

	elif direction=="NO":
		v1[1]=1
		v1[0]=-1

	elif direction=="NE":
		v1[1]=1
		v1[0]=1

	elif direction=="SE":
		v1[1]=-1
		v1[0]=1

	elif direction=="SO":
		v1[1]=-1
		v1[0]=-1

	return v1

#--------------------------------------------------------
def firstDay(boats,distans):
	
	while boats.nextNode!=None:
		otherBoats=boats.nextNode
		while otherBoats!=None:

			node=distanNode()
			node.name=boats.name
			node.nearboat=otherBoats.name
			
			node.vectorLength[0]=otherBoats.X-boats.X
			node.vectorLength[1]=otherBoats.Y-boats.Y
			
			V1=directionvector(boats.direction)
			V2=directionvector(otherBoats.direction)
			
			node.vectorMod[0]=V2[0]-V1[0]
			node.vectorMod[1]=V2[1]-V1[1]

            #se calcula la distancia entre los dos barcos
			node.distan=math.sqrt((node.vectorLength[0]**2)+(node.vectorLength[1]**2))
			
			if distans==None:
				distans=node
			else:
				node.nextNode=distans
				distans=node

			otherBoats=otherBoats.nextNode

		boats=boats.nextNode

	return distans

#--------------------------------------------------------

def otherDay(distans):
	while distans!=None:
		distans.vectorLength[0]=distans.vectorLength[0]+distans.vectorMod[0]
		distans.vectorLength[1]=distans.vectorLength[1]+distans.vectorMod[1]
		distans.distan=math.sqrt((distans.vectorLength[0]**2)+(distans.vectorLength[1]**2))
		distans=distans.nextNode
	
	return distans

#--------------------------------------------------------

def distanDays(estructura):
	for i in range(0,len(estructura)):
		if i==0:
			estructura[0].distanList=firstDay(estructura[0].head,estructura[0].distanList)
			#ordenamiento(estructura[0].distanList)
		else:
			estructura[i].distanList=estructura[i-1].distanList
			estructura[i]=otherDay(estructura[i].distanList)
			#ordenamiento(estructura[i].distanList)
    
	return estructura

#========================================================
def search(date,name):
	
	navigation=None #local_path_navigation
	n=date%len(navigation)
	currentnode=navigation[n].head
	
	while currentnode!=None:
		
		if currentnode.name==name:
			position=Array(2,0)
			position[0]=currentnode.X
			position[1]=currentnode.y
			return position
			
		currentnode=currentnode.nextNode
	return "No se encontró el barco"

#========================================================
