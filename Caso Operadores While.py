nombre_usuario = input("Ingresa tu nombre: ")
print("Elija la opcion a, b o c dependiendo de lo que desee:")
opcion = input("Lista de opciones: \na) Operadores Matematicos \nb) Operadores Relacionales \nd) Terminar Proceso \n")
while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d":
    opcion = input("Por favor elije una de las opciones ingresando a, b, c o d: ")
while opcion != "d":       
    if opcion == "a":
        print("-----Operadores Matematicos-----")
        operadores_matematicos =input("¿Que deseas hacer? \na) Sumar \nb) Restar \nc) Multiplicacion \nd) Division \ne) Modiulo(Resto) \nf) Potencia \ng) Volver al menu principal \nh) Terminar proceso \n")
        while operadores_matematicos != "a" and operadores_matematicos != "b" and operadores_matematicos != "c" and operadores_matematicos != "d" and operadores_matematicos != "e" and operadores_matematicos != "f" and operadores_matematicos != "g" and operadores_matematicos != "h":
            operadores_matematicos = input("por favor ingresa alguna de las opciones anteriores: ")
        if operadores_matematicos == "a":
            numero_1 = int(input("Por favor ingrese el primero numero que desee sumar: "))
            numero_2 = int(input("Por favor ingrese el segundo numero que desea sumar: "))
            resultado_suma = numero_1 + numero_2
            print(f"{nombre_usuario} el resultado de la suma es: {resultado_suma}")
        elif operadores_matematicos == "b":
            numero_1 = int(input("Por favor ingrese el primero numero que desea restar: "))
            numero_2 = int(input("Por favor ingrese el segundo numero que desea restar: "))
            resultado_resta = numero_1 - numero_2
            print(f"{nombre_usuario} el resultado de la resta es: {resultado_resta}")
        elif operadores_matematicos == "c":
            numero_1 = int(input("Por favor ingrese el primero numero que desea multiplicar: "))
            numero_2 = int(input("Por favor ingrese el segundo numero que desea multiplicar: "))
            resultado_multiplicacion = numero_1 * numero_2
            print(f"{nombre_usuario} el resultado de la multiplicacion es: {resultado_multiplicacion}")
        elif operadores_matematicos == "d":
            numero_1 = int(input("Por favor ingrese el primero numero: "))
            numero_2 = int(input("Por favor ingrese el segundo numero: "))
            resultado_division = numero_1 / numero_2
            print(f"{nombre_usuario} el resultado de la division es: {resultado_division}")
        elif operadores_matematicos == "e":
            numero_1 = int(input("Por favor ingrese el primero numero: "))
            numero_2 = int(input("Por favor ingrese el segundo numero: "))
            resultado_modulo = numero_1 % numero_2
            print(f"{nombre_usuario} el resultado del modulo es: {resultado_modulo}")
        elif operadores_matematicos == "f":
            numero_1 = int(input("Por favor ingrese el numero de la base: "))
            numero_2 = int(input("Por favor ingrese el numero del exponencial: "))
            resultado_potencia = numero_1**numero_2
            print(f"{nombre_usuario} el resultado del modulo es: {resultado_potencia}")
        elif operadores_matematicos == "g":
            opcion = input("Lista de opciones: \na) Operadores Matematicos \nb) Operadores Relacionales \nc) Validadores de tipos de datos \nd) Terminar Proceso \n")  
            while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d":
                opcion = input("Por favor elije una de las opciones ingresando a, b, c o d: ")
        elif operadores_matematicos == "h":
            print(f"{nombre_usuario} se ha terminado el proceso, nos vemos!")
            break
    if opcion == "b":
        print("-----Operadores Relacionales-----")
        operadores_relaciones = input("a) Hacer Operaciones \nb) Volver al menu principal \nc) Terminar proceso \n")
        while operadores_relaciones != "a" and operadores_relaciones != "b" and operadores_relaciones != "c":
            operadores_relaciones = input("a) Hacer Operaciones \nb) Volver al menu principal \nc) Terminar proceso \n")
        if operadores_relaciones == "a":
            numero_1 = int(input("Por favor ingrese el primero numero: "))
            numero_2 = int(input("Por favor ingrese el segundo numero: "))
            if numero_1 > numero_2:
                print(f"{nombre_usuario} el {numero_1} es mayor que {numero_2} y son distintos")
            elif numero_1 == numero_2:
                print(f"{nombre_usuario} el {numero_1} es igual al {numero_2}")
            elif numero_1 <  numero_2:
                print(f"{nombre_usuario} el {numero_2} es mayor que {numero_1}  y son distintos")   
                operadores_relaciones = input("a) Hacer Operaciones \nb) Volver al menu principal \nc) Terminar proceso \n")   
        elif operadores_relaciones == "b":
            opcion = input("Lista de opciones: \na) Operadores Matematicos \nb) Operadores Relacionales \nc) Validadores de tipos de datos \nd) Terminar Proceso \n")  
            while opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d":
                    opcion = input("Por favor elije una de las opciones ingresando a, b, c o d: ")
        elif operadores_relaciones == "c":
            print(f"{nombre_usuario} se ha terminado el proceso, nos vemos!")
            break
if opcion == "d":
    print(f"{nombre_usuario} se ha termiando el proceso, nos vemos!")