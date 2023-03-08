

def flotante2Binario(num):
    partEnt,partDec=str(num).split(".")
    resultado=bin(int(partEnt))[2:]
    resultado=str(resultado)+"."
    partDec=convADecimal(int(partDec))
    for i in range(10):
        partDec*=2
        partEnt,partDec=str(partDec).split(".")
        partEnt=int(partEnt)
        partDec=(convADecimal(float(partDec)))
        resultado+=str(partEnt)
    return resultado

def flotante2Oct(num):
    partEnt, partDec = str(num).split(".")
    resultado = oct(int(partEnt))[2:]
    resultado = str(resultado) + "."
    partDec = convADecimal(int(partDec))
    for i in range(10):
        partDec *= 8
        partEnt, partDec = str(partDec).split(".")
        partEnt = int(partEnt)
        partDec = (convADecimal(float(partDec)))
        resultado += str(partEnt)
    return resultado

def float2Hex(num):
    partEnt, partDec = str(num).split(".")
    resultado = hex(int(partEnt))[2:]
    resultado = str(resultado) + "."
    partDec = convADecimal(int(partDec))

    for i in range(10):
        partDec *= 16

        partEnt, partDec = str(partDec).split(".")
        partEnt = int(partEnt)
        partDec="0."+partDec
        partDec=float(partDec)

        resultado += str(hex(partEnt)[2:])

    return resultado

def entero2Bin(num):
    resultado=bin(num)[2:]
    return resultado

def entero2Oct(num):
    resultado=oct(num)[2:]
    return resultado

def entero2Hex(num):
    resultado=hex(num)[2:]
    return resultado

def convADecimal(num):
    while num>1:
        num/=10
    return num

def binario2Decimal(num):
    resultado=int(num,2)
    return resultado
def binario2Oct(num):
    resultado=oct(int(num,2))[2:]
    return resultado
def binario2Hex(num):
    resultado=hex(int(num,2))[2:]
    return resultado

def binarioFDecimal(num):
    partIzq, partDer = str(num).split(".")
    resultado = int(partIzq, 2)

    lista = list(partDer)

    suma = 0
    con = 1
    for i in lista:

        if (i == '1'):
            suma += float((1 / (2 ** con)))

        con += 1

    resultado += (suma)
    return resultado

def binarioF2Oct(num):
    dec=binarioFDecimal(num)
    resultado=flotante2Oct(dec)
    return resultado
def binarioF2Hex(num):
    dec=binarioFDecimal(num)
    resultado=float2Hex(dec)
    return resultado

def oct2Dec(num):
    resultado=int(num,8)
    return resultado
def oct2Bin(num):
    resultado=int(num,8)
    resultado=bin(resultado)[2:]
    return resultado
def oct2Hex(num):
    resultado=hex(int(num,8))[2:]
    return resultado

def octF2Dec(num):
    partIzq, partDer = str(num).split(".")
    resultado = int(partIzq, 8)

    lista = list(partDer)

    suma = 0
    con = 1
    for i in lista:
        suma+=int(i)*(8**-con)
        con+=1
    resultado+=suma
    return resultado
def octF2Bin(num):
    dec=octF2Dec(num)
    resultado=flotante2Binario(dec)
    return resultado

def octF2Hex(num):
    dec = octF2Dec(num)
    resultado = float2Hex(num)
    return resultado

def hex2Dec(num):
    resultado=int(num,16)
    return resultado
def hex2Bin(num):
    resultado=bin(hex2Dec(num))[2:]
    return resultado
def hex2Oct(num):
    resultado=oct(hex2Dec(num))[2:]
    return resultado
def hexF2Dec(num):
    partIzq, partDer = str(num).split(".")
    resultado = int(partIzq, 16)

    lista = list(partDer)

    suma = 0
    con = 1
    for i in lista:
        suma+=int(i,16)*(16**-con)
        con+=1
    resultado+=suma
    return resultado

def hexF2Oct(num):
    dec=hexF2Dec(num)
    return flotante2Oct(dec)
