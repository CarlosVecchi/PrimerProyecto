
# Legajos
Lista_Legajos = [
    [1034, 'Carlos Alvarez', 28205770, 4], 
    [1100, 'Marcos Moreno', 27267554, 4], 
    [1103, 'Leonardo Garcia', 24975521, 5],
    [1129, 'Claudio Valero', 28428046, 6],
    [1130, 'Carlos Sanchez', 29768463, 4],
    [1144, 'Juan Ramires', 17629924, 5]
    ]

# Escala Jornales
Escala_Socaya = {1:407, 2:440, 3:466, 4:480, 5:499, 6:519, 7:537, 8:556, "MinGar":522.48}

while (True):
    print(" -.-.- M E N U   I N G R E S O   D E   L E G A J O S -.-.- ")
    print("")
    print(" 1.- INGRESO DE LEGAJO NUEVO")
    print(" 2.- CONSULTAR LEGAJO")
    print(" 3.- LIQUIDAR LEGAJO")
    print("") # Con Opcion 9 imprime Lista_Legajos
    print(" 0.- SALIR")
    print("")

    try:
        op = int(input( "ingrese una opcion: "))
        if (op == 1): # Ingreso Legajo nuevo
            while(True): # Legajo
                try:
                    legajo = int(input("Ingrese el Numero de legajo: "))
                    if (legajo <= 9999 and legajo >= 0):
                        break
                    else:
                        print("")
                        print(" el legajo debe ser entre 0 y 9999")
                        print("") 
                except:
                    print("")
                    print("El legajo debe ser un numero")
                    print("") 
            # Fin legajo

            nombre ="" # Apellido y Nombre
            while(len(nombre)<3):
                nombre = input("Ingrese Nombre y Apellido: ")
                if (len(nombre)<3):
                    print("")
                    print(" el nombre y apellido no es valido")
                    print("")
            # Fin Apellido y Nombre
            
            while(True): # DNI
                try:
                    DNI = int(input("Ingrese el Numero de DNI: "))
                    if (DNI <= 99999999 and DNI >= 0):
                        break
                    else:
                        print("")
                        print("DNI Invalido")
                        print("") 
                except:
                    print("")
                    print("El DNI debe ser un numero")
                    print("") 
            # Fin DNI     
                
            while(True): # Categoria
                try:
                    Categoria = int(input("Ingrese la categoria: "))
                    if (Categoria <= 9 and Categoria >= 1):
                        break
                    else:
                        print("")
                        print("Categoria Invalida debe ser entre 1 y 9")
                        print("") 
                except:
                    print("")
                    print("La categoria debe ser un numero entre 1 y 9")
                    print("") 
            # Fin Categoria
            # guardamos el nuevo legajo a la lista
            Lista_Legajos.append([legajo, nombre, DNI, Categoria])
            # Lista_Legajos.append([legajo, nombre, DNI, {Categoria:Escala_Socaya[Categoria]}])
            print("")
            print("Legajo Cargado Correctamente")
            print("")
            # Fin Legajo guardado
        # Fin Legajo Nuevo
        elif (op == 2): #Busqueda de Legajo
            while(True):
                try:
                    Busqueda_Legajo = int(input("Ingrese el Numero de legajo a buscar: "))
                    if (Busqueda_Legajo <= 9999 and Busqueda_Legajo >= 0):
                        for leg in range(len(Lista_Legajos)):
                            for i in range(len(Lista_Legajos[leg])):
                                if Busqueda_Legajo== Lista_Legajos[leg][i]:
                                    #print(Lista_Legajos[leg])
                                    print("Legajo: ", Lista_Legajos[leg][0])
                                    print("Nombre y Apellido: ", Lista_Legajos[leg][1])
                                    print("DNI: ", Lista_Legajos[leg][2])
                                    print("Categoria: ", Lista_Legajos[leg][3])
                                    #print("Brutos del Semestre: ", Lista_Legajos[leg][4])
                                    break
                        break
                    else:
                        print("")
                        print(" el legajo debe ser entre 0 y 9999")
                        print("") 
                except:
                    print("")
                    print("El legajo debe ser un numero")
                    print("") 
        # Fin Busqueda Legajo    
        elif (op == 3):
            print("Proximamente")
        elif (op == 9):
            print(Lista_Legajos)
        elif (op == 0):
            print("")
            print("Hasta luego")
            break
        else:
            print("")
            print("Error ingrese una opcion valida....")
            print("")

    except:
        print("")
        print(" Error....volviendo al menu princial ")
        print("")
        
