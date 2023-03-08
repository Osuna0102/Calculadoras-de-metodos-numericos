import numpy as np
import os

if os.name == "posix":
    var = "clear"
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"

def OKI(n):
    try:
        n=int(n)
    except:
        n=OKI(input("Caracter no valido: "))
    return n

def OK(n):
    try:
        n=float(n)
    except:
        n=OK(input("Caracter no valido: "))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' según su opción: ")
    return(c)

def val(tp):
    while tp!="N" and tp!="M":
        tp=input("Introduzca \'N\' para dato numérico y \'M\' para matriz: ")
    return tp

#FUNCIÓN DE TIPO DE DATO
def dato():
    tipo_dato=val(input("Tipo de dato: "))
    if tipo_dato=="M":
        matr=crea_matriz(fil,col)
    else:
        matr=OK(input("Introduce número: "))
    return matr

#FUNCIÓN PARA DEFINIR MATRIZ
def crea_matriz(fil,col):
    print("")
    f=-1;c=-1
    e_fil=[]
    for f in range(fil):
        e_col=[]
        f+=1
        for c in range(col):
            c+=1
            valor=OK(input('Introduzca el componente (%d,%d): '%(f,c)))
            e_col.append(valor)
        e_fil.append(e_col)
        matri=np.array(e_fil,float)
    return matri

cantidad = (input("Indique número de matrices a ingresar: "))

if cantidad == '2':

    print("          CALCULADORA DE MATRICES          ")   
    fil=OKI(input("Indique número de filas de A: "))
    col=OKI(input("Indique número de columnas de A: "))
    A = crea_matriz(fil,col)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    B = crea_matriz(fil1,col1)
    
if cantidad == '3':
    
    print("          CALCULADORA DE MATRICES          ")   
    fil=OKI(input("Indique número de filas de A: "))
    col=OKI(input("Indique número de columnas de A: "))
    A = crea_matriz(fil,col)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    B = crea_matriz(fil1,col1)

    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    C = crea_matriz(fil1,col1)

if cantidad == '4':
    
    print("          CALCULADORA DE MATRICES          ")   
    fil=OKI(input("Indique número de filas de A: "))
    col=OKI(input("Indique número de columnas de A: "))
    A = crea_matriz(fil,col)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    B = crea_matriz(fil1,col1)

    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    C = crea_matriz(fil1,col1)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    D = crea_matriz(fil1,col1)

if cantidad == '5':
    
    print("          CALCULADORA DE MATRICES          ")   
    fil=OKI(input("Indique número de filas de A: "))
    col=OKI(input("Indique número de columnas de A: "))
    A = crea_matriz(fil,col)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    B = crea_matriz(fil1,col1)

    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    C = crea_matriz(fil1,col1)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    D = crea_matriz(fil1,col1)

    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    E = crea_matriz(fil1,col1)

if cantidad == '6':
    
    print("          CALCULADORA DE MATRICES          ")   
    fil=OKI(input("Indique número de filas de A: "))
    col=OKI(input("Indique número de columnas de A: "))
    A = crea_matriz(fil,col)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    B = crea_matriz(fil1,col1)

    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    C = crea_matriz(fil1,col1)
    
    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    D = crea_matriz(fil1,col1)

    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    E = crea_matriz(fil1,col1)

    fil1=OKI(input("Indique número de filas de B: "))
    col1=OKI(input("Indique número de columnas de B: "))
    F = crea_matriz(fil1,col1)  

ecuacion = input("Ingrese la ecuacion a operar:  ")
print(eval(ecuacion))

















    
    
