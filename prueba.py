income = float(input("Introduce el ingreso anual:"))
ipi = 85528
e_fiscal = 556.02
ipi_mayor = 14839.02
if income < ipi :
    tax = (income * .18) - e_fiscal
else:
    excedente = (income - 85528) * .32
    tax = ipi_mayor + excedente

if tax < 0:
    tax = 0


tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
