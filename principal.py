import funciones as fn # importo las funciones del archivo funciones.py

alumnos = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"] #  esta es una lista de los nombres de los alumnos

# Ejemplo de lista: Nombres de personas
# nombres = ['Ana', 'Carlos', 'María', 'Pedro', 'Luisa']

# Modificación de un elemento
# nombres[1] = 'Carmen'

# Agregar elementos a la lista
# nombres.append('Juan')
# nombres.insert(2, 'Sofía')  # Insertar en una posición específica

# Eliminar un elemento de la lista
# ultimo_nombre = nombres.pop()  # Elimina y devuelve el último elemento
# nombres.remove('María')  # Elimina por valor

creditos_alumnos={} # diccionario para almacenar los creditos de los alumnos

# {} diccionario almacena pares clave-valor de manera eficiente.
# Las claves deben ser únicas dentro de un diccionario, pero los valores pueden ser de cualquier tipo de datos.

# Acceso a elementos del diccionario
# Ejemplo: print(f"Nombre: {estudiante1['nombre']}")

# Modificación de un valor
# Ejemplo: estudiante1['promedio'] = 9.0


while True: # bucle infinito
    try: # sirve para controlar excepciones del menu
        print("\n ------MENU-----")
        print("0. Inicializar Créditos")
        print("1. Asignar Créditos aleatorios")
        print("2. Clasificar Créditos")
        print("3. Calcular Estadísticas")
        print("4. Generar Reporte en csv")
        print("5. Salir")

        opcionMenu = int(input(" Ingrese una opción de 0 a 5 : ")) # leo la opcion del menu
        
        if opcionMenu== 0: # si la opcion es 0 entonces, inicializo los creditos en cero para todos los alumnos --->
            creditos_alumnos = {alumno :0 for alumno in alumnos} # establecemos los creditos_alumnos en cero al diccionario
            print(" Créditos inicializados correctamente ") # printeo que se inicializaron los creditos
            
        elif opcionMenu== 1: # si la opcion es 1 entonces
            if not creditos_alumnos: # si NO existen creditos_alumnos 
                print(" Primero debe inicializar los creditos ! ") # printeo que primero debe inicializar los creditos
            else: # si existen creditos_alumnos --->
                creditos_alumnos= fn.asignar_creditos_aleatorios(alumnos) # llamo a la funcion que genera creditos aleatorios y le entrego la lista de alumnos
                
        elif opcionMenu== 2: # si la opcion es 2 entonces
            if creditos_alumnos: # si existen creditos_alumnos
                fn.clasificar_creditos(creditos_alumnos) # llamo a la funcion que clasifica los creditos y le entrego la lista de creditos_alumnos
            else: # si no existen creditos_alumnos --->
                print(" Primero debe asignar creditos") # printeo que primero debe asignar creditos
                
        elif opcionMenu== 3:# si la opcion es 3 entonces
            # esta opcion implementa una función para calcular las estadísticas básicas de los créditos de los estudiantes: 
            # ▪ Máximo crédito ▪ Mínimo crédito ▪ Promedio de créditos 
            if creditos_alumnos: # si existen creditos_alumnos entonces calculo estadisticas --->
                max_credito,min_credito,promedio_credito = fn.calcular_estadistica(creditos_alumnos) # llamo a la funcion que calcula estadisticas y le entrego la lista de creditos_alumnos junto a las estadisticas basicas
                if max_credito is not None: # si max_credito no es None (no esta vacio) entonces, muestra estadisticas --->
                    print("Máximo crédito : ",max_credito) # muestra el maximo credito  
                    print("Mínimo crédito : ",min_credito) # muestra el minimo credito  
                    print("Promedio crédito : ",promedio_credito) # muestra el promedio credito
                else:# si no hay creditos_alumnos entonces, muestra mensaje de error --->
                    print(" Primero debe asignar creditos ") # printeo que primero debe asignar creditos
                    
        elif opcionMenu== 4: # si la opcion es 4 entonces
            if creditos_alumnos: # si existen creditos_alumnos entonces genero reportes --->
                fn.generar_reporte(creditos_alumnos) # generar reporte de quien? (de creditos_alumnos) - CSV
                fn.reporte_txt(creditos_alumnos) # generar reporte de quien? (de creditos_alumnos) - TXT
            else: # si no existen creditos_alumnos entonces, muestra mensaje de error
                print(" Primero debe asignar crédito ") # printeo que primero debe asignar creditos
        elif opcionMenu== 5: # si la opcion es 5 entonces, salgo del sistema   
            print("Saliendo del sistema...") # printeo que salgo del sistema
            break # salgo del bucle infinito
        else: # si la opcion no es un numero entre 0 y 5 entonces, muestra mensaje de error
            print(" Ingrese una opción valida entre 0 y 5") # printeo que ingrese una opcion invalida
    except:ValueError # capturo ValueError cuando se ingresa un valor no numerico