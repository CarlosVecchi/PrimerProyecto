Lista_Legajos = [
    [1034, 'Carlos Alvarez', 28205770, 4, {'Enero': 120000, 'Febrero': 140000}], 
    [1100, 'Marcos Moreno', 27267554, 4], 
    [1103, 'Leonardo Garcia', 24975521, 5],
    [1129, 'Claudio Valero', 28428046, 6],
    [1130, 'Carlos Sanchez', 29768463, 4],
    [1144, 'Juan Ramires', 17629924, 5]
    ]

busqueda = int(input("ingrese el legajo: "))
for leg in range(len(Lista_Legajos)):
    for i in range(len(Lista_Legajos[leg])):
        if busqueda == Lista_Legajos[leg][i]:
            print(Lista_Legajos[leg])
            print("Legajo: ", Lista_Legajos[leg][0])
            print("Nombre y Apellido: ", Lista_Legajos[leg][1])
            print("DNI: ", Lista_Legajos[leg][2])
            print("Categoria: ", Lista_Legajos[leg][3])
            print("Brutos del Semestre: ", Lista_Legajos[leg][4])
            break
                