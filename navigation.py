import sys
import os
import pickle
from lib.algo1 import *
from lib.sort import *
import math


#========================================================


def fecha(lineas):
    #Funcion encargada de distinguir el dia, mes y año de la fecha
    cont=0
    year=0
    for j in range(0,len(lineas[0])-1): #Se recorre la primer linea del texto para ver la fecha
        if lineas[0][j]=="0" or lineas[0][j]=="1" or lineas[0][j]=="2" or lineas[0][j]=="3" or lineas[0][j]=="4" or lineas[0][j]=="5" or lineas[0][j]=="6" or lineas[0][j]=="7" or lineas[0][j]=="8" or lineas[0][j]=="9" or lineas[0][j]=="/":
            cont+=1
        else:
            print(f"Error: The date entered is incorrect")  
            quit()
        if cont==4:
            month=lineas[0][j]+lineas[0][j+1]
        elif cont>=7:
            yearn=string_to_num(lineas[0][j])
            year=year*10+yearn
    return month,year

#========================================================

def dias(month,year):
    #Funcion encargada de calcular la cantidad de dias en cada mes
    if month=="02":
        if not year % 4 and (year % 100 or not year % 400): #Calculo que se realiza para saber si es año bisiesto o no
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

    #Funcion encargada de pasar de Caracter a Valor
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
def oneDay(estructura):
    
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


def completar_estructura(lineas,estructura,size):
    #Funcion encargada de Completar la lista head de la Estructura para todos los dias
    for i in range(1,len(lineas)):
        cont=0
        nombre=lineas[i][0]
        X=0
        Y=0
        direction=""
        for j in range(1,len(lineas[i])-1):
            verif=True
            if lineas[i][j]!=" " and cont==0:
                nombre=nombre+lineas[i][j] #Se busca el nombre del barco
            elif lineas[i][j]==" ": #Se distingue entre nombre, x, y, direccion por los espacios
                cont+=1 
                verif=False
                verif2=False 
            elif lineas[i][j]=="-":
                verif2=True
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==1 and verif==True and verif2==False:
                num=string_to_num(lineas[i][j]) #Se convierte los numeros de String a caracter
                X=X*10+num #Se busca la posicion en X
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==1 and verif==True and verif2==True:
                num=string_to_num(lineas[i][j])
                X=X*10-num
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==2 and verif==True and verif2==False:
                num=string_to_num(lineas[i][j])
                Y=Y*10+num #Se busca la posicion en Y
            elif lineas[i][j]!=" " and lineas[i][j]!="-" and cont==2 and verif==True and verif2==True:
                num=string_to_num(lineas[i][j])
                Y=Y*10-num                
            elif lineas[i][j]!=" " and cont==3 and verif==True:
                direction=direction + lineas[i][j] #Se busca la direccion en la que se dirije el barco
        addhead(estructura[0],nombre,X,Y,direction)
        for k in range (1,size): #Se modifican X e Y dependiendo su direccion
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
    return estructura
#========================================================

def create(local_path):
    if os.path.exists(local_path):
        sistema=crear_estructura(local_path)
        with open("informe.bin", "bw") as crear_informe:
            pickle.dump(sistema, crear_informe)
            print("navy created successfully")
    
    else:
        print("Error: The path entered was not found")

#========================================================
#Función que busca la ubicación de un barco en especifico en tal día
def search(date,name):
	date=String(date)
	n=0
	for i in range (0,len(date)): #Se convierte el dia ingresado a Valor
		dia=string_to_num(date[i])
		n=n*10+dia

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
		return print("Boat not found")

#========================================================

def closer(date):
    date=String(date)
    n=0
    for i in range (0,len(date)): #Se convierte el dia ingresado a Valor
        dia=string_to_num(date[i])
        n=n*10+dia
    Node=None
    n-=1
    if n>=0:
        with open('informe.bin','br') as leer_estructura:
            estructura=pickle.load(leer_estructura)
            if n<len(estructura):
                estructura[n]=oneDay(estructura[n]) #Se crea la lista distanList de la Estructura para el dia deseado
                estructura[n].distanList=MergeSort(estructura[n].distanList) #Se ordena la lista
                Node=estructura[n].distanList
                lista=None
                lista=Linkedlist()
                while Node!=None:
                    if Node.value.distan<Node.nextNode.value.distan: #Se busca verifica si el valor encontrado es el unico o ultimo con esa distancia
                        lista=add(lista,Node.value)
                        break
                    elif Node.value.distan==Node.nextNode.value.distan:
                        lista=add(lista,Node.value)
                    Node=Node.nextNode
                while lista!=None:
                    print("Los Barcos, con menor distancia son: ", lista.value.name, " y ", lista.value.nearboat, " con una distancia de ", lista.value.distan)
                    lista=lista.nextNode
            else:
                print("The date entered is incorrect")
    else:
        print("The date entered is incorrect")

