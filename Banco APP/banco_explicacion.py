# proyecto de banco
"""
Creado por Diego Fernando Macana Naranjo
Este repositorio tiene como objetivo mostrar el uso de archivos.txt
Lo programe con la mente de un programador novato con el fin de mostrar todo un proceso en una sola funcion.
Es un mal habito hacer funciones tan grandes, este programa se pudo reducir mucho en sus lineas de codigo usando
otras formas de programar, pero en AYPR aun no se usan metodos como recurencia.
Si quieren intentar, pueden hacer una funcion que valide la cedula y el tipo de cedula, y disminuyan el codigo, si lo hacen bien el codigo
disminuira aproximadamente en 25 renglones.



"""
from datetime import date         #Libreria util para usar el tiempo, por ejemplo, la hora que tiene registrada en su sistema operativo y operaciones con fechas.


def pedir_edad(nacimiento):
    nacimiento=nacimiento.split("/")                                             # transformo la fecha de nacimiento asi: ["02","02","1990"]

    nacimiento=date(int(nacimiento[2]),int(nacimiento[1]),int(nacimiento[0]))    # Agrego la funcion date, que hace que date(año,mes,dia)  quede asi: 1990-02-02
    x=date.today()                                                               # x seria como el dia actual 
    y=nacimiento.replace(year=(x.year))                                          # y seria como la fecha de cumpleaños, el "dia"
    if y>x:                                                                      # digo que si el dia del cumpleaños es mayor al actual entonces 
        return x.year-nacimiento.year-1                                          # aun no ha cumplido años, es decir si este año cumplo 21, entonces tengo 20 
    else:
        return x.year-nacimiento.year                                            # aca si seria tener 21, ya que este año ya cumpli años 


#La funcion pedir_datos es de las mas largas que tiene este programa. Realmente es una mala practica
#lo deje asi para que puedan ver todo un proceso lineal, pero si lo desean pueden volver mas chico esta funcion usando mas metodos.
#Pero digo que es una mala practica pero nunca lo explico, aca les va el carretazo: "hagan de cuenta que tienen un programa como esta funcion pero
# con 5 mil lineas de codigo, y que les aparezca un error en la funcion main... tendrian que revisar las 5 mil lineas para solucionar el problema
#AHora bien si estas 5 lineas estan repartidas en muchas funciones, un error puede aparecer en la funcion sumar, tendrian que revisar solo esa funcion
#Se recomienda que una funcion no supere los 20 renglones, para su facil comprension.


