import random as rd # estamos importando la biblioteca random para generar numeros aleatorios
import csv # estamos importando la biblioteca csv para trabajar con archivos csv

''' FUNCION QUE GENERA CREDITOS ALEATORIOS - OPCION 1'''
def asignar_creditos_aleatorios(alumnos):# función para generar creditos aleatorios
    
    # asignar creditos aleatorios entre 50 y 100 a cada alumno
    
    #Devolver un diccionario con los creditos asignados
    
    creditos_alumnos = {} # diccionario vacio para almacenar los creditos_alumnos,vuelvo a inicializarlo vacio
    #iterar sobre cada alumno en la lista alumnos
    for alumno in alumnos:# recorre cada alumno en la lista alumnos
        #genera numero entero aleatorio para cada alumno
        credito = rd.randint(50,200) #uso la biblioteca random, función randint() que toma dos parámetros(min y max)
        # biblioteca de python ,forma funciones aleatorias ,dentro coloco rango, me devuelve un valor entero y lo guarda en la variable 'credito'
        # se lo asignaremos a 'credito' generado al alumno que corresponde en el diccionario
        creditos_alumnos[alumno] = credito # guardo el credito_alumnos en el diccionario 

    print(" Créditos aleatorios asignados correctamente ") # imprimo que se han generado los creditos aleatorios
    print(creditos_alumnos) # imprimo el diccionario con los creditos_alumnos
    return creditos_alumnos # devuelvo el diccionario con los creditos_alumnos
''' FUNCION QUE CLASIFICA LOS CREDITOS - OPCION 2 '''
def clasificar_creditos(creditos_alumnos): # función para clasificar los creditos
    #realizo un diccionario porque guardo clave-valor (alumno con su respectivo credito)
    menor_100={} # en este diccionario guardo alumnos con creditos menor_100
    entre_100_150={} # en este diccionario guardo alumnos con creditos entre 100_150
    mayor_150={} # en este diccionario guardo alumnos con creditos mayor_150
    
    for alumno ,credito in creditos_alumnos.items():# el 'for' revisa c/cada alumno y el credito (cada items)
        if credito < 100: # si credito es menor que 100       
            menor_100[alumno]= credito #le asigno a ese 'alumno' el 'credito' o se lo paso a esa variable
        elif credito <=150: #sino si ,menor o igual a 150
            entre_100_150[alumno]=credito # le asigno a ese 'alumno' el 'credito' o se lo paso a esa variable
        else:
            mayor_150[alumno]=credito # le asigno a ese 'alumno' el 'credito' o se lo paso a esa variable
        
    # mostrar resultados de clasificación
    # 'len' cuenta los contenidos dentro de una colección
    # menores a 100
    print("\n Créditos menor a 100 ,TOTAL",len(menor_100)) # lee los creditos menor_100, 'len' lee el tamaño menor_100 (valor-dato)
    for alumno,credito in menor_100.items(): # recorro alumno y credito en menor_100( el items es el valor)                 
        print(alumno,": $",credito) # printeo para verificar que datos estan bien
        
    # entre 100_150
    print("\n Créditos entre 100 y 150 ,TOTAL",len(entre_100_150))# lee los creditos entre_100_150, len lee el tamaño de entre_100_150 (valor-dato)
    for alumno,credito in entre_100_150.items():# recorro alumno y credito en entre_100_150( el items es el valor)  
        print(alumno,": $",credito)# printeo para verificar que datos estan bien
        
    # mayor_150
    print("\n Créditos mayor a 150 ,TOTAL",len(mayor_150))# lee los creditos mayor_150, len lee el tamaño de entre 100 y 150 (valor-dato)
    for alumno,credito in mayor_150.items():# recorro alumno y credito en mayor_150( el items es el valor)  
        print(alumno,": $",credito) # printeo para verificar
''' FUNCION QUE CALCULA ESTADISTICAS - OPCION 3'''
def calcular_estadistica(creditos_alumnos): # calcular estadisticas de creditos
    '''calcular maximo,minimo y promedio'''

    creditos = list(creditos_alumnos.values()) # de 'creditos_alumnos' solamente sacaremos el valor / creamos una lista de los datos de creditos_alumnos
    if not creditos: # si creditos no tiene datos entonces de la lista de los datos de creditos
        print(" No se han asignado creditos aún ") # printeo para avisar que no se han asignado creditos
        return None,None,None # no se han asignado creditos no tiene datos entonces
       
    max_credito = max(creditos) # dentro de esta lista,se calcula el maximo , 'max' es una funcion de python
    min_credito = min(creditos) # dentro de esta lista,se calcula el minimo , 'min' es una funcion de python
    promedio_credito = sum(creditos)/len(creditos) # la suma de los 'creditos' dividido x la 'cantidad(len)
    return max_credito,min_credito,promedio_credito # puedo retornar 3 valores enseguida(mismo orden)

''' GENERAR REPORTE EN FORMATO CSV - OPCION 4'''
def generar_reporte(creditos_alumnos): # generar reporte en formato csv con los creditos de los alumnos
    with open ('reporte_creditos.csv','w',newline='') as archivo: # nombre archivo + 
        escritor = csv.writer(archivo,delimiter=',') # creo una variable escritor y le paso el archivo y el separador
        escritor.writerow(['Nombre Alumno','Creditos']) # escribo cabecera del csv , encabeza que la primera columna es el nombre del alumno y la segunda es los creditos
        # ahora escribo cada alumno y su credito en el csv
        for alumno,credito in creditos_alumnos.items(): # el 'for' revisa c/cada alumno y el credito (cada items es el valor)  
                escritor.writerow([alumno,credito]) # escribo cada alumno y su credito en el csv
    print(" Reporte generado correctamente en el archivo reporte_creditos.csv") # muestro que el reporte se generó correctamente

'''  GENERAR REPORTE EN FORMATO TXT - OPCION 4 *ALTERNATIVA''' 
def reporte_txt(creditos_alumnos): # generar reporte en formato txt con los creditos de los alumnos
    with open ('reporte_creditos.txt','w') as archivo: # nombre archivo + 'w' es para escribir en el archivo
    # ahora escribo cada alumno y su credito en el txt
        for alumno,credito in creditos_alumnos.items(): # el 'for' revisa c/cada alumno y el credito (cada items es el valor)  
            archivo.write(f"{alumno}: $ {credito}\n") # escribo cada alumno y su credito en el txt
    print(" Reporte generado correctamente en el archivo reporte_creditos.txt") # muestro que el reporte se generó correctamente