def hexF2Bin(num):
    dec=hexF2Dec(num)
    return flotante2Binario(dec)

def flotante2BinIEE32(num):
    num = float(num)

    if num < 0:
        signo = 1
        num = (num * -1)
    else:
        signo = 0

    if (num >= 0 and num < 1):
        mantisa = ""
        exp = 0
        frac = 0
        while frac < 1:
            frac = num / 2 ** -(exp + 1)
            exp += 1

        exp = bin(-exp + 127)[2:]

        frac = str(frac).lstrip("1.")

        frac = "0." + frac
        frac = float(frac)

        mantisa = ((flotante2Binario(frac))).lstrip("0.")
        signo = str(signo)
        exp = str(exp)
        while len(mantisa) < 23:
            mantisa += "0"
        while len(exp)<8:
            exp="0"+exp
        res = (signo + "-" + exp + "-" + mantisa)

    else:

        binarioF = flotante2Binario(num)

        lista = list(binarioF)

        cont = 0
        mantisa = ""
        for x in lista:
            if x != ".":
                cont += 1

            else:
                break

        cont = cont - 1 + 127

        exponente = bin(cont)[2:]


        for x in range(len(lista)):

            if not (x == 0 or lista[x] == "."):

                mantisa += str(lista[x])


        while len(mantisa) < 23:
            mantisa += "0"


        signo = str(signo)
        exponente = str(exponente)

        res = (signo + "-" + exponente + "-" + mantisa)
    return res

def binIEEE32ToFlotante(num):
    signo, exponente, mantisa = str(num).split("-")
    signo=int(signo)

    binario = ""
    num = int(exponente, 2)

    num -= 127

    mantisa="1"+mantisa
    lista = list(mantisa)
    lista.insert(num+1,".")

    for x in range(len(lista)):
        binario+=lista[x]

    res = binarioFDecimal(binario)
    if(signo==1):
        res=res*-1

    return res

def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def menu():
    salir = False
    opcion = 0

    while not salir:

        print("1. Decimal")
        print("2. Binario")
        print("3. Octal")
        print("4. Hexadecimal")
        print("5. IEE 32 bits")
        print("6. salir")
        print("Elige una opcion")

        opcion = pedirNumeroEntero()

        if opcion == 1:
            num = input("Escriba un numero decimal: ")

            try:
                num = float(num)
                print(flotante2Binario(num))
                print(flotante2Oct(num))
                print(float2Hex(num))
            except ValueError:
                num = int(num)
                print(entero2Bin(num))
                print(entero2Oct(num))
                print(entero2Hex(num))
        elif opcion == 2:
            num = input("Escriba un numero binario: ")
            if num.__contains__("."):
                print(binarioFDecimal(num))
                print(binarioF2Oct(num))
                print(binarioF2Hex(num))

            else:
                print(binario2Decimal(num))
                print(binario2Oct(num))
                print(binario2Hex(num))
        elif opcion == 3:
            num=input("Escriba un numero octal: ")
            if not num.__contains__("."):
                print(oct2Dec(num))
                print(oct2Bin(num))
                print(oct2Hex(num))
            else:
                print(octF2Dec(num))
                print(octF2Bin(num))
                print(octF2Hex(num))
        elif opcion==4:
            num=input("Escriba un numero hexadecimal: ")
            if not num.__contains__("."):
                print(hex2Dec(num))
                print(hex2Bin(num))
                print(hex2Oct(num))
            else:
                print(hexF2Dec(num))
                print(hexF2Bin(num))
                print(hexF2Oct(num))
        elif opcion==5:
            num=input("Escriba un numero decimal o binario IEEE 32 bits (separar con guiones): ")
            if num.__contains__("."):
                print(flotante2BinIEE32(num))
            else:
                print(binIEEE32ToFlotante(num))

        elif opcion == 6:
            salir = True
        else:
            print("Introduce un numero entre 1 y 3")

    print("Fin")

menu()