#Esta funcion pide los datos de un usuario y dependiendo su edad pide un deposito. Si se dan cuenta son puros input, nada del otro mundo
def pedir_datos(asociados):
    asociado=[]
    tipo_de_documento=(input("Diguite su tipo de documento: "))
    salirr=0
    aux=0
    
    while salirr==0:    
        numero_de_documento=(input("Diguite su numero de documento "))
        for i in range (len(asociados)):
            if numero_de_documento in asociados[i]:
                print ("el documento que digito ya se encuentra registrado.")
                return (asociados)
            else:
                aux=aux+1
        if aux==len(asociados):
            salirr=1
            
    nacimiento=(input("Diguite su fecha de nacimiento dd/mm/aaaa "))
    
    tipo=input("Digite si es estudiante, administrativo o profesor ")
    nombre=input("Diguite sus nombres junto sus apellidos ")
    salir=0
    clave=""
    while salir==0:
        if len(list(clave))==4:
            salir=1
        else:
            clave=input("Diguite una clave de 4 digitos ")
    Estado_del_asociado="activo"
    edad=pedir_edad(nacimiento)                             
    
    if edad>50:
        if tipo=="profesor" or tipo=="administrativo":
            fondo_inicial=str(input("Su fondo inicial debe ser mayor a 30.000, cuando desea depositar?: "))
            salir1=0            
            while salir1==0:           #veras otros while parecidos a este, su funcion es controlar que un valor este en un rango, podrias programar un while asi para pedir siempre un numero positivo por ejemplo.
                if int(fondo_inicial)>30000:
                    salir1=1
                else:
                    print ("valor insuficiente. ")
                    fondo_inicial=str(input("Su fondo inicial debe ser mayor a 30.000, cuando desea depositar?: "))            
        else:
            fondo_inicial=50000
    elif edad>=18 or edad<=50:
        if tipo=="profesor" or tipo=="administrativo":
            fondo_inicial=str(input("Su fondo inicial debe ser mayor a 60.000, cuando desea depositar?: "))
            salir2=0            
            while salir2==0:
                if int(fondo_inicial)>60000:
                    salir2=1
                else:
                    print ("valor insuficiente. ")
                    fondo_inicial=str(input("Su fondo inicial debe ser mayor a 60.000, cuando desea depositar?: "))
        else:
            fondo_inicial=str(input("Su fondo inicial debe ser mayor o igual a 50.000, cuando desea depositar?: "))
            salir3=0
            while salir3==0:
                if int(fondo_inicial)>=50000:
                    salir3=1
                else:
                    fondo_inicial=str(input("Su fondo inicial debe ser mayor o igual a 50.000, cuando desea depositar?: "))
    else:
        salir4=0
        fondo_inicial=str(input("Su fondo inicial debe ser mayor o igual a 25.000, cuando desea depositar?: "))
        while salir4==0:
            if int(fondo_inicial)>=25000:
                salir4=1
            else:
                fondo_inicial=str(input("Su fondo inicial debe ser mayor o igual a 25.000, cuando desea depositar?: "))

    asociado=asociado+[tipo_de_documento]+[numero_de_documento]+[nacimiento]+[tipo]+[nombre]+[clave]+[Estado_del_asociado]+[fondo_inicial]+[str(edad)]   #retorna la lista de todos los datos. esta lista entrara a la matriz asociados y al documento de textp. 
    return asociado


#Esta funcion no la documentare debido a que solo sirve para ver el saldo de un usuario y bloquea al usuario al tener mas de 3 intentos
#Prefiero documentar funciones de dificil comprension como la de retiros. 
def consultar(asociados):
    doc=input("Deme el tipo de documento: ")
    num=input("Deme el numero de documento: ")
    conta=0
    for i in range (len(asociados)):
        if doc in asociados[i] and num in asociados[i]:
            if asociados[i][6]=="activo":
                while (conta<3):
                    clave=input("digite la clave : ")
                    if clave in asociados[i]:
                        print ("El saldo actual de su cuenta es: $",asociados[i][7])
                        conta=3
                    else:
                        print("clave incorrecta,recuerde que al 3 intento su cuenta se bloqueara, intentos: ",conta+1)
                        conta=conta+1
                        if conta==3:
                            asociados[i][6]="bloqueado"
                            print("Su cuenta ha sido bloqueada por mas de 3 intentos en la clave. ")
                    
            else:
                print ("Su cuenta esta bloqueada. vaya a la opcion 3 para desbloquear")
    k=0
    for i in range (len(asociados)):
        if num in asociados[i]:
            pass
        else:
            k=k+1
    if k==len(asociados):
        print ("El numero de documento que dio es incorrecto")
    return (asociados)




