#JUEGO DE PICAS Y FIJAS

"""
Creado por Diego Fernando Macana Naranjo
Es un Juego muy sencillo abierto a la extencion, abre la mente en su forma de programacion
y me tome el tiempo para documentar cada linea para su comprension . 


"""
from random import randint # lo que hace esta libreria es permitir que python use las funciones de random 

def pedir_numeros():  # esta funcion pide los numeros al usuario, de tal modo de que los 4 numeros sean enteros positivos en el rango de [0,9]
    lista=[]  # una lista vacia
    conta=0  # contador en 0, que nos servira para mirar cuando el usuario haya digitado los 4 digitos 

    while conta<4:   # este contador es para mirar lo de los 4 digitos 
        while (True):  # este while, lo coloco tu profe en una guia, y quiere decir que mientras el numero digitado no sea entero, vuelvalo a pedir 
            try:  #intar
                a=int((input("Ingrese los digitos de su numero: "))) #intentar... pedir un numero entero
                break # si no genera error, me saca del while y acepta el numero 
            except (ValueError): # si el intento fallo, entonces me dice "error...." y luego vuelve a pedir el numero 
                print ("Error. El numero debe ser entero")
        
        if a>=0 and a<=9:  # esto controla que el numero este entre 0 y 9
            lista.append(a)  # si esta en el rango, lo adiciona a la lista con la funcion .append()
            conta=conta+1 #contador +1. es decir ya tengo un digito mas de los 4 que necesito 
        else:
            print("Error. El digito no esta en el rango [0,9]") # imprime el error si no esta en ese rango 

    #aca termina el while 
            #1,2,2,3
    aux=[] # inicio un auxiliar vacia 
    for i in range (4): # recorro los numeros que da el usuario, con el fin de mirar que no esten repetidos 
        if lista[i] in aux:   # si el digito esta en aux, significa que esta repetido
            print ("Hay digitos repetidos en el numero que ingreso") # imprimo el error
            print ("ingrese de nuevo los digitos de su numero ") # y le digo que tiene que hacer todo desde 0 
            return pedir_numeros()   # y retorno de nuevo a esta misma funcion, es decir "reinicio"
        else: # en caso contrario osea que el digito no este en aux: el digito se adiciona a aux, recuerda que el primer digito siempre sera adicionado porque aux es vacio
            aux.append(lista[i])
        
 
    return [str(lista[0]),str(lista[1]),str(lista[2]),str(lista[3])]  # si llego hasta aca, es porque los digitos que dio el usuario son correctos y se pueden evaluar 
            
            
def repetidas(n):  # esta funcion hace que el numero que da el computador no tenga caracteres repetidos
                    # si el numero es 1,2,3,4 es correcto, pero si es 1,2,3,3 seria incorrecto debido a que tiene numeros que se repiten. 
    lista=[]  # inicio una lista vacia
    n=list(str(n))  # recuerda que el numero es 1233. esto lo transforma en ["1","2","3","3"]
    
    for i in range (len(n)): # recorro el numero transformado en lista
        if n[i] in lista:  # pregunto si el caracter, para el primer caso pregunto "1" esta en la lista? 
            a=n[i]         # de ser asi, a=n[i], y a es una variable que va ser cambiada por un dato que No este en la lista 
            
            salir=0   # salir es 0 hasta que la variable a no este en la lista ["1","2","3","3"]
            while salir==0:  # recorre infinitamente hasta que la condicion se cumpla para que salir=1
                if str(a) in n:  # digo si a esta en ["1","2","3","3"]
                    a=randint(0,9) # entonces, cambie a por un numero aleatorio entre 0,9 
                else:   # en caso que a ya no este en la lista ["1","2","3","3"]
                    lista.append(str(a))  # adicione a a la lista vacia  que cree con el proposito de no ingresar datos repetidos 
                    salir=1  # y pues sale del while 
        else:   # si el caracter no esta en la lista vacia  que cree con el proposito de no ingresar datos repetidos , lo adiciona 
            lista.append(n[i]) #aca el .append() hace la adicion de n[i] donde n[i] es el caracter no repetido
    return lista  # devuelvo el valor correcto tipo ["1","2","3","5"]


