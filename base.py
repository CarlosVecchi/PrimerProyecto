import formulas


Categoria = input("ingrese la categoria: ")
Hs_Normales = float(input("ingrese las horas normales: "))
Hs_50 = float(input("ingrese las hs extras al 50%: "))
Hs_100 = float(input("ingrese las hs extas al 100%: "))

formulas.Normales(Categoria, Hs_Normales)
formulas.Extras50(Categoria, Hs_50)
formulas.Extras100(Categoria, Hs_100)
Bruto = Total_Normales + Total_50 + Total_100
print("el Monto de las Hs Normales Son: $", Total_Normales)
print("el Monto de las Hs Extras al 50% son: $", Total_50)
print("el Monto de las Hs Extras al 100% son: $", Total_100)
print("El Bruto total es: $", Bruto)