#Funcion de desbloquear una cuenta.
def desbloqueo(asociados):
    tipo=input("diguite el tipo de documento que tiene: ")
    num=input("digite su numero de documento: ")
    cont=0
    for i in range (len(asociados)):
        if tipo in asociados[i] and num in asociados[i]:                    #Pregunto si el tipo de identificacion y el numero se encuentra en la base de datos. 
            pass                                                            #EL pass que necesito en mi vida :'v
        else:
            cont=cont+1                                                     #contador que me ayuda a saber si no se encontro a la persona 
    if cont==len(asociados):                                                #aca efectivamente uso a cont 
        print ("El documento que escribio no se encuentra en nuestra base de datos")
    for i in range(len(asociados)):                                         #for que recorre asociados.
        if tipo in asociados[i] and num in asociados[i]:                    #Pregunto si el tipo de identificacion y el numero se encuentra en la base de datos de nuevo. 
            if "activo" in asociados[i]:                                    #Pregunto si la palabra activo se encuentra en la linea donde encontro a la persona 
                f=1                                                  
                print ("La cuenta esta activa. ")                           #si entro al if significa que no necesito hacer nada mas porque esta activa y break, es decir finalizo 
                break
            elif "bloqueado" in asociados[i]:                               #Pregunto si el usuario esta bloqueado
                print ("Debe de realizar un pago de 50.000 el cual sera depositado en su cuenta y se le descontara el costo del servicio")
                print ("La solicitud se a realizado con exito! ")           #Se asume que la persona pago los 50.000 y que el servicio cambia segun lo indicado
                asociados[i][6]="activo"                                    # activo de nuevo al usuario 
                edad=int(asociados[i][8])

                #Dependiento de la clase de persona y su edad se le cobrara de los 50.000 mil un dinero para desbloquear la cuenta 
                if asociados[i][3]=="estudiante":
                    if edad<18:             
                        asociados[i][7]=str(int(asociados[i][7])+30000)      
                    else:                                         
                         asociados[i][7]=str(int(asociados[i][7])+10000)
                elif asociados[i][3]=="administrativo":
                    if edad>50:
                        asociados[i][7]=str(int(asociados[i][7])+32000)
                    else:
                        asociados[i][7]=str(int(asociados[i][7])+15000)
                elif asociados[i][3]=="profesor":
                    if edad>50:                                               
                        asociados[i][7]=str(int(asociados[i][7])+30000)      
                    else:                                              
                        asociados[i][7]=str(int(asociados[i][7])+10000)
                print ("El dinero actual de la cuenta es: "+asociados[i][7])     #Finalmente imprime el saldo actual.  
    return asociados