def fijas1(n,lista):   # si el computador tiene 1234 y el usuario 1245 , fijas debe ser 2
    conta=0  # contador igualado a 0 
    for i in range (4):  # recorro ambas numeros, el que dio el computador y el que dio el usuario 
        if n[i]==lista[i]:   # para cada caracter, si son iguales n[i]=lista[i] y estan en la misma posicion [i]=[i] entonces 
            conta=conta+1    # fijas va sumando 1, es decir cuenta a una fija 
        else:    #caso contrario
            pass  #pase, no haga nada, quedese mirando, medite, la cuarentena es un pass en nuestras vidas, lei una vez. XD 
    return conta   #me devuelve la cantidad de fijas que encontro

def picas1(n,lista):   # si el computador tiene 1234 y el usuario 1245 picas debe ser 1, ya que el 4 esta en ambas, pero no en la misma posicion
    conta=0 #contador es 0 inicialmente
    for i in range (4): #  recorro ambos numero de nuevo, el que da el compu y el que da el usuario 
        if n[i]==lista[i]:  #  para cada caracter, si son iguales n[i]=lista[i] y estan en la misma posicion [i]=[i] entonces 
            pass     #cuarentena 
        elif n[i] in lista:  # si el numero que da el usuario esta en el numero que da el computador, entonces conta+1 osea incrementa el valor de picas 
            conta=conta+1   #conta+1
    return conta   # devuelve la cantidad de picas que encontro


def juego():  # este es el programa principal, en el cual se ejecutaran las funciones puestas anteriormente
    
    print ("HOLA, Bienvenido al juego de Picas y Fijas. ")  #doy inicio inicio al programa
    print ("El juego consiste en adivinar un numero de 4 digitos, en cada intento el juego le mostrara fijas y picas, donde fijas son numeros que estan bien posicionados y correctos, y picas son numeros que pertenecen a la cifra pero que estan mal posicionados")
    print ("Su respuesta debe contener numeros no repetidos")
    n=randint(1000,9999) # pido un numero de 4 digitos 
    n=repetidas(n)  # la respuesta va contener caracteres no repetidos, como ejemplo : 1234, un error seria: 1223
    
    #n=["1","2","3","4"]
    print ("Imprimo el numero correcto con el animo de que vean la funcionalidad mas clara. Para jugar pueden documentar la siguiente linea con un # al inicio del renglon  ")
    print("El numero secreto es: ",n[0]+n[1]+n[2]+n[3])   # 1+2+3+4 = 1234
    
    lista=pedir_numeros()   # son los valores que da el usuario, sin que los caracteres se repitan
    
    r=0 # es una variable que me identifica si el jugador gano el juego 
    
    for i in range (3):   # recuerda que el jugador tiene solo 3 intentos para ganar 
        print ("Intento #",i+1,"del jugador: ")   # imprime intento 0+1 del jugador:     recuerda que el i siempre inicia en 0 
        print (str(lista[0])+str(lista[1])+str(lista[2])+str(lista[3]))   # recuerda el holamundo entonces "1"+"2"+"3"+"5" = 1235
        print ("Fijas:",fijas1(n,lista))   # aca ejecuta la funcion fijas y muestra cuantas fijas tuve 
        print ("Picas:",picas1(n,lista))   # aca ejecuta la funcion picas y muestra cuantas picas tuve 
        
        if n[0]+n[1]+n[2]+n[3]==str(lista[0])+str(lista[1])+str(lista[2])+str(lista[3]):  # si 1+2+3+4 == 1+2+3+4 osea 1234=1234 entonces: 
            print ("GANASTE el numero era: ",n[0]+n[1]+n[2]+n[3])  #ganaste!!!!!!!!!!!!!!! el numero es 1234
            print ("Gracias por jugar con juegos divertidos SAS") # gracias por ganar .-.
            r=1    # identifica que el jugador gano el juego 
            break    # a mumir, es decir, ya no haga nada mas en este for 
        
        elif i==2:  # este fue un arreglo al error que te conte, entonces cuando se acaben los intentos, de una vez 
            break   # a mumir (a dormir )
        else:  # en caso contrario, osea que los intentos aun no se acaben 
            lista=pedir_numeros()  # vuelva y pida los numeros al usuario

            
    #aca termina el juego
            
    if r!=1:   # si r es diferente de 1, es porque perdio
        print ("¡perdiste!")                # imprime PERDIO JAJA inutil ni pa un juego puede... o algo asi. :c
    
juego()              #esta linea es la mas importante, sin ella nada de lo que esta escrito en este archivo se ejecuta, juego() es la funcion que me permite jugar 
