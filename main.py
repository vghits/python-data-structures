from funciones import *

'''1) Generar una lista de 50 letras mayúsculas aleatorias (utilizar el código ASCII).
2) Mostrar la lista generada, formateada de manera que sea entendible para el usuario.
3) Solicitar al usuario el ingreso de una letra mayúscula por consola, validando que sea una única
letra entre la ‘A’ y la ‘Z’. Una vez validada, buscar la letra en la lista generada en la opción 1 e
informar si existe o no. En caso de que exista, también informar en qué posiciones/índices se
encuentra.
4) Solicitar al usuario el ingreso de una cadena de caracteres “ASC” o “DESC” por consola y
validarla. Luego, ordenar una COPIA de la lista generada en la opción 1 según el criterio
ingresado por el usuario, y mostrarla. La lista original no debe ser modificada.
5) Solicitar al usuario el ingreso de dos (2) números enteros por consola, validando su tipo de dato
(mediante código ASCII) y su pertenencia al rango de “3” a “9”, ambos inclusive. El primer
número representará la cantidad de filas, y el segundo, la cantidad de columnas.
6) Generar una matriz de números enteros aleatorios entre 1 y 9, utilizando los números ingresados
en la opción 5 como cantidad de filas y columnas.
7) Mostrar la matriz generada en la opción 6, separando las filas entre sí con guiones medios (“-”)
y las columnas con barras verticales (“|”), incluyendo los bordes de la matriz.
8) Salir del programa.

NOTAS:
Nota 1: No se podrá acceder a los ítems:
● 2, 3 o 4, sin antes haber generado la lista de manera aleatoria (ítem 1).
● 6, sin antes haber solicitado los dos números enteros por consola (ítem 5).
● 7, sin antes haber generado la matriz de manera aleatoria (ítem 6).
En tal sentido, realizar las validaciones correspondientes (utilizar banderas).
Nota 2: Los puntos deben ser accedidos mediante un menú de opciones.
Nota 3: Resolver el manejo de ingreso de letras minúsculas o mayúsculas en el punto 4. El usuario
puede ingresar “Asc” o “aSC” e igualmente será un string válido.
Nota 4: Toda validación del programa debe volver a solicitar el dato y no volver al menú principal
hasta que se ingrese el dato que se pide, opcionalmente pueden agregar una cantidad de intentos.
Nota 5: Se deberá desarrollar biblioteca “funciones.py” que contendrá todas las funciones propias, las
mismas deberán estar correctamente documentadas.
Nota 6: El menú y todas las variables necesarias para el funcionamiento del programa estarán
contenidas en el programa principal “examen.py”.
'''
lista=[]
filas = 0
columnas = 0
matriz = 0
matriz_generada = False #puse esta bandera para poder controlar si la matriz fue generada o no


menu = ''' 

==================== MENU DE OPCIONES ====================

1) Generar una lista.
2) Mostrar la lista generada.
3) Validar la letra de la A hasta la Z, luego buscarla e informar si existe o no.
4) Ingresar cadena de caracteres de manera ASCENDENTE o DESCENDIENTE.
5) Solicitar ingreso de numeros y validar su tipo de dato.
6) generar matriz aleatoria.
7) Mostrar la matriz generada en la opcion 6.
8) Salir del programa.

============================================================
'''
while True:
    print(menu)
    Ingreso_de_numeros=(input("Ingrese un numero de el menu de opciones: "))

    match Ingreso_de_numeros:
        case "1":
            lista = generar_lista(50, 65, 90) #dentro de estos parametro para que funcione el programa hay que ponner la longitud= 50, min= 50, max= 90 seria del ascci
            print("La lista fue creada de manera correcta")    
        case "2":
            if len(lista) == 50:
                mostrar_lista(lista)
            else:
                print("Primero hay que generar la lista (es la opcion 1)")
        case "3":
            if len(lista) == 50:
                ubicar_letra_lista(65, 90, "Ingrese MAYUSCULA: ", "Letra INvalida, ingrese letra de la A hasta la Z: ", lista)
            else:
                print("Primero debes generar la lista (es la opcion 1)")
        case "4":
            if len(lista) == 50:
                ordenar_lista(lista)
            else:
                print("Primero debes generar la lista (es la opcion 1)")  
        case "5":
            filas, columnas = ingresar_filas_y_columnas()
            matriz_generada = False 
            print(f"Filas: {filas}, Columnas: {columnas}")
        case "6":
            if filas != 0 and columnas != 0:
                matriz = generar_matriz_aleatoria(filas, columnas)
                matriz_generada = True #esta bandera es para poder utilizarla en el punto 7
            else:
                print("Primero debe ingresar filas y columnas (opcion 5)")
        case "7":
            if matriz_generada:
                mostrar_borde_de_matriz(matriz, filas, columnas)    
            else:
                print("Primero tiene que generar la matriz.(opcion 6)")
        case "8":
            print("Usted salio del programa")
            break
        case _:
            print("Opcion no valida, Ingrese un numero del 1 al 8")