def retiro(asociados):
    tipo=input("digite su tipo de documento: ") # pido el tipo de documento, por lo general para los usuarios que tenemos es cc, mire el documento de texto para saber la informacion
    documento=input("digite su documento: ")    # pido el numero de documento, para hacer pruebas use los que ya tiene en la base de datos
    conta=0                                     #inicio un contador en 0 para luego si llega a 3 bloquea al usuario por la clave incorrecta 3 veces 
    for i in range (len(asociados)):            # recorre todas las filas de la matriz, recurde que cada fila es un usuario tipo:
                                                #[cc,1019144022,10/10/1990,estudiante,diego,1234,51.000,22]  
                                                #[i][0]:tipo documento [i][1]: numero documento   [i][2]:fecha de cumpleaños [i][3]: tipo de persona en ese caso "estudiante" y asi 
        if documento in asociados[i] and tipo in asociados[i]:  # preguntamos si en alguna fila esta el documento que digito el usuario
            print ("Bienvenido")                                # en el caso que encuentre el documento, entonces dice bienvenido, es una señal para nosotros de que el documento si esta
            print("Se pueden hacer retiros mayores a 10 mil y menores a 600 mil") #una simple advertencia 
            if "activo" in asociados[i]:                                                    # pregunto si en esa fila donde encontro el documento, se encuentra la palabra "activo"
                while (conta<3):                                                            # inicio un ciclo que para cuando conta llegue a 3, este ciclo es para controlar la clave 
                    clave=input("digite la clave : ")                                       #pido la clave 
                    if clave in asociados[i]:                                               # si la clave esta en la fila donde encontro el documento, entonces deja continuar el proceso
                        cantidad=int(input("que cantidad desea retirar?: "))                # pido el monto a retirar 
                        conta=3                                                             # y como la clave es correcta, entonces conta=3 significa, saqueme del ciclo de la clave cuando termine lo que queda 
                        if cantidad>10000 or cantidad<600000:                               # el ejercio dice que no permite hacer retiros menores a 10 luks y mayores a  600 palos 
                            cuatro=(cantidad*4)/1000                                        # calculo el 4 x mil, es decir por cada mil pesos retirados,el banco cobra 4 pesos

                            #aca calculo la comision del banco de la escuela que depende si es estudiante, administrativo o profesor 
                            if asociados[i][3]=="estudiante":                                                           # si es estudiante 
                                comision=cantidad*0.02                                                                  # entonces se le cobra el 2% de la cantidad que quiera retirar
                            else:                                                                                       #si no es estudiante, entonces se infiere que es profesor o administrativo
                                comision=cantidad*0.01                                                                  # entonces se le cobra el 1% de la cantidad que quiera retirar
                            total=cantidad+cuatro+comision                                                              # hacemos una variable total, que es el monto que quiere retirar mas la suma de los dos impuestos
                            
                            if float(asociados[i][7])>=total:                                                           # asociados[i][7] es el dinero de la persona que se identifico el documento,
                                                                                                                        # preguntamos si el tiene la cantidad que desea retirar mas los impuestos 
                                asociados[i][7]=str(float(asociados[i][7])-total)                                       # si es asi, entonces se le resta al dinero de la persona el total
                                print ("ud retiro: ",cantidad,"se le cobro: ",cuatro+comision,"por impuestos")          # se le informa a la persona cuanto saco de dinero y cuanto se le cobro por la transaccion

                                asociados[0][7]=str(float(asociados[0][7])+cuatro)                                      #entonces en la matriz la posicion asociados[4][7] fijese que no usamos la i, sino 4 y 7
                                                                                                                        #pero porque? bueno, pues porque en esa posicion se encuentra el dinero del banco, siempre va ser esa..
                                asociados[1][7]=str(float(asociados[1][7])+comision)                                    # lo mismo para la posicion del dinero del banco de la escuela [5][7].
                                                                                                                        #al banco le sume al dinero que ya tenia el 4 x mil y al banco de la escuela le sume el dinero que ya tenia mas la comision
                                print("Su saldo ahora es: ",asociados[i][7])                                            # imprimo el nuevo saldo de la persona que retiro, fijese que el i es para la persona que realiza el retiro
                                
                        else:                                                                                           # este es el caso en donde la persona quiere retirar menos de 10 mil o mas de 600 mil
                            print ("la cantidad suministrada incumple nuestras politicas")                              # imprime el mensaje del error del usuario 
                            break                                                                                       # break lo que hace es hacer terminar el for de una. haga de cuenta como que es un boton de apagado
                            
                    else:                                                                                               # este es el caso en donde digita la contraseña mal, entonces 
                        print("clave incorrecta,recuerde que al 3 intento su cuenta se bloqueara, intentos: ",conta+1)  #imprime el error y
                        conta=conta+1                                                                                   # hace conta+1 es decir ya el computador sabe que lleva un intento fallido en la contraseña
                        if conta==3:                                                                                    # cuando conta es igual a 3 entonces procede a bloquear la cuenta 
                            asociados[i][6]="bloqueado"                                                                 # vea que de nuevo usamos el i, es decir la informacion del usaurio osea [i][6] que estaba en activo ahora es "bloqueado"
                            print("Su cuenta ha sido bloqueada por mas de 3 intentos en la clave. ")                    # imprime lo que paso :(
            else:                                                                                                       # en el caso que el usuario este bloqueado le dice el error 
                print ("su cuenta esta inactiva")
                break                                                                                                   # y de nuevo lo saca del for 

    #listo eso es todo, esto de abajo no es tan importante, simplemente avisa cuando el usuario digito un documento que no esta registrado, es decir no esta en la base de datos
    k=0                                                                             #inicio un contador
    for i in range (len(asociados)):                                                # recorro las filas de la matriz
        if documento in asociados[i]:                                               #si encuentra el documento que estamos buscando no hace nada 
            pass                                                                    # pass significa "no haga nada" ,"pase", "ignore" hahaha aveces necesito un pass en mi vida 
        else:                                                                       # en el caso que no encuentre el documento hay si hace algo, k=k+1 es decir va acomulando las veces que no encontro el documento en una fila 
            k=k+1

    if k==len(asociados):                                                           #  esto es lo que realmente importa, dice: si k recorrio todas las filas y en ninguna encontro el documento entonces:
        print ("El numero de documento que dio es incorrecto")                      # diga que el documento es incorrecto
        
    return asociados                                                                #aca retorna asociados, si no hace nada por algun error del usuario, la devuelve intacta y no cambia nada, pero si la modifico, pues la devuelve modificada
                                                                                    #recuerde que en ambos casos, el documento posteriormente se borra y se actualiza con esta "nueva matriz" que esta en este return.



