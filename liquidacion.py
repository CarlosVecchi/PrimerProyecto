Escala_Socaya = {"1":407,"2":440,"3":466,"4":480,"5":499,"6":519,"7":537,"8":556}

def Normales(Categoria, Hs_Normales):
  global Total_Normales
  Valor = Escala_Socaya[Categoria]
  Total_Normales = Valor * Hs_Normales
  
def Extras50(Categoria, Hs_50):
  global Total_50
  Valor = Escala_Socaya[Categoria]
  Total_50 = (Valor * 1.50) * Hs_50

def Extras100(Categoria, Hs_100):
  global Total_100
  Valor = Escala_Socaya[Categoria]
  Total_100 = (Valor * 2) * Hs_100

Categoria = input("ingrese la categoria: ")
Hs_Normales = float(input("ingrese las horas normales: "))
Hs_50 = float(input("ingrese las hs extras al 50%: "))
Hs_100 = float(input("ingrese las hs extas al 100%: "))

Normales(Categoria, Hs_Normales)
Extras50(Categoria, Hs_50)
Extras100(Categoria, Hs_100)
Bruto = Total_Normales + Total_50 + Total_100
print("el Monto de las Hs Normales Son: $", Total_Normales)
print("el Monto de las Hs Extras al 50% son: $", Total_50)
print("el Monto de las Hs Extras al 100% son: $", Total_100)
print("El Bruto total es: $", Bruto)