#========================================================
#Función que devuelve los dias y los barcos que tuvieron en riesgo de colición        
def collision():

    #Se abre a donde se encuentra la estructura anteriormente creada
	with open('informe.bin','br') as leer_estructura:
		estructura=pickle.load(leer_estructura)
		trueCollision=False
		for i in range(0,len(estructura)):
			if not trueCollision:
				trueCollision=collisionDay(estructura[i],i+1)
			else:
				collisionDay(estructura[i],i+1)

		if not trueCollision:
			return print(False)

#========================================================

def collisionDay(estructura,day):
	boats=estructura.head
	firstTime=False
	while boats.nextNode!=None:

			otherBoats=boats.nextNode

			while otherBoats!=None:

				#Se copian los nombres de los barcos involucrados
				name=boats.value.name
				nearboat=otherBoats.value.name

				#Se crea el array que contendra el vector distancia
				vectorLength=Array(2,0)
				
				#Se ingresan los valores del vector distancia restando la ubicación del primer barco con la ubicación del segundo
				vectorLength[0]=otherBoats.value.X-boats.value.X
				vectorLength[1]=otherBoats.value.Y-boats.value.Y
				
				#se calcula la distancia entre los dos barcos
				distan=math.sqrt((vectorLength[0]**2)+(vectorLength[1]**2))

				if distan<=1:
					if not firstTime:
						firstTime=True
						print("")
						print("el día",day,"los siguientes barcos estuvieron en riesgo de colición:")
						
					print("-",name," y ",nearboat, distan, ", " ,end="")
				
				
				otherBoats=otherBoats.nextNode
			
			boats=boats.nextNode
	if 	firstTime:	
		return True
	else:
		return False

#========================================================
#Función que muestra el ranking de los 10 acercamientos	entre los barcos del día			
def collision_ranking(date):
    
    date=String(date)
    n=0

    for i in range (0,len(date)):
        dia=string_to_num(date[i])
        n=n*10+dia

    n-=1
    if n>=0:
        #Se abre a donde se encuentra la estructura anteriormente creada
        with open('informe.bin','br') as leer_estructura:
            estructura=pickle.load(leer_estructura)
            if n<len(estructura):
                #Se agarra la lista de distancias del día 
                estructura[n]=oneDay(estructura[n])
                #mergesort(estructura[date-1])

                estructura[n].distanList=MergeSort(estructura[n].distanList)

                currentnode=estructura[n].distanList
                i=0

                #Bucle que recorrela lista de distancias hasta el decimo nodo o que se acabe la lista 
                while currentnode!=None and i<10:
                    i=i+1

                    #Se imprime la posición del ranking, los barcos involucrados y a que distancia estaban
                    print("Puesto",i,":",currentnode.value.name,"y",currentnode.value.nearboat,"con una distancia de", currentnode.value.distan)
                    currentnode=currentnode.nextNode
            else:
                print("The date entered is incorrect")
    else:
        print("The date entered is incorrect")


#========================================================
            


if strcmp(String(sys.argv[1]), String('-create')):
    # Ejecutar '-create'
    create(sys.argv[2])
elif strcmp(String(sys.argv[1]), String('-search')):
    # Ejecutar '-search'
    search(sys.argv[2],sys.argv[3])
elif strcmp(String(sys.argv[1]), String('-closer')):
    #Ejecutar '-closer'
    closer(sys.argv[2])
elif sys.argv[1] =='-collision_ranking':
    #Ejecutar '-collision_ranking'
    collision_ranking(sys.argv[2])
elif strcmp(String(sys.argv[1]), String('-collision')):
    #Ejecutar '-collision'
    collision()


