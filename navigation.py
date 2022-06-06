from asyncio.base_futures import _FINISHED
import sys
import os
import pickle
from lib.algo1 import *

class dayNode:
    head=None
    distanlist=None

class distanNode:
    name=None
    nearbote=None
    distan=None
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
            for j in range(0,len(lineas[i])-1):
                verif=True
                if lineas[i][j+1]!=" " and cont==0:
                    nombre=nombre+lineas[i][j+1]
                elif lineas[i][j+1]==" " and cont==0:
                    cont+=1
                    X=lineas[i][j+2]
                    verif=False
                if lineas[i][j+1]!=" " and cont==1 and verif==True:
                    X=X+lineas[i][j+2]
                elif lineas[i][j+1]==" " and cont==1 and verif==True:
                    cont+=1
                    Y=lineas[i][j+2]
                    verif=False
                if lineas[i][j+1]!=" " and cont==2 and verif==True:
                    Y=Y+lineas[i][j+2]
                elif lineas[i][j+1]==" " and cont==2 and verif==True:
                    cont+=1
                    direction=lineas[i][j+2]
                    verif=False
                if lineas[i][j]!=" " and cont==3 and verif==True:
                    direction=direction + lineas[i][j+1]
            addhead(estructura[00],nombre,X,Y,direction)
        print("")
    


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