def transferencia(asociados):
    print (asociados)
    tipo=input("digite su tipo de documento: ")
    documento=input("digite su documento: ")   
    conta=0  
    for i in range (len(asociados)):
        if documento in asociados[i] and tipo in asociados[i]:                                              # preguntamos si en alguna fila esta el documento que digito el usuario
            print ("Bienvenido")                                                                            # en el caso que encuentre el documento, entonces dice bienvenido, es una señal para nosotros de que el documento si esta
            print("Se pueden hacer transferencias mayores a $10.000 y menores a $400.000 ")                 #una simple advertencia 
            if "activo" in asociados[i]:                                                                    # pregunto si en esa fila donde encontro el documento, se encuentra la palabra "activo"
                while (conta<3):                                                                            # inicio un ciclo que para cuando conta llegue a 3, este ciclo es para controlar la clave 
                    clave=input("digite la clave : ")                                                       #pido la clave 
                    if clave== asociados[i][5] and conta==0:                                                # si la clave esta en la fila donde encontro el documento, entonces deja continuar el proceso
                        tipo1=input("digite el tipo de documento de la cuenta que desea transferir ")
                        documento1=input("digite el # de documento de la cuenta que desea transferir  ")

                        h=0                                                                                 # un contador que nos ayudara a saber si el documento de pepe no esta en base de datos o si esta inactivo
                        for k in range (len(asociados)):                                                    # este for lo usare para encontrar a pepe 
                            if documento1 in asociados[k] and tipo1 in asociados[k] and "activo" in asociados[k]:  # aca hago la pregunta si pepe esta en base de datos y si esta activo
                                cantidad_trans=float(input("digite la cantidad de dinero que desea transferir : "))  # si es verdad lo de arriba, pido el monto al que va a transferir
                                if cantidad_trans>10000 and cantidad_trans<400000:                          # si el cantidad_trans se encuentra en este rango entonces:
                                    if asociados[i][3]=="estudiante":                                       # si es estudiante 
                                        comision=cantidad_trans* 0.04                                       #la comision es el 4 porciento, 
                                    else:                                                                   # si es administrativo o profesor
                                        comision=cantidad_trans* 0.03                                       #la comision es el 3 porciento 
                                else:  
                                    print ("La cantidad de la transacion es errada debido a que maximo se puede transferir $400.000 y minimo $10.000 ") 
                                    break                                                                   #y aca lo saca
                                if float(asociados[i][7])>=(cantidad_trans+comision):                       # aca dice que si el que va a transferir tiene el dinero mas comision               
                                    asociados[i][7]=(str(float(asociados[i][7])-(comision+cantidad_trans))) # aca le quita el dinero + comision
                                    asociados[1][7]=str(float(asociados[5][7])+(comision))                  # aca abona a la cuenta del banco el dinero 
                                    asociados[k][7]=str(float(asociados[k][7])+(cantidad_trans))            # aca le transfieren la plata a pepe
                                    
                                    print ("El saldo despues de la transferencia es: ",asociados[i][7])     # imprimo el nuevo saldo del que transfirio
                                else:                                                                       # este es el caso en donde el que va a transferir no tiene el dinero para hacer el proceso
                                    print ("El dinero en su cuenta no tiene capacidad para la transaccion. ")# le dice: vayase pobre (un poco de humor )
                                    break                                                                   #adios y lo saca
                            else:
                                h=h+1                                                                       # cada vez que no encuentre el documento de pepe o este inactivo suma k=k+1
                            if h==len(asociados):                                                           # dice si k recorrio toda la base de datos y no encontro a pepe:
                                print ("no se encontro el documento al que desea transferir")               # no encontre a pepe :(           
                        conta=3
                    elif clave in asociados[i] and conta!=0:                                                # si la clave esta bien y no fue digitada bien a la primera, te deja salir 
                            print ("volviendo al menu... ")                                                 # esto te deja salir del while y acaba el proceso
                            break

                    else:                                                                                   # este es el caso en donde digita la contraseña mal, entonces 
                        print("clave incorrecta,recuerde que al 3 intento su cuenta se bloqueara, intentos: ",conta+1)
                        conta=conta+1                                                                       # hace conta+1 es decir ya el computador sabe que lleva un intento fallido en la contraseña
                        if conta==3:                                                                        # cuando conta es igual a 3 entonces procede a bloquear la cuenta 
                            asociados[i][6]="bloqueado"                                                     # vea que de nuevo usamos el i, es decir la informacion del usaurio osea [i][6] que estaba en activo ahora es "bloqueado"
                            print("Su cuenta ha sido bloqueada por mas de 3 intentos en la clave. ")        # imprime lo que paso :(
            else:                                                                                           # en el caso que el usuario este bloqueado le dice el error 
                print ("su cuenta esta inactiva")
                break                                                                                       # y de nuevo lo saca del for 



    k=0                                                         #inicio un contador
    for i in range (len(asociados)):                            # recorro las filas de la matriz
        if documento in asociados[i]:                           #si encuentra el documento que estamos buscando no hace nada 
            pass                                                # pass significa "no haga nada" ,"pase", "ignore" hahaha aveces necesito un pass en mi vida 
        else:                                                   # en el caso que no encuentre el documento hay si hace algo, k=k+1 es decir va acomulando las veces que no encontro el documento en una fila 
            k=k+1

    if k==len(asociados):                                       # esto es lo que realmente importa, dice: si k recorrio todas las filas y en ninguna encontro el documento entonces:
        print ("El numero de documento que dio es incorrecto")  # diga que el documento es incorrecto
        
    return asociados
        
                    
            
