#Listas
from multiprocessing import get_all_start_methods


Dueno = [28957346, "Juan", "Perez", 4789689, "Belgrano 101"]
Dueno2 = [23546987, "Maria", "Perez", 4789689, "Pueyrredon 811"]
Perro = [13, "Puppy", "12/12/2012", "Macho", 123]
Perro2 = [14, "Fido", "12/12/2012", "Macho", 23546987]
Clientes = ["Juan", "Mario", "Ariel", "Josefina", "Marianella"]

#Tuplas
Historial = (2350, 5960, 23000, 1000, 8900)
Historial2 = (23500, 5960, 2300, 10200, 8900)
Historial3 = (9530, 4120, 4580, 1500, 890, 7516, 426)
Historial4 = (7510, 7960, 76180, 800, 4100)
Historial5 = (8520, 9510, 7530, 3570, 1590)

#Ejercicio 1
if Dueno[0] > 26000000:
    print (Dueno[3])

#Ejercicio 2
Longitud = len(Dueno2)
for i in range(Longitud):
    if i == 0 or i == 2:
        continue
    else:
        print(Dueno2[i])

#Ejercicio 3
Perro[2] = "13/12/2012"
Perro[4] = 28957346
print(Perro)

#Ejercicio 4
Perro2.reverse()
for i in range(len(Perro2)):
    print(Perro2[i])

#Ejercicio 5
Total_Gastado = 0
for i in range(len(Historial)):
    Total_Gastado += Historial[i]

if Total_Gastado < 30000:
    print(Total_Gastado)
else:
    print("Gastos por encima de lo presupuestado")

#Ejercicio 6
def Superior5000():
    gastos = 0
    for atencion in Historial2:
        if atencion > 5000:
            gastos += 1
    return gastos

gastos = Superior5000()
print("la cantidad de atenciones con un costo superior a $5000 fueron: ", gastos)

#Ejercicio 7
cantidad = len(Historial3)
Total = 0
for atencion in Historial3:
    Total += atencion

Promedio = Total / cantidad
print(Promedio)
if Promedio > 4500:
    print("Se ha excedido del gasto promedio para su mascota")











# Ejercicio 8
#Primero defino la Funcion
def Valor_Minimo():
    Minimo = Historial4[0]
    for atencion in Historial4:
        if atencion < Minimo:
            Minimo = atencion
    return Minimo

#Para ejecutar el programa pregunto si quiere saber el Valor minimo de atencion
#Como el ejercicio pide solo de la mascota Olivia, asumo que es solo de ella
Pregunta = input("Desea saber cual fue el servicio/consulta de menor valor de Olivia? (S/N): ")

#Como no pide nada mas el ejercicio no le doy otra opcion al Condicional
if Pregunta == "S":
    Atencion_Minima = Valor_Minimo()
    print("El Valor minimo fue: $",Atencion_Minima)

    