# Aca hago un menu muy sencillo. su unica funcion es mostrar las opciones y pedir una opcion. retorna x
def menu():
    print ()
    print ("                 Bienvenido al banco Escuela de Ingenieria. ")
    print()
    print ()
    print ("        __________________MENU PRINCIPAL___________________   ")
    print ("        1. Registrar a un asociado")
    print ("        2. Consultar saldo")
    print ("        3. Desbloquear usuario")
    print ("        4. Retiros")
    print ("        5. Transferencias. ")
    print ("        6. salir. ")
    print ()
    x=int(input("        Que opcion desea:   "))
    print ()
    return x


def main():                                                 # inicialmente tenemos que subir la base de datos, la que tenemos guardada con nombre "datos.txt" entonces debajo del main estaran las funciones que
                                                            #usan bine de datos y encima del main estaran las funciones que usan la matriz. 
    asociados=abrir()                                       # usando esta funcion lo que hago es traer los datos del documento de texto, volverla una matriz y ahora esta matriz se llama asociados 
    leer_archivo(asociados)                                 # este renglon soluciona el problema de los enter que se daban dentro de la matriz, /n <--- *quita esta cosa 
    x=menu()                                                # imprime el menu y pide una opcion 

    while x!=6:                                             # si el usuario digita 6 es porque quiere salir 
        if x==1:                                            #registrar asociado
            
            asociado=pedir_datos(asociados)                 # voy a crear una lista, es decir un nuevo usuario, 
            asociados=asociados+[asociado]                  # agrego al nuevo usuario "lista" a la matriz
            borrar()                                        # borro el documento que tenia, por el hecho de que ahora tengo uno nuevo para agregar 
            subir(asociados)                                # agrego la nueva informacion junto con la que ya tenia. 
            
        elif x==2:                                          # consultar saldo 
            asociados=consultar(asociados)                  # esta vez lo que hago es cambiar algo a la matriz asociados, en este caso seria el estado "activo" a "bloqueado"
                                                            # en ese caso como modifico la matriz, entonces, de nuevo borro el documento y reemplazo
            borrar()                                        #borro de nuevo el archivo
            subir(asociados)                                #vuelvo a subir todos los datos al archivo
            
        elif x==3:                                          # desbloquear
            asociados=desbloqueo(asociados)                 # modifico de nuevo a asociados, con la funcion desbloqueo ya que hago cambios de "bloqueado" a "activo" y lo mismo
            borrar()                                        #borro y luego 
            subir(asociados)                                #vuelvo a subir la informacion actualizada
        elif x==4:                                          # retiros
            asociados=retiro(asociados)                     # modifico la matriz asociados, esta vez en la parte de dinero."""esta parte esta en def retiro(asociados), suba y hay le explico
            borrar()                                        #borro y luego 
            subir(asociados)                                # agrego la informacion actualizada
        elif x==5:                                          #transferencias
            asociados=transferencia(asociados)              #Uso la funcion transferencia para actualizar la matriz y solucionar el problema
            borrar()                                        #borro y luego 
            subir(asociados)                                #vuelvo a subir todos los datos al archivo
            
        x=menu()                                            #aca vuelvo a pedir una opcion del menu, hasta que en esta "pedida" digite "5"
    







"""
ESTE APARTADO ES LA ZONA DE MANIPULACION DE ARCHIVOS .TXT. EXAMINESE BIEN 
"""


#Abre un archivo llamado datos.txt en el cual crea una matriz vacia con la cantidad de lineas que tenga un archivo, examine la funcion cuantas()
#Por cada dato necesario necesitamos una columna adicional, este ejercicio requiere 9 datos, nombre, cedula... etc , entonces agrego 9 espacion vacios en una matriz vacia
# al entrar al for lleno la matriz con cada linea, es decir x.split(",") hace lo siguente dato="hola,soy,diego" lista=dato.split(",") es lista=["hola","soy","Diego"] entonces al tener esa lista lleno
#los espacios de la matriz vacia. Falla si los datos no superan el rango de la matriz, cuidado con eso !.
def abrir():
    f=open("datos.txt","r")
    i=0
    dato=cuantas()
    matriz=[[[""] for x in range(9)]for y in range(dato)]
    for x in f:
        info=x.split(",")
        matriz[i][0]=info[0]
        matriz[i][1]=info[1]
        matriz[i][2]=info[2]
        matriz[i][3]=info[3]
        matriz[i][4]=info[4]
        matriz[i][5]=info[5]
        matriz[i][6]=info[6]
        matriz[i][7]=info[7]
        matriz[i][8]=info[8]
        i=i+1
    f.close()
    return matriz

#Borra un documento de texto, recuerde que es posible usar datos.txt ya que este programa esta en la misma carpeta de este programa, sino, tiene que copiar la direccion del archivo asi c:/desktop/user/etc..
def borrar():
    f=open("datos.txt","r")
    lineas=f.readlines()
    f.close()
    f=open("datos.txt","w")
    for linea in lineas:
        f.write("")
    f.close()        
            
# Sube los datos de una matriz ordenados por comas a un archivo. 
def subir (asociados):
    f=open("datos.txt","w")  # Usen open(nombre del archivo, w ) donde w es write es decir que abres el archivo con proposito de escribir en el 
    datos=asociados
    
    
    for i in range (len(datos)):
        f.write(datos[i][0]+","+datos[i][1]+","+datos[i][2]+","+datos[i][3]+","+datos[i][4]+","+datos[i][5]+","+datos[i][6]+","+datos[i][7]+","+datos[i][8])
        f.write("\n")
    f.close()




#Funcion que cuenta las lineas de un archivo y retorna el numero de renglones    
def cuantas():
    fichero = open("datos.txt",'r')   # Usas la r "read" para solo hacer lectura del archivo
    dato=(len(fichero.readlines())) 
    fichero.close()
    return dato



#Esta funcion lee un archivo .txt, recuerden que pueden usar archivos excel y demas, en este caso use un bloc de notas.
#La funcion abre el archivo y cuenta cuantos renglones tiene llenos, borra un error por defecto que es \n, que se coloca al final de cada dato.
def leer_archivo(base_datos):
    with open("datos.txt") as f:
        contenido = f.readlines()
    fila_actual=len(contenido)
    contador=0
    for i in contenido:
        base_datos[contador]=i.replace("\n","").split(",")
        contador=contador+1
    


                #llamamos a la funcion Main para que ejecute el programa que acabamos de crear
main()

   
    



    





















